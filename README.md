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


## Особенности реализации на Orange Pi Zero
На плате установлена `ARMBIAN 5.38 stable Ubuntu 16.04.4 LTS 3.4.113-sun8i`. Для взаимодействие с telegram мы используем `shadowsocks`-клиент на плате, который обращается к удаленному `shadowsocks`-серверу. 

Скрипт `ss_requirements.sh` должен доставить все необходимые библиотеки. Следует запустить сначала его, так как `requests[...]` может не устанавливаться без библиотек из первой строки этого скрипта.

Затем в папке `/root/KIT_scripts/` создаются 2 скрипта:

`copy_bot_and_token.sh`: 
```
#!/bin/bash
cp -r /root/KIT /tmp/KIT
echo "token = 'YOUR TOKEN'" >> /tmp/KIT/config.py
```
и `start_KIT.sh`:
```
#!/bin/bash
. /root/KIT_scripts/copy_bot_and_token.sh
/tmp/KIT/bot.py &
```

Как видно из конфига, `bot.py` *исполняемый* (в начале был прописан путь до интерпритатора из virtualenv). Virtualenv нужен для того, чтобы поставить последний python на Orange Pi Zero.

Работа бота реализована следующим образом:
При загрузке запускается:
- `shadowsocks`-клиент
- скрипт, запускающий бота

В наешей реализации бот копируется в `/tmp` и запускается оттуда. Благодаря этому, мы можем обновилять его по команде.

Выполнение описанных выше шагов при загрузке мы реализовали поменяв `/ect/rc.local`:


`root@orangepizero:~# cat /etc/rc.local `


```
#!/bin/sh -e
sslocal -c /root/ssconfig.conf &
. /root/KIT_scripts/start_KIT.sh

exit 0
```
