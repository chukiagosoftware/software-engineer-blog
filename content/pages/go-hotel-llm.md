---
title: "Alpaca - Hotel Data Microservice"
date: 2026-02-21
categories: ["Go", "Microservices", "AWS"]
tags: ["Go", "API", "LLM", "SQLite", "Amadeus", "DevOps"]
author: "Eric Arellano"
description: "A comprehensive Go microservice for fetching, consolidating, and analyzing hotel data from multiple sources, featuring multi-source aggregation, review crawling, and LLM-powered recommendations."
draft: false
---

# Alpaca - Hotel Data Microservice

A comprehensive Go microservice that fetches, consolidates, and analyzes hotel data from multiple sources. Features multi-source data aggregation, review crawling, and LLM-powered recommendation analysis.

## Architecture

Alpaca is a single microservice that:
- Fetches hotel data from multiple sources (Amadeus, Expedia, Tripadvisor, Google, Booking.com)
- Consolidates hotel data into a unified schema
- Crawls reviews from multiple sources (Tripadvisor, Google, Expedia, Booking, hotel websites, etc.)
- Uses LLM (GPT-4, Claude, Grok) to analyze reviews for Quality and Quiet
- Generates intelligent recommendations based on review analysis
- Stores data in SQLite (default) with raw SQL
- Uses a generalized provider interface for easy API integration
- Processes data in concurrent batches with rate limiting

## Project Structure
