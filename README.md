# Trybe Bank
Este é um projeto Web Banking que eu criei como parte de uma etapa do processo seletivo da Trybe.

Link do repositório: https://github.com/renanleitev/bank-system

## Features
<li> É possível criar uma nova conta e obter um número único de conta ao fazer o sign-in.
<li> Os dados dos usuários são armazenados em um banco de dados (PostgreSQL). 
<li> É possível transferir dinheiro (fictício) de uma conta do banco para outra conta cadastrada.
<li> As transferências bancárias são disponiblizadas para o usuário, com conta de origem, conta de destino, valor e data da transferência.

<br/>

# Servidor local (com Docker)

1. Tenha o Docker instalado. Mais informações: https://docs.docker.com/desktop/install/windows-install/
2. Execute o seguinte comando (com o Docker rodando):
   ```
   docker pull renanleitev/bank:1.0
   ```
3. Link do DockerHub: https://hub.docker.com/r/renanleitev/bank
4. Acessar no navegador: http://127.0.0.1:8000
## Superusuário (admin)
Para acessar a página de Administrador (dentro do servidor local do Django que está rodando na sua máquina):

1. Insira na barra de endereços do navegador: http://127.0.0.1:8000/admin
2. Administrador: admin / Senha: admin
3. Para voltar para a página principal, digite http://127.0.0.1:8000

# Servidor local (sem Docker)

## Pré-requisitos
1. Um terminal ou CMD (prompt de comando).
2. PostgreSQL instalado. Mais informações: https://www.guru99.com/download-install-postgresql.html 
   1. Primeiro, é necessário criar o banco de dados do PostgreSQL:
      1. Nome da base de dados: 'postgres',
      2. Usuário (padrão do PostgreSQL): 'postgres',
      3. Senha: 'postgres',
      4. PORT (padrão): '5432'.
3. Python 3.4 ou acima instalado. Mais informações: https://www.digitalocean.com/community/tutorials/install-python-windows-10 
4. PIP instalado (python get-pip.py). Mais informações: https://phoenixnap.com/kb/install-pip-windows  
5. Abrir o terminal, e ativar o ambiente virtual do Python. Mais informações: https://docs.python.org/pt-br/3/library/venv.html
6. Instalar as bibliotecas requeridas.
   1. Acessar a pasta onde o projeto está:
        ```
        cd Bank_Management_System_Django
        ```
    1. E depois:
        ```
        pip install -r requirements.txt
        ```
7. Caso não consiga instalar com o comando acima, é possível instalar manualmente com os seguintes comandos (cada biblioteca deve ser instalada manualmente, uma por vez):
   1. Django==4.1.3
        ```
        pip install Django
        ```
   2. django-tables2==2.4.1
        ```
        pip install django-tables2
        ```
   3. psycopg2-binary==2.9.5
        ```
        pip install psycopg2-binary
        ```
8. Obs: asgiref and sqlparse estão inclusos quando o Django é instalado. Se eles não estiverem instalados, execute os comandos abaixo:
    1. asgiref==3.5.2
    ```
    pip install asgiref
    ```
    2. sqlparse==0.4.3
    ```
    pip install sqlparse
    ```
## Iniciando o servidor
1. Abra o terminal e entre na pasta principal do projeto.
    ```
    cd Bank_Management_System_Django
    ```
2. Inicie o servidor digitando o seguinte comando:
    ```
    python manage.py runserver
    ```
    Se isso não funcionar, tente substituir `python` por `python3` ou por `py -u`.

## Superusuário (admin)
Para acessar a página de Administrador (dentro do servidor local do Django que está rodando na sua máquina):

1. Abrir o terminal e entre na pasta principal do projeto.
    ```
    cd Bank_Management_System_Django
    ```
2. Digitar o seguinte comando:
    ```
    python -u manage.py createsuperuser
    ```
3. Cadastrar o nome do administrador e a senha.
4. Insira na barra de endereços do navegador: http://127.0.0.1:8000/admin
5. Digitar o nome do administrador e a senha escolhida no passo 3.

### Observação
Na tabela "Histórico de transações/transferência", às vezes é necessário clicar duas vezes no título da coluna para que a lista seja filtrada pela ordem desejada (crescente ou decrescente).

### Disclaimer
Este app representa um banco fictício. Todas as transações, números de contas e valores não são reais.
