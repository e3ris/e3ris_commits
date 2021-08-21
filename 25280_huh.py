► EVALPy
from addons.g import allpaste as n
p(n(reply.text)) 

 ► OUTPUT: 
Traceback (most recent call last):
  File "/root/TeamUltroid/plugins/devtools.py", line 132, in _
    await aexec(cmd, event)
  File "/root/TeamUltroid/plugins/devtools.py", line 181, in aexec
    return await locals()["__aexec"](event, event.client)
  File "<string>", line 6, in __aexec
TypeError: allpaste() missing 1 required positional argument: 'ext'