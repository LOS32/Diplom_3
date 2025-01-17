# Stellar Burgers Test Automation

# Описание
Автотесты для веб-приложения **Stellar Burgers**, покрывающие ключевой функционал:
- Лента заказов.
- Оформление заказов.
- Проверка разделов "История заказов" и "В работе".

# Запуск тестов
Установите зависимости:
   ```bash
   pip install -r requirements.txt

Запустите тесты в Chrome:
pytest tests --browser=chrome -v

Для Firefox:
pytest tests --browser=firefox -v