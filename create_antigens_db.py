import sqlite3
import csv
import os

# Define the path to the CSV file and the SQLite database
csv_file = "updated_antigens_csv.csv"
db_file = "antigens.db"

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table to store the antigen data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS antigens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        antigen_name TEXT,
        paper_title TEXT,
        paper_dois TEXT,
        organism_studied TEXT,
        type_of_work TEXT,
        brief_methodology TEXT,
        uniprot_ids TEXT,
        fasta TEXT
    )
''')

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        # Ensure the row has the expected number of columns
        if len(row) == 8:
            cursor.execute('''
                INSERT INTO antigens (
                    antigen_name, paper_title, paper_dois, organism_studied,
                    type_of_work, brief_methodology, uniprot_ids, fasta
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', row)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print(f"SQLite database '{db_file}' created successfully.")