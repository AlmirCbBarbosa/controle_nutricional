# Fastapi - Controle Nutricional

## Andamento
1. Ambiente virtual criado;
1. Instalado as dependências e desativado o seu rastreamento;
1. Criado o arquivo main.py e a variável app;
1.criado os arquivos de rotas:
    1. pessoa.py;
    1. peso.py;
    1. dieta.py
  
    Criado as rotas raizes dos respectivos documentos.
1. models e o banco de dados criados.
1. criando rotas para cadastrar informações no banco de dados
    1. rota para criar pessoa;
    1. criando a criptografia no arquivo main.

## Erros
1. Ao criar o algoritmo de criptografia, foi encontrado incompatibilidade com o modulo bcrypt >4.x (estava instalado a versão
5.0). Para corrigir este erro instala a versão 4.0.1, com o seguinte comando:
```bash
    pip install brcrypt==4.0.1
```
