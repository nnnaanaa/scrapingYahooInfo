#!/usr/bin/python3

"""列車運行状況
"""

import requests
from bs4 import BeautifulSoup
import config

def train_status():
    
    normal_texts = []
    trouble_texts = []

    for url in config.route_confirmation_url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # /* タイトル取得 */
        elm_label = soup.find(class_='labelLarge')
        title_text = elm_label.find(class_='title').text

        # /* 運行状況　*/
        elm_service_status = soup.find(class_='elmServiceStatus')

        # /* 詳細情報1 */
        dt_text = elm_service_status.find('dt').text

        # /* 詳細情報2 */
        dd_class = ''.join(elm_service_status.find('dd').get('class'))
        dd_text = elm_service_status.find('dd').text

        # /* テキスト作成 */
        if dd_class == "normal":
            voicevox_text = "{}。".format(title_text)
            normal_texts.append(voicevox_text)

        else:
            voicevox_text = "{}は{}です。{}".format(title_text, dt_text, dd_text)
            trouble_texts.append(voicevox_text)
    
    join_texts = ''.join(trouble_texts)
    join_texts += ''.join(normal_texts) + "は平常運転です。"
    return join_texts

if __name__ == "__main__":
    pass