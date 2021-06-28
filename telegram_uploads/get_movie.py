# " Made by @e3ris for Ultroid "
# < https://github.com/TeamUltroid/Ultroid >

# Thanks to @AlPacinoDump And @ProSearchBot
# This plugin uses (Backup of APD channel) and
# And (Inline query of @ProSearchBot) 
# to fetch Movies.

"""
✘ **USE :**
• Get Movies Easily with one CMD :)
• Its not 100% perfect, use some 🧠

✘ **Commands Available :**
• `{i}imovie <some_movie_name>`
• `{i}movie <some_text>`

*imovie works using @prosearchbot.
*movie and c_movie uses a pvt channel,
*Use {i}c_movie to check.
"""

from asyncio import sleep
from telethon.tl.types import InputMessagesFilterVideo as Video
from telethon.errors import ChannelInvalidError, ChannelPrivateError

from . import *


@ultroid_cmd(pattern="movie ?(.*)")
async def apd_get_movie(event):
    if event.fwd_from:
        return
    here, skip = event.chat_id, 0
    chat = -1001233287542
    skip_error = "`Skip Value should be a Number,`\n"
    skip_error += "correct format: `{HNDLR}movie Interstellar ; 3`"
    not_joined_error = "You haven't joined the channel yet,\n"
    not_joined_error += "Click [Here](https://t.me/joinchat/2mDXUO6PU0Q5OGUx) to join."
    # if Link's dead, msg @e3ris 🚶🤡🚶
    args = event.pattern_match.group(1)
    if not args:
        if not event.is_reply:
            await eor(event, "`Gib a Movie name, peru...` 🙆")
            return
        else:
            args = str((await event.get_reply_message()).message)
    eris = await eor(event, f"`Searching for {args}`")
    if ";" in args:
        split = args.split(";", 2)
        args = split[0].strip()
        try:
            skip = int(split[1].strip())
            if skip > 20:
                return await eris.edit("Woah, too mach stress, me nu work")
        except ValueError:
            return await eris.edit(skip_error)
    try:
        total_result = ((await ultroid_bot.get_messages(
            chat, search=args, filter=Video,
            )).total
        )
    except (ChannelPrivateError, ValueError):
        return await eris.edit(f"{not_joined_error}", link_preview=False)
    except Exception as ex:
        return await eris.edit(f"Error: `{ex}`")
    if total_result == 0:
        return await eod(eris, f"**No results found for** :\n `{args}`", time=6)
    await eris.edit(
        f"**Found {total_result} results for**\n `{args}`",
    )
    try:
        movie = await ultroid_bot.get_messages(
            chat, search=args, filter=Video, limit=20, reverse=True,
        ) 
        await ultroid_bot.send_file(
            here,
            movie[skip],
            caption=str(movie[skip].text),
        )
    except Exception as ex:
        await eris.edit(f"Error: `{ex}`")
        return
    await sleep(3)
    await eris.delete()


@ultroid_cmd(pattern="cmovie ?(.*)")
async def check_movie(e):
    if e.fwd_from:
        return
    here, chat, c = e.chat_id, -1001233287542, 1
    args = e.pattern_match.group(1)
    if not args:
        await eor(e, "`Wen giving args, sar`")
        return
    eris = await eor(e, "`Processing...`")
    file_names = f"**Result for queries {args}** :\n\n"
    try:
        msgs = await ultroid_bot.get_messages(
            chat, search=args, filter=Video, limit=18, reverse=True,
        )
    except ChannelPrivateError:
        await eris.edit(f"Error. Pls Do `{HNDLR}movie Barfi` for Help.")
        return
    except Exception as ex:
        return await eris.edit(f"Error: `{ex}`")
    if msgs.total == 0:
        return await eod(eris, f"**No results for**:\n`{args}`", time=6)

    for msg in msgs:
        fn = msg.text.split("\n", 1)[0]
        file_names += f"{c}: {fn}\n"
        c += 1
    await eris.edit(file_names)


@ultroid_cmd(pattern="imovie ?(.*)")
async def pro_search_bot(e):
    if e.fwd_from:
        return
    here, skip = e.chat_id, 0
    args = e.pattern_match.group(1)
    if not args:
        await eor(e, "`Wen giving args, senpai`")
        return
    eris = await eor(e, "`...`")
    if ";" in args:
        split = args.split(";", 2)
        args = split[0].strip()
        try:
            skip = int(split[1].strip())
        except ValueError:
            return await eris.edit("Error: use integer in args")
    try:
        pro_search = await ultroid_bot.inline_query(
            "ProSearchBot", args,
        )
    except BotResponseTimeoutError:
        return await eris.edit("Bot R.I.P")
    except Exception as ex:
        return await eris.edit(f"Error: \n{ex}")
    if len(pro_search) == 0:
        await eod(eris, "**No movies found for :**\n`{args}`", time=6)
        return
    msg = await pro_search[skip].click(
        "me", silent=True,
    )
    caption = str(msg.text)
    await ultroid_bot.send_file(
        here,
        msg,
        caption=f"{caption} \n ➠ **Plugin : @TestingPluGinnn**",
        reply_to=e.reply_to_msg_id if e.is_reply else None,
        silent=False,
    )
    await msg.delete()
    await sleep(3)
    await eris.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
