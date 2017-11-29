Title: [Shaarli] Pacman - Empêcher l'installation de locales
Date: 2016-11-14 05:39
Author: HS-157
Category: Informatique
Tags: Shaarli, Gnu/Linux, Archlinux, Pacman, Libre

# [Pacman - Empêcher l'installation de locales](https://wiki.archlinux.fr/Pacman#Emp.C3.AAcher_l.27installation_de_locales)

Ce que je trouve bien sur le canal #archlinux-fr, c’est quand un sujet est intéressant ; tout le monde s’y met et voilà le résultat : Comment gagner un peu de place quand son système est installé sur la fameuse carte SD de 2Go !

Grâce à l’option ```NoExtract``` de Pacman, on peut lui dire de ne pas extraire certains fichiers des paquets, comme des trucs pas forcément utiles, c’est le cas les locales qu’on n’utilise pas et qui prennent quand même un peu de place. Exemple du avant/après sur mes systèmes :

Sur ma Banana :

- Avant :
~~~bash
╭─hs-157@moeKyun  ~  
╰─$ du -hs /usr/share/locale/
93M     /usr/share/locale/
~~~

- Après :
~~~
╭─hs-157@moeKyun  ~  
╰─$ du -hs /usr/share/locale/                                                                           
4,9M    /usr/share/locale/
~~~


Sur mon ordinateur portable :

- Avant :
~~~
╭─hs-157@V17  ~  
╰─$ du -hs /usr/share/locale/
291M	/usr/share/locale/
~~~

- Après :
~~~
╭─hs-157@V17  ~  
╰─$ du -hs /usr/share/locale/
8,8M	/usr/share/locale/
~~~

Donc ce qui en ressort de tout ça, c’est de trouver les bons arguments pour ```NoExtract``` et la commande pour virer les locales non-utilisées.
