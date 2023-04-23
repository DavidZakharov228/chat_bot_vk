import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia

wikipedia.set_lang("ru") # устанавливаем язык для Википедии

# функция для отправки сообщения пользователю
def send_message(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# функция для обработки сообщений от пользователя
def handle_message(user_id, text, next_question=None):
    try:
        if next_question:
            # если есть следующий вопрос, то задаем его пользователю
            send_message(user_id, next_question)
            return
        # ищем информацию в Википедии
        page = wikipedia.page(text)
        summary = wikipedia.summary(text, sentences=3)
        url = page.url
        # отправляем ответ пользователю
        send_message(user_id, f'Вот что я нашел по запросу "{text}":\n\n{summary}\n\nПодробнее: {url}\n\nЕсть ли у вас еще вопросы?')
    except wikipedia.exceptions.DisambiguationError as e:
        # если запрос неоднозначен, то предлагаем пользователю выбрать из списка
        options = "\n".join(e.options[:10])
        send_message(user_id, f'Я не смог найти информацию по запросу "{text}", но нашел несколько возможных вариантов:\n\n{options}\n\nВыберите один из них и напишите мне еще раз.')
    except wikipedia.exceptions.PageError:
        # если страница не найдена, сообщаем об этом
        send_message(user_id, f'Я не смог найти информацию по запросу "{text}". Попробуйте изменить запрос и написать мне еще раз.')
    except:
        # если произошла какая-то ошибка, сообщаем об этом
        send_message(user_id, 'Произошла ошибка. Попробуйте написать мне еще раз.')

# функция для обработки событий
def on_event(event):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower()
        if text == "помощь":
            # если пользователь написал "помощь", то отправляем список доступных команд
            send_message(user_id, 'Я могу помочь вам найти информацию в Википедии. Просто напишите мне запрос.')
        else:
            # если пользователь написал что-то другое, то обрабатываем его сообщение
            if "еще вопросы" in text:
                # если пользователь ответил на предыдущий вопрос, то задаем следующий
                handle_message(user_id, None, "Какой еще вопрос у вас есть?")
            else:
                handle_message(user_id, text)
# функция для обработки событий
def on_event(event):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.lower()
        if text == "помощь":
            # если пользователь написал "помощь", то отправляем список доступных команд
            send_message(user_id, 'Я могу помочь вам найти информацию в Википедии. Просто напишите мне запрос.')
        else:
            # если пользователь написал что-то другое, то обрабатываем его сообщение
            handle_message(user_id, text)

# авторизация в ВКонтакте
vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# главный цикл программы
for event in longpoll.listen():
    try:
        on_event(event)
    except Exception as e:
        print(e)
