import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Задайте URL страницы с изображениями
url = "https://daaam.info/3rd-daaam-international-internship-gallery"

# Инициализируйте браузер с помощью Selenium
driver = webdriver.Chrome()  # Используйте соответствующий драйвер для вашего браузера

# Откройте страницу в браузере
driver.get(url)

# Подождите несколько секунд, чтобы страница полностью загрузилась
time.sleep(5)

# Теперь вы можете искать и нажимать на изображения, чтобы увеличить их размер
# Например, используйте методы find_element_by_... для поиска и клика на элементы

# Пример: нажатие на изображение с определенным CSS-селектором
element = driver.find_element_by_css_selector("#ngg-image-0 > div > a > img")
element.click()

# Подождите несколько секунд, чтобы изображение увеличилось
time.sleep(3)

# Теперь вы можете извлекать URL увеличенных изображений и загружать их
# Например, используйте Requests для загрузки изображений

# Пример: извлечение URL изображения с определенным CSS-селектором
image_url = driver.find_element_by_css_selector(
    "body > div.sl-wrapper.simple-lightbox > div.sl-image > img").get_attribute("src")

# Используйте Requests для загрузки изображения
response = requests.get(image_url)

# Сохраните изображение на диск
with open("изображение.jpg", "wb") as f:
    f.write(response.content)

# Завершите работу браузера
driver.quit()
