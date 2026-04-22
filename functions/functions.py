__all__ = ["simple_get","get_static_variable","get_dynamic_variable"]

def simple_get():
    return {"message": "HelloW orld"}

def get_static_variable(var: int):
    return {"message": f"Your Input: {var}"}

def get_dynamic_variable(var: int | None):
    returnVal = {}
    if var:
        if var == 1:
            returnVal = {"message": "You have input: One"}
        elif var == 2:
            returnVal = {"message": "You have input: Two"}
        else:
            returnVal = {"message": "You have input something else"}

    else:
        returnVal = {"message": "You have not input anything"}

    return returnVal