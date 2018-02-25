Title: Installation de Archlinux avec du LUKS en BIOS avec Syslinux
Date: 2016-10-22 02:33
Author: HS-157
Category: Informatique
Tags: Archlinux, Libre, Luks, Gnu/Linux

Aujourd'hui, je vais prendre note sur comment installer un Archlinx avec du LUKS en BIOS avec Syslinux pour tout chiffrer bien ce qu'il faut.

On va s'appuyer sur [l'installation de base](https://wiki.archlinux.fr/Installation) du wiki d'Archlinux, et plus perticulairement sur la [révision du 19 juin 2016](https://wiki.archlinux.fr/index.php?title=Installation&oldid=6714) car il y a la commande pour rajouter un utilisateur bien ce qu'il faut.

Il y a plein de blabla dans le wiki que moi je vais sauter, et on commence donc par changer le clavier :
~~~
loadkeys fr
~~~

Ainsi que demander qu'une IP à notre DHCP :
~~~
dhcpcd
~~~

On commence par partitionner le disque, mais là commence la différence, on va créer deux partition, la première sera pour le /boot et la deuxième sera pour notre partion LUKS. Donc par exemple on aura ça avec `cfdisk` :

- /dev/sda1 pour le /boot avec le drapeau boot
- /dev/sda2 pour la partion LUKS

On crée la partition LUKS :
~~~
cryptsetup luksFormat -c aes-xts-plain64 -s 512 -h sha256 /dev/sda2
~~~
+ `-c` Pour choisir le type de chiffrement, on peut tester avec un `cryptsetup benchmark`, le mieux est de choisir celui le plus rapide avec une clef élevé.
+ `-s` Pour la taille de la clef.
+ `-h` Pour choisir le type de hash.

Il faut maintenant ouvrir le volume chiffré :
~~~
cryptsetup luksOpen /dev/sda2 ssd
~~~

Comme on ne peut pas créer plusieurs partitions sur un volume LUKS, il faut donc s'amuser avec LVM en créant un volume LVM !
~~~bash
pvcreate /dev/mapper/ssd
# Initialise un conteneur physique LVM
vgcreate ssd /dev/mapper/ssd
# Initialise un volume groupe dans le conteneur
lvcreate -L 15G ssd -n root
# Initialise une partition de 15Go nommée 'root' dans le groupe de volume 'ssd'
lvcreate -L 2G ssd -n swap
# Initialise une partition de 2Go nommée 'swap' dans le groupe de volume 'ssd'
lvcreate -l +100%FREE ssd -n home
# Initialise une partition nommée 'home' dans le groupe de volume 'ssd'
~~~
À personnaliser.

Il faut formater au bon format :
~~~
mkfs.ext2 /dev/sda1
mkfs.ext4 /dev/mapper/ssd-root
mkfs.ext4 /dev/mapper/ssd-home
mkswap /dev/mapper/ssd-swap
~~~

On monte les volumes :
~~~
mount /dev/mapper/ssd-root /mnt
mkdir /mnt/boot && mkdir /mnt/home
mount /dev/sda1 /mnt/boot
mount /dev/mapper/ssd-home /mnt/home
swapon /dev/mapper/ssd-swap
~~~

Pour la suite on peut suivre le wiki pour [installer un système](https://wiki.archlinux.fr/Installation#Installation_du_syst.C3.A8me_de_base) normalement :
~~~bash
pacstrap /mnt base base-devel vim zsh syslinux
genfstab -U -p /mnt >> /mnt/etc/fstab
arch-chroot /mnt
echo NomDeLaMachine > /etc/hostname
ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
locale-gen
echo LANG="fr_FR.UTF-8" > /etc/locale.conf
export LANG=fr_FR.UTF-8
echo KEYMAP=fr > /etc/vconsole.conf
passwd
~~~

Pour dire au noyau qu'on doit déchiffrer la partition qu'on a du LVM dans `/etc/mkinitcpio.conf` avec l'ordre qui est important :
~~~
HOOKS="... keyboard keymap encrypt lvm2 resume ... filesystems ..."
~~~
Et un coup de `mkinitcpio -p linux` après.

Pour la suite, il faut s'amuser avec Syslinux dans `/boot/syslinux/syslinux.cfg` :
~~~
LABEL arch
	MENU LABEL Arch Linux
	LINUX ../vmlinuz-linux
	APPEND root=/dev/mapper/ssd-root cryptdevice=/dev/sda2:ssd rw
	INITRD ../initramfs-linux.img
~~~
C'est surtout le `APPEND` qu'il faut modifier pour bien démarrer sur le système :

+ `root=` C'est pour dire où est la partition /.
+ `cryptdevice=` C'est pour dire quel est la partition chiffré.
+ `rw` C'est pour dire qu'on est en lecture / écriture.

Et hop :
~~~
syslinux-install_update -iam
~~~

Et rajout d'un utilisateur et de son mot de passe :
~~~
useradd -g users -m -s /bin/zsh hs-157
passwd hs-157
~~~

Après le doute, on reboot et normalement tout marche !
Et je vous laisse vous amusez à installer votre système perso.

Références :

- [SSD : dm-crypt, LVM2 et ext4 et l’alignement des partitions](http://www.guiguishow.info/2012/05/27/ssd-dm-crypt-lvm2-et-ext4-et-lalignement-des-partitions/)
- [Archlinux sur un SSD avec LUKS / LVM2 / BTRFS](https://blog.zenithar.org/post/2016/01/24/archlinux-ssd-luks-lvm-btrfs/)
- [Installation de base](https://wiki.archlinux.fr/Installation)
