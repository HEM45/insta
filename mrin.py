import telebot
import requests
import re
import threading
import time
import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired

# Function to read token from file
def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

REQUIRED_CHANNEL = '@mrinxdildos'
BOT_LIST = "https://t.me/MRiNxDiLDOS/92"
OWNER_URL = "https://t.me/MrinMoYxCB"
OWNER_IDS = {2007860433}
CHANNEL_URL = "https://t.me/mrinxdildos"

# Initialize bot with token
BOT_TOKEN = read_token_from_file('token.txt')
bot = telebot.TeleBot(BOT_TOKEN)

# === NEW: Initialize Instagrapi client and login ===
INSTAGRAM_USERNAME = "mikimaos23"  # replace with your IG username
INSTAGRAM_PASSWORD = "passhihi38284"  # replace with your IG password
SESSION_FILE = "cookie.txt"   # You can use any filename, e.g., session.json

def login_with_session():
    cl = Client()
    session_loaded = False

    # Try to load session (cookies/settings) from file if it exists
    if os.path.exists(SESSION_FILE):
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            cl.get_timeline_feed()  # Check if session is valid
            session_loaded = True
            print("Logged in using saved session.")
        except LoginRequired:
            print("Session invalid or expired, logging in with username/password.")
        except Exception as e:
            print(f"Error loading session: {e}")

    # If session could not be loaded, do a fresh login and save new session
    if not session_loaded:
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        cl.dump_settings(SESSION_FILE)
        print("Logged in with credentials and saved new session.")

    return cl

cl = login_with_session()

# Delete existing webhook before polling
bot.remove_webhook()

def delete_after_delay(chat_id, message_id):
    time.sleep(9)
    bot.delete_message(chat_id, message_id)

def check_user_membership(message):
    try:
        user_status = bot.get_chat_member(REQUIRED_CHANNEL, message.from_user.id).status
        if user_status not in ["member", "administrator", "creator"]:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(
                telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL)
            )
            markup.add(
                telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦 | ➖]", url=BOT_LIST)
            )
            user_id = message.from_user.id
            try:
                photos = bot.get_user_profile_photos(user_id)
                has_photo = photos.total_count > 0
            except Exception:
                has_photo = False
            caption = f"🚨𝗛𝗜 👋 *{message.from_user.first_name}* \n\n‼ 𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗 ! \n\n🔒 *𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 !* 🔒"
            if has_photo:
                try:
                    photo_file_id = photos.photos[0][0].file_id
                    bot.send_photo(
                        message.chat.id, 
                        photo_file_id,
                        caption=caption,
                        parse_mode="Markdown",
                        reply_markup=markup
                    )
                except Exception:
                    bot.send_message(
                        message.chat.id,
                        caption,
                        parse_mode="Markdown",
                        reply_markup=markup
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    caption,
                    parse_mode="Markdown",
                    reply_markup=markup
                )
            return False
        return True
    except Exception as e:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(
            telebot.types.InlineKeyboardButton("[➖ 𝟭𝗦𝗧 𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ➖]", url=CHANNEL_URL)
        )
        bot.send_message(
            message.chat.id,
            f"Error checking membership: {str(e)}",
            reply_markup=markup
        )
        return False

# === START COMMAND ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not check_user_membership(message):
        return

    user_id = message.from_user.id

    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="[➖ 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗢𝗪𝗡𝗘𝗥 ➖]", url=OWNER_URL)
    button2 = telebot.types.InlineKeyboardButton(text="[➖ 𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ➖]", url=CHANNEL_URL)
    button3 = telebot.types.InlineKeyboardButton(text="[➖ | 𝗠 𝘅 𝗗™ 𝗔𝗟𝗟 𝗕𝗢𝗧𝗦 | ➖]", url=BOT_LIST)
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    welcome_text = (
        "𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗥𝗶𝗡 𝘅 𝗗𝗶𝗟𝗗𝗢𝗦™ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗩𝗜𝗗𝗘𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧\n\n"
        "📎 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀 !\n\n"
    )

    try:
        photos = bot.get_user_profile_photos(user_id)
        has_photo = photos.total_count > 0
    except Exception:
        has_photo = False

    if has_photo:
        try:
            photo_file_id = photos.photos[0][0].file_id
            bot.send_photo(
                message.chat.id, photo_file_id,
                caption=welcome_text,
                parse_mode="Markdown",
                reply_markup=markup
            )
        except Exception:
            bot.send_message(
                message.chat.id, welcome_text,
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=markup
            )
    else:
        bot.send_message(
            message.chat.id, welcome_text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=markup
        )

    # Notify owner(s) about new user
    user_name = (message.from_user.username and f"@{message.from_user.username}") or message.from_user.first_name or str(message.from_user.id)
    notify_text = f"👤 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗛𝗔𝗦 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗢𝗨𝗥 𝗕𝗢𝗧\n\n 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: {user_name}\n 𝗨𝗦𝗘𝗥 𝗜𝗗: {message.from_user.id}"

    for owner_id in OWNER_IDS:
        if owner_id != message.from_user.id:  # Don't notify if owner starts the bot
            try:
                bot.send_message(owner_id, notify_text)
            except Exception as e:
                print(f"Failed to notify owner {owner_id}: {e}")


# Regular expression to check if the message is a valid Instagram URL
def is_instagram_url(url):
    instagram_url_pattern = r"^(https?://)?(www\.)?instagram\.com/.*$"
    return re.match(instagram_url_pattern, url) is not None

def extract_shortcode_from_url(url):
    pattern = r'instagram\.com\/(?:p|reel)\/([A-Za-z0-9_-]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# === REPLACE THIS FUNCTION ===
def get_caption_with_instagrapi(shortcode_or_url):
    try:
        # Accept either shortcode or full URL
        if '/' in shortcode_or_url:
            media_pk = cl.media_pk_from_url(shortcode_or_url)
        else:
            media_pk = cl.media_pk_from_code(shortcode_or_url)
        media = cl.media_info(media_pk)
        return media.caption_text
    except Exception as e:
        print(f"Error fetching caption via instagrapi: {str(e)}")
        return None

def safe_caption(caption, max_words=950, max_chars=1024, branding=""):
    if not caption:
        caption = ""
    words = caption.split()
    trimmed_caption = " ".join(words[:max_words])
    space_for_caption = max_chars - len(branding)
    if len(trimmed_caption) > space_for_caption:
        trimmed_caption = trimmed_caption[:space_for_caption - 1] + "…"
    return trimmed_caption + branding

@bot.message_handler(func=lambda message: re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def download_reel_with_caption(message):
    # Check membership
    if not check_user_membership(message):
        return

    url = message.text

    # 1. Send the processing message instantly
    processing_msg = bot.reply_to(message, "⏳ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗹𝗶𝗻𝗸......")

    try:
        # Extract shortcode for instagrapi
        shortcode = extract_shortcode_from_url(url)

        # API call to fetch video URL
        api_url = f"https://instadownload.ytansh038.workers.dev/?url={url}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            if 'result' in data and 'url' in data['result']:
                video_url = data['result']['url']

                try:
                    bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
                except Exception:
                    pass

                progress_msg = bot.reply_to(message, "➖ 𝗩𝗶𝗱𝗲𝗼 𝗙𝗼𝘂𝗻𝗱 ! 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ⤵️")
                threading.Thread(target=delete_after_delay, args=(progress_msg.chat.id, progress_msg.message_id)).start()

                # === Fetch caption using instagrapi ===
                original_caption = get_caption_with_instagrapi(url if shortcode is None else shortcode) or "No caption available."
                branding = "\n\n🎥 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗥𝗲𝗲𝗹 👀 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 @instra_dwn_bymrin_bot ❤️\n\n"
                combined_caption = safe_caption(original_caption, 950, 1024, branding)

                bot.send_video(message.chat.id, video_url, caption=combined_caption)
                bot.send_message(
                    message.chat.id,
                    "𝗜 𝗮𝗺 𝗿𝗲𝗮𝗱𝘆 𝗳𝗼𝗿 𝘆𝗼𝘂 𝗻𝗲𝘅𝘁 𝘃𝗶𝗱𝗲𝗼.... 𝗞𝗶𝗻𝗱𝗹𝘆 𝘀𝗲𝗻𝗱 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 / 𝗥𝗲𝗲𝗹 𝗹𝗶𝗻𝗸, 𝗜 𝘄𝗶𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 👀 \n\n[ 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 > ー @M_o_Y_zZz ]"
                )
            else:
                bot.reply_to(message, "‼️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗲𝗰𝗸 𝘁𝗵𝗲 𝗟𝗜𝗡𝗞‼️")
        else:
            bot.reply_to(message, "‼️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗳𝗲𝘁𝗰𝗵 𝘃𝗶𝗱𝗲𝗼. 𝗨𝗻𝗮𝗯𝗹𝗲 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘁𝗼 𝗻𝗲𝘁𝘄𝗼𝗿𝗸 𝗢𝗿 𝗔𝗣𝗜 𝗺𝗶𝘀𝗺𝗮𝘁𝗰𝗵‼️")
    except requests.RequestException as e:
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝘁𝗼 𝗦𝗲𝗿𝘃𝗲𝗿 ⚠️ : {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"⚠️ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁 ⚠️ : {str(e)}")

@bot.message_handler(func=lambda message: not re.match(r"^(https?://)?(www\.)?instagram\.com/.*$", message.text))
def ignore_message(message):
    pass

bot.polling()