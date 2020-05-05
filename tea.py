
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.tea", outgoing=True))
async def _(event):
if event.fwd_from:
return


await event.edit("`О, привет`")
await asyncio.sleep(0.5)
await event.edit("`попей чаек`")
await asyncio.sleep(0.5)
await event.edit("☕")
await asyncio.sleep(0.5)
await event.edit("☕")
await asyncio.sleep(0.5)
await event.edit("`о, забыл`")
await asyncio.sleep(0.5)
await event.edit("`на`")
await asyncio.sleep(0.5)
await event.edit("🍪")
await asyncio.sleep(0.5)
await event.edit("`Приятного аппетита `")
