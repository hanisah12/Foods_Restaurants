from fastapi import APIRouter,Depends
from schemas.restaurant import Rest
from db.database import Base,engine
from dependencies import connect_db
from sqlalchemy.orm import session
from models.restaurant import res_info


res_router =APIRouter(
    prefix="/restaurant",
    tags=["restaurant"]
)

@res_router.get("/")
def get_all_products(dbs:session=Depends(connect_db)):
    all_product=dbs.query(res_info).all()
    return all_product

    

# get({id})
@res_router.get("/{id}")
def all_products_by_id(id:int):
    return {"message":"update all succesfully"}

#post
@res_router.post("/")
def create_products(new_res:Rest, dbs:session=Depends(connect_db)):
    new_entry=res_info(
        res_name=new_res.res_name,
        status_check=new_res.status_check,
        rating=new_res.rating,
        address=new_res.address

    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)

    

#put
@res_router.put("/{id}")
def update_products(id:int,changed:Rest,dbs:session=Depends(connect_db)):
    changes=dbs.query(res_info).filter(res_info.id==id).first()
    if not changes:
        return {"message":"invalid id"}
    changes.res_name=changed.res_name
    changes.status_check=changed.status_check ,
    changes.rating=changed.rating,
    changes.address=changed.address
    dbs.add(changes)
    dbs.commit()
    dbs.refresh(changes)
    
#delete
@res_router.delete("/{id}")
def delete_products(id:int,dbs:session=Depends(connect_db)):
    deleted=dbs.query(res_info).filter(res_info.id==id).first()
    if not deleted:
        return {"message":"invalid id"}
    dbs.delete(deleted)
    dbs.commit()
   
    return {"message":"id deleted succesfully"}










