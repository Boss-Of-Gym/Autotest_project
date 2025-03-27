# Autotest_Projects 🎉🧪

![Autotest_Projects Banner](images/Bunners.png)

<div align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  </a>
  <a href="https://www.selenium.dev/">
    <img src="https://img.shields.io/badge/Selenium-4.0+-green.svg" alt="Selenium 4.0+">
  </a>
  <a href="https://github.com/Boss-Of-Gym/Stepik_autotest_project.git">
    <img src="https://img.shields.io/github/stars/your_username/MyTestFramework?style=social" alt="GitHub Boss of gym">
  </a>
</div>

---

## ✨ О проекте

**Autotest Project** — это мой проект, в котором я выкладываю свои скрипты на Python для автоматического тестирования сайтов! 🚀  
Здесь будут скрипты начиная от курсов заканчивая моими личными практиками. С помощью **Selenium WebDriver**, **Pytest**, **Unittest**, **Playwright** я буду использовать для написания скриптов. Также здесь будет отображаться прогресс моих навыков в написании автотестов. 🧑‍💻

> 💡 **Цель проекта**: Отслеживание прогресса в написании скриптов для упрощения тестирования UI и API!

---

## 🛠️ Технологии

| Технология         | Версия   | Описание                     |
|--------------------|----------|------------------------------|
| 🐍 **Python**      | 3.8+     | Язык программирования       |
| 🌐 **Selenium**    | 4.0+     | Автоматизация браузера      |
| ✅ **Pytest**      | Latest   | Фреймворк для тестирования  |
| ✅ **UnitTest**    | Latest   | Фреймворк для тестирования  |
| ✅ **Playwright**  | Latest   | Фреймворк для тестирования  |
|--------------------|----------|------------------------------|

---

## ⚙️ Установка

Настройте проект за несколько простых шагов:

1. **Склонируйте репозиторий** 📥:
	bash
		!git clone https://github.com/Boss-Of-Gym/Stepik_autotest_project.git
2. **Перейдите в папку проекта** 📂:
	bash
		!cd MyTestFramework
3. **Создайте виртуальное окружение (рекомендуется)** 🐍:
	bash
		!python -m venv venv
		!source venv/bin/activate  # Для Windows: venv\Scripts\activate
4. **Установите зависимости** 📦:
	bash
		!pip install -r requirements.txt

## 🚀 Использование

**Запуск тестов**

Запустите тесты с помощью одной команды:
	bash
		!pytest tests/ --browser chrome

**Поддерживаемые браузеры**

   | 🌐 Chrome  |
   | 🦊 Firefox |
   | 🌍 Edge    |

**Пример теста**

Вот как выглядит простой тест для проверки заголовка страницы:

	!from selenium import webdriver

	!def test_open_site():
    		!driver = webdriver.Chrome()
   		!driver.get("https://example.com")
    		!assert "Example" in driver.title
    		!driver.quit()

## 📂 Структура проекта

	Stepik_autotest_project/
	|
	|___Stepik/
	|	|___Les*.py	#Скрипты написанные для учебных сайтов по курсу
	|			#Дальнейшая структура в разработке

## 📬 Контакты

**Связаться со мной, если у вас есть предложение по улучшению работ можно с помощью…:**

	📧 **Email:** alienlifeform423@gmail.com
	🐦 **Telegram:** @Dator_Deus
	🌐 **Сайт:** my_future_job.mail.com

## 🎉 Спасибо за интерес к проекту

Если вам понравился проект, не забудьте поставить ⭐ на GitHub! Это очень помогает! 😊
