from db import clientPS
#from schema import producte

def consulta():
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute("select * from public.product")
        data=cur.fetchone()
        #data=producte.product_schema(data)
    except Exception as e:
        return(f"Hi ha hagut un problema: {e}")
    finally:
        conn.close()
        return(f"Consulta de: {e}")