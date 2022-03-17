#!/bin/sh
echo "Seeding Database"
docker exec trivia_api_1 python server.py seed_db
echo "Seeding Finished"