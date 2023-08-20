# Telegram Bot with Parser of Data

![Telegram](https://github.com/ToshiroAkihabara/icons/blob/main/telegram_icon-icons.com_72055%20(1).png)
![Bot](https://github.com/ToshiroAkihabara/icons/blob/main/user_bot_robot_icon_146900.png)

Continuation of the previous project where we was parsed some data from the [site](https://pitergsm.ru/). 
Now, I combined previous function with a bot in telegram together using aiogram library. 
The bot could send you a data from site to you in the private chat of telegram in real life. 
You could use the bot as it is if you want but my recomendation to remake it for your own project.


# Installation

Clone this repository and install the dependencies:
```
git clone https://github.com/ToshiroAkihabara/TGParserBot
```
Open the repository and create a new virtual enviroment on Windows:
```
python -m venv venv
```
Activate the virtual enviroment:
```
venv\Scripts\activate
```
Use the [pip](https://pip.pypa.io/en/stable/) package manager to install the project dependencies.
```
pip install -r requirements.txt
```
Open the .env.example and change a secret data inside. 
```
TOKEN=YOUR_TOKEN
ADMIN=YOUR_ADMIN_ID
```
You can get secret TOKEN from [Bot Father](https://t.me/bote_father) and ADMIN_ID from this [bot](https://t.me/username_to_id_bot).
After that you must to delete the file extension of .env.example. In finally you have file .env without any extension. 
```
.env
```
# Usage

Run the main file to start: 
```
python PiterGSM_bot.py
```
The bot will send you a notification message in private chat of telegram after running. 

You have access the following commands:

- /start - Run the bot; 

- /help - Command list.

There are some photos of project working process below:
<div id="header" align="center">
<img src="https://github.com/ToshiroAkihabara/icons/blob/main/photos/mainmenu.png" width="262"/>
<img src="https://github.com/ToshiroAkihabara/icons/blob/main/photos/models.png" width="250"/>
<img src="https://github.com/ToshiroAkihabara/icons/blob/main/photos/iphones.png" width="270"/>
</div>

# License

[MIT License](https://choosealicense.com/licenses/mit/)
