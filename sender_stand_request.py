# Импорт необходимых модулей, конфигурации для отправки запросов и данных для запроса
import configuration
import requests
import data

# Определение функции post_create_order для отправки POST-запроса на создание нового пользователя
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Определение функции get_order_by_track для отправки GET-запроса на получение заказа по его номеру
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + "?t=" + str(track))




