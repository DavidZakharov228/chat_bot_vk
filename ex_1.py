import vk_api


LOGIN = 'login'
PASSWORD = 'password'


vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()


vk = vk_session.get_api()


friends = vk.friends.get(fields=['bdate', 'last_name', 'first_name'], order='last_name')


sorted_friends = sorted(friends['items'], key=lambda x: x['last_name'])


for friend in sorted_friends:
    last_name = friend['last_name']
    first_name = friend['first_name']
    bdate = friend.get('bdate', 'Дата рождения не указана')
    print(f'{last_name} {first_name}, {bdate}')
