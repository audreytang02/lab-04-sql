import os
import logging
import pandas as pd
import mysql.connector

logging.basicConfig(level=logging.INFO)

type_mapping = {
    "int64": "BIGINT",
    "int32": "INT",
    "float64": "DOUBLE",
    "bool": "TINYINT(1)",
    "datetime64[ns]": "DATETIME",
    "object": "VARCHAR(255)",  # safe default varchar length
    "string": "VARCHAR(255)",
}


def read_data(filename):
    """Load CSV into a pandas DataFrame."""
    logging.info("Reading data from CSV...")
    return pd.read_csv(filename)

def clean_data(data):
    """Remove rows with missing values and return cleaned DataFrame."""
    logging.info("Cleaning data (dropping rows with missing values)...")
    cleaned = data.dropna()
    logging.info(f"Rows before: {len(data)}, after cleaning: {len(cleaned)}")
    return cleaned

def load_data(data, table):
    """Create table if needed and upload DataFrame to MySQL."""
    logging.info("Connecting to database...")

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database=os.getenv("DBNAME")
        )
        cursor = conn.cursor()

        # Build CREATE TABLE statement
        logging.info("Creating table if it does not exist...")
        cols = []
        for col, dtype in data.dtypes.items():
            sql_type = type_mapping.get(str(dtype), "VARCHAR(255)")
            cols.append(f"`{col}` {sql_type}")

        create_stmt = f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(cols)});"
        cursor.execute(create_stmt)

        logging.info("Uploading rows...")
        placeholders = ", ".join(["%s"] * len(data.columns))
        insert_stmt = f"INSERT INTO {table} VALUES ({placeholders})"

        for _, row in data.iterrows():
            cursor.execute(insert_stmt, tuple(row.values))

        conn.commit()
        logging.info("Upload complete.")

    except Exception as e:
        logging.error(f"Error during upload: {e}")

    finally:
        cursor.close()
        conn.close()
        logging.info("Database connection closed.")

def main():
    df = read_data("MOCK_DATA.csv")
    cleaned = clean_data(df)
    load_data(cleaned, "mock")

if __name__ == "__main__":
    main()