import bs4
import csv # モジュール"CSV"の呼び出し

# スクレイピング対象のhtmlファイルからsoupを作成
soup = bs4.BeautifulSoup(open('Active.vue'), 'html.parser')

links = soup.find_all('a') # 全てのaタグ要素を取得

csvlist = [] # 配列を作成

for link in links: # aタグのテキストデータを配列に格納
    sample_txt = link.text
    csvlist.append(sample_txt)

# CSVファイルを開く。ファイルがない場合は新規作成
f = open("output_sample.csv", "w")
writecsv = csv.writer(f, lineterminator='\n')

writecsv.writerow(csvlist) # 出力

f.close() # CSVファイルを閉じる