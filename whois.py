#from .. import catub
import random
@ultroid_cmd(pattern="whois")
async def infoo(event):
  re = await event.get_reply_message()
  an = await bot.get_permissions(event.chat_id,re.sender_id)
  if not re:
    await event.edit("Reply any user")
  else:
    await event.edit("processing....")


  numm = ["+918210284978","+919798216579"]
  fnn = f"{random.choice(numm)}"


  h = await bot.get_messages(event.chat_id)
  i = await bot.get_messages(event.chat_id,from_user=re.sender_id)
  j = await bot.get_participants(event.chat_id)
  gmsg = f"𝗧𝗼𝘁𝗮𝗹 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 : {h.total}"
  userm = f"𝗧𝗼𝘁𝗮𝗹 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 : {i.total}"
  gcm = f"𝗧𝗼𝘁𝗮𝗹 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿𝘀: {j.total}"
  st = "💚 𝗦𝗢𝗠𝗘 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 💜"

  photo = await bot.download_profile_photo(re.sender_id)
  a = await bot.get_permissions(event.chat_id,re.sender_id)
  b = a.is_admin
  if not b:
    c = "𝗔𝗱𝗺𝗶𝗻 : He is not admin"
    d = await bot.get_entity(re.sender_id)
    e = await bot.get_permissions(event.chat_id,re.sender_id)
    id = f"𝗜𝗗 : `{d.id}`"
    uname = f"𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{d.username}"
    fname = f"𝗡𝗮𝗺𝗲 : {d.first_name}"
    jdate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"
    prom = "𝗣𝗿𝗼𝗺𝗼𝘁𝗲𝗱 : Not promoted"
    perm = "𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 : Not admin"
  else:
    c = "𝗔𝗱𝗺𝗶𝗻 : He is admin"
    d = await bot.get_entity(re.sender_id)
    e = await bot.get_permissions(event.chat_id,re.sender_id)
    id = f"𝗜𝗗 : {d.id}"
    f = await bot.get_entity(e.participant.promoted_by)
    usn = f"@{f.username}"
    uname = f"𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{d.username}"
    fname = f"𝗡𝗮𝗺𝗲 : {d.first_name}"
    jadate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"
    prom = f"𝗣𝗿𝗼𝗺𝗼𝘁𝗲𝗱 : `{e.participant.promoted_by}`({usn})"
    perm = f"𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 : below admin permission"
    
    

  
  if not d.phone:
    phone = "𝗣𝗵𝗼𝗻𝗲 : This user number hidden"
  else:
    phone = f"𝗣𝗵𝗼𝗻𝗲 : @{d.phone}"




  if re.sender_id == 500774612:
    phone = f"𝗣𝗵𝗼𝗻𝗲 : {fnn}"


  if e.participant.date:
    jdate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"


  if b == True:
    await event.edit("`Findind information..`")
  else:
    await bot.send_message(event.chat_id,f"{st}\n\n 🙂 {c}\n 🙃 {prom}\n 🤦‍♂️ {id}\n 🙋 {uname}\n 👨‍ {fname}\n 😍 {phone}\n 🙄 {userm}\n 🤔 {gmsg}\n 🤗 {gcm}\n\n 😄 {jdate}\n 🤩 {perm}\n",file=photo)




@ultroid_cmd(pattern="whois")
async def inf(event):
  re = await event.get_reply_message()
  an = await bot.get_permissions(event.chat_id,re.sender_id)
  perm = f"𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 :"
  


  numm = ["+918210284978","+919798216579"]
  fnn = f"{random.choice(numm)}"


  h = await bot.get_messages(event.chat_id)
  i = await bot.get_messages(event.chat_id,from_user=re.sender_id)
  j = await bot.get_participants(event.chat_id)
  gmsg = f"𝗧𝗼𝘁𝗮𝗹 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 : {h.total}"
  userm = f"𝗧𝗼𝘁𝗮𝗹 𝘀𝗲𝗻𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 : {i.total}"
  gcm = f"𝗧𝗼𝘁𝗮𝗹 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿𝘀: {j.total}"
  st = "💚 𝗦𝗢𝗠𝗘 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 💜"

  photo = await bot.download_profile_photo(re.sender_id)
  a = await bot.get_permissions(event.chat_id,re.sender_id)
  if a.is_creator:
    await event.edit("Not any info of owner")


 
  b = a.is_admin
  if not b:
    c = "𝗔𝗱𝗺𝗶𝗻 : He is not admin"
    d = await bot.get_entity(re.sender_id)
    e = await bot.get_permissions(event.chat_id,re.sender_id)
    id = f"𝗜𝗗 : `{d.id}`"
    uname = f"𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{d.username}"
    fname = f"𝗡𝗮𝗺𝗲 : {d.first_name}"
    jdate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"
    prom = "𝗣𝗿𝗼𝗺𝗼𝘁𝗲𝗱 : Not promoted"
    perm = "𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 : Not admin"
  else:
    c = "𝗔𝗱𝗺𝗶𝗻 : He is admin"
    d = await bot.get_entity(re.sender_id)
    e = await bot.get_permissions(event.chat_id,re.sender_id)
    id = f"𝗜𝗗 : {d.id}"
    f = await bot.get_entity(e.participant.promoted_by)
    usn = f"@{f.username}"
    uname = f"𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{d.username}"
    fname = f"𝗡𝗮𝗺𝗲 : {d.first_name}"
    jadate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"
    prom = f"𝗣𝗿𝗼𝗺𝗼𝘁𝗲𝗱 : `{e.participant.promoted_by}`({usn})"
    perm = f"𝗔𝗱𝗺𝗶𝗻 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻𝘀 : below admin permission"
    
    

  
  if not d.phone:
    phone = "𝗣𝗵𝗼𝗻𝗲 : This user number hidden"
  else:
    phone = f"𝗣𝗵𝗼𝗻𝗲 : @{d.phone}"




  if re.sender_id == 500774612:
    phone = f"𝗣𝗵𝗼𝗻𝗲 : {fnn}"


  if e.participant.date:
    jdate = f"𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗱𝗮𝘁𝗲 : {e.participant.date}"


  
  


  if an.participant.admin_rights.change_info == True:
    ch = "⚡ **  Change Info ** = ✅"
  else:
    ch = "⚡ **  Change Info ** = ❌"
  if an.participant.admin_rights.post_messages == True:
    pm = "⚡ **  Post Messages ** = ✅"
  else:
    pm = "⚡ **  Post Messages ** = ❌"
  if an.participant.admin_rights.edit_messages == True:
    em = "⚡ **  Edit messages ** = ✅"
  else:
    em = "⚡ **  Edit messages ** = ❌"
  if an.participant.admin_rights.delete_messages == True:
    dm = "⚡ **  Delete Messages ** = ✅"
  else:
    dm = "⚡ **  Delete Messages ** = ❌"
  if an.participant.admin_rights.ban_users == True:
    bu = "⚡ **  Ban users ** = ✅"
  else:
    bu = "⚡ **  Ban users ** = ❌"
  if an.participant.admin_rights.invite_users == True:
    iu = "⚡ **  Invite Users ** = ✅"
  else:
    iu = "⚡ **  Invite Users ** = ❌"
  if an.participant.admin_rights.pin_messages == True:
    pms = "⚡ **  Pin Messages ** = ✅"
  else:
    pms = "⚡ **  Pin_Messages ** = ❌"
  if an.participant.admin_rights.add_admins == True:
    ad = "⚡ **  Add Admins ** = ✅"
  else:
    ad = "⚡ **  Add Admins ** = ❌"
  if an.participant.admin_rights.manage_call == True:
    mc = "⚡ **  Manage Voice Chat ** = ✅"
  else:
    mc = "⚡ **  Manage Voice Chat  ** = ❌"
  if an.participant.admin_rights.other == True:
    ot = "⚡ **  Other ** = ✅"
  else:
    ot = "⚡ **  Other ** = ❌"

  await bot.send_message(event.chat_id,f"{st}\n\n 🙂 {c}\n 🙃 {prom}\n 🤦‍♂️ {id}\n 🙋 {uname}\n 👨‍ {fname}\n 😍 {phone}\n 🙄 {userm}\n 🤔 {gmsg}\n 🤗 {gcm}\n\n 😄 {jdate}\n 🤩 {perm} 🧡\n\n{ch}\n{pm}\n{em}\n{dm}\n{bu}\n{iu}\n{pms}\n{ad}\n{mc}\n{ot}",file=photo)

