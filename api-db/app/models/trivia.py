from app import db


class TriviaPool(db.Model):
    __tablename__ = "trivia_pool"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    @property
    def questions(self):
        all_questions = Trivia.query.filter(Trivia.trivia_pool_id == self.id).all()
        return all_questions


class Trivia(db.Model):
    __tablename__ = "trivia"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(128), unique=True, nullable=False)
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
