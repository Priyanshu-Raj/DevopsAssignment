#importing various modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

apps = FastAPI()

# Define a data model for the request body
class CalculationRequest(BaseModel):
    operation: str
    num1: float
    num2: float

@apps.post("/calculate")
async def calculate(request: CalculationRequest):
    """
    Perform a calculation based on the operation specified.
    Operations supported: add, subtract, multiply, divide.
    """
    num1 = request.num1
    num2 = request.num2
    operation = request.operation.lower()

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation. Use add, subtract, multiply, or divide.")

    return {"operation": operation, "num1": num1, "num2": num2, "result": result}

@apps.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Calculator API. Use the /calculate endpoint to perform operations."}
