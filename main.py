from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='Safety'
)

fake_users = [
    {'id': 1, 'role': 'standard', 'name': 'Дмитрий', 'connection': '88005553535'},
    {'id': 2, 'role': 'admin', 'name': 'Александр', 'connection': '89068350343'},
    {'id': 3, 'role': 'standard', 'name': 'Василий', 'connection': '89063843035'},
]


class User(BaseModel):
    id: int
    role: str
    name: str
    connection: str


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}
