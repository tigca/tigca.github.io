from hikka.types import Message
from .. import loader, utils

@loader.tds
class NotesModule(loader.Module):
    strings = {
        "name": "Notes"
    }
    
    def __init__(self):
        self.notes = {}
    
    async def client_ready(self, client, db):
        self.client = client
    
    async def save_notes(self):
        await self.client.save_module_value(self.__name__, self.notes)
    
    async def load_notes(self):
        self.notes = await self.client.get_module_value(self.__name__, {})
    
    async def on_module_load(self):
        await self.load_notes()
    
    async def on_module_unload(self):
        await self.save_notes()
    
    @loader.command()
    async def note(self, message: Message):
        '''Сохранить заметку'''
        note_text = utils.get_args_raw(message)
        if note_text:
            note_id = len(self.notes) + 1
            self.notes[note_id] = note_text
            await utils.answer(message, f"Заметка сохранена с идентификатором {note_id}.")
            await self.save_notes()
        else:
            await utils.answer(message, "Пожалуйста, укажите текст заметки.")
    
    @loader.command()
    async def notes(self, message: Message):
        '''Посмотреть заметки'''
        if self.notes:
            notes_list = "\n".join([f"{note_id}: {note_text}" for note_id, note_text in self.notes.items()])
            await utils.answer(message, f"Список заметок:\n{notes_list}")
        else:
            await utils.answer(message, "Нет сохраненных заметок.")
    
    @loader.command()
    async def delnote(self, message: Message):
        '''Удалить заметку'''
        note_id = utils.get_args_raw(message)
        if note_id:
            try:
                note_id = int(note_id)
                if note_id in self.notes:
                    del self.notes[note_id]
                    await utils.answer(message, f"Заметка с идентификатором {note_id} удалена.")
                    await self.save_notes()
                else:
                    await utils.answer(message, f"Заметки с идентификатором {note_id} не существует.")
            except ValueError:
                await utils.answer(message, "Неверный формат идентификатора заметки.")
        else:
            await utils.answer(message, "Пожалуйста, укажите идентификатор заметки.")
