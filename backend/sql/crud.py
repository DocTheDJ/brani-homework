from sqlalchemy.orm import Session
from . import models, schemas

# these are all kinda selfexplanatory

def get_orders(db: Session):
    return db.query(models.Order).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_tags(db:Session):
    return db.query(models.Tag).all()

def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def add_tag_to_order(db: Session, link: schemas.OrderTagCreate):
    tmp = models.OrderTag(**link.model_dump())
    db.add(tmp)
    db.commit()
    db.refresh(tmp)
    return tmp

def delete_link(db: Session, order: schemas.Order, tag: schemas.Tag):
    # get the link where order_id is order.id and where tag_id is tag.id
    wanted = db.query(models.OrderTag).where(models.OrderTag.order_id == order.id).where(models.OrderTag.tag_id == tag.id)
    if not (wanted := wanted.first()):
        return False
    #delete
    db.delete(wanted)
    db.commit()
    return True

def delete_tag(db: Session, tag_id: int):
    wanted = db.query(models.Tag).where(models.Tag.id == tag_id).limit(1)
    if not (wanted := wanted.first()):
        return False
    db.delete(wanted)
    db.commit()
    return True