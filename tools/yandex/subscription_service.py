# Сервис подписки





Необъяснимая аномалия! На серверах Яндекс Маркета отказывает оборудование: ломаются жесткие диски, плавится оперативная память, выходит из строя система охлаждения. Системные администраторы локализовали проблему — причиной поломок оказалась используемая база данных. Руководители приняли решение срочно вывести из эксплуатации упомянутую базу данных и заменить ее самописной. Вам нужно как можно скорее предоставить MVP, который поддерживает:
частичное обновление товарных предложений в базе данных
уведомление сервисов-подписчиков при обновлении данных
Товарное предложение в базе описывается следующей JSON схемой:

{
  "$id": "offer.schema.json",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Offer identifier, only numerical symbols are allowed"
    },
    "price": {
      "type": "integer",
      "description": "Offer price, value in range from 0 to 10̂9"
    },
    "stock_count": {
      "type": "integer",
      "description": "Items left on stocks, value in range from 0 to 10̂9"
    },
    "partner_content": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Offer title filled in by the partner"
        },
        "description": {
          "type": "string",
          "description": "Offer description filled in by the partner"
        }
      }
    }
  },
  "required": [
    "id"
  ]
}
При межсервисном взаимодействии к товарному предложению добавляется контекст, который содержит идентификатор для сквозной трассировки, его схема:

{
  "$id": "message.schema.json",
  "type": "object",
  "properties": {
    "trace_id": {
      "type": "string"
    },
    "offer": {
      "$ref": "offer.schema.json"
    }
  },
  "required": [
    "trace_id",
    "offer"
  ]
}
Сервис, который отправляет запрос на обновление товарного предложения, обязательно заполняет идентификатор оффера (поле
o
f
f
e
r
.
i
d
) и идентификатор для трассировки (поле
t
r
a
c
e
_
i
d
). Все остальные поля в запросе опциональны. В таком случае при применении обновления будет происходить слияние полей. Например, в базе у оффера заполнены поля
p
r
i
c
e
=
9
9
9
0
, и приходит обновление
s
t
o
c
k
_
c
o
u
n
t
=
1
0
0
, тогда в базе будут сохранены оба поля
p
r
i
c
e
=
9
9
9
0
;
s
t
o
c
k
_
c
o
u
n
t
=
1
0
0
. Гарантируется, что все входящие запросы валидны и соответствуют схеме. Так как это прототип, удаление товаров из базы и очищение полей было решено не поддерживать.
Помимо хранения товарных предложений в базе, в сервисе необходима функция доставки обновлений в сервисы-подписчиков. Одна подписка включает в себя два набора полей: trigger и shipment, не обязательно листовых. Когда изменяется любое trigger поле или поле, вложенное в trigger поле, подписчику отправляется сообщение. В сообщении находятся все shipment и trigger поля этого подписчика, а также идентификаторы оффера и трассировки из запроса, который привел к этому сообщению. Инициализация поля также считается за его изменении и создает сообщение об обновлении.

Формат ввода
Первая строка входных данных содержит два целых числа
n
 и
m
 (
1
≤
n
≤
5
0
,
1
≤
m
≤
1
0
,
0
0
0
) — количество сервисов подписчиков и количество запросов на обновления.
Следующие
n
 строк содержат описания сервисов подписчиков:
i
-я строка содержит описание
i
-го подписчика. В начале строки задается
a
i
 и
b
i
 — количество trigger и shipment полей соответственно. Далее
a
i
 trigger полей, и
b
i
 shipment полей.
Следующие
m
 строк содержат запросы на обновление, каждая строка — это валидный json, удовлетворяющий схеме
m
e
s
s
a
g
e
.
s
c
h
e
m
a
.
j
s
o
n
.

Формат вывода
На каждое событие обновления выведите
k
j
 сообщений в формате
m
e
s
s
a
g
e
.
s
c
h
e
m
a
.
j
s
o
n
, где
k
j
 — это количество сервисов-подписчиков, которым данное событие интересно. Сообщения должны идти в том же порядке, что и обновления, которые привели к ним. Сообщения в рамках одного обновления должны быть отсортированы по порядковому номеру подписчика.
Пример
Ввод	Вывод
2 5
2 0 price stock_count
1 0 partner_content
{"trace_id": "1", "offer": {"id": "1", "price": 9990}}
{"trace_id": "2", "offer": {"id": "1", "stock_count": 100}}
{"trace_id": "3", "offer": {"id": "2", "partner_content": {"title": "Backpack"}}}
{"trace_id": "4", "offer": {"id": "1", "stock_count": 100}}
{"trace_id": "5", "offer": {"id": "2", "partner_content": {"description": "Best backpack ever"}}}
{"trace_id":"1","offer":{"id":"1","price":9990}}
{"trace_id":"2","offer":{"id":"1","price":9990,"stock_count":100}}
{"trace_id":"3","offer":{"id":"2","partner_content":{"title":"Backpack"}}}
{"trace_id":"5","offer":{"id":"2","partner_content":{"description":"Best backpack ever","title":"Backpack"}}}
Примечания
Для решений на языке Python доступны библиотеки json, requests и urllib.
Для решений на языке Java доступны библиотеки jackson-core:2.13.1, jackson-annotations:2.13.1 и jackson-databind:2.13.1 . Соответствующие функции импорта могут иметь вид:

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;
Для решений на языке C++ доступна библиотека nlohmann/json v3.8.0. Соответствующая директива include выглядит так:

#include "json.hpp"
Для решений на языке Golang доступны все стандартные пакеты, включая encoding/json, net/http, sort и другие.
Для решений на C# доступны библиотеки System.Text.Json и Newtonsoft.Json. Соответствующие using могут выглядеть так:

using Newtonsoft.Json;
using System.Text.Json
