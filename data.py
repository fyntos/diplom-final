# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# мокковые данные заказа по номеру
order_body = {
     "firstName": "Naruto",
     "lastName": "Uzumaki",
     "address": "Kanoha, 142 apt.",
     "metroStation": "1",
     "phone": "+7 800 355 35 35",
     "rentTime": 5,
     "deliveryDate": "2020-06-06T00:00:00.000Z",
     "track": 521394,
     "status": 1,
     "color": [
         "BLACK"
     ],
}
