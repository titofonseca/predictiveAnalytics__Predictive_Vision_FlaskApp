# Bridge Analytics: Continuous Timeline from UA's Legacy to GA4's Innovation with Prophet's Time Series Forecasting

## Introduction

On August 1, 2023, Google unveiled a new era in analytics by transitioning 
from the well-established Universal Analytics (UA) to the more dynamic 
Google Analytics 4 (GA4). This move, while introducing advanced features, 
posed a challenge: seamlessly merging the rich e-commerce revenue history 
in UA with GA4. In predictive modeling, the depth and continuity of data 
are key elements for generating accurate and dependable forecasts.

## The Importance of Time Series Forecasting

### Time Series Forecasting: The Concept

Time series forecasting is a statistical technique used to predict future 
values based on past data. It analyzes patterns over time to make informed 
estimates about future occurrences. This method is especially valuable for 
data with a temporal sequence, like monthly sales or daily website visits.

### Why We Use Time Series Forecasting

In e-commerce, tracking sales trends is crucial. Time series forecasting 
provides a way to visualize and predict these trends, helping businesses 
anticipate sales spikes and drops. Knowing what might happen tomorrow, 
next week, or next month allows for proactive decision-making.

### Enter Prophet

Developed by Facebook, Prophet is a robust tool for time series forecasting. 
Designed to handle daily datasets' nuances, like missing values or major 
holidays that can impact sales, Prophet excels in generating reliable 
forecasts, even with complex seasonality.

### How Prophet Will Work With Our Data

By feeding Prophet our merged UA and GA4 data, we give it a comprehensive 
view of e-commerce revenue trends. Prophet will scrutinize this data, 
identify patterns or seasonality, and use these insights to forecast 
future trends. Its adaptability ensures accurate predictions, even when 
integrating two different data sources.

## The Challenge: Bridging the Data Divide

The GA4 launch signified a new analytics era, equipped with advanced tools 
and fresh perspectives. However, this beginning came with a challenge. 
The extensive e-commerce revenue data in UA, which captured years of user 
behaviors, seasonal trends, and business growth, didn't automatically 
integrate into GA4. This gap made merging these two distinct timelines 
crucial to ensure future predictions had a solid foundation based on 
past patterns.

## Our Approach: Weaving Past and Present into a Cohesive Data Tapestry

In analytics, continuity is vital. Valuing UA's historical data and GA4's 
modern insights, our goal was clear: intertwine these separate data threads 
into a unified narrative. By combining UA's extensive history with GA4's 
contemporary insights, we created a continuous, holistic data timeline. 
This comprehensive dataset not only strengthens our predictions but also 
enhances our understanding, allowing businesses to anticipate e-commerce 
revenue trends with greater clarity and confidence.

## The Outcome: A Panoramic Perspective for Precise Predictions

Merging past depth with present immediacy offers businesses a panoramic 
view of their revenue trajectory. This seamless insight flow connects 
historical patterns with current momentum, providing a clear e-commerce 
landscape view. This broad perspective enables businesses to make decisions 
anchored in past experiences and present trends. With this enhanced 
understanding, companies can not only interpret past performance narratives 
but also navigate a more informed path towards future growth and opportunities.

# Time Series Forecasting with Prophet and Google Analytics

## Table of Contents

1. [Prerequisites and Installations](#prerequisites-and-installations)
2. [Google Services Configuration](#google-services-configuration)
3. [Access Settings](#access-settings)
4. [Development Environment Setup](#development-environment-setup)
5. [Local Configuration and Execution](#local-configuration-and-execution)

## 1. Prerequisites and Installations

Before diving in, ensure you've set up the required tools and accounts.

### 1.1 Google Account

You'll need a Google Account to access various Google services.

If you don't have one, [create it here](https://accounts.google.com/signup).

### 1.2 Python Installation

Our tool runs on Python.

If Python isn't installed on your machine, [download and install the latest version here](https://www.python.org/downloads/).

### 1.3 Visual Studio Code

We recommend using Visual Studio Code as the code editor for this project.

If you don't have VSCode, [download and install it here](https://code.visualstudio.com/). After installation, open VSCode and install the Microsoft `Python` extension from the Extensions marketplace.

### 1.4 Git Installation

We'll use Git to clone the repository and manage versions.

If Git isn't installed on your machine, follow the instructions appropriate for your operating system:

- **Windows**: `choco install git`
- **MacOS**: `brew install git`
- **Linux**: `sudo apt-get install git`

### 1.5 Google Cloud Platform (GCP) Account

You'll need a GCP account to set up and access Google APIs.

If you don't have a GCP account, [sign up here](https://cloud.google.com/).

## 2. Google Services Configuration

### 2.1 Google Cloud Platform (GCP)

#### 2.1.1 Create a Project

Start by creating a dedicated project space for this application.

1. Log into the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project dropdown in the top bar and then select "New Project".
3. Name your project and click "Create".

#### 2.1.2 Enable APIs

These APIs allow us to fetch data from Google Analytics and manipulate Google Sheets.

To enable the Google Analytics Data API:

1. Navigate to `APIs & Services` > `Library`.
2. Search for "Google Analytics Data API" and select it.
3. Click "Enable".

To enable the Google Sheets API:

1. Go back to `APIs & Services` > `Library`.
2. Search for "Google Sheets API" and select it.
3. Click "Enable".

### 2.2 Service Account Credentials on GCP

This step ensures secure API interactions.

1. Navigate to `APIs & Services` > `Credentials`.
2. Click "Create Credentials" and select "Service account".
3. Name your service account and grant it either the "Editor" or "Owner" role.
4. Click "Done".
5. Under the "Actions" column (three dots), click "Manage keys".
6. Click "Add Key", then select "JSON". This will prompt a key download.
7. Rename the downloaded file to `service_account_file.json`.

## 3. Access Settings

### 3.1 Grant Service Account Email Access to UA and GA4

To ensure our tool accesses the necessary data, grant the appropriate permissions.

1. Access your Google Analytics account (both UA and GA4).
2. Navigate to the user management section.
3. Add the email associated with your GCP service account (found in the `client_email` field of the downloaded JSON file).
4. Ensure this service account has read and analyze permissions.

### 3.2 Google Sheets Configuration

1. [Make a copy of the Google Sheet template by clicking here](https://docs.google.com/spreadsheets/d/1jW-eY7GjnrEBg6PHd_h76NEJDfR3rm_uxZputKPfTfE/copy).
2. Note the Google Sheet ID from its URL (the long string between `/d/` and the next `/`).
3. Open the copied Google Sheet.
4. Click "Share" in the top right corner.
5. Enter the email address associated with your GCP service account.
6. Click "Send".

## 4. Development Environment Setup

This section is about setting up the development environment on your local machine.

### 4.1 Clone Repository

1. Open your terminal or command prompt.
2. Clone the repository using the command:

    ```
    git clone [YOUR_REPOSITORY_LINK]
    ```

### 4.2 Setting Up a Python Virtual Environment

A virtual environment provides an isolated environment for our project:

1. Inside the terminal or command prompt, navigate to the directory where you cloned the repository.
2. Create a new virtual environment:

    ```
    python -m venv venv
    ```
3. Activate the virtual environment:
      - **Windows**: 
        ```
        .\venv\Scripts\activate
        ```
      - **MacOS/Linux**:
        ```
        source venv/bin/activate
        ```

### 4.3 Install Required Python Packages

Once the virtual environment is activated, you'll need to install the necessary Python packages:

1. Use the following command to install the required packages from the `requirements.txt` file:

```
pip install -r requirements.txt
```

## 5. Local Configuration and Execution

### 5.1 Configure `.env` File

Setting up local environment variables is crucial for our project to run smoothly:

1. Navigate to the root of the project directory.
2. Create a new file named `.env`.
3. Populate the file with the necessary variables, such as `GOOGLE_SHEETS_ID`, `GA4_PROPERTY_ID`, `UA_VIEW_ID`, and the path to `service_account_file.json` in `GOOGLE_SERVICE_KEY_PATH`.

Example format:

    ```
    GOOGLE_SERVICE_KEY_PATH=path_to_your_service_account_file.json
    GA4_PROPERTY_ID=your_ga4_property_id
    UA_VIEW_ID=your_ua_view_id
    GOOGLE_SHEETS_ID=your_google_sheet_id
    ```

### 5.2 Position and Rename Service Account Key

To interact with Google's APIs, the service account key is essential:

1. Place the `service_account_file.json` in the root directory of the project.

### 5.3 Running the Main Script

With everything set up, you're now ready to fetch, analyze, and predict data using Prophet with Universal Analytics and Google Analytics 4:

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Execute the main script:

    ```
    python main.py
    ```

If you've followed all steps, your setup should be complete. Run the script and observe the analytics and predictions. In case of any issues, refer to the troubleshooting section or raise an issue in the repository.



