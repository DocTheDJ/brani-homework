from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

#create database
models.Base.metadata.create_all(bind=engine)

#create API
app = FastAPI()

#put settings to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# yield DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# different URLs for the api and their functions

@app.post("/orders/", response_model=schemas.OrderCreate)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/", response_model=list[schemas.OrderChildren])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db=db)

@app.post("/tags/", response_model=schemas.TagCreate)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)

@app.get("/tags/", response_model=list[schemas.TagChildren])
def get_tags(db: Session = Depends(get_db)):
    return crud.get_tags(db=db)

@app.post("/link/", response_model=schemas.OrderTagCreate)
def create_link(link: schemas.OrderTagCreate, db: Session = Depends(get_db)):
    return crud.add_tag_to_order(db=db, link=link)

@app.post("/delink/")
def delete_link(order: schemas.Order, tag: schemas.Tag, db: Session = Depends(get_db)):
    if crud.delete_link(db=db, order=order, tag=tag):
        return Response(status_code=status.HTTP_200_OK)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    if crud.delete_tag(db=db, tag_id=tag_id):
        return Response(status_code=status.HTTP_200_OK)
    return Response(status_code=status.HTTP_404_NOT_FOUND)