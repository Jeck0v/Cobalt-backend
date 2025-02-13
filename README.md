
# <p align="center">Cobalt e-commerce PWA - Back-end</p>
  

- Front-end en React
- Back-end en Flask
- BDD MongoDB
- Swagger pour les tests des routes


Clone le projet

```bash
git clone https://github.com/Jeck0v/Cobalt-backend.git
```
Lancer l'app avec le docker-compose.

```bash
docker compose up --build
```

Pour tester les routes vous pouvez aller sur : <br>
http://localhost:5000/swagger/

Pour voir Mongo-Express: <br>
http://localhost:8081/

The db is only initialized in the `express-mongo` when the request is received, so when a user creates an account,  the request creates the db with the user collection.


### Issues:

If you have mongo `dependency failed to start: container mongo is unhealthy`.
Please make this:
suppr the storage folder
 ```bash
docker compose up --build
```
 ```bash
docker compose down --v 
```
 ```bash
docker compose up --build
```
