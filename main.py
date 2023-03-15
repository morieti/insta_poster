import os
import random

import pandas as pd
from instabot import Bot

from config import Config


def get_caption(file: str):
    captions = pd.read_csv('caption/captions.csv')
    filename = file.split('/')[1]
    files = list(captions.get('file'))

    try:
        index = files.index(filename)
        return captions.get('caption')[index]
    except ValueError:
        return ''


def main():
    bot = Bot()
    bot.login(username=Config.username, password=Config.password)

    files = os.listdir('posts')
    file = f'posts/{random.choice(files)}'
    caption = get_caption(file)
    bot.upload_photo(file, caption=caption)


if __name__ == '__main__':
    main()
