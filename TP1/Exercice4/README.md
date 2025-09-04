# 1

docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
b1badc6e5066: Pull complete
a2da0c0f2353: Pull complete
e5d9bb0b85cc: Pull complete
14a859b5ba24: Pull complete
716cdf61af59: Pull complete
14e422fd20a0: Pull complete
c3741b707ce6: Pull complete
Digest: sha256:33e0bbc7ca9ecf108140af6288c7c9d1ecc77548cbfd3952fd8466a75edefe57
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

# 2
docker run -d -p 8080:80 --name mon_nginx nginx
452f976bef838b663bd6cdca7d056883138c8a83cd38964a570ca96dc8546e66

# 3
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
452f976bef83   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   mon_nginx

# 4
[a](./nginx.png)

# 5
docker stop mon_nginx
mon_nginx

# 6
docker rm mon_nginx
mon_nginx