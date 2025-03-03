# AlpacaStreaming

Pipeline to stream alpaca market data from Python API to GCP BigQuery.

## Features

- Stream market data from Alpaca API.
- Integrate and store data in Google Cloud Platform's BigQuery.
- Configurable using YAML files.

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
   Create a configuration file `api.yaml` with your Alpaca API credentials. Remember to keep these private and never feature them in a repository!:
   ```yaml
   Key: 'YourAlpacaAPIKey'
   Secret: 'YourAlpacaAPISecret'
   ```

## Usage

Run the main script to start streaming data:
```bash
python main.py
```

This will set up the connection to the Alpaca API and start streaming data for the configured stock symbol (e.g., 'AAPL').

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
```

