from db import clientPS
from schema import producte

def getAllProducts():

    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"select * from public.product")

        data = cur.fetchall()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error connexió: {e}'
    
    finally:
        conn.close()
        return f"[{data}]"

def productByID(id:int):

    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"select * from public.product where product_id={id}")

        data = cur.fetchone()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error connexió: {e}'
    
    finally:
        conn.close()
        return f"{data}"

def insertProduct(id,name,desc,company,price,units,subCate):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({id}, '{name}', '{desc}', '{company}', '{price}', '{units}', '{subCate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

        conn.commit()
        
    except Exception as e:
        return f'Error connexió: {e}'
    
    finally:
        conn.close()
    
    return f"Producte afegit"

def deleteProductByID(id:int):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"DELETE from public.product where product_id={id}")

        conn.commit()
        
    except Exception as e:
        return f'Error connexió: {e}'
    
    finally:
        conn.close()
    
    return f"Producte eliminat"

def updateProductByID(id:int):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"UPDATE from public.product where product_id={id}")

        conn.commit()
        
    except Exception as e:
        return f'Error connexió: {e}'
    
    finally:
        conn.close()
    
    return f"Producte modificat"