
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.hui", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       

    await event.edit('''`    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/`''')
    await asyncio.sleep(0.5)
    await event.edit('''`    (  )   (   (  ()
     ) (   ()  )  )
     ( )  (    ( (
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/`''')
    await asyncio.sleep(0.5)
	await event.edit('''`    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/`''')
    await asyncio.sleep(0.5)
    await event.edit('''`    (  )   (   (  ()
     ) (   ()  )  )
     ( )  (    ( (
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/`''')
