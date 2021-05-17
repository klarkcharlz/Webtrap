from flask import Flask, make_response, request  # для создания нашего апи сервиса
from loguru import logger  # Для логирования
import argparse  # для парсинга аргументов командной строки, отлавливаем port


parser = argparse.ArgumentParser()  # парсер аргументов командной строки
parser.add_argument(
    '--port',
    type=int,
    default=5000,
    help='web service port (default: 5000)'
)  # аргумент порт
args = parser.parse_args()  # парсим

app = Flask(__name__)   # веб сервер

logger.add('Webtrap.log', format='{time} {level} {message}', level='DEBUG')  # логирование


@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def index(path):
    """Обрабатываваем любой url"""
    # вытаскиваем необходимые параметры
    method, url, args = request.method, request.base_url, dict(request.args)
    params = ", ".join(list(map(lambda t: f"{t[0]}={t[1]}", list(args.items()))))
    # Логгируются все входящие запросы
    logger.info(f" :\nreceived a request with a method {method} "
                + f"at the url {url} with arguments: {params if params else 'no arguments!'}")
    # Запрос с параметром invalid=1 (GET /any_url?invalid=1) обрабатывать и логгировать как ошибку
    # в случае если был передан параметр notawaiting=1, валидация должна вызывать ошибку и соответствующе логгироваться
    if args.get('invalid', None) == "1" or args.get('notawaiting', None) == "1":
        logger.error(f" :\nInvalid arguments in request!")
    # Методы запроса кроме GET валидировать и логгировать как ошибку
    if method != "GET":
        logger.error(f" :\nNot supported method: {method}")
    # Обработка запросов на path отличный от /api обрабатывать как ошибку
    if not request.url.startswith(request.url_root + "api/"):
        logger.error(f" :\nNot api url: {request.url}")

    res = make_response("<h1>Status: OK</h1>", 200)  # Приложение всегда отдаёт статус 200
    return res


if __name__ == "__main__":
    app.run(port=args.port)  # запуск приложения
