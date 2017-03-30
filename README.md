Tuncel
======

Tuncel is a fork of GPL licensed Heinemann Jürgen's rpmxdgtool.
(http://gitweb.hjcms.de/cgi-bin/index.cgi/rpmxdgtool/)

It provides KDE4, PLASMA and TRINITY service menus,
nautilus-actions for GNOME,caja-actions for MATE,
nemo-actions for Cinnamon.

Tuncel has full translation support. If someone who talks your native
language, translates related gettext po files then tuncel talks your 
language.

Installation:
-------------
Please refer to INSTALL file before proceeding.
Also you should previously install these dependencies first:

- autoconf
- automake
- coreutils
- gettext-devel
- rpm-devel
- kdelibs (for KDE4 support)
- trinity-tdelibs (Trinitiy support)
- kdialog (for KDE4/PLASMA/TRINITY support)
- zenity (for GNOME/MATE/NEMO support)
- intltool
- python-polib


Basically you should first create configuration and make
files by issuing:

    ./autogen.sh
    
    or 
    
    autoreconf
    automake

in tuncel's root directory.

After that, if all dependencies met; simply configure, make and make install should work.

Supply configure script with desired servicemenu/actions options. E.g.

    ./configure --enable-kde4 \
        --enable-plasma \
        --enable-tde \
        --enable-nautilus \
        --enable-nemo

If all dependencies met, kde4/plasma/trinity, nautilus, caja and nemo support will be installed.

Runtime Dependencies
--------------------
Depending your compilation choice, these should be installed on your system before running tuncel.

- nautilus-actions (for GNOME/Nautilus support)
- caja-actions (for MATE/Caja support)
- kdelibs (KDE4 support)
- trinity-tdelibs (Trinitiy support)
- zenity (GNOME/MATE/CINNAMON support)
- kdialog (KDE4/PLASMA/TRINITY support)
- rpm2cpio
- gettext (i18n support)
- rpm (of course!)

Translations:
-------------
Main tuncel script and related .desktop files could be 
translated using Gettext po format. 
First extract translation template from *.pot file:

    msginit -i po/*.pot -o po/LANG_Code.po
    
Then translate it. 

Also you can use Transifex web instance for translation workflow:

https://www.transifex.com/projects/p/tuncel/


Bugs:
------------
If you encounter any bugs please open an issue at projects' github page:
    https://github.com/tarakbumba/tuncel/issues/new 

Authors:
-----------
rpmxdgtool by Heinemann Jürgen http://gitweb.hjcms.de/cgi-bin/index.cgi/rpmxdgtool/

tuncel by Atilla ÖNTAŞ (aka tarakbumba) https://github.com/tarakbumba/tuncel
