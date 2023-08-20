# Telegram Bot with Parser of Data

![Telegram](https://github.com/ToshiroAkihabara/icons/blob/main/telegram_icon-icons.com_72055%20(1).png)
![Bot](https://github.com/ToshiroAkihabara/icons/blob/main/user_bot_robot_icon_146900.png)


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
You can get secret TOKEN from Bot Father. 

ADMIN_ID from this [bot](https://t.me/username_to_id_bot) or in another way.

# Usage

Run the main file: 
```
python piterGSM.py
```
After running the script it'll create a new catalog "json_files" with json files and a new catalog "csv_files" with csv files.
# Feedback

This is my a first project in python. I'll glad to see the feedback.
# License

[MIT License](https://choosealicense.com/licenses/mit/)
