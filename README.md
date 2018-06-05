# KIT
## Что это?
Перед вами реализация телеграм бота, который умеет:

- отвечать на команду /help, где он объясняет, что он умеет
- отвечать на команду /hhelp (от слова hidden), где выводятся вообще все команды, поддерживаемыe ботом 
- воспроизводить заранее заготовленные звуки по команде (маукать, урчать и чихать)
- воспроизводить голосовые сообщения
- обрабатывать команды (говорить, если они не корректны)
- разрешать общение с ботом только определенному кругу лиц

В скрытых коммандах есть:
- update (обновление до последний версии с этого репозитория, есть только в ветке `OrangePiZero`)
- kill (убить зпущеный процесс бота)

## Что в репозитории?
Две ветки: `master` и `OrangePiZero`.

В `master` реализация просто реализация бота, в `OrangePiZero` еще всякие штуки для того, чтобы это работало на Orange Pi Zero

## Зависимости
Для корректной работы нужно подгрузить библиотеки из `requirements.txt`. Для работы с socks5 прокси нужна библиотека `requests[socks]`, а иногда и что-то из `requests[security]`.

## Как это работает?
В `config.py` нужно задать свои `token` (который выдается *@BotFather*) и `proxy`, если вы хотите использовать proxy/находитесь в местах, где заблокирован telegram. `h` в `socks5h` означает, что DNS запросы так же проксируются (в России это необходимо, для того, чтобы достучаться до telegram). Затем, нужно запустить `bot.py` и радоваться жизни)
