import requests
from bs4 import BeautifulSoup
import os

# URL страницы, содержащей изображения
url = "https://daaam.info/3rd-daaam-international-internship-gallery"

# Получение пути к рабочему столу
desktop_path = r'C:\Users\murav\Desktop\Austria2017'
download_folder = os.path.join(desktop_path)

# Отправляем GET-запрос и получаем содержимое страницы
response = requests.get(url)

# Проверяем, что запрос прошел успешно
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.text, "html.parser")

    # Находим все элементы img на странице
    img_tags = soup.find_all("img")

    # Создаем папку для сохранения изображений, если ее еще нет
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Перебираем найденные изображения и сохраняем их
    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if img_url:
            img_filename = os.path.basename(img_url)
            img_data = requests.get(img_url).content
            img_path = os.path.join(download_folder, img_filename)

            width = img_tags["width"]
            height = img_tags["height"]
            ratio = width / height

            if ratio == 1:
                # Это похожее изображение
                pass

            with open(img_path, "wb") as img_file:
                img_file.write(img_data)
            print(f"Сохранено: {img_filename}")

else:
    print("Ошибка при получении страницы:", response.status_code)
