Title: Faisons de l'internet, Transmission-nous
Date: 2015-10-04 03:05
Category: Informatique
Tags: Libre, Archlinux, Gnu/Linux, Transmission

Faisons de l’internet et non du Minitel 2.0, car aujourd'hui c'est [Transmission](http://www.transmissionbt.com/), c'est un nœud BitTorrent Libre ! (Def de [Wikipédia](https://fr.wikipedia.org/wiki/Transmission_%28logiciel%29)) Oui le Libre c'est bien ! ! !  
Donc ça permet de faire du torrent en Libre ! Et partager tout plein de fichier Libre de droit !

Donc pour l’installer, c'est comme d’habitude : vous sortez votre gestionnaire de paquet préféré, ouais, mais c'est pas en installant le premier Transmission qui passe que ça va marcher.  
Il existe plusieurs versions de Transmission, le démon, le contrôle à distance en ncurses, la version GTK et QT, qui eux marche en autonome, mais qui ont normalement le contrôle à distance pour le démon.  
Donc, je vais parler aujourd’hui du démon et du contrôle à distance en ncurses, donc pour installer le démon, le paquet ça doit être transmission-cli ou quelque chose comme ça, et oui, on peut communiquer avec le démon en ligne de commande, pour plus d'infos, regarde ton putain de manuel !, 
et pour le contrôle à distance, c'est transmission-remote-cli, ou une connerie de ce genre, et oui c'est en ncurses, pour ce qui sont sous Archlinux, vous avez la liste des paquets sur le [wiki](https://wiki.archlinux.fr/Transmission#Installation) d'Archlinux.

Comme tout bon service, il faut bien le lancer, avec SystemD, donc un p'tit coup de ``sudo systemctl start transmission``.  
Ouais mais il est lancé avec l'utilisateur *transmission* par défaut, si vous avez envie de changer d'utilisateur, vous pouvez en modifiant le fichier ``/etc/systemd/system/multi-user.target.wants/transmission.service``, il existe si vous avez activé le service avec un petit coup de ``sudo systemctl enable transmission``, donc il suffit juste de modifier le *User*.  
Voilà, il est tout beau, tout mignon, il tourne.

Après, après ? Il faut le configurer, il a une configuration de base, mais c’est plus sympa avec une petite configuration personnelle. Donc si vous avez gardé comme utilisateur *transmission*, le fichier de configuration se situe dans ``/var/lib/transmission-daemon`` ou dans ``/var/run/transmission``, ceci dépend de la distribution, telle que Debian ou Ubuntu, pour ne citer personne (Quel idée de ne pas suivre la norme de hiérarchie...), et si vous avez décidé d’utiliser votre utilisateur, ceci se situe dans ``$HOME/.config/transmission-daemon``, tout les infos sur les chemins des fichiers de configuration se situent [ici](https://trac.transmissionbt.com/wiki/ConfigFiles#LinuxGTKDefaults) pour GNU/Linux.

La liste des paramètres est disponible sur le [wiki](https://trac.transmissionbt.com/wiki/EditConfigFiles#Options) de Transmission, vous faites votre configuration personnelle.

Par defaut, Transmission-deamon a une interface web, et le contrôle à distance se fait par là, donc si vous voulez pas avoir l'interface web qui traine sur l’internet ou votre réseau local, mettez en liste blanche votre localhost, soit 127.0.0.1 (Essayez pas de la hacker !).  
Après, il suffit de lancer transmission-remote-cli sur la même machine que le démon pour avoir le contrôle.

Pour d'autres infos, l'internet, sinon les wikis [fr](https://wiki.archlinux.fr/Transmission) et [en](https://wiki.archlinux.org/index.php/Transmission) d’Archlinux sont assez complète avec celui de [Transmission](https://trac.transmissionbt.com/) et pour le remote-cli, je ferais peut-être un autre article s'il y a des trucs sympa à faire avec.
