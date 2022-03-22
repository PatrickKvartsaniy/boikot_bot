import logging

from fastapi import FastAPI, Request

from bot import TelegramBot

app = FastAPI()


@app.post("/webhook/")
async def webhook(req: Request):
    body = await req.json()
    print(body)

bot = TelegramBot()
logging.info(bot.set_webhook())
