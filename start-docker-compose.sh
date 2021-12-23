#!/usr/bin/env bash
cd containerisation/
docker-compose --env-file .env up --build

close-docker() {
    docker-compose down
}

trap close-docker EXIT INT SIGTERM ERR