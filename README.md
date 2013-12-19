Tuncel
======

Tuncel is a fork of GPL licensed Heinemann Jürgen's rpmxdgtool.
(http://gitweb.hjcms.de/cgi-bin/index.cgi/rpmxdgtool/)
It provides kde3/4 service menus, nautilus-actions actions for GNOME,
caja-actions actions for MATE, nemo-actions actions for Cinnamon.

Installation:
-------------
Please refer to INSTALL file before proceeding.
Also you should previously install these dependencies first:

- autoconf
- automake
- coreutils
- gettext-devel
- rpm-devel
- kdelibs (for kde4 support)
- kdialog (for kde4 support)
- zenity (for GNOME/MATE/NEMO support)


Basically you should first create configuration and make
files by issuing:

    autoreconf
    automake

in tuncel's root directory.

After that, if all dependencies met; simply configure, make and make install should work.

If all dependencies met, kde4, nautilus, caja and nemo support will be installed.

If you do not want to install one of these features just supply configure script with
appropriate option. E.g.:

    ./configure --disable-kde4

Runtime Dependencies
--------------------
Depending your compilation choice, these should be installed on your system before running tuncel.

- nautilus-actions (for GNOME/Nautilus support)
- caja-actions (for MATE/Caja support)
- nemo-actions (for Cinnamon/Nemo support)
- kdelibs (KDE4 support)
- zenity (GNOME/MATE/CINNAMON support)
- kdialog (KDE4 support)
- rpm2cpio
- gettext (i18n support)
- rpm (of course!)

Translations:
-------------
All files can be translated. First extract translation template from po/tuncel.pot file:

    msginit -i po/tuncel.pot -o po/LANG_Code.po
    
Then translate it. Also you may translate *.desktop files. 
If you translate all of them open a bug report requesting merge
with project.

Bugs:
------------
If you encounter any bugs please open an issue at projects' github page:
    https://github.com/tarakbumba/tuncel/issues/new 

Authors:
-----------
rpmxdgtool by Heinemann Jürgen http://gitweb.hjcms.de/cgi-bin/index.cgi/rpmxdgtool/

tuncel by Atilla ÖNTAŞ (aka tarakbumba) https://github.com/tarakbumba/tuncel
