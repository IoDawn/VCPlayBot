from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIkK2CzXewg1aRmhaabhXBJ-5EBSYJMAALEAwAC5ISYVR_otwhfP9zrHwQ")
    await message.reply_text(
        f"""<b>Hei {message.from_user.first_name}!
\nSaya adalah *Roso* musik bot! Selain Strong dan berEnergi saya juga pandai bernyanyi,Saya dapat menyanyikan semua lagu yang anda pilih untuk obrolan grup anda♬
\nHubungi [Owner](https://t.me/assistenpokonya_bot) saya jika anda juga ingin mendengarkan saya bernyanyi!
\nTekan /help untuk melihat daftar perintah.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Support Channel", url="https://t.me/arunasupportbot",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑‍💻 Contact me", url="https://t.me/assistenpokonya_bot"
                    ),
                    InlineKeyboardButton(
                        "🤖 Other bot", url="https://t.me/MrsRoso_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍺 Add Roso To Your Group", url="https://t.me/MisRoso_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support 📢", url="https://t.me/arunasupportbot"
                    ),
                    InlineKeyboardButton(
                        "Help ❔", url="https://t.me/assistenpokonya_bot"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hei {message.from_user.first_name}!
\n/play <judul lagu> - Menyanyikan lagu yang anda minta
/dplay <judul lagu> - Memutar lagu yang anda minta melalui deezer
/splay <judul lagu> - Menyuruh jio saavn untuk menyanyikan lagu yang anda minta
/playlist - Menunjukkan daftar putar lagu
/current - Menampilkan lagu yang sekarang sedang diputar
/song <judul lagu> - unduh lagu yang anda inginkan dengan cepat
/search <pertanyaan> - mencari detail video diyoutube
/deezer <judul lagu> - unduh lagu yang kamu dengan cepat via deezer
/saavn <judul lagu> - unduh lagu yang kamu inginkan dengan cepat via saavn
/video <judul video> - unduh lagu yang kamu inginkan dengan cepat
\n*Khusus Admin Grup*
/player - buka panel pengaturan pemutar musik
/pause - suruh Roso diam dulu
/resume - suruh Roso lanjut nyanyi
/skip - memutar lagu berikutnya
/end - suruh Roso berhenti bernyanyi
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Support", url="https://t.me/arunasupportbot"
                    ),
                    InlineKeyboardButton(
                        "❔ Help", url="https://t.me/assistenpokonya_bot"
                    )
                ]
            ]
        )
    )    
