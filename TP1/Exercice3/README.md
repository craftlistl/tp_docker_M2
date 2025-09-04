# tp_docker_M2

# 1
docker --version : Docker version 26.1.3, build 26.1.3-0ubuntu1~24.04.1

# 2
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
postgres     latest    f23dc7cd74bd   16 months ago   432MB

# 3 
Using default tag: latest
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
Digest: sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest

# 4 
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

# 5
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# 6
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS                      PORTS     NAMES
df280ad29f21   hello-world       "/hello"                 2 minutes ago   Exited (0) 2 minutes ago              nifty_diffie
984f5f41bb14   postgres:latest   "docker-entrypoint.s…"   14 months ago   Exited (0) 17 minutes ago             hopeful_rubin

# 7
docker rm df280ad29f21

# 8

docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    1b44b5a3e06a   3 weeks ago     10.1kB
postgres      latest    f23dc7cd74bd   16 months ago   432MB

docker rmi 1b44b5a3e06a
Untagged: hello-world:latest
Untagged: hello-world@sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567
Deleted: sha256:1b44b5a3e06a9aae883e7bf25e45c100be0bb81a0e01b32de604f3ac44711634
Deleted: sha256:53d204b3dc5ddbc129df4ce71996b8168711e211274c785de5e0d4eb68ec3851
