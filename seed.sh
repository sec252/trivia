#!/bin/sh
echo "Seeding Database"
docker exec trivia_api python server.py seed_db
echo "Seeding Finished"