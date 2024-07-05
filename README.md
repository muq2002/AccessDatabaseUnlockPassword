# Access Database Data Extraction

This repository contains a Python script to extract data from an Access database without a password. The script connects to the database, retrieves table names, and allows exporting data to an Excel file.

## Requirements

- Python 3.x
- pyodbc
- pandas

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/access-db-extraction.git
   cd access-db-extraction
2. **Install Dependencies**
   ```sh
   pip install pyodbc pandas

## Notes
- Ensure the path to the Access database file (your_database.mde) is correct.
- Adjust the table name and output path as needed.
- The scripts assume the Access database does not require a password. If a password is needed, the connection string should be adjusted accordingly.

## License
This project is licensed under the MIT License.

### Explanation

1. **Requirements:** Lists the necessary software and libraries.
2. **Installation:** Provides steps to clone the repository and install dependencies.
3. **Usage:**
   - **Getting Table Names:** Includes a script to retrieve and print all table names.
   - **Exporting Data to Excel:** Includes a script to fetch data from a specific table and export it to an Excel file.
4. **Notes:** Provides additional information about paths and assumptions.
5. **License:** States the project's license.

This `README.md` file should help users understand how to use the scripts to interact with an Access database and extract data without requiring a password. Adjust paths, table names, and other details as needed for your specific use case.
