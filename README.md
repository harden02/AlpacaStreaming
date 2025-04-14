# AlpacaStreaming

Pipeline to stream alpaca market data from Python API to GCP BigQuery. In the future I am planning on using GCP DataFlow to transform the data and create some further features/rolling metrics.

## Features

- Stream market data from Alpaca API.
- Integrate and store data in Google Cloud Platform's BigQuery.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harden02/AlpacaStreaming.git
   cd AlpacaStreaming
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   Create a configuration file `api.yaml` with your Alpaca API credentials. Remember to keep these private and never feature them in a repository!
   Do the same with a `config.yaml` for your GCP Pub/Sub details:
   ```yaml
   Key: 'YourAlpacaAPIKey'
   Secret: 'YourAlpacaAPISecret'
   ```
   ```yaml
   projectId: "your-project-id"
   pubSubTopic: "your-topic-name"
   ```
4. **GCP Setup and Authentication:**
   Create a BigQuery table to act as a sink for your streamed data with the following schema:
   ```json
   {
    "name": "Type",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
   },
   {
    "name": "Symbol",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
   },
   {
    "name": "Open",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   },
   {
    "name": "High",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   },
   {
    "name": "Low",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   },
   {
    "name": "Close",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   },
   {
    "name": "Volume",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "",
    "fields": []
   },
   {
    "name": "Timestamp",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
   },
   {
    "name": "numTradeTickers",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   },
   {
    "name": "VolumeWeightedPrice",
    "mode": "NULLABLE",
    "type": "NUMERIC",
    "description": "",
    "fields": []
   }
   ```
   After this you need to set up a GCP Pub/Sub topic which has a service account that is Authenticated to write to BigQuery. This can be done either through the console or through the cloud shell with the           following:
   ```bash
   bq add-iam-policy-binding --member="serviceAccount:service-<project number>@gcp-sa-pubsub.iam.gserviceaccount.com" --role=roles/bigquery.dataEditor -t "<dataset>.<table>"
   ```
   From there you need to set up a BigQuery streaming subscription for the topic to be able to write data directly into BQ. View the documentation here: https://cloud.google.com/pubsub/docs/bigquery. Make sure to set the appropriate schema so that the topic can write to your BQ table. You'll also need to ensure it complies with the custom JSON object mapping in the `pubsubHandler.py` so that all schema titles match across the whole pipeline.

   You will then need to create a file holding your service account information so that the container can authenticate to GCP resources. Using the service account of your choice, navigate to it in the console under the service accounts tab and download a JSON key using the "add key" function. Place this JSON in your application and point to it in your dockerfile as an environment variable like below:
   ```bash
   ENV GOOGLE_APPLICATION_CREDENTIALS="your-svc-key.json"


## Usage

1. **Build the docker image:**
```bash
docker build -t <your-tag> .
```

2. **Verify it functions correctly locally:**
```bash
docker run <your-tag> 
```

3. **Upload your docker image to Google Artifact Registry:**
View the documentation here to learn how to authenticate docker with the Gcloud CLI and push images to GAR: https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling#whats_next

From there you can pull the image into a compute engine instance, and the program will begin streaming minute bars for your listed stocks and pushing the data to BigQuery through your specified Pub/Sub BigQuery subscription.
