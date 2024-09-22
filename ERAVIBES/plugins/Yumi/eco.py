from pyrogram import Client, filters
from ERAVIBES.misc import SUDOERS
from ERAVIBES import app 

# /eco command handler
@app.on_message(
    filters.command(["eco", "co"], prefixes=["/", "!", "%", ",", "-", ".", "@", "#", "e", "E"]) 
    & filters.reply 
    & SUDOERS 
    & filters.group
)
async def eco_reply(client, message):
    if not message.reply_to_message:
        await message.reply("Please reply to a user's message to use this command.")
        return
    
    # Split the command from the message (removing the command /eco)
    command_text = message.text.split(" ", 1)
    
    if len(command_text) < 2:
        await message.reply("Please provide a message after the /eco command.")
        return
    
    # The message to reply with
    reply_message = command_text[1]
    
    # Delete the original command message
    await message.delete()
    
    # Reply to the target message
    await message.reply_to_message.reply(reply_message)