#!/usr/bin/env bash

source deployment/scripts/.env

docker run --name "${DOCKER_CONTAINER_NAME}" "${DOCKER_IMAGE}"