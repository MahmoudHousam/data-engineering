# You Need to Know

This file aims at instructing the user to have the following setup:

- Chocolatey
- Make
- Dokcer
- Terraform
- Google Cloud SDK
- Create GCP account and set configurations for your project

## Installing Chocolatey

- Install with powershell.exe

- With PowerShell, you must ensure Get-ExecutionPolicy is not Restricted. We suggest using Bypass to bypass the policy to get things installed or AllSigned for quite a bit more security.

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
- Set up Application Default Credentials (ACD). Just write this command in your terminal `gcloud auth application-default login`. For more detailed info, visit the [ACD Offecial Documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc?_gl=1*1bnte70*_ga*MTkyNzM4MTU5Ni4xNzA0MDMzOTc3*_ga_WH2QY8WWF5*MTcxMTA3NTEyMy4yNC4xLjE3MTEwNzk2NjguMC4wLjA.&_ga=2.15902966.-1927381596.1704033977)
- Create a service account key using the Google Cloud console, the gcloud CLI, the `serviceAccounts.keys.create()` method, or one of the [client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries). A service account can have up to 10 keys. For more detailed info, visit the [Service Account Keys Offecial Documentation](https://cloud.google.com/iam/docs/keys-create-delete?_gl=1*1bnte70*_ga*MTkyNzM4MTU5Ni4xNzA0MDMzOTc3*_ga_WH2QY8WWF5*MTcxMTA3NTEyMy4yNC4xLjE3MTEwNzk2NjguMC4wLjA.&_ga=2.15902966.-1927381596.1704033977)
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

- Add these roles in addition to Viewer : **Storage Admin + Storage Object Admin + BigQuery Admin**

- Enable these APIs for your project:

  - [IAM API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
  - [IAM API Cradentials](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)

- Please ensure GOOGLE_APPLICATION_CREDENTIALS env-var is set.

  ```
  export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
  ```