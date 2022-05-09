import datetime as _dt
import pydantic as _pydantic


class Question(_pydantic.BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: _dt.datetime

    class Config:
        orm_mode = True





