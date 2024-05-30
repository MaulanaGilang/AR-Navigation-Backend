import pandas as pd
from sqlalchemy import create_engine

# Define your PostgreSQL URI connection string
db_uri = 'postgresql://postgres:lulusprotelsem7aamiin@db.vsjaooaxfprqgizgwgiz.supabase.co:5432/postgres'

# Path to your CSV file
csv_file = 'Distance_CSV.csv'

# Use Pandas to read data from the CSV file
data = pd.read_csv(csv_file)

# Create a SQLAlchemy engine for bulk data insertion
engine = create_engine(db_uri)

# Insert data into the PostgreSQL database
data.to_sql('distance', engine, if_exists='append', index=False)

print("Data has been seeded to the database.")
