from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.orders import Orders
from models.order_items import OrderItems
from schemas.orders import OrderSchema

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


# GET
@orders_router.get("/")
def get_all_orders(dbs: Session = Depends(connect_to_db)):
    orders_list = dbs.query(Orders).all()
    return orders_list


@orders_router.post("/")
def create_an_order(new_order: OrderSchema, dbs: Session = Depends(connect_to_db)):
    adding_an_order = Orders(
        user_id=new_order.user_id,
        rest_id=new_order.rest_id,
        total_amount=new_order.total_amount,
    )

    dbs.add(adding_an_order)

    dbs.commit()

    dbs.refresh(adding_an_order)
    return {"message": "new order created"}


# GET by ID
@orders_router.get("/{id}")
def get_orders_by_id(id:int,dbs: Session = Depends(connect_to_db)):
    find_order = dbs.query(Orders).filter(Orders.id == id).first()
    
