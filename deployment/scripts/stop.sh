#!/usr/bin/env bash

source deployment/scripts/.env

docker stop "${DOCKER_CONTAINER_NAME}"