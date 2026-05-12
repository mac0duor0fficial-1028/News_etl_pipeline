import psycopg2
from configs.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def load_news(df_articles):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Creating an insert query with placeholders for parameterized queries to prevent SQL injection
        insert_query = """
        INSERT INTO articles_data (title, author, source_name, published_at, url, content, sentiment_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """ 
        # Define the columns to be inserted in the same order as the placeholders in the insert query
        columns_for_insertion = ["title", "author", "source_name", "published_at", "url", "content", "sentiment_score"]

        data_to_insert = []

        # Iterate through the DataFrame and prepare the data for insertion
        for _, row in df_articles.iterrows():
            row_values = []
            for col_key in columns_for_insertion:
                row_values.append(row.get(col_key))
            data_to_insert.append(tuple(row_values))

        # Execute the insert query for each row of data using executemany for batch insertion
        cursor.executemany(insert_query, data_to_insert)
        
        conn.commit()
    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()