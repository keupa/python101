# python101

Proyecto de ejemplo para el programa rockstar

### Requisitos 
- Python 3
- Docker 

### Instrucciones
- Clonar este repo
- Crear imagen de docker
```
docker build -t "python101" .
```
- Correr imagen de docker en modo developer (salir con [CTRL] + [C])

```
 docker run -it -p 5000:5000 --rm --name python101-container python101
```

- Correr imagen en modo servicio

```
 docker run -p 5000:5000 --rm --name python101-serv python101
```
