CONTATOS = {
  'gazela@gmail.com': {'nome': 'Gazela', 'TELEFONE': '9999-9999'},
  'poney@gmail.com': {'nome': 'Poney', 'TELEFONE': '8888-8888'},
  'urubu@gmail.com': {'nome': 'Urubu', 'TELEFONE': '7777-7777'},
  'peixoto@gmail.com': {'nome': 'Peixoto', 'TELEFONE': '6666-6666'},
  'boizao@gmail.com': {'nome': 'Boizão', 'TELEFONE': '5555-5555', 'EXTRA': {'a': 1, 'b': 2}}
}

TELEFONE = CONTATOS['gazela@gmail.com']['TELEFONE']
print(TELEFONE) # 9999-9999

EXTRA = CONTATOS['boizao@gmail.com']['EXTRA']['b']
print(EXTRA) # 2
