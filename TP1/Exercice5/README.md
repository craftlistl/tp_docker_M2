
creer le dockerfile

le app.py

refaire le app.py avec un template de hello world avec le bon host : app.run(host='0.0.0.0', port=5000)

build
docker build --tag 'app_python' ./
[+] Building 1.1s (9/9) FINISHED                                                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                  0.0s
 => => transferring dockerfile: 167B                                                                                  0.0s 
 => [internal] load metadata for docker.io/library/python:latest                                                      0.9s 
 => [internal] load .dockerignore                                                                                     0.0s
 => => transferring context: 2B                                                                                       0.0s 
 => [1/4] FROM docker.io/library/python:latest@sha256:18634e45b29c0dd1a9a3a3d0781f9f8a221fe32ee7a853db01e9120c710ef5  0.0s 
 => [internal] load build context                                                                                     0.0s 
 => => transferring context: 28B                                                                                      0.0s 
 => CACHED [2/4] WORKDIR /app                                                                                         0.0s 
 => CACHED [3/4] RUN pip install Flask                                                                                0.0s 
 => CACHED [4/4] COPY app.py /app/app.py                                                                              0.0s 
 => exporting to image                                                                                                0.0s 
 => => exporting layers                                                                                               0.0s 
 => => writing image sha256:34e3dda1768025eb0aa026376ac74f9ef92f5b057692d359cc07611993f97bb2                          0.0s 
 => => naming to docker.io/library/app_python 

run

docker run -d -p 8080:5000 --name mon_app_python app_python
29152d4aad6d632b218941a786df493b4baa8231ee9df43b1b1926962009ced9

[a](./hello.png)