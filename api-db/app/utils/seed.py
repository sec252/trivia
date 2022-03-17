from werkzeug.security import generate_password_hash
from app import app, db
from app.models.users import User
from app.models.trivia import TriviaPool, Trivia
from app.models.category import Category
import random


def seed_db():

    random_questions = []
    random_answers = []

    for x in range(1, 100):
        random_questions.append(f"This is a random #{x} question for this trivia")
        random_answers.append(f"This is a random #{x} answer")

    trivias = []
    for x in range(1, 10):
        db.session.add(
            User(username=f"user_{x}", password=generate_password_hash("password"))
        )
    db.session.commit()

    categories = ["Food", "General", "Games", "Coding", "Movies", "Anime"]
    trivia_titles = [
        {"cat_id": 1, "title": "Pizza"},
        {"cat_id": 1, "title": "Sushi"},
        {"cat_id": 1, "title": "Indian"},
        {"cat_id": 2, "title": "Shaped and Stuff"},
        {"cat_id": 2, "title": "Common Sense"},
        {"cat_id": 2, "title": "daily Life"},
        {"cat_id": 3, "title": "Splitgate"},
        {"cat_id": 3, "title": "COD"},
        {"cat_id": 3, "title": "Halo"},
        {"cat_id": 4, "title": "JavaScript"},
        {"cat_id": 4, "title": "Python"},
        {"cat_id": 4, "title": "Haskell"},
        {"cat_id": 5, "title": "Django"},
        {"cat_id": 5, "title": "Star Wars"},
        {"cat_id": 5, "title": "Step Brothers"},
        {"cat_id": 6, "title": "Hunter x Hunter"},
        {"cat_id": 6, "title": "Vinland Saga"},
        {"cat_id": 6, "title": "steins gate"},
    ]
    user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for c in categories:
        db.session.add(Category(name=c))

    db.session.commit()

    for t in trivia_titles:
        trivias.append(
            TriviaPool(
                name=t["title"].lower().title(),
                category_id=t["cat_id"],
                creator_id=random.choice(user_ids),
                plays=random.choice(range(1, 100)),
            )
        )

    db.session.bulk_save_objects(trivias)
    db.session.commit()

    all_trivias = TriviaPool.query.all()

    for t in all_trivias:
        for n in range(random.choice(user_ids)):
            db.session.add(
                Trivia(
                    text=random.choice(random_questions),
                    answer=random.choice(random_answers),
                    trivia_pool_id=t.id,
                )
            )
    db.session.commit()
