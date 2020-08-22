# Overview

This is a proof of concept (POC) using [Locust](https://locust.io)!

# What is Locust?

Locust is an open-source load testing tool. 

Define user behavior with Python code, and swarm your system with millions of **simultaneous users**.

# Setup

1º Install [Docker](https://docs.docker.com/get-docker/)

2º Install [Docker Compose](https://docs.docker.com/compose/install/)

# Testing

To test the Locust, we are going to use `docker-compose` to start, setup, and stop our environment that is composed of:

- 1 Application
- 1 Locust Master
- 3 Locust Workers

```yaml
version: '3'

services:

  application:
    image: chentex/go-rest-api
    # Omitted lines

  master:
    image: locustio/locust
    # Omitted lines

  worker:
    image: locustio/locust
    # Omitted lines
```

It is not necessary to know about `docker-compose`, because, we already have a set of scripts to do it for us.

- **start.sh:** Start the environment (locust master, worker, and application)
- **stop.sh:** Stop the environment (locust master, worker, and application)

Let us a test?

We need to start the environment to do that, run the above script:

`sh start.sh`

After starting the environment, open the Locust address `http://localhost:8089` and set the information:

- **Number of total users to simulate:** 500
- **Hatch rate:** 10
- **Host:** http://127.0.0.1:8080

Click at `Start swarming` button and go to the `Charts` tab!

![alt text](/images/locust-performance-test.png "Locust Chart Tab")

To stop the test and environment, run the above script:

`sh stop.sh`

# Be Happy!