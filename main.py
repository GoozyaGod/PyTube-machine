import yt_dlp
import time

# Чтение списка ссылок из файла
with open('urls.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f if line.strip()]

# yt-dlp параметры
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]/best[height<=720]',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'socket_timeout': 30,
    'quiet': False,
}

# Лог ошибок
error_log = []

# Основной цикл
for url in urls:
    success = False
    for attempt in range(1, 4):  # до 3 попыток
        print(f'\n🔽 Попытка {attempt} — {url}')
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            success = True
            print(f'✅ Успешно: {url}')
            break  # если успех — выходим из цикла попыток
        except Exception as e:
            print(f'⚠️ Ошибка при загрузке: {e}')
            time.sleep(5)  # Пауза между попытками

    if not success:
        print(f'❌ Не удалось скачать: {url}')
        error_log.append(url)

# Запись неудачных ссылок
if error_log:
    with open('errors.txt', 'w', encoding='utf-8') as f:
        for bad_url in error_log:
            f.write(bad_url + '\n')
    print(f'\n⚠️ Скачивание завершено с ошибками. См. errors.txt')
else:
    print('\n✅ Все видео успешно скачаны.')
