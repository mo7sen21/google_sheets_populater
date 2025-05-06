# Automated Google Sheets Updater

A general-purpose script to automate data updates in Google Sheets.

## Features
- Upload CSV/Excel files to Google Sheets.
- Customizable file-to-sheet mappings.
- Handles authentication via Google Service Accounts.

## Setup
1. **Install Dependencies**:
pip install gspread pandas openpyxl numpy


2. **Google Cloud Setup**:
- Create a Service Account and download its JSON key.
- Share your Google Sheet with the service account email.

3. **Configuration**:
- Update `CREDENTIALS_JSON` with your key path.
- Modify `FILE_PATTERNS` to match your file naming conventions.

## Usage
1. Place your data files in `DATA_DIR`.
2. Run the script. Files will be renamed and uploaded automatically.

## Customization
- Extend `process_files()` for advanced data transformations.
- Modify `update_sheet()` for custom sheet formatting.
