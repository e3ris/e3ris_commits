# " Made by @e3ris for Ultroid "
# < https://github.com/TeamUltroid/Ultroid >
# This Plugin uses @Text2gifBot.

"""
• t2g -> text2gif 
✘ Make Fancy Gif from your own text!
✘ **CMD** : `{i}t2g (some_text)`
"""


import random
import emoji
import re

from .. import *


def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)

@catub.cat_cmd(pattern="t2g ?(.*)")
async def ttg(e):
    if e.fwd_from:
        return
    chat = "text2gifBot"
    c = None
    eris = await e.edit("`...`")
    args = e.pattern_match.group(1)
    if not args:
        args = "give some text"
    if ";" in args:
    	fx = args.split(";")
    	args = fx[0].strip()
    	c = int(fx[1].strip()) - 1
    args = remove_emoji(args)
    if not c or c > 28:
        c = random.randint(1, 28)
    try:
        res = await ultroid.inline_query(
            chat, args,
        )
        qi = await res[c].click("me")
        await ultroid.send_file(
            e.chat_id,
            qi,
            reply_to=e.reply_to_msg_id if e.is_reply else None,
        )
        await qi.delete()
        await eris.delete()
    except Exception as fn:
        await eod(eris, f"`{fn}`")
        return


