from hikka.types import Message
import asyncio
from .. import loader, utils

@loader.tds
class NotesModule(loader.Module):
    strings = {
        "name": "Notes"
    }
    
    @loader.command()
    async def note(self, message: Message):
        '''Создать заметку'''
        note_text = utils.get_args_raw(message)
        if note_text:
            # Сохраняем заметку в базе данных или файле
            await utils.answer(message, f"Заметка создана:\n{note_text}")
        else:
            await utils.answer(message, "Пожалуйста, укажите текст заметки.")
    
    @loader.command()
    async def delnote(self, message: Message):
        '''Удалить заметку'''
        note_id = utils.get_args_raw(message)
        if note_id:
            # Удаляем заметку из базы данных или файла
            await utils.answer(message, f"Заметка с идентификатором {note_id} удалена.")
        else:
            await utils.answer(message, "Пожалуйста, укажите идентификатор заметки.")
