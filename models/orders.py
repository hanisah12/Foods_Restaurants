from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Orders(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    total_amount = Column(Integer)

    # cart_items = relationship("OrderItems",back_populates="order_items")
    

    # # foreign key
    # user_id = Column(Integer, ForeignKey("customers.id"))
    # rest_id = Column(Integer, ForeignKey("restaurants.id"))
    # # relationship with parent table
    # customer = relationship("Customers")
    # restaurants = relationship("Restaurants")

    