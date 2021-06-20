► EVALPy
import os
from telethon import utils, types
dl = await bot.download_media(reply.media, "k.opus")
await bot.send_file(chat, dl, attributes=[types.DocumentAttributeAudio(duration=210, voice=True, title="huehue", waveform=utils.encode_waveform(bytes((1, 2, 4, 6, 8, 10, 20, 30, 40, 43, 44, 45, 44, 43, 40, 30, 20, 10, 8, 6, 4, 2, 1)) * 2))]) 

 ► OUTPUT: 
Success