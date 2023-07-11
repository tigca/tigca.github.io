import logging

from telethon import events, sync
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

notes = {}

# Function to add a new note
async def add_note_cmd(message: Message):
    syntax_error = False
    try:
        folder, note = message.text.split(' ',1)[1].split(' ',1)
    except ValueError:
        syntax_error = True
    if syntax_error or not folder or not note:
        await message.respond('Invalid syntax, please use `.note <folder> <note>`')
        return
    if folder not in notes:
        notes[folder] = []
    notes[folder].append(note)
    await message.respond(f'Added note "{note}" to {folder}')

# Function to fetch notes
async def fetch_notes_cmd(message: Message):
    if not notes:
        await message.respond('No notes found')
        return
    notes_list = ''
    for folder, notes_in_folder in notes.items():
        notes_list += f'<b>{folder.capitalize()}:</b>\n'
        for note in notes_in_folder:
            notes_list += f'- {note}\n'
    await message.respond(notes_list)

# Function to delete a note
async def delete_note_cmd(message: Message):
    syntax_error = False
    try:
        folder, note = message.text.split(' ',1)[1].split(' ',1)
    except ValueError:
        syntax_error = True
    if syntax_error or not folder or not note:
        await message.respond('Invalid syntax, please use `.delnote <folder> <note>`')
        return
    if folder not in notes or note not in notes[folder]:
        await message.respond(f'Note "{note}" not found in {folder}')
        return
    notes[folder].remove(note)
    await message.respond(f'Deleted note "{note}" from {folder}')

# Create the event handler for new messages
@events.register(events.NewMessage(pattern=r'\.note'))
async def add_note_handler(event):
    await add_note_cmd(event.message)

# Create the event handler for new messages
@events.register(events.NewMessage(pattern=r'\.notes'))
async def fetch_notes_handler(event):
    await fetch_notes_cmd(event.message)

# Create the event handler for new messages
@events.register(events.NewMessage(pattern=r'\.delnote'))
async def delete_note_handler(event):
   
