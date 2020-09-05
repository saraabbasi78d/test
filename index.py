from telethon.sync import TelegramClient
from telethon import events

#======================
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
#======================

app = TelegramClient(
    "your_name",
    api_id='sdfg',
    api_hash="sdfg"
)

def add():
    pass

@app.on(events.NewMessage())
async def add_to_db(event):
    async for message in client.iter_messages(chat):
        add(message.text)
    


if _name_ == '_main_':
    app.start()
    print("App Started... :)")
    app.run_until_disconnected()
