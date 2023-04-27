# **Description**

### This application was created to calculate deposit.
### API path "/deposit/calculation"

# **Work with docker**

## **To build docker image:**

    ./deployment/scripts/build.sh

## **To run docker container:**

    ./deployment/scripts/run.sh

## **To stop docker container:**

    ./deployment/scripts/stop.sh

## **To start stopped docker container:**

    ./deployment/scripts/start.sh

## **To delete docker container and image:**

    ./deployment/scripts/delete.sh

# **Technology stack**
* FastAPI - for building API
* Uvicorn - ASGI
* Pydantic - for validate input data
* Pytest - for test api