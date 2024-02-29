import psycopg

def client():
    connection_string = """
        dbname=postgres
        user=user_postgres
        password=pass_postgres
        host=localhost
        port=5432
    """
    try:
        conn = psycopg.connect(connection_string)
    except Exception as e:
        print(f"Hi ha un problema: {e}");
        
