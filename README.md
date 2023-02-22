# Python Applications
> List of various applications and functions built into python


## Tools
- Python 3.10
- Poetry
- Pillow
- Buildozer


## Description

*I have created and created many different tools, experiences and applications in Python. Some are lost, and some are preserved. Maybe they will be useful to you now or in future projects*

- Relevant topics:
	- Exceptions
	- Parsers
	- Tools
	- Types
	- Applications


```python
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

```