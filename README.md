# DAY_18_CSV_OS
# ContactBook

**ContactBook** is a Python command-line application to manage personal or professional contacts. It allows you to add, view, search, update, delete, count contacts, and open the CSV file directly in Excel.

## Features
- Add a contact (name + 10-digit phone number, prevents duplicates)  
- View all contacts  
- Search for a contact by name  
- Update contact phone number  
- Delete a contact  
- Count total contacts  
- Open contacts CSV in Excel  

## Requirements
- Python 3.x  
- Windows OS (for `os.startfile` to open Excel)  

## Usage
1. Clone or download the repository.  
2. Make sure the CSV path exists and is correctly set in the code:
```python
book = ContactBook("E:\\TEST\\CONTACT.csv")

