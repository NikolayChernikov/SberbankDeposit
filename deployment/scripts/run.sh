#!/usr/bin/env bash

source deployment/scripts/.env

docker run --name "${DOCKER_CONTAINER_NAME}" -p 8000:8000 "${DOCKER_IMAGE}"