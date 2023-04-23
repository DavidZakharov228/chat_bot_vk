from flask import Flask, render_template
import vk_api

app = Flask(__name__)


@app.route('/vk_stat/<int:group_id>')
def vk_stat(group_id):
    vk_session = vk_api.VkApi(token='vk1.a.gV418o9HEmTOQI2gPvO04uTQ_fzNuRTeH6ruGpoLL6ZtfSrf_QsYWEwGdtGEo2eZLdu7lkkdw8T-bg3gV7Lr8eR4I6H6Qmk9wDbN3vI8dRgR1qLUa3kLXoT3MjLddbZ-CoDmNmLFt1VNFvSscfHtwzPfkkiYyJN-Nq1GUi2abNf_jLTb2dj065ckqDJBxHswivvucSBLXFGLODaT3WaxLA')
    vk = vk_session.get_api()
    stats = vk.stats.get(group_id=group_id, fields='reach', interval=86400, intervals_count=10)

    # производим необходимые вычисления и подготавливаем данные для отображения в таблице
    # ...

    return render_template('table.html', data=data)