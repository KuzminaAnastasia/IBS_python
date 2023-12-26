from fastapi import FastAPI, UploadFile
from ex1.ex1 import calculate_average_age_by_position

app = FastAPI()


@app.post("/calculate_average_age_by_position")
async def calculate_average_age(file: UploadFile = UploadFile(...)):
    data = calculate_average_age_by_position(file)
    return {"average_ages": data}