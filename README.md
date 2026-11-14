# Console Speedtest Script

Простой и надежный консольный скрипт на Python для оценки скорости интернета путем выполнения серии последовательных HTTP-запросов.

## Требования
- Python 3.8+
- Установленная библиотека `httpx`

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone [https://github.com/SSUHOY/speedtest.git](https://github.com/SSUHOY/speedtest.git)
   cd speedtest-cli
   ```
2. Установите зависимости
   ```bash
   pip install httpx
   ```
## Использование 
   ```bash
  python speedtest.py
   ```
## Пример 
  ```bash
   python speedtest.py https://aurora-labeling.ru/product/testovaya-liniya-etiketirovki/
  ```

## Выбранные единицы измерения:
- Объём данных: Мегабайты (МБ / MB), рассчитанные как байты / 1024 / 1024.
- Время: Секунды (сек. / s).
- Скорость скачивания:
- Мегабиты в секунду (Мбит/с / Mbps) — стандарт для сетевых тестов.
- Мегабайты в секунду (МБ/с / MB/s) — для оценки реальной скорости загрузки файлов.
