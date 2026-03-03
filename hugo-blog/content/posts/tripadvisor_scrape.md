---
title: "Web scraping TripAdvisor Hotel Reviews with Go Colly and Applescript"
date: 2026-03-03
categories: ["hotel", "scraping", "go", "colly", "applescript", "hotel reviews"]
tags: ['Go', 'Colly', 'Applescript', 'hotel reviews', 'tripadvisor', 'google places', 'expedia', 'vertex', 'vector search']
author: "Eric Arellano"
description: "We are forced to scrape TripAdvisor Hotel Reviews with Go Colly and Applescript."
draft: false
---


"I needed to gather as Hotel reviews as possible to process them with RAG (Retrieval Augmented Generation). The goal is to input hotel reviews to LLMs for a Generative AI based assistant and find the best hotels in any given city.  

However, it turns out that the available Hotel APIs are not very charitable.  Google Places and Yelp only give you five hotel results per city, even with a paid plan, and TripAdvisor has a difficult to understand pay as you go model.  Expedia and Booking also restrict access to their prized reviews behind an obscure API pay model.

So, we were forced to scrape HTML for this project. The saviour: AppleScript.

With Applescript, I was able to run MacOS native Safari web queries, browsing each location's hotel list, and gathering reviews from each hotel without a $1,000+  price tag.  Do note, if this were a commercial project would not mind spending money on the APIs. But the amount of red tape and restrictive pricing versus lack of information and ambiguity in the documentation led me to accept the call of the wild.

Without further ado, we have the [alpaca](github.com/chukiagosoftware/alpaca/) scraping package, which allows us to gather Hotel Reviews from any city with just an m1 Mac and a broadband connection.

The details:

## Step 1: Setting Up the AppleScript for Safari Automation

We started by writing an AppleScript to control Safari. The script quits Safari to ensure a clean state, then activates it and builds a direct search URL for TripAdvisor based on the hotel name, city, and country. The cities come from our prefetched list of cities and countries with lots of airports. 

For example, it constructs something like `https://www.tripadvisor.com/Search?q=Hotel+Name+City+Country`. This avoids the hassle of interacting with the site's search form, which can be unreliable across different regions and includes CDN blockers as captchas.

The script loads this URL in Safari, waits for the page to load, finds the first hotel matching result in the search list, and then navigates to the hotel's page. From here we use Applescript to click the "All Reviews" link to load the full review section. Our Applesript then captures the entire page source as HTML and saves it to a file in a structured folder like `hotelReviewsSaved/City,Country/hotelid_tripadvisor_hotelname.html`.

To handle potential issues like popups or varying page load times, the script includes checks for elements and retries. It also ensures Safari closes properly after each run to avoid interference with the next scrape.

## Step 2: Integrating with the Hotel Database

We already had a database of cites and of hotels gathered from previous API calls or sources, with fields like hotel ID, name, city, and country. Using GORM in Go, we queried the database to get a list of hotels for a specific city and country. For instance, for Austin, US, we ran `SELECT city, country, hotel_id, name FROM hotels WHERE city = 'Austin' AND country = 'US'`.

The Go program loops through each hotel, passes the details (name, city, country, ID) to the AppleScript via command-line arguments, and executes it using `os/exec`. Between each hotel, we added a delay (e.g., 30 seconds) to avoid triggering TripAdvisor's rate limits or bot detection.

If the AppleScript fails for any hotel (e.g., due to network issues or page changes), the program logs the error and moves to the next one, ensuring the process is robust.

## Step 3: Processing the Saved HTML Files

Once the HTML files are saved, we use Go with the Colly library to parse each file. Colly is great for scraping static HTML, so we load the saved page source and extract the review data. This includes details like reviewer names, review titles, full text, ratings, and dates—focusing on genuine human experiences.

The parsing code walks through the saved files in the directory structure, identifies review elements using CSS selectors (e.g., targeting specific divs or classes for reviews), and cleans the data. We then save each review to the database, associating it with the hotel ID and source (TripAdvisor).

To handle duplicates or updates, we use hashing on the review text to create unique IDs. The process logs progress for each hotel and provides a total count of reviews processed across all files.

## Final Thoughts

This setup gave us thousands of reviews without API costs, using just macOS tools. The key was AppleScript's ability to automate Safari natively, combined with Go for database handling and file processing. If TripAdvisor changes their site, the selectors might need tweaks, but the foundation is solid. For production, we'd add more error handling or switch to paid APIs, but for our RAG/LLM project, it's perfect."