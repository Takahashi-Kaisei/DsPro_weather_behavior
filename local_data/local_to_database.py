import pandas as pd
import numpy as np
import sqlite3


class Local2Database:

    def __init__(self, local_csv):
        self.local_csv = local_csv

    def convert(self, local_csv):
        #私のlocalファイルにアクセスしています
        df = pd.read_csv(f'{local_csv}')


        #変換しかしないので注意
        con = sqlite3.connect(f'{local_csv}') #データベースにアクセス
        df.to_sql('screantime_data', con, if_exists='replace', index=False) #データベースに変換、if_exists='replace'で同じ名前のものがあったときに置き換える。index=Falseでindexを入れないように指定してる
        con.close() #データベースを閉じる