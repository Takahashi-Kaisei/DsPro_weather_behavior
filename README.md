# DsPro_weather_behavior

## no_use_fileディレクトリについて
・no_use_fileはあっても意味ないファイルです。努力の記念に残してあります
・function_testはスクレイピングを関数で定義しようとしました。やめました
・weather_behaviorはpyで実装する前に動くか実験したノートみたいなものです。
・screantime_to_databaseも同じ

## scrape_modelディレクトリについて
・howtouse_ScrapeWeatherFromKisyochoはモジュールの使い方のようなものです
・scrape_data_kisyochoの中にモジュールが定義してあります。
※インポートするとき
    from howtouse_ScrapeWeatherFromKisyocho import scrape_data_kisyocho
※使うとき
    sr = ScrapeWeatherFromKisyocho(start_year=　, end_year=)
    sr.scrape(start_year=, end_year=)
    基底クラスがよくわからないので二回入れないとなんかダメです。

## local_dataディレクトリについて
・howtouse_Local2Databaseはモジュールの使い方のようなものです。
・local_to_databaseの中にモジュールが定義されてあります。
※インポートするとき
    from local_to_database import Local2Database
※使うとき
    conversion = Local2Database(local_csv = csvのパス)
    conversion.convert(local_csv = csvのパス)
    基底クラスがよくわからないので二回入れないとなんかダメです。
・csvファイルは自分のスクリーンタイム

## 注意
これらのモジュールはデータを入力(or変換)する機能しか持っていません。
テーブルの作成、削除は自分で行なってください。(テーブルの名前は自由じゃないです)

localデータのsns game youtubeの単位は分です