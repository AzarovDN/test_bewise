import datetime as _dt
import sqlalchemy as _sql
import database as _database


class Question(_database.Base):
    __tablename__ = 'question'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    question_id = _sql.Column(_sql.Integer, index=True)
    question = _sql.Column(_sql.String, index=True)
    answer = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow())
    