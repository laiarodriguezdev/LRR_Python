from typing import Union
from fastapi import FastAPI

from model.Product import Product
from db import clientPS
from db import productDB

app = FastAPI()

# AGAFA TOTS ELS PRODUCTES
@app.get("/product/")
def getAllProducts():
    return productDB.getAllProducts()

# LLEGEIX I MOSTRA NOMÉS EL PRODUCTE SEGONS ID
@app.get("/product/{id}")
def productByID(id):
    return productDB.productByID(id)

# AFEGEIX EL PRODUCTE
@app.post("/product/")
def createProduct(prod: Product):
    return productDB.insertProduct(prod.id,prod.name,prod.description,prod.company,prod.price,prod.unit,prod.subcategory_id)

# ESBORRA EL PRODUCTE SEGONS ID
@app.delete("/product/{id}")
def deleteProductByID(id):
    return productDB.deleteProductByID(id);

# ACTUALITZA EL PRODUCTE SEGONS ID  --------- NO FUNCIONA
@app.put("/product/{id}")
def updateProductByID(id:int, prod:Product):
    return productDB.updateProductByID(id, prod);

