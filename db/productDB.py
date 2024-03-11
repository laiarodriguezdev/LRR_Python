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

def insertProduct(prod):
    try:
        conn = clientPS.client()

        cur = conn.cursor()
        
        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({prod.id}, '{prod.name}', '{prod.description}', '{prod.company}', '{prod.price}', '{prod.unit}', '{prod.subcategory_id}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

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

def updateProductByID(prod):
    try:
        conn = clientPS.client()

        cur = conn.cursor()
        
        cur.execute(f"""UPDATE public.product
                        SET name='{prod.name}', 
                            description='{prod.description}', 
                            company='{prod.company}', 
                            price={prod.price}, 
                            units={prod.unit}, 
                            subcategory_id={prod.subcategory_id},
                            updated_at=CURRENT_TIMESTAMP
                        WHERE product_id={prod.id}""")

        
        conn.commit()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto añadido"