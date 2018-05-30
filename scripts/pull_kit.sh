#!/bin/bash
kill -9 `ps -ef | grep /root/py3/bin/python\ /tmp/KIT/bot.py| grep -v grep | awk '{print $2}'`
rm -rf /tmp/KIT
git -C /root/KIT pull
. /root/copy_bot_and_token.sh
/tmp/KIT/bot.py