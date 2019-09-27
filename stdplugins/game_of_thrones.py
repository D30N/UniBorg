# BY @Deonnn
""" Game of thrones quotes plugin
    by @Deonnn
 command  .got
 """

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.got", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x=(random.randrange(1,11))

    if x==1:

        await event.edit("`A mind needs books as a sword needs a whetstone, if it is to keep its edge.`")

    if x==2:

        await event.edit("`There is only one thing we say to death:` **Not today!**")

    if x==3:

        await event.edit("`If you think this has a happy ending, you haven’t been paying attention!.`")

    if x==4:

        await event.edit("`Chaos isn’t a pit. Chaos is a ladder!`")

    if x==5:

        await event.edit("`You know nothing, Jon Snow!`")

    if x==6:

        await event.edit("`Fear cuts deeper than swords.`")

    if x==7:

        await event.edit("`When you play the Game of Thrones, you win or you die.`")    

    if x==8:

        await event.edit("`I'm not going to stop the wheel, I'm going to break the wheel.`")

    if x==9:

        await event.edit("`When people ask you what happened here, tell them the North remembers!`\n`Tell them winter came for House Frey.`")

    if x==10:

        await event.edit("`When the snows fall and the white winds blow...\nThe lone wolf dies, but the pack survives!`")
