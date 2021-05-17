# Webtrap
Test task

Описание. Разработать простейшее вэб-приложение (очень не хочется джангу увидеть, так как за ней тянется шлейф всего самого ненужного для этой задачи, можно использовать, например, twisted или flask).

1. Приложение слушает какой-нибудь порт, передаётся параметром окружения PORT при запуске приложения, например, так PORT=8001 kek.py

2. Приложение всегда отдаёт статус 200, не зависимо от исхода обработки входных данных запроса

3. Логгируются все входящие запросы. Полезна информация: метод, урл, параметры, естественно время запроса (штамп)

3.1. Методы запроса кроме GET валидировать и логгировать как ошибку

3.2. Запрос с параметром invalid=1 (GET /any_url?invalid=1) обрабатывать и логгировать как ошибку

4. Логи должны легко читаться, мы под этим понимаем то, что мы без проблем должны выделить все записи в логе для прослеживания цепочки событий (пусть это будет timestamp запроса) по искомому происшествию (накручивать для просмотра этого какое-то решение не нужно) (происшествие в данном контексте - это запрос). Из лог записи должно быть понятно в каком месте цепочки вызовов была сделана запись.

5. Обработка запросов на path отличный от /api обрабатывать как ошибку

6. Запрос /api обрабатывать следующим образом:
def query(request):
...здесь логгируем изначальный запрос...
...здесь проверки на метод, путь и необходимая обработка...
process1(request)
process2(request)
process3(request)

6.0.1. реализация методов processX любая (хоть pass, кроме полезной нагрузки...), главное, чтобы в них делалась соответствующая лог-запись;

6.0.2. В process2, в случае если был передан параметр notawaiting=1, валидация должна вызывать ошибку и соответствующе логгироваться.

+ Хочется посмотреть покрытие модульными тестами


Реализация.

1. При запуске скрипта ему можно передать порт:

python Webtrap --port 5005. 

Если хотите в качестве аргумента передавать переменную окружения, она сначала должна быть создана. Для парсинга аргументов используется argparse. Если порт не был передан по умолчанию он равен 5000.

2. Надеюсь все условия понял верно, логирование осуществляется через простой и удобный loguru, все зависимости в файле requirements.txt.

3.Так же имеются тесты через unittest, перед запуском тестов, сервер должен быть запущен перед этим отдельно.

