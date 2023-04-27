#!/usr/bin/env bash

source deployment/scripts/.env

docker build -f "${DOCKER_DOCKERFILE}" -t "${DOCKER_IMAGE}" .