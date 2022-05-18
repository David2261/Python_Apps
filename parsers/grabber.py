class GrabberArticle:
    url = "https://finance.tut.by/news696516.html" # URL статьи, которую хотим обработать.
    filename = "str" # имя файла для сохранения
    path = "D:/Grabber" # Путь для сохранения обработанного текста
    content_tags = ['p'] # HTML-теги для обработки
    wrap = 80 # количество символов в строке очищенного текста


def get_text(self):
    r = requests.get(self.url).text
    soup = BeautifulSoup(r, 'html.parser')
    # найдем все теги по списку self.content_tags
    content = soup.find_all(self.content_tags)
    wrapped_text = ""
    for p in content:
        # пропускаем теги без значений
        if p.text != '':
            # форматирование ссылок в вид [ссылка]
            links = p.find_all('a')
            if links != '':
                for link in links:
                    p.a.replace_with(link.text + str("[" + link['href'] + "]"))
            # устанавливаем ширину строки равной self.wrap (по умолчанию, 80 символов)
            wrapped_text += ''.join(textwrap.fill(p.text, self.wrap)) + "\n\n"
    self.write_in_file(wrapped_text)

def __init__(self, url_address):
    self.url = url_address
    path_arr = self.url.split('/')
    if path_arr[-1] != '':
        self.filename = path_arr[-1] + ".txt"
        self.path = os.getcwd() + "/".join(path_arr[1:-1])
    else:
        self.filename = path_arr[-2] + ".txt"
        self.path = os.getcwd() + "/".join(path_arr[1:-2])
    if not os.path.exists(self.path):
        os.makedirs(self.path)

def write_in_file(self, text):
    # записывает text в каталог self.path:"[CUR_DIR]/host.ru/path_item1/path_item2/..."
    file = open(str(self.path) + '/' + str(self.filename), mode="a")
    file.write(text)
    file.close()


class GrabberArticle:
    url = "https://finance.tut.by/news696516.html" # URL статьи, которую хотим обработать.
    filename = "str" # имя файла для сохранения
    path = "D:/Grabber" # Путь для сохранения обработанного текста
    content_tags = ['p'] # HTML-теги для обработки
    wrap = 80 # количество символов в строке очищенного текста


def get_text(self):
    r = requests.get(self.url).text
    soup = BeautifulSoup(r, 'html.parser')
    # найдем все теги по списку self.content_tags
    content = soup.find_all(self.content_tags)
    wrapped_text = ""
    for p in content:
        # пропускаем теги без значений
        if p.text != '':
            # форматирование ссылок в вид [ссылка]
            links = p.find_all('a')
            if links != '':
                for link in links:
                    p.a.replace_with(link.text + str("[" + link['href'] + "]"))
            # устанавливаем ширину строки равной self.wrap (по умолчанию, 80 символов)
            wrapped_text += ''.join(textwrap.fill(p.text, self.wrap)) + "\n\n"
    self.write_in_file(wrapped_text)

def __init__(self, url_address):
    self.url = url_address
    path_arr = self.url.split('/')
    if path_arr[-1] != '':
        self.filename = path_arr[-1] + ".txt"
        self.path = os.getcwd() + "/".join(path_arr[1:-1])
    else:
        self.filename = path_arr[-2] + ".txt"
        self.path = os.getcwd() + "/".join(path_arr[1:-2])
    if not os.path.exists(self.path):
        os.makedirs(self.path)

def write_in_file(self, text):
    # записывает text в каталог self.path:"[CUR_DIR]/host.ru/path_item1/path_item2/..."
    file = open(str(self.path) + '/' + str(self.filename), mode="a")
    file.write(text)
    file.close()

