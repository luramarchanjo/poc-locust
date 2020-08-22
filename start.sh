#!/bin/bash
sh stop.sh
docker-compose up -d --scale worker=3