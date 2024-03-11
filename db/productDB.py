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

# INTERNAL ERROR, NO SÉ PAS EN QUE M'EQUIVOCO. 
def updateProductByID(id:int):
    try:
        conn = clientPS.client()

        cur = conn.cursor()
        
        cur.execute(f"""UPDATE public.product
                        SET name='{name}', 
                            description='{desc}', 
                            company='{company}', 
                            price={price}, 
                            units={units}, 
                            subcategory_id={subCate},
                            updated_at=CURRENT_TIMESTAMP
                        WHERE product_id={id}""")

        
        conn.commit()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto añadido"