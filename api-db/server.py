from unicodedata import category
from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from app import app, db
from app.models.users import User
from app.models.trivia import TriviaPool, Trivia
from app.models.category import Category


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
    seed_db()


# @cli.command("seed_db")
def seed_db():
    db.session.add(Category(name="Food"))
    db.session.add(Category(name="Sports"))
    db.session.add(Category(name="Games"))
    db.session.add(TriviaPool(name="Splitgate", category_id=3, creator_id=1))
    db.session.add(
        Trivia(text="Who is the best in splitgate", answer="david", trivia_pool_id=1)
    )
    db.session.add(
        Trivia(
            text="What do you do after you kill an enemy",
            answer="Teabag",
            trivia_pool_id=1,
        )
    )
    db.session.add(
        Trivia(
            text="What is the game mode that we play the most",
            answer="Showdown",
            trivia_pool_id=1,
        )
    )
    db.session.commit()


if __name__ == "__main__":
    cli()
