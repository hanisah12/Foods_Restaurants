from pydantic import BaseModel


class OrderSchema(BaseModel):
    # user_id: int
    # rest_id: int
    order_id:int
    total_amount: int









