# BY @STARKTM1

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.sing", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Singing...")

    await asyncio.sleep(1)

    x=(random.randrange(1,11))

    if x==1:

        await event.edit("🎶 ഒരുനാൾ തരളമിവനിൽ... പടരൂ വനലതികയായ്... മുറുകെ... മതിവരുവോളം സഖീ... 🎶")

    if x==2:

        await event.edit("🎶 അഴലിന്റെ ആഴങ്ങളിൽ അവൾ മാഞ്ഞുപോയ്... നോവിന്റെ തീരങ്ങളിൽ ഞാൻ മാത്രമായ്... 🎶")

    if x==3:

        await event.edit("🎶 ആവണിപ്പൊന്നൂഞ്ഞാലാടിക്കാം നിന്നെ ഞാൻ... ആയില്ല്യം കാവിലെ വെണ്ണിലാവേ... 🎶")

    if x==4:

        await event.edit("🎶 ഇന്ദ്രനീലിമയോലും ഈ മിഴി പൊയ്കകളിൽ... ഇന്നലെ നിൻ മുഖം നീ നോക്കി നിന്നൂ... 🎶")

    if x==5:

        await event.edit("🎶 മയിലായ് പറന്നുവാ മഴവില്ലു തോൽക്കുമെന്നഴകേ... 🎶")

    if x==6:

        await event.edit("🎶 നിലാവിന്റെ നീലഭസ്മ കുറിയണിഞ്ഞവളേ... കാതിലോലക്കമ്മലിട്ടു കുണുങ്ങി നിന്നവളേ... 🎶")

    if x==7:

        await event.edit("🎶 നീയൊരു പുഴയായ് തഴുകുമ്പോൾ ഞാൻ പ്രണയം വിടരും കരയാവും... 🎶")    

    if x==8:

        await event.edit("🎶 അരികിൽ നീയുണ്ടായിരുന്നെങ്കിലെന്നു ഞാൻ... ഒരുമാത്ര വെറുതേ നിനച്ചുപോയി... 🎶")

    if x==9:

        await event.edit("🎶 എത്രയോ ജന്മമായ് നിന്നെഞാൻ തേടുന്നു... അത്രമേൽ ഇഷ്ടമായ് നിന്നെയെൻ പുണ്യമേ... 🎶")

    if x==10:

        await event.edit("🎶 മഴത്തുള്ളികൾ പൊഴിഞ്ഞീടുമീ നാടൻ വഴി... നനഞ്ഞോടിയെൻ കുടക്കീഴിൽ നീ വന്ന നാൾ... 🎶")
