# Анна Болдырева, 19-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# Записываем в переменные коды ответов от сервера
RESPONSE_CODE_STATUS_OK_201 = 201

RESPONSE_CODE_STATUS_OK_200 = 200

# Функция для создания заказа
def create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    return response.json()["track"]

# Тест 1. Клиент может создать заказ
def test_create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    assert response.status_code == RESPONSE_CODE_STATUS_OK_201
    assert response.json()["track"] > 0

# Тест 2. По треку заказа можно получить данные о заказе.
def test_get_order():
    track = create_order()
    response = sender_stand_request.get_order_by_track(track)

    assert response.status_code == RESPONSE_CODE_STATUS_OK_200
    assert response.json()["order"]["track"] == track

