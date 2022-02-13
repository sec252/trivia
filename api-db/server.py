from flask.cli import FlaskGroup

from app import app, db
from app.models.users import User
from app.models.trivia import TriviaPool


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(username="admin"))
    db.session.add(TriviaPool(name="Tets trivia"))
    db.session.commit()


if __name__ == "__main__":
    cli()
