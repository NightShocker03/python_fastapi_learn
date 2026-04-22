from fastapi import FastAPI
from functions import functions

# Initialize FastAPI
api = FastAPI()

@api.get("/")                                               # http://localhost:8081/
def route_one():
    return functions.simple_get()

@api.get("/route_three/{var}")                              # http://localhost:8081/route_three/*int*
def route_two(var: int):
    return functions.get_static_variable(var)

@api.get("/route_three/")                                   # http://localhost:8081/route_three?someVar=*int*
def route_three(someVar: int):
    return functions.get_dynamic_variable(someVar)