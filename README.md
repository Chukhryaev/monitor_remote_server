# monitor_remote_server

Пример расписания

_**step** - Шаг слота в секундах_


<pre>
{
  "step": "300",
  "videos": [
    {
      "link": "URL1",
      "start": 30,
      "end": 35
    },
    {
      "link": "URL3",
      "start": 65,
      "end": 75
    }
  ]
}
</pre>


Методы взимодействия с мониторами

<pre>
GET "/monitors"
Получает список всех мониторов
</pre>

<pre>
"monitors": [
    {
        "guid": {guid},
        "name": {name},
        "location": {location}
    }
]
</pre>
