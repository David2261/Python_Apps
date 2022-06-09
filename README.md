# Python_Apps

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=F7385B&lines=The+Python+Apps)](https://git.io/typing-svg)


## Tools

![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?style=for-the-badge&logo=sublime-text&logoColor=important) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)


## Description

*I have created and created many different tools, experiences and applications in Python. Some are lost, and some are preserved. Maybe they will be useful to you now or in future projects*

- Relevant topics:
	- Exceptions
	- Parsers
	- Tools
	- Types


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