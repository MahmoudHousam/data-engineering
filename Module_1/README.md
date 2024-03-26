# Module Setup

This file aims at instructing the user to have the following setup:

- Chocolatey
- Make
- Dokcer
- Terraform
- Google Cloud SDK
- Create GCP account and set configurations for your project

## Installing Chocolatey

Install with powershell.exe:

- With PowerShell, you must ensure `Get-ExecutionPolicy` is not `Restricted`. We suggest using Bypass to bypass the policy to get things installed or AllSigned for quite a bit more security.

- Run `Get-ExecutionPolicy`. If it returns `Restricted`, then run `Set-ExecutionPolicy AllSigned` or `Set-ExecutionPolicy Bypass -Scope Process`.

- Now run the following command:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Paste the copied text into your shell and press Enter.
Wait a few seconds for the command to complete.
If you don't see any errors, you are ready to use Chocolatey! Type `choco` or `choco -?`

## Installing Dokcer

`choco install docker-desktop`

## Installing Terrform

`choco install terraform`

## Download Google Cloud SDK

Open a PowerShell terminal and run the following PowerShell commands:

```

(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe

```

## Create Google Cloud Platform (GCP) account

- Create a GCP account with your Gmail account
- Setup your first project. Read the bold notes provided by Google and keep a careful eye on it.
- Set up Application Default Credentials (ACD). Use these commands in your terminal to create the ACD file

  - `gcloud init`
  - `gcloud auth application-default login`.

  For more detailed info, visit the [ACD Offecial Documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc?_gl=1*1bnte70*_ga*MTkyNzM4MTU5Ni4xNzA0MDMzOTc3*_ga_WH2QY8WWF5*MTcxMTA3NTEyMy4yNC4xLjE3MTEwNzk2NjguMC4wLjA.&_ga=2.15902966.-1927381596.1704033977)

- Create a service account key following these steps:

  - **Before applying these steps, make sure to grant these roles: Service Account Key Admin, Service Account Token Creator**
  - From AIM and Admin list, navigate to the Service accounts page in the Google Cloud console and create your first service account.
  - Select the project and service account for which you want to create a key.
  - Click on the Keys tab and locate the Add key drop-down menu.
  - From the drop-down menu, choose the Create new key option.
  - Select JSON as the Key type and click the Create button. You can create up to 10 keys. A key is never expired but you can configure [an expiry date](https://cloud.google.com/resource-manager/docs/resource-settings/overview#iam-serviceAccountKeyExpiry).
  - Download the service account keys JSON file to use with [Terraform Google Porivder for GCP](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference)

- Set environment variable to point to your downloaded GCP keys:

  ```
  export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

  # Refresh token/session, and verify authentication
  gcloud auth application-default login
  ```

## Project Setup

IAM Roles for Service account:

- Go to the IAM section of [IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

- Click the Edit principal icon for your service account.

- Add these roles : **Storage Admin + Storage Object Admin + BigQuery Admin**

- Enable these APIs for your project:

  - [IAM API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
  - [IAM API Cradentials](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)

- Please ensure GOOGLE_APPLICATION_CREDENTIALS env-var is set.

  ```
  export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
  gcloud auth application-default login
  ```

## Terraform Setup

- Save the service account keys JSON file in you project repo. **Add it to `.gitignore` file**
- Create a `main.tf` file to save Terraform-GCP configurations.
- Copy-paste the following object in `main.tf` file:

  ```
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
  ```

- In project terminal, create an environment variable, Terraform guides users to name it `GOOGLE_CREDENTIALS` to be used later in Terraform Cloud service so that no need to hard-code your account service key. Follow the same guide locally:
  ```
  export GOOGLE_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
  ```
- Once finished, run `terraform init` to initialize basic Terraform infrastructure file in your project.

## Terraform infrastructure Setup Demo with GCP

The following example is a demo for creating a cloud storage backet on GCP.

- Instantiate a Terraform google_storage_bucket object in your `main.tf` file. An example:

  ```
  resource "google_storage_bucket" "auto-expire" {
    name          = "auto-expiring-bucket"
    location      = "US"
    force_destroy = true

    lifecycle_rule {
      condition {
        age = 3
      }
      action {
        type = "Delete"
      }
    }

    lifecycle_rule {
      condition {
        age = 1
      }
      action {
        type = "AbortIncompleteMultipartUpload"
      }
    }
  }
  ```

  Find more info and reference on [Terraform Registry | GCP Cloud Bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket)

- Type `terraform plan -out "name-your-plan"` (e.g. `terraform plan -out "gcb_storage_bucket_plan"`)
- Type `terraform apply "your-plan-name"`. Navigate to GCP|Cloud Storage page and see the newly bucket created.
- As this is for demonstration purposes only, remember to `terraform destroy` to delete the bucket.
- For plan-versioning and code review purposes, convert your terraform plan to a human-readable format via this command `terraform show -json "your_plan_name" | jq > your_plan_name.json`
  - `jq` is a command-line tool to filter and transform JSON data.

**Side note:** If you want to dive deep with `terraform plan`, check out [Create a Terraform Plan](https://developer.hashicorp.com/terraform/tutorials/cli/plan)
