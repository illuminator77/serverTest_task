# serverTest_task
 Просьба выполнить тестовое задание: необходимо сделать tcp сервер, который распознаёт заданный формат данных и отображает его в требуемом формате. Обязательна запись данных во внешний файл. Интерфейс и способ отображения на выбор разработчика. Формат данных BBBBxNNxHH:MM:SS.zhqxGGCR Где BBBB - номер участника x - пробельный символ NN - id канала HH - Часы MM - минуты SS - секунды zhq - десятые сотые тысячные GG - номер группы CR - «возврат каретки» (закрывающий символ) Пример данных: 0002 C1 01:13:02.877 00[CR] Выводим «спортсмен, нагрудный номер BBBB прошёл отсечку NN в «время»" до десятых, сотые и тысячные отсекаются. Только для группы 00. Для остальных групп данные не отображаются, но пишутся в лог полностью. Язык Python, версия не ниже 3.2 Передача данных должна поддерживаться с помощью telnet клиента.
![image](https://user-images.githubusercontent.com/67760549/173030544-a57cad01-03ce-4128-8ebc-f8be709c75db.png)