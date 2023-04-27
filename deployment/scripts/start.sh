#!/usr/bin/env bash

source deployment/scripts/.env

docker start "${DOCKER_CONTAINER_NAME}"