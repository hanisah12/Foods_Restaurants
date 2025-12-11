from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Foods(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    price = Column(Integer)
    qty = Column(Integer)
    availability = Column(Boolean)
    #foreighnkey
    
    rest_info = Column(Integer, ForeignKey ("restaurants.id"))

    rest = relationship("Restaurants")


