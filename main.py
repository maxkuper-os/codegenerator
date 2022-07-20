from fastapi import FastAPI
from schemas import InputData
from hash import Generator
app = FastAPI()



@app.post('/')
def home(item: InputData):
    salt = Generator.generate_salt(item.saltLenght)
    password = Generator.generate_pass(item.passLenght)
    hashcode = Generator.generate_hash(salt,password)
    return {"salt": salt,"password": password,"hash": hashcode}
