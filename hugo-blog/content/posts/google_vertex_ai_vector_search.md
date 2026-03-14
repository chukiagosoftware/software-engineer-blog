---
title: "Retrieval Augmented Generation with Vertex AI"
date: 2026-03-14
categories: ["Go", "Python", "Google Vertex", "RAG", "AI", "Vector Search", "Generative AI", "Text Embeddings]
tags: ['Go', 'Python', 'Vector', 'Google Vertex', 'AI', 'RAG', 'Vector Search', 'Vertex Search', 'Generative AI', 'gemini', 'text embeddings']
author: "Eric Arellano"
description: "Working with Google Cloud's Vertex AI Vector Search features for RAG (Retrieval Augmented Generation)"
draft: false
---

Building a RAG system with Vertex AI Vector Search is a great way to get started with the Google Cloud platform's latest Generatei. This post will walk you through the process of setting up a RAG system with Vertex AI Vector Search.

Google Cloud has a bunch of new features and services which are similar but confusingly named. Gemini is the umbrella name for their Generative AI platform featuring the models of the same name and can be used for quick development as a ChatGPT/Llama alternative at https://ai.google.dev/gemini. However, that is pretty much separate from Enterprise level Vertex AI.

Under Vertex AI platform we can still deploy Gemini models, and for the Alpaca project, we will use Vertex Vector Search and Gemini-001 Text Embeddings.

Vertex Vector Search is a partially managed Vector Database service to which we can import our vector embeddings from Big Query, and serve an Index Endpoint for similarity searches.  This gives a medium level of control and flexibility where we can choose the embedding models, batch sizes, metadata, scaling of the endpoint and other features. I chose to use the latest Gemini-001 text embeddings model which is a 732 dimensions model and is better than the old text-embedding-004 per the Google Docs.  The fully managed Google Vertex AI Search offering doesn't yet allow Gemini-001 and only has the older models for embeddings. The AI Search can be used for similarity search, but essentially is more appropriate for website indexing and navigation of a large body of text rather than for similarity RAG searches. There is also the Vertex AI RAG Engine, which is a managed service that can be used to build RAG systems as well. RAG Engine and AI Search both take input from GCS Buckets, JSON documents, even things like Jira or other information platforms.

The Go Libraries for Vector Search Index Creation, Embedding creation (with Gemini calls to GenAi library) and Index Creation/Management didn't work out, so this will be handed using Python with Github Actions in the automation production stage.  For now, Indexes were created manually or using gcloud commands.

We will use the Go SDK for Vertex AI Vector Search to query the index and generate a response. To convert a user question into vectors we use the Go SDK for Generative AI.

{{< emoji accordion >}}

Since this is under active development, please check back soon for updates, links, pictures and other fine content.

