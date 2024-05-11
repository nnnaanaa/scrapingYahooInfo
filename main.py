#!/usr/bin/env python3

from train_status import train_status
from synthesis import synthesis, play_wav
import requests
from bs4 import BeautifulSoup
import time

def main():
    wav_file = f"audio.wav"

    text = "おはようございます。6時になりました。"
    text += "列車の運行情報をお知らせします。"

    # /* 列車運行情報 */
    train_status_text = train_status()
    text += train_status_text

    # /* WAVファイル生成 */
    synthesis(text, wav_file)

    # /* WAVファイル再生 */
    play_wav(wav_file)

if __name__ == '__main__':
    main()
