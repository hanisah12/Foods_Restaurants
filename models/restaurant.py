from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class res_info(Base):
    __tablename__ = "restaurant"

    rest_id = Column(Integer, primary_key=True, index=True)
    res_name = Column(String)
    status_check = Column(Boolean)
    rating=Column(Integer)
    address=Column(String)
