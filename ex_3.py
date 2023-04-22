import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime


def get_weekday(date):
    weekday_dict = {
        0: 'понедельник',
        1: 'вторник',
        2: 'среду',
        3: 'четверг',
        4: 'пятницу',
        5: 'субботу',
        6: 'воскресенье'
    }
    weekday_num = date.weekday()
    return weekday_dict[weekday_num]


vk_session = vk_api.VkApi(
    token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        if 'день недели' in message:
            vk = vk_session.get_api()
            vk.messages.send(chat_id=event.chat_id,
                             message='Введите дату в формате YYYY-MM-DD:')
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    date_str = event.text
                    try:
                        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        weekday = get_weekday(date)
                        vk.messages.send(chat_id=event.chat_id,
                                         message=f'Дата {date_str} была в {weekday}.')
                    except ValueError:
                        vk.messages.send(chat_id=event.chat_id,
                                         message='Некорректный формат даты. Попробуйте еще раз.')
