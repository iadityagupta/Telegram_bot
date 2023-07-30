#Importing basic libraries
from telegram.ext._updater import Updater
from telegram._update import Update
from telegram.ext._basehandler import BaseHandler
from telegram.ext._commandhandler import CommandHandler
from telegram.ext._messagehandler import MessageHandler
from telegram.ext.filters import UpdateFilter

telegram_token= "6428726769:AAGPc2SPsXQ5sI3a-7ayqgeomm2pLhSoFus"

updater = Updater('6428726769:AAGPc2SPsXQ5sI3a-7ayqgeomm2pLhSoFus', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text('Hello! Welcome to C-Cube bot. We are building a coding community for IET students!',"\n")    
    update.message.reply_text('We aim to enhance the coding culture of IET. This is a community to interact with each other and share valuable resources with the student of IET DAVV!',"\n", 'Using of foul language is strictly prohibited in the group.')    

    update.message.reply_text('Type /help for the content to display!')

  
def help(update, context):
      update.message .reply_text(
      """
      /start -> Welcome to the C-Cube BOT!
      /Send message~Group -> If you have valuable insights to share in the group, you can share in the group.
      /Send message~Admin -> If you wish to share something with the Admin.
      /Suggestions -> You can suggest changes to the admin through this.
      /Contribute -> If you wish to contribute to this community, you are more than welcome.
      /Stop -> If you wish to stop the bot.
      
      """)    
      
      dispatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('Send Message~Group', Message~Group))
updater.dispatcher.add_handler(CommandHandler('Send Message~Admin', Message~Admin))
updater.dispatcher.add_handler(CommandHandler('Suggestions',Suggestions))
updater.dispatcher.add_handler(CommandHandler('Contribute',Contribute))
updater.dispatcher.add_handler(CommandHandler('Stop',Stop))
updater.start_polling()  # Start the bot
updater.idle() # Wait for the script to be stopped; this will stop the bot

