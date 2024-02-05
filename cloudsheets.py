import gspread
import sqlite3
import pandas
from oauth2client.service_account import ServiceAccountCredentials

def insertSheet(data_list,sheet_name):
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('./credential.json', scope)
        gc = gspread.authorize(credentials)
        spreadsheet_id = '1hato2fVEn8jPVdEaSVh_nJWcf__Gw4KkDlUzeaqIbXI'
        sheet = gc.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(sheet_name)
        rows_to_append = [data_list]
        worksheet.append_rows(rows_to_append)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

def updateSheet(new_values, value_to_update, column_name, sheet_name):
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('./credential.json', scope)
        gc = gspread.authorize(credentials)
        spreadsheet_id = '1hato2fVEn8jPVdEaSVh_nJWcf__Gw4KkDlUzeaqIbXI'
        sheet = gc.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(sheet_name)
        # Get the column names (header row) and find the index of the specified column
        header_row = worksheet.row_values(1)
        column_index = header_row.index(column_name) + 1
        # Get all values in the specified column
        column_values = worksheet.col_values(column_index)
        # Find the row index where the value matches
        row_index = next((i for i, value in enumerate(column_values, start=1) if value == value_to_update), None)
        if row_index:
            # Update the values in the found row
            for j in range(len(new_values)):
                worksheet.update_cell(row_index, column_index + j, new_values[j])
            print(f"Row with {value_to_update} updated successfully.")
        else:
            print(f"No row found with {value_to_update}.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def deleteSheet(value_to_delete, column_name, sheet_name):
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('./credential.json', scope)
        gc = gspread.authorize(credentials)
        spreadsheet_id = '1hato2fVEn8jPVdEaSVh_nJWcf__Gw4KkDlUzeaqIbXI'
        sheet = gc.open_by_key(spreadsheet_id)
        worksheet = sheet.worksheet(sheet_name)
        # Get the column names (header row) and find the index of the specified column
        header_row = worksheet.row_values(1)
        column_index = header_row.index(column_name) + 1
        # Get all values in the specified column
        column_values = worksheet.col_values(column_index)
        # Find the row index where the value matches
        row_index = next((i for i, value in enumerate(column_values, start=1) if value == value_to_delete), None)
        if row_index:
            # Delete the entire row based on the found index
            worksheet.delete_rows(row_index)
            # Shift all below data one row up
            for i in range(row_index + 1, worksheet.row_count + 1):
                values_to_shift_up = worksheet.row_values(i)
                # worksheet.update_row(i - 1, values_to_shift_up)
                break
            print(f"Row with {value_to_delete} deleted successfully and data shifted up.")
        else:
            print(f"No row found with {value_to_delete}.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

