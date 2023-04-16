from sqlalchemy.orm import Session
from .models import Post


def get_post_list(db: Session):
    return db.query(Post).all()