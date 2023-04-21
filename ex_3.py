import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        name = vk.users.get(user_ids=event.user_id)[0]['first_name']
        city = vk.users.get(user_ids=event.user_id, fields='city')[0].get('city', {}).get('title')
        message = f"Привет, {name}!"
        if city:
            message += f" Как поживает {city}?"
        vk.messages.send(
            peer_id=event.peer_id,
            message=message,
            random_id=0
        )