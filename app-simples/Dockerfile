FROM tiangolo/meinheld-gunicorn-flask:python3.7
# Imagem base do nosso container

COPY ./app /app
# Copia o nosso app para dentro do container

COPY requirements.txt /app
# Copia o arquivo requirements para dentro do container

RUN pip install -r requirements.txt
# Executa o arquivo requirements quando o container for criado, instalando nossos pacotes

# COMANDO PARA FAZER O BUILD
# docker build -t nome_da_imagem

# COMANDO PARA RODAR O CONTAINER
# docker run -d -p 80:80 --name nome_do_container nome_da_imagem_base
