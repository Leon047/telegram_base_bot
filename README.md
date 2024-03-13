# Telegram Base Bot 

> MVC Architecture with Aiogram

<div align='center'>

[![Python](https://img.shields.io/static/v1?label=Python&message=v3.11.x&color=green)](https://www.python.org/downloads/release/python-394/)
[![aiogram](https://img.shields.io/static/v1?label=aiogram&message=v3.4.1&color=blue)](https://docs.aiogram.dev/en/latest/)

</div>

## Overview
Telegram Base Bot is a foundational architectural skeleton for building Telegram bots using Python 3.11 and the Aiogram framework. This project follows the Model-View-Controller (MVC) design pattern, providing a structured and modular approach to developing feature-rich Telegram bots.


## Features
* MVC Architecture: Organize your bot's code in a clean and maintainable structure, separating concerns into models, views, and controllers.
* Aiogram Framework: Leverage the power of Aiogram, a asynchronous Python framework for Telegram Bot API, to streamline bot development.
* Modular Design: Easily extend and customize your bot by adding new features or modifying existing components without affecting the entire codebase.


## Getting Started
> Follow these steps to set up your Telegram Base Bot.

Clone the Repository:
```bash
git clone https://github.com/your_username/telegram_base_bot.git
```

Configure your Bot Token:

Create a new bot on Telegram and obtain the API token.
<pre>
https://t.me/BotFather
</pre>

To add the bot key to the .env file:
<pre>
# bot api key
export BOT_TOKEN=''
</pre>

Set environment variables:
```bash
source .env
```


## Installation using venv

Install Dependencies:
```bash
pip install --upgrade -r requirements.txt
```

Run the Bot:
```bash
python run.py
```


## Installation using Docker

Build and run the Docker Compose services:
```bash
docker-compose -f docker-compose.dev.yml up --build
```


## Project Structure

<pre>
telegram_base_bot/
│
├── src/
│   ├── __init__.py
│   ├── keyboards.py
|   ├── messages.py
|   ├── models.py
|   ├── views.py
│   └── ...
│
├── static/
│   └── ...
|
├── tests/
│   └── ...
|
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.py
</pre>


## License
This project is licensed under the MIT License
