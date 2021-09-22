# Kompose

### Adicione aqui os erros e correções aplicadas

Nào tinha psycopg2 instalado
post retornava ok
python 2.7 dockerfile

---

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
