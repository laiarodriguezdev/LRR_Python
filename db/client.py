import psycopg

def db_client():
    
    try:
        dbname = 'postgres'
        user = 'user_postgres'
        password = 'pass_postgres'
        host = 'localhost'
        port = '5432'
        
        return psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    except Exception as e:
        return{"status": -1, "message": f"Hi ha un problema: {e}"};
        
