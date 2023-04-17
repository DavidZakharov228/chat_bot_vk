import vk_api

# Введите логин и пароль от вашей страницы ВКонтакте
LOGIN = '89106026103'
PASSWORD = 'tadgikmadgik'

# Авторизация в VK API
vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()

# Получаем объект API
vk = vk_session.get_api()

# Получаем список друзей пользователя
friends = vk.friends.get(fields=['bdate', 'last_name', 'first_name'], order='last_name')

# Сортируем список друзей по фамилии
sorted_friends = sorted(friends['items'], key=lambda x: x['last_name'])

# Выводим информацию о каждом друге
for friend in sorted_friends:
    last_name = friend['last_name']
    first_name = friend['first_name']
    bdate = friend.get('bdate', 'Дата рождения не указана')
    print(f'{last_name} {first_name}, {bdate}')
