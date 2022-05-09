from typing import TYPE_CHECKING, List
import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def save_question(question: dict, db: 'Session') -> _schemas.Question:
    question = _models.Question(**question)
    db.add(question)
    db.commit()
    db.refresh(question)
    return _schemas.Question.from_orm(question)


async def get_all_questions(db: 'Session') -> List[_schemas.Question]:
    questions = db.query(_models.Question).all()
    return list(map(_schemas.Question.from_orm, questions))


async def check_question(question_id: int, db: 'Session'):
    question = db.query(_models.Question).filter(_models.Question.question_id == question_id).first()
    print('question is None=',  question is None)
    print('question_id=', question_id)
    return question is not None






