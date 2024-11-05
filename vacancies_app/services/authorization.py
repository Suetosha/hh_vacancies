from os import getenv

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from urllib.parse import urlparse, parse_qs

from dotenv import load_dotenv

import pygame

load_dotenv()
pygame.mixer.init()


def get_auth_code():
    url = (f"https://hh.ru/oauth/authorize?"
           f"response_type=code&"
           f"client_id={getenv('CLIENT_ID')}&"
           f"state={getenv('STATE_VALUE')}&"
           f"redirect_uri={getenv('REDIRECT_URL')}")

    chrome_profile_url = r"C:\Users\lizas\AppData\Local\Google\Chrome\User Data"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("user-data-dir=" + chrome_profile_url)

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, '.bloko-button.bloko-button_kind-primary.bloko-button_stretched').click()
    current_url = driver.current_url
    parsed_url = urlparse(current_url)
    authorization_code = parse_qs(parsed_url.query).get('code', [None])[0]

    driver.quit()

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
