
# <p align="center">Cobalt e-commerce PWA - Back-end</p>
  
## Start the app:

- [Front-end in React](https://github.com/Alexis-Gontier/Cobalt-frontend)
- Back-end in Flask
- BDD MongoDB
- Swagger UI


Clone the project:

```bash
git clone https://github.com/Jeck0v/Cobalt-backend.git
```
Stating app with:

```bash
docker compose up --build
```
For Swagger: <br>
http://localhost:5000/swagger/

For Mongo-Express: <br>
http://localhost:8081/

The db is only initialized in the `express-mongo` when the request is received, so when a user creates an account,  the request creates the db with the user collection.


## How to fix the known error:

If you have mongo `dependency failed to start: container mongo is unhealthy` or any error from `storage`: <br>
Please make this: <br>
 ```bash
docker compose down -v 
```
```bash
rm -rf storage/
```
```bash
docker compose up --build
```
## 🙇 Authors:
- [Arnaud Fischer](https://github.com/Jeck0v)
- [Hugo Martins](https://github.com/AkaTFL)
- [Louis Dondey](https://github.com/Kae134)


