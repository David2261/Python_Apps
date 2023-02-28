# Aiogram Bot
*Бот приветствует по нику, потом просит ввести номер. Этот номер проверяется на серваке, после ответ возвращается в телегу, типо: "Бик зур рэхмет - Большое спасибо". Ах да номер и ник записывается в БД*


## Tools
- Python 3.9
- Debian
- Aiogram 2.25.1
- Django 4.1
- Telegram API ❤️🤍💚

## Setup
1. Нужно создать файл: 
```bash
.env
```
2. Нужно в нем написать и токен создается в телеге, у бота FatherBot:
```bash
API_TELEGRAM_TOKEN="YOUR-TOKEN-FROM-TELEGRAM"
```
## Install
1. Лучше использовать [Poetry](https://python-poetry.org/ "Залетай посмотри...")
```bash
poetry install
source .venv/bin/activate
```
2. Ну или как старпЁры, через pip
```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

