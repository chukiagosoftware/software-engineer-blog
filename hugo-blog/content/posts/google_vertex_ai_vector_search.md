---
title: "Retrieval Augmented Generation with Vertex AI"
date: 2026-03-14
categories: ["Go", "Python", "Google Vertex", "RAG", "AI", "Vector Search", "Generative AI", "Text Embeddings"]
tags: ['Go', 'Python', 'Vector', 'Google Vertex', 'AI', 'RAG', 'Vector Search', 'Vertex Search', 'Generative AI', 'gemini', 'text embeddings']
author: "Eric Arellano"
description: "Working with Google Cloud's Vertex AI Vector Search features for RAG (Retrieval Augmented Generation)"
draft: false
---

Building a RAG system with Vertex AI Vector Search is a great way to get started with the Google Cloud platform's latest Generative AI and Machine Learning tools. This post will walk you through the process of setting up a RAG system with Vertex AI Vector Search.

### Gemini API vs Vertex AI
Google Cloud has a bunch of new features and services which are similar but confusingly named. Gemini is the umbrella name for their Generative AI platform featuring the models of the same name and can be used for quick development as a ChatGPT/Llama alternative at https://ai.google.dev/gemini. However, that is separate from Enterprise level Vertex AI.

### BigQuery Text Embeddings
Under Vertex AI platform we can still deploy Gemini models, and for the Alpaca project, we will use Vertex Vector Search and Gemini-001 Text Embeddings. To generate embeddings on BigQuery table, we run the following command. ML.GENERATE_EMBEDDINGS is the older function which requires some GCP IAM magic. For new development use AI.GENERATE_EMBEDDINGS which allows more seamless IAM permissions flow and also will support streaming new table data into the embeddings table.

    CREATE OR REPLACE TABLE `<project-id>.alpacaCentral.review_embeddings`
    AS
    SELECT
    r.id,
    r.review_text,
    h.name AS hotel_name, -- Assuming 'name' is the hotel's name column
    h.City AS city,
    h.Country AS country,
    embeddings.ml_generate_embedding_result AS embedding
    FROM
    `<project-id>.alpacaCentral.reviews` AS r
    JOIN
    `golang1212025.alpacaCentral.hotels` AS h
    ON
    r.hotel_id = h.hotel_id -- Corrected join condition
    JOIN
    ML.GENERATE_EMBEDDING(
    MODEL `<project-id>.alpacaCentral.alpaca-gemini-embedding-001`,
    (
    SELECT reviews.id, reviews.review_text AS content
    FROM `<project-id>.alpacaCentral.reviews` AS reviews
    WHERE reviews.review_text IS NOT NULL AND LENGTH(reviews.review_text) > 0
    ),
    STRUCT(TRUE AS flatten_json_output)
    ) AS embeddings
    ON
    r.id = embeddings.id
    WHERE r.review_text IS NOT NULL AND LENGTH(r.review_text) > 0;


### Google Vertex AI Vector Search
Vertex Vector Search is a partially managed Vector Database service to which we can import our vector embeddings from Big Query, and serve an Index Endpoint for similarity searches.  This gives a medium level of control and flexibility where we can choose the embedding models, batch sizes, metadata, scaling of the endpoint and other features. I chose to use the latest Gemini-001 text embeddings model which is a 3072 vector dimension model and is better than the old text-embedding-004 per the Google Docs.

Once an index exists, we can upload data to it from BigQuery using the following command. This will be done with Python via GHA because the Go SDK is not fantastic yet. Actually, for one-time or batch processes a pipeline or even Terraform might be better than Go code. We'll stick to Go for querying, orchestrating and any other intensive or real-time stuff.

    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "@vertex/importIndex.json" \
    "https://<location>-aiplatform.googleapis.com/v1beta1/projects/<project-id>/locations/<location>/indexes/<index-id>:import"

where config.json is:

    {
    "name": "projects/<project-id>/locations/<location>/indexes/<index-id>",
    "isCompleteOverwrite": true,
    "config": {
    "bigQuerySourceConfig": {
    "tablePath": "bq://<project-id>.alpacaCentral.review_embeddings",
    "datapointFieldMapping": {
    "idColumn": "id",
    "embeddingColumn": "embedding",
    "restricts": [
    {
    "namespace": "hotel_name",
    "allowColumn": ["hotel_name"]
    },
    {
    "namespace": "city",
    "allowColumn": ["city"]
    },
    {
    "namespace": "country",
    "allowColumn": ["country"]
    }
    ],
    "numericRestricts": [
    {
    "namespace": "rating",
    "valueColumn": "rating",
    "valueType": "INT"
    }
    ],
    "metadataColumns": [
    "review_text",
    "hotel_name",
    "city",
    "country",
    "rating"
    ]
    }
    


### Google Vertex AI Search
The fully managed Google Vertex AI Search offering doesn't yet allow Gemini-001 and only has the older models for embeddings. The AI Search can be used for similarity search, but essentially is more appropriate for website indexing and navigating a large body of text rather than for similarity RAG searches. 

### Google Vertex RAG Engine
There is also the Vertex AI RAG Engine, which is a managed service that can be used to build RAG systems as well. RAG Engine and AI Search both take input from GCS Buckets, JSON documents, even things like Jira or other information platforms.

### GO SDK Support
The Go Libraries calls for Vector Search Index Creation, Embedding creation and Endpoint didn't work out, so this will be handed using Python with Github Actions in the automation production stage.  For now, Indexes were created manually and updated using gcloud commands. The embeddings were generated via the BigQuery functions as previously described.

Here we will take an HTML form input and generate a vector embedding for the question to feed into our RAG system.

    // GenerateEmbedding converts a user question string into a 768-dimensional vector using Gemini embedding model
    func (s *VertexSearchService) GenerateEmbedding(ctx context.Context, question string) ([]float32, error) {
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
        return nil, fmt.Errorf("failed to create GenAI client: %w", err)
        }
        // not Close method defer client.Close()
    
        content := genai.NewContentFromText(question, "")
        result, err := client.Models.EmbedContent(ctx, "gemini-embedding-001", []*genai.Content{content}, nil)
        if err != nil {
            return nil, fmt.Errorf("failed to generate embedding: %w", err)
        }
    
        if len(result.Embeddings) == 0 {
            return nil, fmt.Errorf("no embeddings generated")
        }
    
        // Convert to []float32
        embedding := make([]float32, len(result.Embeddings[0].Values))
        for i, v := range result.Embeddings[0].Values {
            embedding[i] = float32(v)
        }
        return embedding, nil
    }

We will use the Go SDK "cloud.google.com/go/aiplatform/apiv1" for Vertex AI Vector Search (RAG, basically) to query the index and generate a response. To convert a user question into a vector array we used the Go SDK for Generative AI "google.golang.org/genai".

{{< emoji accordion >}}

Since this is under active development, please check back soon for updates, links, pictures and other fine content.

