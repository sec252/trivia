from tkinter.filedialog import SaveFileDialog
from app import db
import datetime
from app.models.category import Category
from app.models.users import User


class TriviaPool(db.Model):
    __tablename__ = "trivia_pool"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    plays = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"TriviaPool({self.name})"

    @property
    def questions(self):
        all_questions = Trivia.query.filter(Trivia.trivia_pool_id == self.id).all()
        return all_questions

    @property
    def category(self):
        category = Category.query.filter(Category.id == self.category_id).first()
        return category.name

    @property
    def author(self):
        author = User.query.filter(User.id == self.creator_id).first()
        return author


class Trivia(db.Model):
    __tablename__ = "trivia"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(128), nullable=False)
    answer = db.Column(db.String(128), nullable=False)
    trivia_pool_id = db.Column(
        db.Integer, db.ForeignKey("trivia_pool.id"), nullable=False
    )
    trivia_pool = db.relationship(
        "TriviaPool", backref=db.backref("trivias", lazy=True)
    )

    def __init__(self, text, answer, trivia_pool_id):
        self.text = text
        self.answer = answer
        self.trivia_pool_id = trivia_pool_id


class TriviaUserPlays(db.Model):
    __tablename__ = "trivia_user_plays"
    trivia_id = db.Column(
        db.Integer, db.ForeignKey("trivia_pool.id"), nullable=False, primary_key=True
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, primary_key=True
    )
    plays = db.Column(db.Integer, default=0)


class TriviaUserScores(db.Model):
    __tablename__ = "trivia_user_scores"
    id = db.Column(db.Integer, primary_key=True)
    trivia_id = db.Column(db.Integer, db.ForeignKey("trivia_pool.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    wrong = db.Column(db.Integer, nullable=False)
    correct = db.Column(db.Integer, nullable=False)
    played_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def score(self):
        total = self.wrong + self.correct
        print("TOTAL: ", total)

        score = round((self.correct / total) * 100)
        print("SCORE:", score)
        return score


class TriviaIPPlay(db.Model):
    __tablename__ = "trivia_ip_plays"
    trivia_id = db.Column(
        db.Integer, db.ForeignKey("trivia_pool.id"), nullable=False, primary_key=True
    )
    ip = db.Column(db.String(128), nullable=False, primary_key=True)
    plays = db.Column(db.Integer, default=0)
