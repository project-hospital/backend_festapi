```shell
docker run --name postgres-db-hostpital -e POSTGRES_DB=hospital -e POSTGRES_USER=admin_user -e POSTGRES_PASSWORD=qwert1234 -p 5432:5432 -d postgres:13
```

```shell
docker start postgres-db-hostpital
```

```shell
docker stop postgres-db-hostpital
```

