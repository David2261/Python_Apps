import re
import speedtest


test = speedtest.Speedtest()


# без re.DOTALL мы сломаемся на первом же переносе строки
number_regex = re.compile(r"(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(.*)", re.DOTALL)
def parse_number(src):
    match = number_regex.match(src)
    if match is not None:
        number, src = match.groups()
        return eval(number), src  # использовать eval - не лучшее решение, но самое простое


string_regex = re.compile(r"('(?:[^\\']|\\['\\/bfnrt]|\\u[0-9a-fA-F]{4})*?')\s*(.*)", re.DOTALL)
def parse_string(src):
    match = string_regex.match(src)
    if match is not None:
        string, src = match.groups()
        return eval(string), src  # здесь мы вообще подменили JSON'овский
                                  # формат строк на питоновский, ну да ладно


def parse_word(word, value=None):
    l = len(word)
    def result(src):
        # добавьте в следующую строчку вызовы .lower() для case-insensitive языка!
        if src.startswith(word):  # опять if! вот живучая тварь!
            return value, src[l:].lstrip()  # lstrip нужен для игнорирования пробелов, см. ниже
    result.__name__ = "parse_%s" % word  # для отладки
    return result

parse_true = parse_word("true", True)
parse_false = parse_word("false", False)
parse_null = parse_word("null", None)


download = test.download()/1025/1024
upload = test.upload()/1024/1024

print(f'Download speed: {round(download, 2)} Mb/s')
print(f'Upload speed: {round(upload, 2)} Mb/s')