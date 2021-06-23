# telegram-bot

###Errors 
1 polling recursion error
```commandline
2021-06-23 08:58:26,846 (__init__.py:544 MainThread) ERROR - TeleBot: "A request to the Telegram API was unsuccessful. Error code: 409. Description: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running"
```
solution
```commandline
pip install -U git+https://github.com/eternnoir/pyTelegramBotAPI.git
```

old version has bugs in new ver this bug fixed

I forgot and ran from two consoles. it was necessary from one console. an error means that the bot is trying to run in two different applications
