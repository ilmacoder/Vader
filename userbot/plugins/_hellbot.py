"""HellBot Help Command"""

from userbot import *
from userbot import CMD_HELP
from hellbot.utils import *


@bot.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def hellbott(event):
    if event.fwd_from:
        return
    """ .plinfo cmd """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`▶️ `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.edit(["NEED_MODULE"] + "\n\n" + string)

# COPYRIGHT (C) 2021 By Ilma_Coder and LEGENDX22 and HELLBOT

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by Hellbot
# Mobile me back option he uspe click karde madhachod kang kiya to dekh


import os, re
try:
    from Hellbot import id
except:
    os.system("pip install HellBot")
  
os.system("pip install -U telethon")
from Hellbot import id
from telethon.tl.functions.contacts import BlockRequest as block
from telethon import Button, custom, events, functions

# back button click kr madarchod
from ..import ALIVE_NAME
HELL_USER = ALIVE_NAME

BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_MAD = f"Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ HellBot, ғᴏʀ {HELL_USER}'s Pʀᴏᴛᴇᴄᴛɪᴏɴ "
else:
    BOT_MAD = BOT_MSG   

WARN = (
  f'''
{BOT_MAD}
Hᴇʏ ᴛʜᴇʀᴇ!!Hellbot here _ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ {HELL_USER}..\nDᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈__**
__Mʏ Mᴀsᴛᴇʀ {HELL_USER}  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !!__ \n"
Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..
Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...
Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ..
Cʜᴏᴏsᴇ ᴀɴʏ Rᴇᴀsᴏɴ & GTFO
''')

HELL_BOT_PIC = os.environ.get("PMPERMIT_PIC", None)
if HELL_BOT_PIC is None:
    HELL_PIC = "https://telegra.ph/file/47c75258c3e5b14c88f0f.jpg"
else:
    HELL_PIC = HELL_BOT_PIC

back = [[Button.inline("«« Bᴀᴄᴋ", data="pm_back")]]
@tgbot.on(events.InlineQuery())
async def inline_Ilma(event):
  piro = event.text
  if event.query.user_id == bot.me.id and piro == 'pmsecure' or event.query.user_id==id and piro=='pmpermit':
    LEGENDX = event.builder
    Ilma = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
    Ilma += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
    PROBOYX = LEGENDX.photo(file=HELL_PIC, text=WARN, buttons=Ilma)
    await event.answer([PROBOYX])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chutia')))
async def chutia_aayaa(event):
  global back
  if event.sender_id !=bot.me.id or event.sender_id != id:
     CONFIRM = [[Button.inline("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", data='confirm_chutia')]]
     CONFIRM += back
     await event.edit("**Aʀᴇ ʏᴏᴜ sᴘᴀᴍᴍᴇʀ?**", buttons=CONFIRM)
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'confirm_chutia')))
async def confirmed(event):
  pro=event.sender_id
  global block
  if pro != bot.me.id or pro != ID:
    await event.edit("**Oʜᴋ sᴏ ɢᴏ ᴛᴏ ʜᴇʟʟ ᴅᴜᴅᴇ 😁**")
    await bot(block(pro))
  else:
     No = "**Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ**"
     await event.answer(No, alert=False)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'frnd_bsdk')))
async def Inline_legendx(event):
  piro = event.sender_id
  global back
  if piro != bot.me.id or piro != id:
    await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  else:
    await event.answer("**Mᴀsᴛᴇʀ, ᴜsᴇ** .approve ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʜɪᴍ")
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'noobda')))
async def noobda (event):
  global back
  Piro = [[Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/hellbotchat"), Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/UltraXoT")]]
  Piro += [[Button.url("Rᴇᴘᴏ", "https://github.com/hellboy-op")]]
  Piro += back
  await event.edit("**Cʜᴇᴄᴋɪɴɢ ᴛʜᴇsᴇ ʟɪɴᴋs**", buttons=Piro)
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pm_back')))
async def inline_legend(event):
  acha = event.sender.first_name
  jnl = bot.me.first_name
  Ilma = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
  Ilma += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
  await event.edit(f"Hᴇʟʟᴏ {acha}, ᴍʏ sᴇʟғ UʟᴛʀᴀX, ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ {jnl}!", buttons=Ilma)
  
  
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'nino')))
async def _(event):
  global back
  await event.edit("**Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!**", buttons=back)
  
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'hmmmmm')))
async def _(event):
  kk = [[Button.inline("Yᴇs", data='confirm_chutia')]]
  kk += [[Button.inline("Nᴏ", data='nino')]]
  await event.edit("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", buttons=kk)

  


# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar madharchod 

# Last Warn - Undo the removed part else be ready for DMCA by Hellbot
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
