#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url_dict = [
    'https://transit.yahoo.co.jp/diainfo/84/0',
    'https://transit.yahoo.co.jp/diainfo/71/0',
    'https://transit.yahoo.co.jp/diainfo/38/0',
]

def train_status():
    texts = []

    for url in url_dict:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # /* タイトル関連 */
        elm_label = soup.find(class_='labelLarge')
        title_text = elm_label.find(class_='title').text

        # /* 運行状況　*/
        elm_service_status = soup.find(class_='elmServiceStatus')
        dt_text = elm_service_status.find('dt').text
        dd_text = elm_service_status.find('dd').text

        # /* テキスト作成 */
        voicevox_text = "{}は{}です。{}".format(title_text, dt_text, dd_text)
        texts.append(voicevox_text)
    
    join_texts = ''.join(texts)
    return join_texts

if __name__ == "__main__":
    pass