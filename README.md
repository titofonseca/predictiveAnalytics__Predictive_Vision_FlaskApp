# Predictive Vision: Sculpting the Future by Merging UA's Past and GA4 Present through Prophet's Precision Analysis

## Introduction

On August 1, 2023, the analytics landscape underwent a transformative shift. Google transitioned from the legacy-rich Universal Analytics (UA) to the dynamic innovations of Google Analytics 4 (GA4). This shift, while heralding groundbreaking features, presented an intricate puzzle: How do we craft a forward-looking predictive vision by merging the invaluable e-commerce revenue chronicles of UA with GA4's contemporary insights? In the realm of predictive analytics, the depth and continuity of data sculpt the foundation for precise and actionable forecasts.

## The Importance of Time Series Forecasting

### Time Series Forecasting: The Concept

Time series forecasting serves as the lens to the future, enabling us to predict forthcoming values based on historical data. By analyzing temporal patterns, it crafts informed projections about what lies ahead. Its significance is paramount, especially for temporally sequenced data such as monthly sales or daily online traffic.

### Why We Use Time Series Forecasting

In the ever-evolving world of e-commerce, deciphering sales trajectories is paramount. Time series forecasting offers a visionary tool, enabling businesses to predict and prepare for both sales crescendos and decrescendos. By illuminating what might lie ahead, it empowers businesses with proactive strategy formulation.

### Enter Prophet

Hailing from Facebook's innovation labs, Prophet stands as a vanguard in time series forecasting. Tailored to address the intricacies of daily datasets—be it missing entries or influential holidays that sway sales—Prophet carves a niche in crafting dependable forecasts amidst intricate seasonality.

### How Prophet Will Work With Our Data

When Prophet is entrusted with our harmonized UA and GA4 data, it gains a panoramic view of the e-commerce revenue landscape. Prophet meticulously sculpts this data, pinpointing patterns and rhythms, employing these insights to craft future projections. Its inherent adaptability guarantees precision, even amidst the challenge of amalgamating two distinct data sources.

## The Challenge: Bridging the Data Divide

GA4's debut marked the dawn of an advanced analytics epoch, infused with state-of-the-art tools and a fresh paradigm. Yet, this inception was accompanied by a data chasm. The rich e-commerce revenue narratives from UA, encapsulating years of consumer interactions and growth trajectories, faced integration challenges with GA4. Bridging these disparate timelines was paramount, ensuring that our predictive vision stood on a robust foundation of historical insights.

## Our Approach: Weaving Past and Present into a Cohesive Data Tapestry

In the realm of analytics, data continuity is the cornerstone. With reverence for UA's archival depth and GA4's cutting-edge insights, our mission was crystal-clear: weave these diverse data strands into a singular, coherent narrative. This fusion of UA's historical wisdom with GA4's modern-day revelations birthed a unified, holistic timeline. This enriched dataset not only amplifies the precision of our predictions but also deepens our comprehension, paving the way for businesses to envision e-commerce revenue trends with unprecedented clarity and conviction.

## The Outcome: A Panoramic Perspective for Precise Predictions

The alchemy of blending historical profundity with contemporary immediacy presents businesses with a holistic vista of their revenue arc. This seamless data continuum links archival patterns with present-day vigor, rendering a lucid snapshot of the e-commerce terrain. Empowered by this expansive view, businesses can sculpt decisions rooted in both historical wisdom and current momentum. This profound understanding allows enterprises to not only decipher past performance tales but also chart a well-informed trajectory towards burgeoning growth and opportunities.

## Visualizing and Interpreting Predictions
While Prophet's time series forecasting offers a visionary glimpse into potential revenue horizons, it's imperative to interpret these predictions judiciously for strategic orchestration.

### Key Considerations:

#### Comparative Analysis: 
Contrast "Real Sales" with "Predicted Sales" in visual representations to gauge prediction fidelity and to detect emergent patterns.

#### Confidence Intervals:
The "Lower Bound" and "Upper Bound" sketches a spectrum within which actual sales might oscillate. While "Predicted Sales" offers a focused estimate, these bounds paint a broader canvas of potential realities.

#### Potential Anomalies: 
Occasional rifts between "Real Sales" and "Predicted Sales" might surface, influenced by unforeseen dynamics. Embrace these deviations as learning moments, refining subsequent forecasts.

#### Strategic Action Points:
Scour for intervals characterized by heightened sales predictions, identifying them as golden opportunities. While exact numerics might be elusive, these moments signify heightened sales propensities, making them prime for strategic maneuvers.

In essence, while predictions sculpt a visionary roadmap, they aren't absolute. Engage with them as guiding beacons, incorporate the delineated confidence spectra, and stay agile, ready to pivot based on real-time data fluctuations and evolving scenarios.


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

These APIs allow us to fetch data from Google Analytics 4, Universal Analytics and manipulate Google Sheets.

To enable the Google Analytics Data API (for GA4):

1. Navigate to `APIs & Services` > `Library`.
2. Search for "Google Analytics Data API" and select it.
3. Click "Enable".


To enable the Google Analytics Reporting API (for UA):

1. Go back to `APIs & Services` > `Library`.
2. Search for "Google Analytics Reporting API" and select it.
3. Click "Enable".

To enable the Google Sheets API:

1. Go back to `APIs & Services` > `Library` once more.
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