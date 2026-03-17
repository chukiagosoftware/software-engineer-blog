---
title: "Retrieval Augmented Generation with Vertex AI and Go"
date: 2026-03-14
categories: ["Go", "Python", "Google Vertex", "RAG", "AI", "Vector Search", "Generative AI", "Text Embeddings", "MLops"]
tags: ['Go', 'Python', 'Vector', 'Google Vertex', 'AI', 'RAG', 'Vector Search', 'Vertex Search', 'Generative AI', 'gemini', 'text embeddings', 'mlops']
author: "Eric Arellano"
description: "Working with Google Cloud's Vertex AI Vector Search features for RAG (Retrieval Augmented Generation)"
draft: false
---

I am building a Go-based Hotel Reviews RAG system with Vertex AI Vector Search, BigQuery and Gemini. This post will describe some MLops, AI Text models, and overall working with Google Cloud platform's latest Generative AI and Machine Learning tools. 

I will walk you through the process of setting up an end-to-end Retrieval Augmented Generation system with Vertex AI Vector Search. The project is called [Alpaca](https://github.com/chukiagosoftware/alpaca) which is my Hotel Review Search turbocharged with AI.  End goal: finding quality hotels that meet your criteria based on natural language analysis and a fine-tuned curation of LLMs, Vector Similarity Search, and the related APIs. My preliminary research shows that it is possible to do better than a raw ChatGPT/Grok/Gemini/Llama question and answer prompt.

### Google Gemini API vs Vertex AI
Google Cloud has a bunch of new features and services which are similar but confusingly named. Vertex AI is the longstanding AI and Machine Learning platform suite. Gemini is the umbrella name for their Generative AI platform featuring the various models of the same name. Gemini API can be used for quick development as a ChatGPT/Llama alternative at https://ai.google.dev/gemini. However, that is separate from Enterprise level Vertex AI and doesn't include the batteries, picks, and shovels that Vertex does.

### BigQuery Text Embeddings Generation
Under the enterprise Vertex AI platform one can still deploy Gemini models including text and diffusion, embeddings, and video generation. For the Alpaca project, I will use Vertex Vector Search with Gemini-001 Text Embeddings and Gemini 2 or 3 LLM initially. To generate embeddings on a BigQuery table, I ran the following command. ML.GENERATE_EMBEDDINGS is the older function that requires some GCP IAM magic. For new development I would use AI.GENERATE_EMBEDDINGS, which allows seamless IAM authentication and will support streaming new table data into the embeddings table, in the near term.

So, the Generative AI RAG journey begins with SQL on BigQuery. Actually, it began with SQLite, Go's `net/http`, Object Relational Mapping (ORM) and data ingestion.  To upload my SQL data to BigQuery I chose to use the GO Vertex SDKs and I honestly don't recommend it. The Go Python SDKs are far more mature, better documented, and it's easy to navigate and find answers to issues you find along the way. Even using `gcloud ai` and `gcloud bigquery` CLI commands was more productive and reliable than deciphering the sparse mix of Marketing, API Docs, Structs, and Protobuffers which constitute the Go Vertex AI SDKs. Hopefully this will change in the future as GenAI adoption rapidly increases and the need for performant software is paramount.

In short, I used the standard `*bigquery.Client` nested in a Go struct with my metadata to upload the City, IATA, Hotel, and Review data to BigQuery. This part works well. For generating embeddings, you can attempt to use the SDK to run queries, revert to Python where it will just work, or use the trusty GCP BigQuery console to execute. Since these are one-time queries, I just did that and will iterate to coding the embedding process if and when the need for streaming arises. 

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
    `<project-id>>.alpacaCentral.hotels` AS h
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
Vertex Vector Search is a partially managed Vector Database as a service, to which we can import our vector embeddings from Big Query or GCS Buckets. The import process is partially documented in at least 5 different documentation paths and was not easy to figure out at first. When creating a Vector Search Index you are required to provide a GCS Bucket path which contains `json, parquet, avro` files but you can ignore that and just create it or provide a dummy path and then import for BigQuery.  The key input information is the BigQuery embeddings table and the metadata which Vertex Vector Search Index requires in json form.

##### importIndex.json
    
    "name": "projects/<project-id>/locations/<location>>/indexes/<index-id>",
        "isCompleteOverwrite": <true|false>,
        "config": {
            "bigQuerySourceConfig": {
            "tablePath": "bq://<project-id>>.<dataset-id>>.<embeddings_table_name>",
            "datapointFieldMapping": {
            "idColumn": "id",
            "embeddingColumn": "embedding",
            "restricts": [
                {
                "namespace": "<field_name>",
                "allowColumn": ["allow_field_name"]
                },
                {
                "namespace": "<other_field_name>",
                "allowColumn": ["<allow_other_field_name>"]
                }],
            "metadataColumns": [...]
            }
        }
    }
    


Once data is imported to an Index, we verify the `dense vector count` and create Index Endpoint to query for similarity searches. This gives a medium level of control and flexibility where we can choose the text embedding model, batch size, metadata, query restrict filter columns, shard size, machineType, and auto-scaling configuration of each IndexEndpoint. I chose to use the latest Gemini-001 text embeddings model, using 3072 vector dimensions over the older text-embedding-004 per the Google Docs that deprecate the latter. Both are really good and based on Google's original 2020 [ScaNN whitepaper](https://research.google/blog/announcing-scann-efficient-vector-similarity-search/). 

Once an index exists, we can upload data to it from BigQuery using the following command and configuration. This can best be done with Python in a Github Actions (or Google Cloudbuild) pipeline because the equivalent Go SDK is not fantastic yet.  For one-time or batch processes a Python pipeline or even Pulumi in Go is the better alternative. We'll stick to Go for querying endpoints, orchestrating LLM calls, serving HTTP, traditional database CRUD, BigQuery CRUD, OpenTelemetry, and other performant real-time and per-request tasks.

    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "@vertex/importIndex.json" \
    "https://<location>-aiplatform.googleapis.com/v1beta1/projects/<project-id>/locations/<location>/indexes/<index-id>:import"


    

#### What success looks like

Upon successful import, the operations query endpoint will return done: true. The Index will show a Dense Vector Count that should match the number of records in the BigQuery embeddings table. Sources of errors include mismatched BigQuery table schema, duplicate IDs, and other issues. By default BigQuery does not enforce a primaryKey or unique constraint on `id` fields so this is a common pitfall for iterative uploads from local database to BigQuery.

    Using endpoint [https://<location>-aiplatform.googleapis.com/]
    done: true
    metadata:
    '@type': type.googleapis.com/google.cloud.aiplatform.v1beta1.UpdateIndexOperationMetadata
    genericMetadata:
    createTime: '2026-03-14T06:58:03.768807Z'
    updateTime: '2026-03-14T07:28:16.694113Z'
    nearestNeighborSearchOperationMetadata:
    contentValidationStats:
    - sourceGcsUri: gs://caip-tenant-values>/values>/bq-export/<values>/export-000000000001.json
    validRecordCount: '12086'
      - sourceGcsUri: gs://caip-tenant-<values>/values>/bq-export/values>/export-000000000000.json
      validRecordCount: '12126'
      name: projects/<values>/locations/<location>>/indexes/<index-id>>/operations/756618008847187968
      response:
      '@type': type.googleapis.com/google.cloud.aiplatform.v1beta1.Index
      createTime: '2026-03-13T22:50:07.506856Z'
      description: Alpaca Hotel Reviews Embedding with Gemini-001
      displayName: alpacaReviewsGemini001
      encryptionSpec: {}
      etag: AMEw9yMa4E1giqL87OSEKrMOgQvF6V0yPc2pdlMTO3Wpd11TgnhdOYfw9hdokoxLd6o3
      indexStats:
      shardsCount: 1
      indexUpdateMethod: BATCH_UPDATE
      metadata:
      config:
      algorithmConfig:
      treeAhConfig:
      fractionLeafNodesToSearch: 0.05
      leafNodeEmbeddingCount: '1000'
      approximateNeighborsCount: 10
      dimensions: 3072
      distanceMeasureType: DOT_PRODUCT_DISTANCE
      featureNormType: NONE
      shardSize: SHARD_SIZE_SMALL
      metadataSchemaUri: gs://google-cloud-aiplatform/schema/matchingengine/metadata/nearest_neighbor_search_1.0.0.yaml
      name: projects/<project>>/locations/<location>/indexes/<index-id>>
      updateTime: '2026-03-13T22:53:18.342670Z'

In a future blog post I will describe in greater detail the MLops steps and pipeline for:

1. Creating a BigQuery table with embeddings
2. Creating a Vertex AI Vector Search Index
3. Uploading embeddings to the Index
4. Deploying an Index Endpoint with Go Pulumi

We will also cover the basics of setting up OpenTelemetry to gather trace and metrics of our Embedding, Gemini LLM prompt completion, HTTP server, and API calls.

### Google Vertex AI Search
The fully managed Google Vertex AI Search offering doesn't yet allow Gemini-001 and only has the older models for embeddings. The AI Search can be used for similarity search, but essentially is more appropriate for website indexing and navigating a large body of text rather than for similarity RAG searches. It does not allow the flexibility of choosing embedding models, fine-tuning your own data columns for search filters, autoscaling of nodes, and using a single node IndexEndpoint for testing.

### Google Vertex RAG Engine
There is also the Vertex AI RAG Engine, which is a fully managed service that can be used to build RAG systems as well. RAG Engine and AI Search both take input from GCS Buckets, JSON documents, even things like Jira or other information platforms. The RAG engine handles the heavy lifting of embedding and indexing and is more expensive and less configurable. It also signified that you are tied-in to Google Vertex platform whereas with Vector Search, I can eventually replace it with AWS Sagemaker and AWS Aurora Vector Database for embeddings and Bedrock for the Index, or a Weaviate Vector Database. I could also use non-Google text embedding model if that becomes a priority. 

### GO SDK Support
The Go Libraries calls for Vector Search Index crud, Embeddings generation, and IndexEndpoint are not too well documented. There are two or three alternative functions and corresponding data structs for almost every function call. Mostly because each is an iteration of autogenerated code from OpenAPI specs, Vertex Go SDK was spit up into feature-specific libraries but the main SDK continues to be developed also. Probably a majority of developers use the Vertex Python/Typescript SDK or middleware such as Pulumi, LangChain depending on which component of the system they are working on.

I use Pulumi Go for the infrastructure aspects such as creating one-time resources (BigQuery Table, Index, IndexEndpoint, Kubernetes Cluster, App Engine Deployment, etc.), `gcloud` CLI commands orchestrated with Bash scripts for development and Python SDK in a pipeline for any recurring data operations that will run on a continuous schedule.

The below Go SDK-based codebase takes an HTML form input via Gin HTTP server. It then does the following:


1. Generates a 3072 dimension vector embedding for the question with Gemini-001 embeddings model.
2. Queries a deployed Vertex AI Vector Search IndexEndpoint for the nearest neighbors including search filters.
3. Feeds the resulting nearest neighbor results and metadata into a custom LLM prompt to generate a verified response of the top 3 results.

    
GenerateEmbedding converts a user question string into a 3072-dimensional vector using Gemini embedding model

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

I will use the Go SDK "cloud.google.com/go/aiplatform/apiv1" for Vertex AI Vector Search RAG similarity lookup. To convert a user question into a vector array I used the Go SDK for Generative AI "google.golang.org/genai".

{{< emoji accordion >}}

This project is under active development, please check back soon for updates, demos, and further detailed how-to's.
