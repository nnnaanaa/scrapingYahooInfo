#!/usr/bin/env python3
from datetime import datetime

def greeting_text():
    if datetime.now().hour < 6:
        greeting = "夜更かしは良くないですよ！"
    elif datetime.now().hour < 12:
        greeting = "おはようございます"
    elif datetime.now().hour < 18:
        greeting = "こんにちは"
    else:
        greeting = "こんばんは"
    return greeting