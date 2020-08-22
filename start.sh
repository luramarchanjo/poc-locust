#!/bin/bash
sh stop.sh
docker-compose -f locust/docker-compose.yml up -d --scale worker=3