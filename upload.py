import pandas as pd
import psycopg2

# Replace these with your actual file path and Supabase URI
csv_file_path = 'protel\Data\distance2.csv'
supabase_uri = 'postgres://postgres.vsjaooaxfprqgizgwgiz:lulusprotelsem7aamiin@aws-0-us-east-1.pooler.supabase.com:5432/postgres'

# Read CSV file
df_distances = pd.read_csv(csv_file_path)

# Connect to Supabase/PostgreSQL database using the URI
conn = psycopg2.connect(supabase_uri)
cur = conn.cursor()

# Insert data into "distances" table
for _, row in df_distances.iterrows():
    # Construct the SQL INSERT statement dynamically
    columns = ', '.join(row.index)
    placeholders = ', '.join(['%s'] * len(row))
    sql = f"INSERT INTO distance ({columns}) VALUES ({placeholders})"
    values = tuple(row)

    try:
        cur.execute(sql, values)
        conn.commit()  # Commit after each insert
        print("Data inserted successfully")
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        print(f"Failed to insert data: {e}")

# Close the cursor and connection
cur.close()
conn.close()
