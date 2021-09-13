import sys
sys.path.insert(1, './data')
from src.database import Database, Note
from src.utils import load_template
import urllib

def index(request):
    db = Database('database')
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[chave] = urllib.parse.unquote_plus(valor, encoding='utf-8', errors='replace')
        
        if params['method'] == 'POST':
            db.add(Note(title=params['title'], content=params['content']))
        elif params['method'] == 'DELETE':
            db.delete(note_id=params['id'])
        elif params['method'] == 'UPDATE':
            db.update(Note(id=params['id'], title=params['title'], content=params['content']))

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, content=dados.content, id=dados.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    response = load_template('index.html').format(notes=notes)

    return response
