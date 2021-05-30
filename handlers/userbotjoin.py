from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "assistenmusik"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Saya sudah bergabung disini seperti yang Anda minta")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@assistenmusik sudah ada didalam chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Kesalahan flood Tunggu 🛑 \n Pengguna {user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung untuk asisten musik! Pastikan pengguna tidak diban dalam grup."
            "\n\nAtau tambahkan secara manual @assistenmusik kedalam grup anda dan coba kembali</b>",
        )
        return
    await message.reply_text(
            "<b>@assistenmusik Roso bergabung kedalam obrolan</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Pengguna tidak dapat meninggalkan grup Anda! Mungkin menunggu flood."
            "\n\nAnda dapat kick saya secara manual jika tidak dibutuhkan</b>",
        )
        return
