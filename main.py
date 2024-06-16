import asyncio
from pyrogram import Client
from fuzzysearch import find_near_matches
import os
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()

api_id = int(os.getenv("api_id"))
api_hash = os.getenv("api_hash")

with open('key_words.txt', 'r', encoding='utf-8') as f:
    key_words = f.readlines()


app = Client("my_account", api_id, api_hash)


@app.on_message()
async def my_handler(message):
    for key_word in key_words:
        matches = find_near_matches(key_word.replace('\n', ''), message.text, max_l_dist=3)
        if matches:
            await app.forward_messages(
                chat_id=510564762,
                from_chat_id=message.chat.id,
                message_ids=message.id
            )
            break

app.run()
