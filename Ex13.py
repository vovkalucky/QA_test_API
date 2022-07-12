# Ex13: User Agent
#
# User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос.
# Он формируется автоматически клиентом, например браузером.
# Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
#
# Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
# Метод определяет по строке заголовка User Agent следующие параметры:
#
# device - iOS или Android
#
# browser - Chrome, Firefox или другой браузер
#
# platform - мобильное приложение или веб
#
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
#
# Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения,
# GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.
#
# Список User Agent и ожидаемых значений можно найти по этой ссылке: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26
#
# Пример того, как должен выглядеть запрос с указанным User Agent:
#
# requests.get(
#
#     "https://playground.learnqa.ru/ajax/api/user_agent_check",
#
#     headers={"User-Agent": "Some value here"}
#
# )
#
# ============================================================
# На самом деле метод не всегда работает правильно. Ответом к задаче должен быть список из тех User Agent, которые вернули неправильным хотя бы один параметр, с указанием того, какой именно параметр неправильный.
# И, конечно, ссылка на коммит с вашим тестом.
import requests
import json
class TestApi:
    def test_api(self):
        response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check')
        response_text = response.text
        response_json = json.loads(response_text)
        print(response_json)

        if 'user_agent' in response_json:
            assert response_json['user_agent'] == "python-requests/2.26.0", 'User-agent not valid'
        else:
            print('Key user-agent not found')

        if 'platform' in response_json:
            assert response_json['platform'] == "Unknown", 'Platform not valid'
        else:
            print('Key platform not found')

        if 'browser' in response_json:
            assert response_json['browser'] == "Unknown", 'Browser not valid'
        else:
            print('Key browser not found')