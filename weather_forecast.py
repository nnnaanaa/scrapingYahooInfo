#!/usr/bin/env python3

"""天気予報
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

def weather_forecast_text():
    forecast_dict = weather_forecast()
    text = "本日{}の天気は{}です。最高気温は{}で、低気温は{}です。明日{}の天気は{}です。最高気温は{}で、最低気温は{}です。"
    format_text = text.format(forecast_dict['today']['date'], forecast_dict['today']['weather'], forecast_dict['today']['temperature_high'], forecast_dict['today']['temperature_low'],\
                forecast_dict['tomorrow']['date'], forecast_dict['tomorrow']['weather'], forecast_dict['tomorrow']['temperature_high'], forecast_dict['tomorrow']['temperature_low'], )
    return format_text

def weather_forecast():
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # /* 日付 */
        dates_info = []
        dates = soup.select('.forecastCity .date span')
        for _, date in enumerate(dates):
            pattern = r'<span((?!\s*class=)[^>]*)>(.*?)</span>'
            if re.match(pattern, str(date)):
                dates_info.append(date.text)

        # /* 天気 */
        weather_info = []
        weather_elements = soup.select('.forecastCity .pict')
        for weather_element in weather_elements:
            weather_text = weather_element.get_text(strip=True)
            weather_info.append(weather_text)
            
        # /* 最高気温 */
        weather_tmpl_high_info = []
        weather_elements_tmpl_high = soup.select('.forecastCity .temp .high')
        for weather_element_tmpl_high in weather_elements_tmpl_high:
            temperature = weather_element_tmpl_high.find('em').get_text(strip=True)
            weather_tmpl_high_info.append(temperature)

        # /* 最低気温 */
        weather_tmpl_low_info = []
        weather_elements_tmpl_low = soup.select('.forecastCity .temp .low')
        for weather_element_tmpl_low in weather_elements_tmpl_low:
            temperature = weather_element_tmpl_low.find('em').get_text(strip=True)
            weather_tmpl_low_info.append(temperature)

        # /* 返却値指定 */
        forecast_dict = {
            "today" :{
                "date": dates_info[0],
                "weather": weather_info[0],
                "temperature_high": weather_tmpl_high_info[0]  + "度",
                "temperature_low": weather_tmpl_low_info[0]  + "度",
            },
            "tomorrow": {
                "date": dates_info[1],
                "weather": weather_info[1],
                "temperature_high": weather_tmpl_high_info[1] + "度",
                "temperature_low": weather_tmpl_low_info[1]  + "度",
            }
        }

    except Exception as e:
        print(e)
        return False

    return forecast_dict

if __name__ == '__main__':
    pass