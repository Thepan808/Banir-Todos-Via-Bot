# CREATED BY @PIROXPOWER || @OpFriDay

from choot import Var
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


Blaze = TelegramClient(None, Var.API_KEY, Var.API_HASH)
Blaze.start(bot_token=Var.TOKEN)

print("INICIANDO O SERVIDOR DE BANIR TODOS VIA BOT....") 

"""
MUDANDO PARA COMANDOS AGORA
"""

GANDU = []
for x in Var.OWNER_ID: 
    GANDU.append(x)


@Blaze.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in GANDU:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**Eu estou ativo vosso admin 🧐♦️\nPosso começar a banir qualquer grupo =)** \n\n **__ᏢᎾᏁᎶ🧐♦️__ !!** `{ms}` ms")

"""
 RESTART COMMANDS 
"""
@Blaze.on(events.NewMessage(pattern="^/reiniciar"))
async def restart(e):
    if e.sender_id in GANDU:
        text = "Tururu. . .. Reiniciando🤣!!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Blaze.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 BANALL COMMAND
"""
 
@Blaze.on(events.NewMessage(pattern="^/ban"))
async def testing(event):
  if event.sender_id in GANDU:
   if not event.is_group:
        Reply = f"Ridículo (a)! Use este comando no grupo."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       Raichu = await event.get_chat()
       RaichUB = await event.client.get_me()
       admin = Raichu.admin_rights
       creator = Raichu.creator
       if not admin and not creator:
           await event.reply("Não tenho direitos suficientes!")
           return
       await event.reply("**A Magia do Ban, Ban, Ban está para Começar...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == RaichUB.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


"""
  LEAVE COMMAND 
"""
print("Sair do comando em breve Atualmente estou ocupado") 
print("INICIADO COM SUCESSO... PRONTO PARA USO") 
Blaze.run_until_disconnected()
