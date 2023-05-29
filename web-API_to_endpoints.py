from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

subapi = APIRouter()


@subapi.get("/")
def get_users():
    return {"message": "Just main page"}


@subapi.get("/users")
def get_users():
    return {"message": "Get users"}


@subapi.post("/users")
def create_user():
    return {"message": "Create user"}


@app.get("/api/endpoint1")
def endpoint1():
    data = {'message': 'Hello, endpoint 1!'}
    return data


@app.post("/api/endpoint2")
def endpoint2(name: str):
    data = {'message': f'Hello, {name}!'}
    return data


@app.put("/api/endpoint3")
def endpoint3(name: str):
    data = {'message': f'Hello, {name}!'}
    return data


@app.delete("/api/endpoint4")
def endpoint4(name: str):
    data = {'message': f'Hello, {name}!'}
    return data


if __name__ == '__main__':
    import uvicorn

    app.include_router(subapi, prefix="/api")  # Подключаем суб-API к основному приложению FastAPI

    uvicorn.run(app, port=8002)
