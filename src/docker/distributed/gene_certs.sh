#!/bin/bash

export SUPERLINK_IP=172.27.46.12

docker compose -f certs.yml -f ../complete/certs.yml run --rm --build gen-certs