import time
from os import getenv

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from urllib.parse import urlparse, parse_qs

from dotenv import load_dotenv

load_dotenv()


def get_auth_code():
    url = (f"https://hh.ru/oauth/authorize?"
           f"response_type=code&"
           f"client_id={getenv('CLIENT_ID')}&"
           f"state={getenv('STATE_VALUE')}&"
           f"redirect_uri={getenv('REDIRECT_URL')}")

    chrome_profile_url = r"C:\Users\lizas\AppData\Local\Google\Chrome\User Data"

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" + chrome_profile_url)
    time.sleep(2)
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.bloko-button.bloko-button_kind-primary.bloko-button_stretched').click()
    time.sleep(2)

    current_url = driver.current_url
    parsed_url = urlparse(current_url)
    authorization_code = parse_qs(parsed_url.query).get('code', [None])[0]

    driver.close()

    return authorization_code


def get_tokens(auth_code):
    url = 'https://api.hh.ru/token?'
    params = {
        'grant_type': 'authorization_code',
        'client_id': getenv('CLIENT_ID'),
        'client_secret': getenv('CLIENT_SECRET'),
        'code': auth_code,
        'redirect_uri': getenv('REDIRECT_URL')
    }
    response = requests.post(url, data=params)
    tokens = response.json()

    token = tokens.get('access_token')
    return token


def get_vacancies():
    auth_code = get_auth_code()
    access_token = get_tokens(auth_code)

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    url = (f'https://api.hh.ru/vacancies?'
           f'text=Name:((python or django or drf or backend or fastapi or flask)'
           f' and not Преподаватель and not школа and not QA) and'
           f' DESCRIPTION:(django or drf or fastapi or flask)&'
           f'experience=noExperience&'
           f'experience=between1And3&'
           f'per_page=100&'
           f'order_by=publication_time')

    response = requests.get(url, headers=headers)
    vacancies = response.json()['items']

    for vacancy in vacancies:
        requires_cover_letter = vacancy['response_letter_required']
        if not requires_cover_letter:
            response_to_a_vacancy(vacancy, access_token)


def response_to_a_vacancy(vacancy, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = {
        "resume_id": "48b1382bff0c4416b80039ed1f54794e586171",
        "vacancy_id": f"{vacancy["id"]}"
    }

    url = 'https://api.hh.ru/negotiations'

    requests.post(url, data=data, headers=headers)


if __name__ == '__main__':
    get_vacancies()
    print('Вы откликнулись на вакансии')
