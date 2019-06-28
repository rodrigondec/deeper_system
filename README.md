# Deeper System Pyramid Project
Project made with Pyramid + Mongodb for Deeper System interview

## Install
### Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

#### Setting up
- copy the file `.env.example` with the name `.env`
- run the comand `make build` on the project folder
- run the comand `make install` for the *egg* creation

### Mongo
Install [mongodb-org-shell](https://docs.mongodb.com/manual/administration/install-on-linux/) from the documentation

#### Setting up
- connect to mongo container using `mongo -u mongo -p mongo`
- run `use mongo`
- run `db.createUser({user: "mongo", pwd: "mongo", roles: ["readWrite"]})`

## Running Project
Simply run the comand `make up` and _*voilà*_