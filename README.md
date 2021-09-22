# Kompose

### Adicione aqui os erros e correções aplicadas

lib dj_database_url

---

**Erro:** Problema ao conectar o postgres no heroku
**O que ele causa:** Impossibilita o deploy no heroku
**Como corrigir:** Acrescentar o seguinte código nas settings do django

**Código corrigido:**

```sh
import dj_database_url

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    db_from_env = dj_database_url.config(
        default=DATABASE_URL, conn_max_age=500, ssl_require=True)
    DATABASES['default'].update(db_from_env)
```

**Erro:** Ausência do arquivo heroku.yml
**O que ele causa:** Impossibilita o deploy no heroku
**Como corrigir:** Criar o arquivo heroku.yml e acrescentar o seguinte

**Código corrigido:**

```sh
build:
  docker:
    web: Dockerfile
run:
  web: python manage.py runserver 0.0.0.0:$PORT
```

**Erro:** Ausência de build, volumes e porta errada
**O que ele causa:** Múltiplos erros
**Como corrigir:** Acrescentar o código no serviço web

**Código corrigido:**

```sh
  web:
    build: .
    env_file: envs/dev.env

    volumes:
      - .:/code

    ports:
      - 8000:8000

```

**Erro:** Ordem de execução errada no DockerFile
**O que ele causa:** Erro Instalação de dependências
**Como corrigir:** Mudar a ordem

**Código corrigido:**

```sh
FROM python:3.9.4

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
```

**Erro:** Ausência de volumes no docker-compose.yml
**O que ele causa:** Não persistência de dados
**Como corrigir:** Adicionar o volumes

**Código corrigido:**

```sh
db:
    volumes:
        - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
    external: true
```

**Código com erro:**

```sh
return Response(serializer.data, status=status.HTTP_200_OK)
```

**Erro:** O post retorna "ok" ao invés de "created"
**O que ele causa:** Confusão na response
**Como corrigir:** Modificar o status para HTTP_201_CREATED
**Código corrigido:**

```sh
return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---
