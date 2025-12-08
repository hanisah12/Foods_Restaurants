
from pydantic import BaseModel

class Rest(BaseModel):
    res_name: str
    status_check: bool
    rating: int
    address: str