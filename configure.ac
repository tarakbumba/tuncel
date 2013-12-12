dnl
dnl   Copyright (C) 2007 2008 by Juergen Heinemann http://www.hjcms.de
dnl   Copyright (C) 2013 Atilla ÖNTAŞ https://github.com/tarakbumba/zeynep
dnl
dnl   This program is free software; you can redistribute it and/or modify
dnl   it under the terms of the GNU General Public License as published by
dnl   the Free Software Foundation; either version 2 of the License, or
dnl   (at your Argument) any later version.
dnl
dnl   This program is distributed in the hope that it will be useful,
dnl   but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl   GNU General Public License for more details.
dnl
dnl   You should have received a copy of the GNU General Public License
dnl   along with this program; if not, write to the
dnl   Free Software Foundation, Inc.,
dnl   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
dnl

AC_PREREQ(2.57)

dnl -----------------------------------------------
dnl Release Versioning
dnl -----------------------------------------------
m4_define(PKG_NAME, [tuncel])
m4_define(PKG_MAJOR, [1])
m4_define(PKG_MINOR, [0])

dnl -----------------------------------------------
dnl Package name and version number (user defined)
dnl -----------------------------------------------
AC_INIT(PKG_NAME, PKG_MAJOR.PKG_MINOR,[admin (AT) tarakbumba (DOT) com])
AM_INIT_AUTOMAKE([foreign -Wall])

PACKAGE_AUTHOR="Atilla ÖNTAŞ (tarakbumba)"
AC_SUBST([PACKAGE_AUTHOR])

PACKAGE_SUMMARY="RPM Context Menu Desktop Environments"
AC_SUBST(PACKAGE_SUMMARY)

dnl -----------------------------------------------
dnl My Error Handler
dnl -----------------------------------------------
AC_DEFUN([AC_MISSING],AC_MSG_ERROR([can not find $1 application]))

dnl -----------------------------------------------
dnl make set requires
dnl -----------------------------------------------
AC_PROG_AWK
AC_PROG_SED
AC_PROG_MAKE_SET
AC_PROG_MKDIR_P
AC_PROG_INSTALL

dnl -----------------------------------------------
dnl KDE 4 Support
dnl -----------------------------------------------
AC_ARG_ENABLE([kde4],
  [AS_HELP_STRING([--disable-kde4],[disable kde4 servicemenu support])],
  [ac_cv_with_kde4=yes],
  [ac_cv_with_kde4=no]
)

AC_PATH_PROGS([KDEFOURCONFIG],
  [kde4-config kde-config4 kde-config-4 kde-config],
  [AC_MSG_WARN([kde4-config not found skipping kde4 ServiceMenu Support])]
)
ac_cv_kde4_servicedir=
if test -x "$KDEFOURCONFIG" ; then
  ac_cv_kde4_servicedir=`$KDEFOURCONFIG --install services`/ServiceMenus
fi
AC_SUBST([KDE4_SERVICE_MENU_DIR],"$ac_cv_kde4_servicedir")
AM_CONDITIONAL(KDE4_SERVICE_SUPPORT, test "x$ac_cv_with_kde4" = xyes)

dnl -----------------------------------------------
dnl KDE 3 Support
dnl -----------------------------------------------
AC_ARG_WITH([kde3],
  [AS_HELP_STRING([--with-kde3],[enable kde3 servicemenu support])],
  [ac_cv_with_kde3=no],
  [ac_cv_with_kde3=yes]
)
AC_PATH_PROGS([KDETHREECONFIG],
  [kde-config kde3-config kde-config3],
  [AC_MSG_WARN([kde-config not found skipping kde3 ServiceMenu Support])]
)
ac_cv_kde3_servicedir=
if test -x "$KDETHREECONFIG" ; then
  ac_cv_kde3_servicedir=`$KDETHREECONFIG --prefix`/share/apps/konqueror/servicemenus
fi
AC_SUBST([KDE3_SERVICE_MENU_DIR],"$ac_cv_kde3_servicedir")
AM_CONDITIONAL(KDE3_SERVICE_SUPPORT, test "x$ac_cv_with_kde3" = xyes)

dnl -----------------------------------------------
dnl Nautilus/Caja Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nautilus-actions],
  [AS_HELP_STRING([--disable-nautilus],[disable actions support])],
  [ac_cv_with_nautilus=no],
  [ac_cv_with_nautilus=yes]
)
AC_PATH_PROGS([NAUTILUSBIN],
  [nautilus-actions-config-tool caja-actions-config-tool],
  [AC_MSG_WARN([nautilus-actions or caja-actions not found skipping Gnome/Mate support])]
)
ac_cv_nautilus_actionsdir=
if test -x "$NAUTILUSBIN" ; then
  ac_cv_nautilus_actionsdir=${datadir}/filemanager/actions/
fi
AC_SUBST([NAUTILUS_ACTIONS_DIR],"$ac_cv_nautilus_actionsdir")
AM_CONDITIONAL(NAUTILUS_ACTIONS_SUPPORT, test "x$ac_cv_with_nautilus" = xyes)

dnl -----------------------------------------------
dnl Nemo Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nemo-actions],
  [AS_HELP_STRING([--disable-nemo],[disable actions support])],
  [ac_cv_with_nemo=no],
  [ac_cv_with_nemo=yes]
)
AC_PATH_PROGS([NEMOBIN],
  [nemo-actions-config-tool],
  [AC_MSG_WARN(["nemo-actions not found skipping Cinnamon support"])]
)
ac_cv_nemo_actionsdir=
if test -x "$NEMOBIN" ; then
  ac_cv_nemo_actionsdir=${datadir}/nemo/actions/
fi
AC_SUBST([NEMO_ACTIONS_DIR],"$ac_cv_nemo_actionsdir")
AM_CONDITIONAL(NEMO_ACTIONS_SUPPORT, test "x$ac_cv_with_nemo" = xyes)

dnl -----------------------------------------------
dnl Checks for required programs.
dnl -----------------------------------------------
AC_PATH_PROGS([KDIALOG_BIN],[kdialog kdialog3 kdialog-3 kdialog4 kdialog-4],[AC_MISSING([kdialog])])
AC_PATH_PROGS([ZENITY_BIN],[zenity],[AC_MISSING([zenity])])
AC_PATH_PROGS([RPM2CPIO_BIN],[rpm2cpio rpm2cpio4 rpm2cpio5],[AC_MISSING([rpm2cpio])])
AC_PATH_PROGS([RPM_BIN],[rpm rpm4 rpm5],[AC_MISSING([rpm])])
AC_PATH_PROGS([CPIO_BIN],[cpio cpio4 cpio5],[AC_MISSING([cpio])])
AC_PATH_PROGS([MD5SUM_BIN],[md5sum],[AC_MISSING([md5sum])])
AC_PATH_PROGS([TERMINAL],[konsole konsole3 konsole-3 konsole4 konsole-4 gnome-terminal mate-terminal],[AC_MISSING([terminal])])

dnl -----------------------------------------------
dnl gettext
dnl -----------------------------------------------
AC_CHECK_PROGS([GETTEXT],
  [gettext.sh],
  [AC_MSG_ERROR([gettext.sh from gettext not found])]
) dnl
AC_SUBST(GETTEXT)

AC_CHECK_PROGS([ENVSUBST],
  [envsubst],
  [AC_MSG_ERROR([envsubst from gettext not found])]
) dnl
AC_SUBST(ENVSUBST)

eval "localedir=\"${datadir}/locale\""
AC_SUBST(localedir)
AC_SUBST(TEXTDOMAIN,"tuncel")
AM_PO_SUBDIRS

dnl -----------------------------------------------
dnl Install Directories
dnl -----------------------------------------------
AC_PREFIX_PROGRAM([$GETTEXT])

dnl -----------------------------------------------
dnl Generates Makefile's, configuration files and scripts
dnl -----------------------------------------------
AC_CONFIG_FILES([Makefile])
AC_CONFIG_FILES([kde3/Makefile])
AC_CONFIG_FILES([kde4/Makefile])
AC_CONFIG_FILES([nautilus/Makefile])
AC_CONFIG_FILES([nemo/Makefile])
AC_CONFIG_FILES([tuncel])
AC_CONFIG_FILES([tuncel.conf])
AC_CONFIG_FILES([po/Makefile],[AM_POSTPROCESS_PO_MAKEFILE])
AC_OUTPUT

dnl -----------------------------------------------
dnl Result
dnl -----------------------------------------------
AC_MSG_RESULT([Configure finished
---------------------- summary -------------------------
          bindir: \$(DESTDIR)$bindir
         locales: \$(DESTDIR)$localedir
   configuration: \$(DESTDIR)$sysconfdir/tuncel.conf
         datadir: \$(DESTDIR)$datadir/tuncel
install kde3 service menu : $ac_cv_with_kde3
          kde3 service dir: \$(DESTDIR)$KDE3_SERVICE_MENU_DIR
install kde4 service menu : $ac_cv_with_kde4
          kde4 service dir: \$(DESTDIR)$KDE4_SERVICE_MENU_DIR
install nautilus/caja actions : $ac_cv_with_nautilus
          nautilus actions dir: \$(DESTDIR)$NAUTILUS_ACTIONS_DIR
install nemo actions : $ac_cv_with_nemo
          nemo actions dir: \$(DESTDIR)$NEMO_ACTIONS_DIR
---------------------------------------------------------])

echo
echo " Now type 'make' then 'make install' as root or 'make DESTDIR=/tmp install'"
echo

dnl -----------------------------------------------
dnl eof
