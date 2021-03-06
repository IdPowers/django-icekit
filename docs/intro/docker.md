# Why use Docker?

Docker has many advantages over a simple Python virtualenv environment:

  * Eliminates the "works on my machine" problem by exactly reproducing an
    identical runtime environment everywhere.

  * Eliminates the need to install and run service dependencies directly on
    your OS, such as Elastic Search, PostgreSQL, Redis, etc.

  * Eliminates the need to install library dependencies directly on your OS,
    such as libjpeg, libtiff, etc.

  * Easy continuous deployment and rolling deployments on Docker Cloud via auto
    redeploy when a new image is built.

  * Much less (if any) downtime during deployments, because Node modules,
    Bower components and Python packages are already installed in the image.

# Getting started

If you haven't already, install Docker:

  * [OS X](https://download.docker.com/mac/stable/Docker.dmg)
  * [Linux](https://docs.docker.com/engine/installation/linux/)
  * [Windows](https://download.docker.com/win/stable/InstallDocker.msi)

The typical Docker workflow is:

  * Define the image build instructions for each service with a `Dockerfile`.

  * Configure and manage a collection of services with a `docker-compose.yml`
    file.

  * During local development, mount your source directory into containers for
    rapid iteration without having to rebuild images.

# Useful commands

Here are some of the most commonly used Docker commands when getting started:

    # Rebuild images for all services in your compose file
    $ docker-compose build --pull

    # Start all services in your compose file
    $ docker-compose up

    # Stop all services in your compose file
    $ docker-compose stop

    # List all containers for services in your compose file
    $ docker-compose ps

    # Open a new shell (`entrypoint.sh`) inside an already running container
    # for the `django` service
    $ docker-compose exec django entrypoint.sh

    # Remove all exited containers and their volumes
    docker rm -v $(docker ps -a -f status=exited -q)

    # Remove all dangling images (not tagged or used by any container)
    docker rmi $(docker images -f dangling=true -q)

    # Remove all dangling volumes (not used by any container)
    docker volume rm $(docker volume list -f dangling=true -q)

    # Remove ALL containers, images and volumes, to start from scratch
    docker rm -f $(docker ps -a -q)
    docker rmi $(docker images -q)
    docker volume rm $(docker volume ls -q)
