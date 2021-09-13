import json

def extract_route(request):
    print('\n---- Request:')
    print(request)
    request_components = request.split("\n")
    get = request_components[0]
    get_components = get.split(" ")
    route_components = get_components[1].split("/")
    route = ""

    print('ROUTE COMPONENTS')
    print(route_components)

    if len(route_components) != 0:
        for i in range(len(route_components)):
            if i <= 1:
                route = route_components[i]
            else:
                route = route + '/' + route_components[i]
    print('\n---- Rota criada foi:')
    print(route)
    return route   

def read_file(path):
    path_string = str(path)
    path_components = path_string.split('.')
    if path_components[1] in ['txt','css','html','js']:
        read = open(path, mode='rb').read()
    else:
        read = open(path, mode='rb').read()
    return read

def load_data(file):
    with open('data/'+file) as json_file:
        python_object = json.load(json_file)
        print(python_object)
    return python_object

def load_template(file):
    with open('templates/'+file) as html_file:
        html_str = html_file.read()
    return html_str

def add_to_notes(params):
    with open('data/notes.json', 'r') as json_file:
        data = json.load(json_file)
    data.append(params)
    with open('data/notes.json', 'w') as json_file:
        json.dump(data, json_file)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '' and body == '':
        response = 'HTTP/1.1 {} {}\n\n'.format(code, reason)
    elif headers == '':
        response = 'HTTP/1.1 {} {}\n\n{}'.format(code, reason, body)
    elif body == '':
        response = 'HTTP/1.1 {} {}\n{}\n\n'.format(code, reason, headers)
    else:
        response = 'HTTP/1.1 {} {}\n{}\n\n{}'.format(code,reason,headers,body)
        
    
    return response.encode()
