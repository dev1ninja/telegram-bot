1. pip install pyTelegramBotAPI
2. python bot.py

# documentation about ubuntu service
1. script file location -> /etc/telegram-bot/telegram-bot/bot.py
2. service location -> /lib/systemd/system/telegram-bot-py.service
3. how to check service's status? -> sudo systemctl status telegram-bot-py.service
4. how to stop service? -> sudo systemctl stop telegram-bot-py.service
5. how to start service? -> sudo systemctl start telegram-bot-py.service
6. how to restart service? -> sudo systemctl restart telegram-bot-py.service

# PS: Reference link
    https://tecadmin.net/setup-autorun-python-script-using-systemd/