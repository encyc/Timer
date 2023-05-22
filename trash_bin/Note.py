import json

class NoteManager:
    def __init__(self):
        self.notes_file = 'note_file.json'
        self.notes = []
        self.load_notes()

    def load_notes(self):
        # 从文件或数据库中加载保存的笔记列表
        # 将加载的笔记存储在self.notes列表中
        try:
            with open(self.notes_file, 'r') as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            # 如果文件不存在，则不做任何操作
            pass

    def save_notes(self):
        # 将当前的笔记列表self.notes保存到文件或数据库中
        # 示例代码，这里不执行实际的保存操作
        with open(self.notes_file, 'w') as f:
            json.dump(self.notes, f, default=lambda x: x.__dict__)

    def add_note(self, title, content):
        # 创建一个新的笔记，并添加到self.notes列表中
        # 参数title为笔记标题，参数content为笔记内容
        note = {'title': title, 'content': content}
        self.notes.append(note)
        self.save_notes()  # 保存笔记列表

    def edit_note(self, index, title, content):
        # 编辑指定索引的笔记
        # 参数index为要编辑的笔记在self.notes列表中的索引
        # 参数title为笔记标题，参数content为笔记内容
        if index < len(self.notes):
            self.notes[index]['title'] = title
            self.notes[index]['content'] = content
            self.save_notes()  # 保存笔记列表

    def delete_note(self, index):
        # 删除指定索引的笔记
        # 参数index为要删除的笔记在self.notes列表中的索引
        if index < len(self.notes):
            del self.notes[index]
            self.save_notes()  # 保存笔记列表
