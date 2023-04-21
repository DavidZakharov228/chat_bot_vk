import vk_api
from datetime import datetime

# Введите логин и пароль от вашей страницы ВКонтакте
login, password = 'login', 'password'

# Авторизация в VK API
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

# Получаем объект API
vk = vk_session.get_api()

# Получаем последние 5 записей на стене
posts = vk.wall.get(count=5)

# Обходим каждую запись и выводим ее текст и время создания
for post in posts['items']:
    text = post['text']
    unixtime = post['date']
    date_time = datetime.fromtimestamp(unixtime)
    date = date_time.strftime('%Y-%m-%d')
    time = date_time.strftime('%H:%M:%S')
    print(f'{text};\ndate: {date}, time: {time}\n')
