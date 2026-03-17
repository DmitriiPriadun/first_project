# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv()

# Получение значения переменной author из .env
author = os.getenv('AUTHOR')

def print_author(author):
# Допишите здесь ваш код
    print(f"Автор проекта: {author}") 


print_author (author)