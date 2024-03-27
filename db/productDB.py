from db import clientPS
from schema import producte
import json

keys=['product_id', 'name', 'description', 'company', 'price', 'units', 'subcategory_id', 'created_at', 'updated_at']

def transformJSON(datas):
    resultJson=[]
    for data in datas:
        count=0
        result={}
        for key in keys:
            result[key] = data[count]    
            count+=1
        resultJson.append(result)
    return resultJson

def getAllProducts():

    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"select * from public.product")
        data = cur.fetchall()
        result = transformJSON(data)
        return result
    except Exception as e:
        return f'Error connexió: {e}'
    finally:
        conn.close()

def productByID(id:int):

    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"select * from public.product where product_id={id}")
        data = cur.fetchone()
        result = transformJSON(data)
        return result
    except Exception as e:
        return f'Error connexió: {e}'
    finally:
        conn.close()

def insertProduct(prod):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({prod.id}, '{prod.name}', '{prod.description}', '{prod.company}', '{prod.price}', '{prod.unit}', '{prod.subcategory_id}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")
        conn.commit()
        return f"Producte afegit"
    except Exception as e:
        return f'Error connexió: {e}'
    finally:
        conn.close()

def deleteProductByID(id:int):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"DELETE from public.product where product_id={id}")
        conn.commit()
        return f"Producte eliminat"
    except Exception as e:
        return f'Error connexió: {e}'
    finally:
        conn.close()


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
        return f"Producte afegit"
    except Exception as e:
        return f'Error connexió: {e}'
    finally:
        conn.close()

def allProducts():
    try:
        conn= clientPS.client()
        cur = conn.cursor()
        cur.execute("""SELECT 
                    c.name AS categoria,
                    s.name AS subcategoria,
                    p.name AS nom_producte,
                    p.company AS marca_producte,
                    p.price AS preu
                    FROM product p
                    JOIN 
                    subcategory s ON p.subcategory_id = s.subcategory_id
                    JOIN 
                    category c ON s.category_id = c.category_id;""")
        data= cur.fetchall()
        return data
    except Exception as e:
        conn.rollback()
        return f'Error connexió: {e}'
    finally:
        conn.close()