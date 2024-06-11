import asyncio
from pyrogram import Client
from fuzzysearch import find_near_matches
api_id = 12345678
api_hash = "ubrfu9b9081nlsanfl0poifnaosb"

with open('key_words.txt', 'r', encoding='utf-8') as f:
    key_words = f.readlines()

app = Client("my_account", api_id, api_hash)
"""
async def main():
    for key_word in key_words:
        async for message in app.search_messages(-4253540507, query=key_word.replace('\n', '')):
            await app.forward_messages(
                chat_id=510564762,
                from_chat_id=message.chat.id,
                message_ids=message.id
            )
            await asyncio.sleep(2)
"""

@app.on_message()
async def my_handler(client, message):
    for key_word in key_words:
        matches = find_near_matches(key_word.replace('\n', ''), message.text, max_l_dist=3)
        print(matches, key_word.replace('\n', ''), message.text)
        if matches:
            await app.forward_messages(
                chat_id=510564762,
                from_chat_id=message.chat.id,
                message_ids=message.id
            )

app.run()
