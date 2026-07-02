from fastapi import FastAPI
from day_1.calculator import Calculator

app = FastAPI()

calc = Calculator()

@app.get("/add")
def add(a: int, b: int):
    return {"result": calc.add(a, b)}

@app.get("/subtract")
def subtract(a: int, b: int):
    return {"result": calc.subtract(a, b)}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": calc.multiply(a, b)}

@app.get("/divide")
def divide(a: int, b: int):
    return {"result": calc.divide(a, b)}
 