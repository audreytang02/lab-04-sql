import os
import logging
import mysql.connector

logging.basicConfig(level=logging.INFO)

def get_data_by_group(value):
    """
    Return all rows where the `group` column equals the given value.
    Uses a parameterized query to avoid SQL injection.
    """
    logging.info(f"Querying rows where group = {value!r}")

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database=os.getenv("DBNAME")
        )
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM mock WHERE `group` = %s"
        cursor.execute(query, (value,))
        results = cursor.fetchall()

        logging.info(f"Returned {len(results)} rows.")
        return results

    except Exception as e:
        logging.error(f"Error in get_data_by_group: {e}")
        return []

    finally:
        cursor.close()
        conn.close()


def plot_counts(groupby):
    """
    Count rows grouped by the given column name.
    Example: plot_counts('city') → counts rows per city.
    """
    logging.info(f"Counting rows grouped by column: {groupby}")

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASS"),
            database=os.getenv("DBNAME")
        )
        cursor = conn.cursor()

        query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`"
        cursor.execute(query)
        results = cursor.fetchall()

        logging.info("Counts retrieved successfully.")
        return results

    except Exception as e:
        logging.error(f"Error in plot_counts: {e}")
        return []

    finally:
        cursor.close()
        conn.close()


def main():
    print("\n=== Example: get_data_by_group('A') ===")
    rows = get_data_by_group("A")
    for r in rows[:5]:
        print(r)

    print("\n=== Example: plot_counts('group') ===")
    counts = plot_counts("group")
    for value, count in counts:
        print(f"{value}: {count}")


if __name__ == "__main__":
    main()
