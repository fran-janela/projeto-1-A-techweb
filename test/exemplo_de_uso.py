import sys
sys.path.insert(1, '/Users/fpj_mac/Documents/Insper/4ºSemestre/TechWeb/Projeto-01/src')

from database import Database, Note


db = Database('databaseTest')

db.add(Note(title="Pão doce", content="Abra o pão e coloque o seu suco em pó favorito."))
db.add(Note(title=None,content="Lembrar de tomar água"))

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')