# -*- coding: utf-8 -*-
"""General Google Sheets Updater"""

# Install dependencies
!pip install gspread pandas openpyxl numpy --quiet

import gspread
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from google.colab import drive
from oauth2client.service_account import ServiceAccountCredentials

# ========= USER CONFIGURATION =========
# Load credentials and settings (replace with your own)
CREDENTIALS_JSON = "/path/to/your/credentials.json"
SHEET_NAME = "Your Google Sheet Name"
DATA_DIR = "/path/to/your/data/files/"
FILE_PATTERNS = {  # Map file patterns to sheet names
    "sales_data*.csv": "Sales",
    "marketing*.xlsx": "Marketing"
}
# ======================================

# Authenticate and load sheet
def authenticate():
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON, scope)
    return gspread.authorize(creds)

def process_files(data_dir, patterns):
    """Rename and load files based on user-defined patterns."""
    for filename in os.listdir(data_dir):
        for pattern, sheetname in patterns.items():
            if pattern in filename:
                new_name = f"{sheetname.lower().replace(' ', '_')}.csv"
                os.rename(os.path.join(data_dir, filename), 
                          os.path.join(data_dir, new_name))
                print(f"Renamed {filename} to {new_name}")
                return pd.read_csv(os.path.join(data_dir, new_name))
    return None

def update_sheet(worksheet, data, start_row):
    """Update sheet with DataFrame data."""
    worksheet.resize(rows=start_row + len(data))
    worksheet.update(
        f"A{start_row}", 
        data.values.tolist(), 
        value_input_option="USER_ENTERED"
    )

# Main workflow
def main():
    drive.mount('/content/drive')  # For Colab; adjust for local use
    gc = authenticate()
    df = process_files(DATA_DIR, FILE_PATTERNS)
    
    if df is not None:
        sh = gc.open(SHEET_NAME)
        worksheet = sh.worksheet("Data")  # Specify your target sheet
        last_row = len(worksheet.get_all_values()) + 1
        update_sheet(worksheet, df, last_row)
        print("Sheet updated successfully!")

if __name__ == "__main__":
    main()