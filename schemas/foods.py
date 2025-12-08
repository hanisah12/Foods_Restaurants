from pydantic import BaseModel

class Foods_schemas(BaseModel):
    food_name: str
    price: int
    qty: int
    availability: bool



    



    

    