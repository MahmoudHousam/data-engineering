terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.21.0"
    }
  }
}


provider "google" {
  project = "resounding-node-418001"
  region  = "us-central1"
}

resource "google_storage_bucket" "de-cloud-practice" {
  name          = "node-418001-terra-practice"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "create_demo" {
  dataset_id = "bq_demo_01"
}