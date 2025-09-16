Le node modules est insérer dans le zip, dans le dockerfile il fait un copy du node module puis un npm install


Il y a 3 RUN dans le dockerfile on pourrais en faire 1 seul

Le user en root c'est dangereux

Les ports expose servent a quoi


La version de node doit etre fixe


On peu le faire tourner en production plutot qu'en developement pour optimiser le build


Dépendances inutiles dans de package.json



Il faut analyser cette ligne : RUN apt-get update && apt-get install -y build-essential ca-certificates locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
On devrait pouvoir enlever des choses inutiles