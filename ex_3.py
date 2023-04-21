import vk_api
import random
import time

# функция для генерации рандомной строки
def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# функция для отправки сообщения в чат
def send_message(chat_id, message):
    vk.method("messages.send", {"peer_id": chat_id, "message": message})

# авторизация в VK API
vk_session = vk_api.VkApi(token="vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA")

# создание объекта VK API
vk = vk_session.get_api()

# получение ID чата
chat_id = int(input("Введите ID чата: "))

# отправка сообщений в чат до тех пор, пока не придет команда /stop
while True:
    message = generate_random_string(10)
    send_message(chat_id, message)
    time.sleep(3) # задержка в 3 секунды
    messages = vk.method("messages.getConversationsById", {"peer_ids": chat_id, "count": 1})
    if messages["items"][0]["last_message"]["text"] == "/stop":
        send_message(chat_id, "Бот остановлен.")
        break
