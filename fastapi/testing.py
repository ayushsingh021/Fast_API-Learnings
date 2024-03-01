from fastapi import FastAPI

app = FastAPI()

#at going to this url
@app.get("/ayush") 

#this function runs
async def first_api():
    return {"message" : "Hello Ayush"}