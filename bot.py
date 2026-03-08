from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = "8424375544:AAFf6HPJ6geScdjUQj8pUfL8IRJLdwAhpXA"

ADMIN_IDS = [8771036890]
ACTIVE_CHATS = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Lists ​📑​"],
        ["Contact Admin 💬"],
        ["How To Order?💭"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    context.user_data["admin_mode"] = False
    ACTIVE_CHATS[update.effective_user.id] = False

    await update.message.reply_text(
        "Hola, αm᥆𝗋𝗂𝖾𝗌❕\n"
        "Good Morning 👋🏻✨ Hope u have a nice day 🫧\n\n"
        "This bot will help u to answering ur questions, press the menu on the list please. 📨",
        reply_markup=reply_markup
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()
    user = update.effective_user

    if text == "Lists ​📑​":
        await update.message.reply_text(
         "💭 Catalogue:\n\n"             
            "ᥲ. ⍴rᥱmіᥙm m᥆᥎іᥱ ᥲᥴᥴᥱss\n⌗. Netflix\n⌗. Vidio\n⌗. Disney +\n⌗. YouTube\n⌗. Dramabox\n⌗. Loklok\n⌗. Bstation\n⌗. iQIYi\n⌗. WeTV\n⌗. Viu\n⌗. Vision Plus\n\n"             
            "ᑲ. ⍴rᥱmіᥙm mᥙsіᥴ ᥲᥴᥴᥱss\n⌗. Spotify\n⌗. Apple Music\n\n"             
            "ᥴ. ⍴rᥱmіᥙm s𝗍ᥙძᥡ ᥲᥴᥴᥱss\n⌗. ChatGPT\n⌗. Zoom\n⌗. Duolingo\n⌗. Brainly\n\n"             
            "d. ⍴rᥱmіᥙm rᥱᥲძіᥒg ᥲᥴᥴᥱss\n⌗. Wattpad\n⌗. Fizzo Novel\n⌗. Noveltoon\n\n"             
            "ᥱ. ⍴rᥱmіᥙm ᥱძі𝗍s ᥲᥴᥴᥱss\n⌗. Alight Motion\n⌗. Wink\n⌗. Capcut\n⌗. Canva\n⌗. Picsart\n\n"             
            "𝖿. ⍴rᥱmіᥙm 𝗍ᥱᥣᥱgrᥲm\n⌗. Resell Vilog (Via Login) \n⌗. Resell Gift (Via Gift) \n⌗. Pribadi Vilog (Via Login) \n⌗. Pribadi Gift (Via Gift)\n\n"             
            "ᥴ᥆mᥱ sᥱᥱ 𝗍һіs ᑲᥱᥲᥙ𝗍і𝖿ᥙᥣ і𝗍ᥱm, sᥱᥱ 𝗍һᥱ ⍴rіᥴᥱᥣіs𝗍 ᥆ᥒ @oOmamories ᥲᥒძ ᥣᥱᥲ᥎ᥱ ᥡ᥆ᥙr mᥱssᥲgᥱ 𝗍᥆ @omamories ძ᥆ᥒ'𝗍 mіss ᥆𝗍һᥱr ᑲᥱᥲᥙ𝗍і𝖿ᥙᥣ і𝗍ᥱms 💻🖤"
        )

    elif text == "Contact Admin 💬":

        context.user_data["admin_mode"] = True
        ACTIVE_CHATS[user.id] = True

        await update.message.reply_text(
            "Text here, we'll answer ASAP 💨"
        )

    elif text == "How To Order?💭":

        await update.message.reply_text(
            "Cara order:\n"             
            "1. sᥙᑲs kᥱ @oOmamories ძᥲᥒ ⍴ᥲs𝗍іkᥲᥒ ȷ᥆іᥒ kᥱ @omamories 𝗍ᥱrᥱᥣᑲіһ ძᥲһᥙᥣᥙ\n\n"             
            "2. 𝗍ᥱᥒ𝗍ᥙkᥲᥒ ⍴r᥆ძᥙk ᥡᥲᥒg ᥲkᥲᥒ ძі ᑲᥱᥣі\n\n"             
            "3. ᥴᥱk kᥱ𝗍ᥱrsᥱძіᥲᥲᥒ ⍴r᥆ძᥙk ძᥱᥒgᥲᥒ mᥱmᥱᥒᥴᥱ𝗍 mᥱᥒᥙ 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘈𝘥𝘮𝘪𝘯  ძᥲᥒ 𝗍ᥙᥒggᥙ sᥲm⍴ᥲі ᥲძmіᥒ mᥱmᑲᥲᥣᥲs\n\n"             
            "4. ᥴ᥆ᥒ𝖿іrm ⍴ᥱsᥲᥒᥲᥒ ძgᥒ mᥱᥣᥲkᥙkᥲᥒ ⍴ᥲᥡmᥱᥒ𝗍 kᥱ @omamoripay\n\n"             
            "5. kіrіm sᥴrᥱᥱᥒsһ᥆᥆𝗍 ᑲᥙk𝗍і ⍴ᥱmᑲᥲᥡᥲrᥲᥒ ძᥲᥒ sᥱr𝗍ᥲkᥲᥒ ᥙsᥒ kᥲmᥙ\n\n"             
            "6. ⍴ᥱsᥲᥒᥲᥒ sіᥲ⍴! ᥲძmіᥒ ᥲkᥲᥒ mᥱᥒgһᥲm⍴іrі r᥆᥆mᥴһᥲ𝗍mᥙ ᥙᥒ𝗍ᥙk mᥱᥒgіrіm ⍴ᥱsᥲᥒᥲᥒ, m᥆һ᥆ᥒ 𝗍ᥙᥒggᥙ~"
        )

    else:

        if context.user_data.get("admin_mode") and ACTIVE_CHATS.get(user.id):

            message = update.message.text

            for admin_id in ADMIN_IDS:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=(
                        f"📩 New Message\n\n"
                        f"👤 {user.first_name}\n"
                        f"🆔 {user.id}\n\n"
                        f"{message}\n\n"
                        f"Reply message ini untuk balas.\n"
                        f"Ketik /close sambil reply untuk tutup session."
                    )
                )

# 🔹 ADMIN REPLY TANPA KETIK ID
async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in ADMIN_IDS:
        return

    if update.message.reply_to_message:
        replied_text = update.message.reply_to_message.text

        if "🆔" in replied_text:
            try:
                user_id = int(replied_text.split("🆔")[1].split("\n")[0].strip())

                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"📨 Admin:\n\n{update.message.text}"
                )

                await update.message.reply_text("✅ Reply sent!")

            except:
                pass


# 🔹 CLOSE SESSION DARI ADMIN
async def close_session(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Pastikan yang kirim adalah admin
    if update.effective_user.id not in ADMIN_IDS:
        return

    # Pastikan admin reply ke pesan bot
    if update.message.reply_to_message:

        replied_text = update.message.reply_to_message.text

        if "🆔" in replied_text:
            try:
                user_id = int(replied_text.split("🆔")[1].split("\n")[0].strip())

                ACTIVE_CHATS[user_id] = False
                await context.bot.send_message( 
                    chat_id=user_id,
                    text="🔒 This chat session has been closed by admin."
                )       

                await update.message.reply_text("✅ Session closed.")

            except:
                await update.message.reply_text("Failed to close session.")



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("close", close_session))
app.add_handler(MessageHandler(filters.REPLY & filters.TEXT & filters.User(ADMIN_IDS), admin_reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

app.run_polling()
