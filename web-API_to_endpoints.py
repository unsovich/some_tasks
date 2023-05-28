from fastapi import FastAPI

app = FastAPI()


@app.get("/api/endpoint1")
def endpoint1():
    data = {'message': 'Hello, endpoint 1!'}
    return data


@app.post("/api/endpoint2")
def endpoint2(name: str):
    data = {'message': f'Hello, {name}!'}
    return data


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=8002)
