from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import requests

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

URL = 'https://jservice.io/api/random?count='


@app.post('/load_questions')
async def load_questions(questions_num: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    questions_list = get_questions(questions_num)
    message = await save_question(questions_list, db=db)
    return message


def get_questions(questions_num: int):
    response = requests.get(f'{URL}{questions_num}')
    questions_list = response.json()
    return questions_list


@app.get('/questions', response_model=List[_schemas.Question])
async def get_all_questions(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_questions(db=db)


async def save_question(questions_list, db: 'Session'):
    message = ''
    counter = 0

    for question_map in questions_list:
        question_map = dict(question_map)
        question = {'question_id': question_map["id"],
                    'question': question_map['question'],
                    'answer': question_map['answer'],
                    'created_at': question_map['created_at']
                    }
        # # проверяю есть ли поле в таблице
        if await _services.check_question(question_id=question['question_id'], db=db):
            counter += 1
            continue

        await _services.save_question(question=question, db=db)

    if counter != 0:
        await save_question(get_questions(counter), db=db)
        message += f'Вместо уже существующих было загружено {counter} вопроса(ов). '

    message += '[INFO] Данные успешно загружены'
    return message


