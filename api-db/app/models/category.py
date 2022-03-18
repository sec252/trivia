from app import db
from slugify import slugify


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    slug = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        if not "slug" in kwargs:
            kwargs["slug"] = slugify(kwargs.get("name", ""))
        super().__init__(*args, **kwargs)
