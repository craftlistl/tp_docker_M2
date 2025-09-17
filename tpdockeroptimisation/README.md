J'ai lancé le build : 
time docker build . -t "latestNode"

ce qui ma donné : 
real    0m50.393s
user    0m0.166s
sys     0m0.385s

taille image docker 1.2GB

Le node modules est insérer dans le zip, dans le dockerfile il fait un copy du node module puis un npm install

enlever le copy nodemodules :
build
real    0m50.782s
user    0m0.229s
sys     0m0.339s

taille image docker 1.19GB


Il y a 3 RUN dans le dockerfile on pourrais en faire 1 seul

faire une seule ligne run : 

real    0m51.446s
user    0m0.153s
sys     0m0.463s

taille image docker 1.19GB

Le user en root c'est dangereux:

ajout d'un user app

real    0m14.653s
user    0m0.260s
sys     0m0.353s

taille image docker 138.5MB

Les ports expose servent a quoi

j'ai enlever les ports sauf 3000:

real    0m54.861s
user    0m0.199s
sys     0m0.448s

taille image docker 1.19GB

La version de node doit etre fixe

node:18 

real    1m27.640s
user    0m0.168s
sys     0m0.432s
changement vers alpine : 

real    0m12.253s
user    0m0.183s
sys     0m0.338s

taille image docker 138.5MB

les commandes du run on pris du temps

taille image docker 1.17GB


On peu le faire tourner en production plutot qu'en developement pour optimiser le build

real    0m50.840s
user    0m0.152s
sys     0m0.417s

taille image docker 1.19GB

Dépendances inutiles dans de package.json

remove mongo db : 
real    0m20.372s
user    0m0.151s
sys     0m0.244s

taille image docker 130.27MB


Il faut analyser cette ligne : RUN apt-get update && apt-get install -y build-essential ca-certificates locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
On devrait pouvoir enlever des choses inutiles

Suppression de ce run:
real    0m21.489s
user    0m0.306s
sys     0m0.276s

taille image : 1.1GB



ajouter un dockerignore pour ne pas copier ce qui n'est pas utile

real    0m19.628s
user    0m0.106s
sys     0m0.461s

[+] Building 13.9s (9/9) FINISHED   

taille image : 130.12MB


Les modification ayant eu le plus grand impact : changer de version node pour un alpine pour reduire la taille de l'image

enlever la ligne de run  RUN apt-get update && apt-get install -y build-essential ca-certificates locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

pour build plus rapidement l'image

copier uniquement ce qui est necessaire dans l'image (pas besoin du dockerfile ou du readme par exemple) => build plus rapide et image plus legere