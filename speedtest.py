import time
import sys
import httpx

DEFAULT_URL = "https://aurora-labeling.ru/product/testovaya-liniya-etiketirovki/"  # Тестовая ссылка / картинка
NUM_REQUESTS = 10

def measure_speed(url: str):
    print(f"🚀 Начинаем замер скорости для: {url}")
    print(f"Количество последовательных запросов: {NUM_REQUESTS}\n")

    total_bytes = 0
    request_times = []

    for i in range(1, NUM_REQUESTS + 1):
        try:
            start_time = time.perf_counter()
            
            response = httpx.get(url, follow_redirects=True, timeout=30.0)
            response.raise_for_status()
            
            end_time = time.perf_counter()
            
            duration = end_time - start_time
            content_length = len(response.content)
            
            total_bytes += content_length
            request_times.append(duration)
            
            print(f"Запрос {i:2d}: скачано {content_length / 1024 / 1024:.2f} МБ за {duration:.3f} сек.")
            
        except httpx.RequestError as e:
            print(f"❌ Ошибка при выполнении запроса {i}: {e}", file=sys.stderr)
            sys.exit(1)

    avg_time = sum(request_times) / len(request_times)
    total_time = sum(request_times)
    
    total_megabits = (total_bytes * 8) / (1024 * 1024)
    speed_mbps = total_megabits / total_time if total_time > 0 else 0
    speed_mb_s = (total_bytes / (1024 * 1024)) / total_time if total_time > 0 else 0

    print("\n" + "="*40)
    print("📊 ИНФОРМАЦИЯ О ЗАМЕРЕ:")
    print(f"• Всего скачано данных: {total_bytes / (1024 * 1024):.2f} МБ")
    print(f"• Общее время выполнения: {total_time:.3f} сек.")
    print(f"• Среднее время одного запроса: {avg_time:.3f} сек.")
    print(f"• Средняя скорость скачивания: {speed_mbps:.2f} Мбит/с ({speed_mb_s:.2f} МБ/с)")
    print("="*40)

if __name__ == "__main__":
    # Можно передать URL аргументом командной строки, либо использовать дефолтный
    target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    measure_speed(target_url)