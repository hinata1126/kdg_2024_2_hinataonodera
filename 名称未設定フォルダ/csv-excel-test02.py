import pandas as pd
 
# CSVファイルの読み込み
data = pd.read_csv('exams.csv')
 
# Excel形式で出力
data.to_excel('excel-data.xlsx', encoding='utf-8')
