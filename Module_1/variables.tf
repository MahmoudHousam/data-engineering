variable "credentials" {
  description = "GCP Credentials"
  default     = "./keys/gcp_creds.json"
}


variable "project" {
  description = "Project"
  default     = "resounding-node-418001"
}


variable "location" {
  description = "Project Location"
  default     = "US"
}


variable "region" {
  description = "Region"
  default     = "us-central1"
}


variable "bq_basic_dataset" {
  description = "BigQuery Basic Dataset"
  default     = "bq_demo_01"
}


variable "gcp_bucket_name" {
  description = "GCP Bucket"
  default     = "node-418001-terra-practice"
}