"""

Let me find that for you! 

Syntax:

 .mb keyword (MollywoodBot) 

 .tm keyword (teamMalayalam) 

By @Deonnn 

"""

from telethon import events

import os

import requests

import json

from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="mb (.*)"))

async def _(event):

 

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://t.me/share/url?url={}".format(input_str.replace(" ","%20"))

    response_api = sample_url

    if response_api:

        await event.edit("**You can get the file in 2 steps!**\n\nStep 1: Subscribe to @MollywoodBot. \n(ignore this step if you are already subscribed)\n\nStep 2: Click here 👉 [{}]({}) and select MollywoodBot.\n\n`Thank me Later 😇` ".format(input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later.")

@borg.on(admin_cmd(pattern="tm (.*)"))

async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    sample_url = "https://t.me/share/url?url={}".format(input_str.replace(" ","%20"))

    response_api = sample_url

    if response_api:

        await event.edit("**You can get the file in 2 steps!**\n\nStep 1: Join @teamMalayalam.\n(ignore this step if you are already joined)\n\nStep 2: Click here 👉 [{}]({}) and select teamMalayalam.\n\n`Thank me Later 😇` ".format(input_str,response_api.rstrip()))

    else:

        await event.edit("Something went wrong. Please try again later.")
