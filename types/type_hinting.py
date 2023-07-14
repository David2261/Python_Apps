from dataclasses import dataclass
import datetime


@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None
# :NextColorScheme

def validate_user_on_server(_): pass
def check_username(_): pass
def check_birthday(_): pass

def validate_user(user: User):
    """ Проверяет юзера, показывает исключения, если с ним что-то не так """
    validate_user_on_server(user)
    check_username(user)
    check_birthday(user)


