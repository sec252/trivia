from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from app import app, db
from app.models.users import User
from app.models.trivia import TriviaPool, Trivia
from app.models.category import Category
from app.utils.seed import seed_db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.add(
        User(
            username="admin",
            password=generate_password_hash("admin"),
            role="ADMIN",
        )
    )
    db.session.commit()


@cli.command("seed_db")
def seed():
    seed_db()


if __name__ == "__main__":
    cli()
