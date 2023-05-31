import asyncio
from fastapi import FastAPI
import datetime

app = FastAPI()


async def ticker():
    while True:
        print("Tick", datetime.datetime.now().strftime("%H:%M:%S"))  # секунды
        await asyncio.sleep(1)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ticker())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

