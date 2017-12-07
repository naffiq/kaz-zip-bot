## KazZipBot

Телеграм бот, который поможет вам узнать свой почтовый индекс по адресу
[https://t.me/kzZipBot](https://t.me/kzZipBot)

### Установка и запуск

> ⚠️ Проект написан на Python3.6 и не проверялся на второй версии.

Установите зависимости с `pip`:

```bash
$ pip install -r requirements.txt
```

Запросите `token` телеграм бота у [BotFather](https://t.me/botfather) и вставьте его в файл `.env`.
Пример `.env` можно взять из файла `.env.example`:

```bash
$ cp .env.example .env
```

После чего обновить данные в нем, вставив свой `token`.

Запустите `main.py` с python:

```bash
$ python main.py
```

После этого можно начать отправлять боту адрес и получать ответы.