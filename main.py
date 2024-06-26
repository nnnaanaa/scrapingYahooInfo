#!/usr/bin/python3

from train_status import train_status
from weather_forecast import weather_forecast_text
from greeting import greeting_text
from synthesis import synthesis, play_wav
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os

def main():
    wav_file = f"./audio/audio.wav"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    wav_file = os.path.join(current_directory, wav_file)

    try:
        if not os.path.exists(os.path.dirname(wav_file)): os.makedirs(os.path.dirname(wav_file)) # フォルダが存在しないとき
        text = "{}時になりました。".format(datetime.now().hour)

        # /* 列車運行情報 */
        text += "現在の列車の運行情報をお知らせします。"
        train_status_text = train_status()
        text += train_status_text

        # /* 天気予報 */
        text += "続いて天気予報です。"
        weather_text = weather_forecast_text()
        text += weather_text

        # /* WAVファイル生成 */
        synthesis(text, wav_file)

        # /* WAVファイル再生 */
        play_wav(wav_file)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()