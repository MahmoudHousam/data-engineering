# Module Setup

- Mage

# Objectives:

By the end of this module, you should be able to:

- Build Mage image provided by mage-ai.
- Deploy a CSV file to a GCP bucket with Mage.

# Installing Mage Instance

- `git clone git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp`
- `cp dev.env .env && rm dev.env` to create a copy of dev.env and then remove it.
- `docker compose build` to build the image
- `docker compose up -d` to run Mage locally
- Now, navigate to http://localhost:6789 in your browser!
- This should have the following structure
  ```
  ├── mage_data
  │   └── magic-zoomcamp
  ├── magic-zoomcamp
  │   ├── __pycache__
  │   ├── charts
  │   ├── custom
  │   ├── data_exporters
  │   ├── data_loaders
  │   ├── dbt
  │   ├── extensions
  │   ├── interactions
  │   ├── pipelines
  │   ├── scratchpads
  │   ├── transformers
  │   ├── utils
  │   ├── __init__.py
  │   ├── io_config.yaml
  │   ├── metadata.yaml
  │   └── requirements.txt
  ├── Dockerfile
  ├── README.md
  ├── dev.env
  ├── docker-compose.yml
  └── requirements.txt
  ```
