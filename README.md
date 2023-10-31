# Time Series Forecasting with Prophet and Google Analytics 4

## Table of Contents

1. [Prerequisites and Installations](#prerequisites-and-installations)
2. [Google Services Configuration](#google-services-configuration)
3. [Google Sheets Setup](#google-sheets-setup)
4. [Development Environment Setup](#development-environment-setup)
5. [Local Configuration and Execution](#local-configuration-and-execution)

---

## 1. Prerequisites and Installations

Before starting, ensure that the necessary tools and accounts are set up. This section provides step-by-step guides on setting up these tools.

### 1.1 Google Account

- **Purpose**: Required to access Google services.
- **Steps**:
  1. Ensure you have a Google Account. If not, [create one here](https://accounts.google.com/signup).

### 1.2 Python Installation

- **Purpose**: The script is written in Python.
- **Steps**:
  1. If you don't have Python installed, [download and install](https://www.python.org/downloads/) the latest version.

### 1.3 Visual Studio Code

- **Purpose**: Preferred code editor for this project.
- **Steps**:
  1. If you don’t have VSCode, [download and install it](https://code.visualstudio.com/).
  2. Launch VSCode.
  3. Install the `Python` extension by Microsoft from the Extensions marketplace.

### 1.4 Git Installation

- **Purpose**: To clone the repository and manage versions.
- **Steps**:
  1. If you don't have Git, install it based on your operating system:
      - **Windows**: 
        ```
        choco install git
        ```
      - **MacOS**:
        ```
        brew install git
        ```
      - **Linux**:
        ```
        sudo apt-get install git
        ```

### 1.5 Google Cloud Platform (GCP) Account

- **Purpose**: To set up and access Google APIs.
- **Steps**:
  1. Ensure you have a GCP account. If not, [sign up here](https://cloud.google.com/).

---

## 2. Google Services Configuration

This section guides you through setting up necessary Google services.

### 2.1 Google Cloud Platform (GCP)

#### 2.1.1 Create a Project

- **Purpose**: A dedicated project space for this application.
- **Steps**:
  1. Log in to [Google Cloud Console](https://console.cloud.google.com/).
  2. Click on the project dropdown on the top bar, then "New Project".
  3. Name your project and click "Create".

#### 2.1.2 Enable APIs

- **Purpose**: To fetch data from Google Analytics and manipulate Google Sheets.
- **Steps**:
  1. **Enable Google Analytics Data API**:
      - Navigate to `APIs & Services` > `Library`.
      - Search for "Google Analytics Data API" and select it.
      - Click "Enable".
  2. **Enable Google Sheets API**:
      - Go back to `APIs & Services` > `Library`.
      - Search for "Google Sheets API" and select it.
      - Click "Enable".

### 2.2 Service Account Credentials on GCP

- **Purpose**: For secure API interactions.
- **Steps**:
  1. Navigate to `APIs & Services` > `Credentials`.
  2. Click on "Create Credentials" and select "Service account".
  3. Name your service account and grant it the role of "Editor" or "Owner".
  4. Click "Done".
  5. Under the "Actions" column (three dots), click "Manage keys".
  6. Click "Add Key" and select "JSON". This will download the key.
  7. Rename this downloaded file to `service_account_file.json`.

---

## 3. Google Sheets Setup

This section helps you set up Google Sheets for the application.

### 3.1 Duplicate Google Sheet Template

- **Purpose**: A template for our project.
- **Steps**:
  1. Click [here](https://docs.google.com/spreadsheets/d/1ejWZzSOpvC8WGEgvIWsrH-DKcXh0IFBsxfyk2sceVKE/copy) to create a copy of the Google Sheet template.
  2. Note the Google Sheet ID from its URL (it's the long string between `/d/` and the next `/`). This ID will be used later.

### 3.2 Grant Service Account Email Access

- **Purpose**: To allow our script to interact with the Google Sheet.
- **Steps**:
  1. Open the copied Google Sheet.
  2. Click on "Share" (top right).
  3. Enter the email address associated with your GCP service account (from `service_account_file.json` under "client_email").
  4. Click "Send".

---

## 4. Development Environment Setup

This section is about setting up the development environment on your local machine.

### 4.1 Clone Repository

- **Purpose**: To get the project's code.
- **Steps**:
  1. Open the terminal or command prompt.
  2. Run the following command:
    ```
    git clone [YOUR_REPOSITORY_LINK]
    ```

### 4.2 Python Virtual Environment

- **Purpose**: To create an isolated environment for Python packages.
- **Steps**:
  1. Navigate to the cloned directory.
  2. Create a virtual environment:
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

### 4.3 Install Required Packages

- **Purpose**: To get all the necessary Python packages.
- **Steps**:
  1. With the virtual environment activated, run:
    ```
    pip install -r requirements.txt
    ```

---

## 5. Local Configuration and Execution

This section provides steps to configure and run the project locally.

### 5.1 Configure `.env` File

- **Purpose**: To set up local environment variables.
- **Steps**:
  1. In the project directory, create a `.env` file.
  2. Set up the necessary variables such as `GOOGLE_SHEETS_ID`, `GA4_PROPERTY_ID`, and the path to `service_account_file.json`.

### 5.2 Position and Rename Service Account Key

- **Purpose**: To use the service account key for API calls.
- **Steps**:
  1. Place the `service_account_file.json` in the root of the project directory.

### 5.3 Run the Main Script

- **Purpose**: To fetch and analyze the data.
- **Steps**:
  1. In the terminal or command prompt, navigate to the project directory.
  2. Run the main script:
    ```
    python main.py
    ```

---

That's it! If you've followed each step, your environment should be set up, and you should be able to fetch and analyze data with Prophet and Google Analytics 4. If you face any issues, please check the troubleshooting section or raise an issue in the repository.