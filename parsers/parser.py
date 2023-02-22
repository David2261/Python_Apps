"""
ПО позволяет парсить сайты:
**Без аутентификации, платного контента, систем защиты таких как cloud flare
"""
import requests
from bs4 import BeautifulSoup as BS
import speedtest


test = speedtest.Speedtest()


def main():
	# URL нужно вставить ссылку страницы для парсинга.
	r = requests.get("https://quote.rbc.ru/?utm_source=topline")
	html = BS(r.content, 'html.parser')

	# Мы вставим наши дынне в файл test.html . 
	with open('test.html', 'w', encoding='utf-8') as output_file:

		for el in html.select(".q-item > .q-item__wrap"):
			
			title = el.select("a > .q-item__title")
			output_file.writelines("<p>" + title[0].text + "</p>\n")

if __name__  == '__main__':
	main()

download = test.download()/1025/1024
upload = test.upload()/1024/1024

print(f'Download speed: {round(download, 2)} Mb/s')
print(f'Upload speed: {round(upload, 2)} Mb/s')