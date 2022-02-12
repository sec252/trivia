# trivia

## Description 

Small trivia app

## How to run app development mode

Make sure you have docker and docker-compose installed

### Docker Installation instructions
 - [windows](https://docs.docker.com/desktop/windows/install/)

 - [linux](https://docs.docker.com/engine/install/ubuntu/)

 - [mac](https://docs.docker.com/desktop/mac/install/)

 ### Docker Compose installation instructions

  - On desktop systems like Docker Desktop for Mac and Windows, Docker Compose is included as part of those desktop installs.

  - [linux](https://docs.docker.com/compose/install/)

### Windows entry point

If you are using windows run:

`dos2unix api-db/entrypoint.sh`

this will make entrypoint.sh executable

### To start the app

`docker-compose up --build`

### Seed database

open up another terminal and run:
`docker-compose exec web python server.py seed_db`


