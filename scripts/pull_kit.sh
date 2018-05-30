#!/bin/bash
kill -9 `ps -ef | grep /root/py3/bin/python\ /tmp/KIT/bot.py| grep -v grep | awk '{print $2}'`
rm -rf /tmp/KIT
git -C /root/KIT pull
cp -r /root/KIT /tmp/KIT
/tmp/KIT/bot.py