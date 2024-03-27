import pandas as pd
from datetime import datetime
from db import clientPS

# Función para insertar datos en la tabla category
def insert_category(category_id, name):
    try: 
        conn= clientPS.client()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"""SELECT * FROM category WHERE category_id={category_id};""")
        if(cur.fetchone() is not None):
            cur.execute(f"""UPDATE category
                        SET category_id={category_id}, name='{name}', updated_at='{tiempo_actual}'
	                    WHERE category_id={category_id};""")
        else:
            cur.execute(f"INSERT INTO category (category_id, name, created_at, updated_at) VALUES ({category_id}, '{name}', '{tiempo_actual}', '{tiempo_actual}')")
        conn.commit()
    except Exception as e:
        return f'Error connexión: {e}'
    finally:
        conn.close()

# Función para insertar datos en la tabla subcategory
def insert_subcategory(subcategory_id, name, category_id):
    try:
        conn= clientPS.client()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"""SELECT * FROM subcategory WHERE subcategory_id={subcategory_id};""")
        if(cur.fetchone() is not None):
            cur.execute(f"""UPDATE subcategory
                        SET subcategory_id={subcategory_id}, name='{name}', category_id={category_id}, updated_at='{tiempo_actual}'
	                    WHERE category_id={category_id};""")
        else:
            cur.execute(f"INSERT INTO subcategory (subcategory_id, name, category_id, created_at, updated_at) VALUES ({subcategory_id}, '{name}', {category_id}, '{tiempo_actual}', '{tiempo_actual}')")
        conn.commit()
    except Exception as e:
        return f'Error connexión: {e}'
    finally:
        conn.close()


def insert_product(product_id, name, description, company, price, units, subcategory_id):
    try:
        conn= clientPS.client()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"""SELECT * FROM product WHERE product_id={product_id};""")
        if(cur.fetchone() is not None):
            cur.execute(f"""UPDATE product
                        SET product_id={product_id}, name='{name}', description='{description}', company='{company}', price={price}, units={units} , subcategory_id={subcategory_id}, updated_at='{tiempo_actual}'
	                    WHERE product_id={product_id};""")
        else:
            cur.execute(f"INSERT INTO product (product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({product_id}, '{name}', '{description}', '{company}', {price}, {units}, {subcategory_id}, '{tiempo_actual}', '{tiempo_actual}')")
        conn.commit()
    except Exception as e:
        return f'Error connexión: {e}'
    finally:
        conn.close()

def loadFile(fitcherCSV): 
    try:
        conn = clientPS.client()
        df = pd.read_csv(fitcherCSV.file, header=0 )
        
        for index, row in df.iterrows():
            fila= row.to_dict()
            
            insert_category(fila["id_categoria"], fila["nom_categoria"])
            insert_subcategory(fila["id_subcategoria"], fila["nom_subcategoria"], fila["id_categoria"])
            insert_product(fila["id_producto"], fila["nom_producto"], fila["descripcion_producto"], fila["companyia"], fila["precio"], fila["unidades"], fila["id_subcategoria"])

        conn.commit()
        return "Dades pujades"
    except Exception as e:
        return f'Error connexión: {e}'
    finally:
        conn.close()
