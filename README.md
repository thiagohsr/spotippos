[![CircleCI](https://circleci.com/gh/thiagohsr/spotippos/tree/master.svg?style=svg)](https://circleci.com/gh/thiagohsr/spotippos/tree/master)
# Code Challenge Grupo Zap (back-end)

API desenvolvida para corresponder as solicitações do [desafio back-end](https://github.com/grupozap/code-challenge/blob/master/backend.md#desafio).

## Dependências

- Python 3 [Linux](https://realpython.com/installing-python/#linux) / [osx](https://realpython.com/installing-python/#macos-mac-os-x)
- Nodejs [NVM](https://github.com/creationix/nvm#installation)

## Como executar a API

### Configurações

1. Clone o repositório com `git clone https://github.com/thiagohsr/spotippos.git`.
2. Instale as dependências acessando o diretório do repositório clonado, e execute `make setup`.
3. Disponibilize a API e o serviço de persistência dos dados com `make run`.

### Testes

- Na raiz do diretório clonado, `make test`.

## Extras:

- [Arquivo](https://github.com/thiagohsr/spotippos/blob/master/Spotippos.postman_collection.json) com as requisições básicas da API, para serem utilizadas com o [postman](https://www.getpostman.com/apps).

- Caso prefira o modo roots:

  1. Crie imóveis em Spotippos :)

  ````javascript
  curl -X POST http://localhost:5000/api/v1/properties/ -H 'content-type: application/json'
   -d '{"title": "Imóvel código 39, com 5 quartos e 4 banheiros.", "price": 1193000, "description": "Est ullamco officia sit in culpa sint mollit deserunt culpa. Consequat nostrud et deserunt sunt elit anim ullamco aliquip nulla velit ut ipsum id Lorem.", "y": 685, "x": 164, "beds": 5, "baths": 4, "squareMeters": 118}'
  ````

  2. Mostre um imóvel específico em Spotippos =]

  ```javascript
  curl -X GET http://localhost:5000/api/v1/properties/1
  ```

  3. Busque imóveis em Spotippos :D

  ```javascript
  curl -X GET 'http://localhost:5000/api/v1/properties/?ax=20&ay=500&bx=600&by=700' -v
  ```
