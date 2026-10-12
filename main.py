from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Hello FastAPI!"}


@app.get("/hello")
def say_hello():
    return "Hello, FastAPI!"


@app.get("/info")
def get_info():
    return {
        "name": "Hello FastAPI",
        "version": "1.0",
        "description": "My first FastAPI application"
    }


@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mouse"},
        {"id": 3, "name": "Keyboard"}
    ]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Item {item_id}"
    }