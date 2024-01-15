from bs4 import BeautifulSoup #スクレイピングのためのライブラリ
import requests #HTTP操作用
import re
import time
import sqlite3

class ScrapeWeatherFromKisyocho:

    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year

    def scrape(self, start_year, end_year):
        
        y = start_year

        while y <= end_year:
            for m in range(1, 13):
                url = f'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=44&block_no=0370&year={y}&month={m}'
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html.parser')
                tags = soup.find_all('table', {'id': 'tablefix1'}) #これでテーブルを絞る
                for tag in tags:
                    for row in tag.find_all('tr'):
                        if row.find('a'): #aタグがある場合が日数がデータが入力されてる日
                            data = []
                            for td in row.find_all('td'):
                                text = td.get_text(strip=True)
                                data.append(text)
                                
                                
                                
                            con = sqlite3.connect('weather_scrape.sqlite')
                            cur = con.cursor()
                            
                            date = f'{y}/{m}/{data[0]}'

                            cur.execute('INSERT INTO weather_kisyocho (ymd ,total_rain ,max_hour_rain ,max_10minute_rain ,mean_temp ,max_temp ,min_temp ,mean_hum ,min_hum ,mean_windspeed ,max_windspeed ,max_windspeed_directon ,max_instant_windspeed ,max_instant_windspeed_direction ,most_wind_directiion ,total_sun_time ,total_snowfall_depth ,deepest_snowfall) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                        (date,
                                        data[1],
                                        data[2],
                                        data[3],
                                        data[4],
                                        data[5],
                                        data[6],
                                        data[7],
                                        data[8],
                                        data[9],
                                        data[10],
                                        data[11],
                                        data[12],
                                        data[13],
                                        data[14],
                                        data[15],
                                        data[16],
                                        data[17]
                                        )) # データベースにデータを挿入
                            con.commit() #追加
                time.sleep(1)   
            y += 1

        con.close()