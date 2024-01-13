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

                            cur.execute('INSERT INTO weather_kisyocho (日,合計降水量,最大一時間降水量,最大10分間降水量,平均気温,最高気温,最低気温,平均湿度,最小湿度,平均風速,最大風速,最大風速の風向き,最大瞬間風速,最大瞬間風速の風向き,最多風向き,日照時間,降雪の深さの合計,最深積雪) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
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