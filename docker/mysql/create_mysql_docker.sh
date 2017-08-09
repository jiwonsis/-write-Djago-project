#!/usr/bin/env bash

MYSQL_USER="mysql_user"
MYSQL_DATABASE="test_db"
MYSQL_CONTAINER_NAME="mysql"
MYSQL_ROOT_PASSWORD="1q2w3e4r"
MYSQL_PASSWORD="1q2w3e4r"


docker \
  run \
  --detach \
  --env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
  --env MYSQL_USER=${MYSQL_USER} \
  --env MYSQL_PASSWORD=${MYSQL_PASSWORD} \
  --env MYSQL_DATABASE=${MYSQL_DATABASE} \
  --name ${MYSQL_CONTAINER_NAME} \
  --publish 3306:3306 \
  mysqldev:1;
