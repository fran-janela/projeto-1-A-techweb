import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database():
    def __init__(self, name):
        database = './data/' + name + '.db'
        self.conn = sqlite3.connect(database)
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')
    
    def add(self, note):
        query = """INSERT INTO note (title,content) VALUES (?,?);"""
        self.conn.execute(query,(note.title,note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        Notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id=id, title=title, content=content)
            Notes.append(note)
        return Notes

    def update(self, note):
        query = """UPDATE note SET title = ?, content = ? WHERE id = ?"""
        self.conn.execute(query,(note.title,note.content,note.id))
        self.conn.commit()

    def delete(self, note_id):
        query = """DELETE FROM note WHERE id = ?"""
        self.conn.execute(query,(note_id,))
        self.conn.commit()
