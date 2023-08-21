# Telegram Bot with Parser of Data

<div id="header" align="center">
<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjRibzRqZ2YycmJuNWxreXhxczU4MzkxYjJ4NHl1a25iNXIwMWw4ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/EuMes40JZirYe18nYY/giphy.gif" width="100"/>
</div>

Continuation of the previous project where we was parsed some data from the [site](https://pitergsm.ru/). 
Now, I combined previous function with a bot in telegram together using aiogram library. 
The bot could send you a data from site to you in the private chat of telegram in real life. 
You could use the bot as it is if you want but my recomendation to remake it for your own project.


# Installation

Clone this repository:
```
$ git clone https://github.com/ToshiroAkihabara/TGParserBot
```
Create, a new virtual enviroment, activate it for Windows, Linux & MacOS and install required dependencies:
```
$ python -m venv venv
$ venv\Scripts\activate
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Open the .env.example and change a secret data inside: 
```
TOKEN=YOUR_TOKEN
ADMIN=YOUR_ADMIN_ID
```
You can get secret TOKEN from [Bot Father](https://t.me/BotFather) and ADMIN_ID from this [bot](https://t.me/username_to_id_bot).
Rename the file ```.env.example``` to ```.env```

# Usage

Run the main file to start: 
```
$ python PiterGSM_bot.py
```
The bot will send you a notification message in private chat of telegram after running. 

You have access the following commands:

- /start - Run the bot; 

- /help - Command list.

There are some photos of the project working process below:
<div id="header" align="center">
<img src="https://github.com/ToshiroAkihabara/TGParserBot/blob/main/photos/mainmenu.png" width="262"/>
<img src="https://github.com/ToshiroAkihabara/TGParserBot/blob/main/photos/models.png" width="250"/>
<img src="https://github.com/ToshiroAkihabara/TGParserBot/blob/main/photos/iphones.png" width="270"/>
</div>

# License

[MIT License](https://choosealicense.com/licenses/mit/)
