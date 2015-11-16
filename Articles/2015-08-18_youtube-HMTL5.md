Title: Tout Youtube en HTML5 sous GNU/Linux avec Firefox et les site de Pr0n ! ! !
Date: 2015-08-18 00:45
Category: Informatique
Tags: Youtube, Archlinux, Libre, Firefox, HTML5, GNU/Linux
Slug: tout-youtube-en-html5-sous-gnulinux-avec-firefox

En discutant sur IRC, sur le canal #Archlinx-fr, notre cher [Moviuro](http://popho.be/) nous envoie ce [sujet](https://forums.archlinux.fr/viewtopic.php?f=8&t=17210&sid=571035c34bab73d23dae21d41ed64fef) et nous demande si on a le même problème.  
Je lui répond, que bien sûr, j'ai Youtube en 360p, car il doit me manquer des trucs à la con.

Et là je me suis dit, tien, il me doit manquer des dépendances optionnelles à Firefox.

Donc pour commencer, pour savoir ce qui vous manque comme fonctionnalités dans votre Firefox pour lire vos vidéos en 1080p sur Youtube, alle sur ce [lien](https://www.youtube.com/html5).

Pour moi, j'avais déjà les fonctionnalités "HTMLVideoElement" et "WebM VP8" déjà activé. Si vous avez pas ça, chercher sur l'Internet comment les activer.

Après il me manquait la fonctionnalités "H.264", et comme je me suis dit avant, il me manque des dépendances optionnelles et sous Archlinux, il faut les paquets [`gst-libav`](https://www.archlinux.org/packages/extra/x86_64/gst-libav/) et [`gst-plugins-good`](https://www.archlinux.org/packages/extra/x86_64/gst-plugins-good/) (Si vous êtes sur une autre distribution, chercher plus ou moins ça comme nom de paquet pour les rechercher).

Nous y voilà avec la moitié des fonctionnalités activées.

Pour la suite il faut trifouiller dans `about:config` de votre Firefox pour activer quelques clefs.

Pour avoir "Media Source Extensions" et "MSE & WebM VP9", il faut mettre à Vrai `media.mediasource.enabled` et `media.mediasource.webm.enabled`.  
Après, il reste plus à activer "MSE & H.264", pour cela, il faut mettre à Vrai, les clefs `media.fragmented-mp4.exposed` et `media.fragmented-mp4.ffmpeg.enabled`.

Et voilà, normalement après ça, vous pouvez lire les vidéos Youtube en 1080p avec du HTML5 ! Et si c'est pas le cas, vous avez dû vous foirez quelque part.

Note : D'après des discutions sur IRC, l'activation de ces clefs serai des "trucs" expérimentals et peuvent provoquer l'élévation anormal du processeur.  
Et merci à Nheir, Spider-cochon, Moviuro et d'autre que j'oublie pour leur aide.

Re-Note : Pas obliger d'avoir les dépendances optionnelles pour activer "H.264", car en modifiant les clefs `media.mediasource.webm.enabled` et `media.fragmented-mp4.ffmpeg.enabled`, cette fonctionnalité s'active.

__Re-Re-Note : Quand on a fait tout ça, il est possible de regarder des vidéos de Pr0n sans flash sur certain site \o/__
