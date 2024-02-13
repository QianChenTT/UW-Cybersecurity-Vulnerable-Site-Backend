from fastapi import FastAPI

#to run use uvicorn main:app --reload
#this is a test to action
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
