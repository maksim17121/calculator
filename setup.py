from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculator-pkg-calculatoorve",          # Уникальное имя пакета
    version="0.1.0",                             # Версия пакета
    author="Максим",                           # Ваше имя
    author_email="maksim17121@gmailcom",        # Ваш email
    description="Простой калькулятор на Python",
    long_description=long_description,           # Длинное описание из README.md
    long_description_content_type="text/markdown",
    url="https://github.com/chichkanastya/practical2",  # Ссылка на репозиторий или сайт
    packages=find_packages(),         # Поиск всех пакетов внутри проекта
    classifiers=[                                # Классификаторы
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Укажите вашу лицензию
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                     # Требуемая версия Python
)
