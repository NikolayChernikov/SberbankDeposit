#!/usr/bin/env bash

source deployment/scripts/.env

docker rm -f  "${DOCKER_CONTAINER_NAME}"
docker rmi -f  "${DOCKER_IMAGE}"