import requests

from dotenv import load_dotenv

import pygame

from vacancies_app.services.authorization import get_auth_code, get_tokens

load_dotenv()
pygame.mixer.init()


def get_new_vacancies(headers, experience_value):
    url = 'https://api.hh.ru/vacancies'

    text = ('Name:(python or django or drf or backend or fastapi or flask or telegram or ботов)'
            ' not Преподаватель not QA not Школа not ML not Senior not java not php not C'
            'and DESCRIPTION:(python or django or drf or fastapi or flask or боты)')

    params = {
        "text": text,
        "response_letter_required": False,
        "per_page": "100",
        "order_by": "publication_time",
    }
    if experience_value:
        params["experience"] = experience_value

    response = requests.get(url, params=params, headers=headers)
    all_vacancies = response.json()["items"]
    return all_vacancies


def get_already_applied_vacancies(headers):
    url = 'https://api.hh.ru/negotiations'
    vacancies = [v['id'] for v in requests.get(url, headers=headers).json()['items']]
    return vacancies


def get_filtered_vacancies(active_button, experience):
    auth_code = get_auth_code()
    access_token = get_tokens(auth_code)

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    all_vacancies = get_new_vacancies(headers, experience)
    already_applied_vacancies = get_already_applied_vacancies(headers)

    filtered_vacancies = list(filter(lambda v: v['id'] not in already_applied_vacancies, all_vacancies))
    step = 100 / len(filtered_vacancies)
    new_vacancies = []

    for vacancy in filtered_vacancies:
        active_button.update(step)

        response_to_a_vacancy(vacancy, headers)
        new_vacancies.append(vacancy['name'])

    new_vacancies = '\n'.join(new_vacancies)
    return new_vacancies


def response_to_a_vacancy(vacancy, headers):
    url = 'https://api.hh.ru/negotiations'

    data = {
        "resume_id": "48b1382bff0c4416b80039ed1f54794e586171",
        "vacancy_id": f"{vacancy["id"]}"
    }

    requests.post(url, data=data, headers=headers)
