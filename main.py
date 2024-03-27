from typing import Union
from fastapi import FastAPI
from model import Product
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
def createProduct(prod:Product.Product):
    return productDB.insertProduct(prod)

# ESBORRA EL PRODUCTE SEGONS ID
@app.delete("/product/{id}")
def deleteProductByID(id):
    return productDB.deleteProductByID(id);

# ACTUALITZA EL PRODUCTE SEGONS ID
@app.put("/product/{id}")
def updateProductByID(prod:Product.Product):
    return productDB.updateProductByID(prod);

