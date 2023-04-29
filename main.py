from dotenv import load_dotenv
import telegram
import openai
load_dotenv()
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

telegram_Key = os.getenv("BOT_TOKEN")
openai_key = os.getenv("OPENAI_KEY")

bot = telegram.Bot(token=os.environ['BOT_TOKEN'])

# Set up OpenAI API credentials
openai.api_key = os.environ['OPENAI_KEY']

# Define the function to handle user messages
def handle_message(update, context):
    message = "Act Like a Human Interacting with other human .Reply accroding as per user input .Here is user Input->".join(update.message.text)

    # Use GPT to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=1,
    )

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)
    # Send the response back to the user

# Set up the handler for user messages
updater = telegram.ext.Updater(token=telegram_Key, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()