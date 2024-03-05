from db import client
from schema import producte

def consulta():

    try:
        conn = client.db_client()

        cur = conn.cursor()

        cur.execute("select * from public.product")

        data = cur.fetchone()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"

def consultaById(id:int):

    try:
        conn = client.db_client()

        cur = conn.cursor()

        cur.execute("select * from public.product")

        data = cur.fetchone()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"



def insertProduct(id,name,desc,company,price,units,subCate):
    try:
        conn = client.db_client()

        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({id}, '{name}', '{desc}', '{company}', '{price}', '{units}', '{subCate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

        conn.commit()
           
        # data = cur.fetchone()

        # data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto añadido"



def update():
    try:
        conn = client.db_client()

        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({id}, '{name}', '{desc}', '{company}', '{price}', '{units}', '{subCate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

        conn.commit()
           
        # data = cur.fetchone()

        # data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto añadido"