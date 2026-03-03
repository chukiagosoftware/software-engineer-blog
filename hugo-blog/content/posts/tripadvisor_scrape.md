---
title: "Web scraping TripAdvisor Hotel Reviews with Go Colly and Applescript"
date: 2026-03-03
categories: ["hotel", "scraping", "go", "colly", "applescript", "hotel reviews"]
tags: ['Go', 'Colly', 'Applescript', 'hotel reviews', 'tripadvisor', 'google places', 'expedia', 'vertex', 'vector search']
author: "Eric Arellano"
description: "We are forced to scrape TripAdvisor Hotel Reviews with Go Colly and Applescript."
draft: false
---


The goal is to gather as many real Hotel reviews as possible to process them into vector embeddings and run similarity searches with RAG (Retrieval Augmented Generation). The resulting matched reviews will be combined as input prompts for the Generative AI (GenAI) LLM model such as Gemini, Grok, Claude, or ChatGPT. This will allows us to find the best hotels in any given city. The Hotel Assistant will return results based on custom criteria or a user question.  

However, it turns out that the available Hotel Review APIs are not very available.  Google Places returns only 20 hotels per city and only 5 random reviews per hotel (same 5 every time) even with their Paid Tier.  Yelp only give you three hotel reviews per hotel, even with a paid plan. TripAdvisor has a difficult to understand pay as you go model. Expedia and Booking also restrict access to their prized reviews behind an obscure API pay model. 
Fortunately, [amadeus](https://www.amadeus.com) has a good Free Developer plan (available until July 2026) which provides enough hotels for my demo purposes. But Amadeus doesn't provide any Hotel reviews and also doesn't have any hotel metadata for free. So, I was forced to take a quick coding detour and scrape HTML for this project. Enter Go Colly and AppleScript.

Yes, Applescript! TripAdvisor and the others have advanced anti-scraping algorithms, are behind javascript, captcha and Cloudflare security which detects repeated GETs and stops returning new data, if you can even get past the JavaScript using headless chrome. Since my app is a non-commercial pilot project, I don't mind doing some scraping instead of spending several hundred dollars on APIs calls. If I were to turn it into a paid or even a public service for any city using geolocation, I may revisit this decision and buy some API calls. With Applescript, I was able to run MacOS native Safari web queries, browsing each location's hotel list, and gathering reviews from each hotel without a $1,000+  price tag.  Do note, if this were a commercial project would not mind spending money on the APIs. But the amount of red tape and restrictive pricing versus lack of information and ambiguity in the documentation led me to accept the call of the wild.

Without further ado, we have the [alpaca](https://www.github.com/chukiagosoftware/alpaca/) scraping package, which allows us to gather Hotel Reviews from any city with just an m1 Mac and a broadband connection.

The details:

## Step 1: Setting Up the AppleScript for Safari Automation

I started by writing an AppleScript to control Safari. The script first quits Safari to ensure a clean state, then activates it and builds a direct search URL for TripAdvisor based on the hotel name, city, and country. The cities come from our prefetched list of cities and countries with lots of hotels. For example, it constructs something like `https://www.tripadvisor.com/Search?q=Hotel+Name+City+Country`. This avoids the hassle of interacting with the site's search form, which can be unreliable across different regions and includes CDN blockers as captchas. The script loads this URL in Safari, waits for the page to load, finds the first hotel matching result in the search list, and then navigates to the hotel's page. From here we use Applescript to click the "All Reviews" link to load the full review section. Our Applesript then captures the entire page source as HTML and saves it to a file in a structured folder like `hotelReviewsSaved/City,Country/hotelid_tripadvisor_hotelname.html`. To handle potential issues like popups or varying page load times, the script includes checks for elements and retries. It also ensures Safari closes properly after each run to avoid interference with the next scrape.

## Step 2: Integrating with the Hotel Database

Since I have built a database of cities and of hotels from Amadeus and Google, hotels are readily available with fields like hotel ID, name, city, and country. Using GORM in Go, I query the database to get a list of hotels for a specific city and country. For instance, for Austin, US, I can run 

    var hotels []models.Hotel
	
    err = db.Select("city", "country", "hotel_id", "name").Where("city = ? AND country = ?", city, country).Find(&hotels).Error
	if err != nil {
		log.Fatalf("Failed to query hotels: %v", err)
	}


The Go program loops through each hotel, passes the details (name, city, country, ID) to the AppleScript via command-line arguments, and executes it using `os/exec`. Between each hotel, we added a delay (e.g., 30 seconds) to avoid triggering TripAdvisor's rate limits or bot detection.


    for _, hotel := range hotels {
        fmt.Printf("Processing hotel: %s (%s)\n", hotel.Name, hotel.HotelID)

		// Run osascript with the script and arguments: hotelName, city, country, hotelID
		cmd := exec.Command("osascript", scriptPath, hotel.Name, hotel.City, hotel.Country, hotel.HotelID)
		err := cmd.Run()
		time.Sleep(2 * time.Second)
		if err != nil {
			log.Printf("Error running AppleScript for hotel %s: %v", hotel.Name, err)
			continue // Continue with next hotel
		}

		fmt.Printf("Successfully processed hotel: %s\n", hotel.Name)

		// Pause for half a second before the next hotel
		time.Sleep(4 * time.Second)
	}

If the AppleScript fails for any hotel (e.g., due to network issues or page changes), the program logs the error and moves to the next one, ensuring the process is robust.

## Step 3: Processing the Saved HTML Files

Once the HTML files are saved, we use Go with the Colly library to parse each file. Colly is great for scraping static HTML, so we load the saved page source and extract the review data. This includes details like reviewer names, review titles, full text, ratings, and dates—focusing on genuine human experiences. The parsing code walks through the saved files in the directory structure, identifies review elements using CSS selectors (e.g., targeting specific divs or classes for reviews), and cleans the data. We then save each review to the database, associating it with the hotel ID and source (TripAdvisor). To handle duplicates or updates, I generate a sha256 hash of the review text and save it as hotel_review_id. The process logs progress for each hotel and provides a total count of reviews processed across all files.

## Final Thoughts

This setup allowed me to gather a few thousand reviews without API costs, using just macOS tools. I'm excited to see how this project evolves and how it can be used in the future. If it does have any commercial use then of course I will sign up for Paid Tiers and fully automate Hotel and Review data gathering.