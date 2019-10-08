"""
 Filemanager 
 .lsroot to see the list of files in root directory.
 .lslocal to see the list of files in local download directory.
 .rnlocal file_name|new_name to rename a file in local directory.
 .delocal file_name to delete a file in local directory.
"""

# This Source Code Form is subject to the terms of the Mozilla Public

# License, v. 2.0. If a copy of the MPL was not distributed with this

# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events

import subprocess

from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError

import io

import asyncio

import time

import os



if not os.path.isdir("./SAVED"):

     os.makedirs("./SAVED")

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):

     os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)



@borg.on(events.NewMessage(pattern=r"\.lslocal", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    DELAY_BETWEEN_EDITS = 0.3

    PROCESS_RUN_TIME = 100

#    dirname = event.pattern_match.group(1)

#    tempdir = "localdir"

    cmd = "ls ./DOWNLOADS/"

#    if dirname == tempdir:

	

    eply_to_id = event.message.id

    if event.reply_to_msg_id:

        reply_to_id = event.reply_to_msg_id

    start_time = time.time() + PROCESS_RUN_TIME

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    OUTPUT = f"**Files in DOWNLOADS folder:**\n"

    stdout, stderr = await process.communicate()

    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:

        with io.BytesIO(str.encode(stdout)) as out_file:

            out_file.name = "exec.text"

            await borg.send_file(

                event.chat_id,

                out_file,

                force_document=True,

                allow_cache=False,

                caption=OUTPUT,

                reply_to=reply_to_id

            )

            await event.delete()

    if stderr.decode():

        await event.edit(f"**{stderr.decode()}**")

        return

    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

#    else:

#        await event.edit("Unknown Command")







@borg.on(events.NewMessage(pattern=r"\.lsroot", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    DELAY_BETWEEN_EDITS = 0.3

    PROCESS_RUN_TIME = 100

    cmd = "ls"

	

    reply_to_id = event.message.id

    if event.reply_to_msg_id:

        reply_to_id = event.reply_to_msg_id

    start_time = time.time() + PROCESS_RUN_TIME

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    OUTPUT = f"**Files in root directory:**\n"

    stdout, stderr = await process.communicate()

    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:

        with io.BytesIO(str.encode(stdout)) as out_file:

            out_file.name = "exec.text"

            await borg.send_file(

                event.chat_id,

                out_file,

                force_document=True,

                allow_cache=False,

                caption=OUTPUT,

                reply_to=reply_to_id

            )

            await event.delete()

    if stderr.decode():

        await event.edit(f"**{stderr.decode()}**")

        return

    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

	

@borg.on(events.NewMessage(pattern=r"\.lssaved", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    DELAY_BETWEEN_EDITS = 0.3

    PROCESS_RUN_TIME = 100

    cmd = "ls ./SAVED/"

	

    reply_to_id = event.message.id

    if event.reply_to_msg_id:

        reply_to_id = event.reply_to_msg_id

    start_time = time.time() + PROCESS_RUN_TIME

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    OUTPUT = f"**Files in SAVED directory:**\n"

    stdout, stderr = await process.communicate()

    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:

        with io.BytesIO(str.encode(stdout)) as out_file:

            out_file.name = "exec.text"

            await borg.send_file(

                event.chat_id,

                out_file,

                force_document=True,

                allow_cache=False,

                caption=OUTPUT,

                reply_to=reply_to_id

            )

            await event.delete()

    if stderr.decode():

        await event.edit(f"**{stderr.decode()}**")

        return

    await event.edit(f"{OUTPUT}`{stdout.decode()}`")

@borg.on(events.NewMessage(pattern=r"\.rnsaved ?(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    DELAY_BETWEEN_EDITS = 0.3

    PROCESS_RUN_TIME = 100

    input_str = event.pattern_match.group(1)

    if "|" in input_str:

        src, dst = input_str.split("|")

        src = src.strip()

        dst = dst.strip()

    cmd = f"mv ./SAVED/{src} ./SAVED/{dst}"

    reply_to_id = event.message.id

    if event.reply_to_msg_id:

        reply_to_id = event.reply_to_msg_id

    start_time = time.time() + PROCESS_RUN_TIME

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    OUTPUT = f"**Files in root directory:**\n"

    stdout, stderr = await process.communicate()

    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:

        with io.BytesIO(str.encode(stdout)) as out_file:

            out_file.name = "exec.text"

            await borg.send_file(

                event.chat_id,

                out_file,

                force_document=True,

                allow_cache=False,

                caption=OUTPUT,

                reply_to=reply_to_id

            )

            await event.delete()

    if stderr.decode():

        await event.edit(f"**{stderr.decode()}**")

        return

    await event.edit(f"🖊 File renamed successfully!\nOld name: `{src}` \nNew name: `{dst}`")

	

@borg.on(events.NewMessage(pattern=r"\.rnlocal ?(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    DELAY_BETWEEN_EDITS = 0.3

    PROCESS_RUN_TIME = 100

    input_str = event.pattern_match.group(1)

    if "|" in input_str:

        src, dst = input_str.split("|")

        src = src.strip()

        dst = dst.strip()

    cmd = f"mv ./DOWNLOADS/{src} ./DOWNLOADS/{dst}"

    reply_to_id = event.message.id

    if event.reply_to_msg_id:

        reply_to_id = event.reply_to_msg_id

    start_time = time.time() + PROCESS_RUN_TIME

    process = await asyncio.create_subprocess_shell(

        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE

    )

    OUTPUT = f"**Files in root directory:**\n"

    stdout, stderr = await process.communicate()

    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:

        with io.BytesIO(str.encode(stdout)) as out_file:

            out_file.name = "exec.text"

            await borg.send_file(

                event.chat_id,

                out_file,

                force_document=True,

                allow_cache=False,

                caption=OUTPUT,

                reply_to=reply_to_id

            )

            await event.delete()

    if stderr.decode():

        await event.edit(f"**{stderr.decode()}**")

        return

    await event.edit(f"🖊 File renamed successfully!\nOld name: `{src}`\nNew name: `{dst}`")

        

@borg.on(events.NewMessage(pattern=r"\.delsave (.*)", outgoing=True))

async def handler(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    pathtofile = f"./SAVED/{input_str}"



	

    if os.path.isfile(pathtofile):

     os.remove(pathtofile)

     await event.edit("🗑 File deleted successfully!")

	 

    else:

         await event.edit("⚠️ File not found!\nUse `.lssaved` to list available files in **SAVED** folder.")

        

@borg.on(events.NewMessage(pattern=r"\.delocal (.*)", outgoing=True))

async def handler(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    pathtofile = f"./DOWNLOADS/{input_str}"



	

    if os.path.isfile(pathtofile):

     os.remove(pathtofile)

     await event.edit("🗑 File deleted successfully!")

	 

    else:

         await event.edit("⚠️ File not found!\nUse `.lslocal` to list available files in **DOWNLOADS** folder.")