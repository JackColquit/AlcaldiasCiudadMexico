#!/bin/bash

#se debe de crear una base de datos llamada 'cdMexico'
#y correr el siguiente script
cat Dump20220429.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root cdMexico
