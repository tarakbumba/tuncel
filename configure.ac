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

AC_INIT([tuncel], [2.0],
	[https://github.com/tarakbumba/tuncel/issues],
	[https://github.com/tarakbumba/tuncel])

AM_INIT_AUTOMAKE(1.10 dist-xz no-dist-gzip check-news)

AC_CONFIG_MACRO_DIR([m4])
AC_PREFIX_DEFAULT(/usr)

test "$sysconfdir" = '${prefix}/etc' && sysconfdir=/etc
AC_SUBST(SYSCONFDIR,${sysconfdir})

dnl -----------------------------------------------
dnl Package name and version number (user defined)
dnl -----------------------------------------------
PACKAGE_AUTHOR="Atilla ÖNTAŞ (tarakbumba)"
AC_SUBST([PACKAGE_AUTHOR])

PACKAGE_SUMMARY="RPM Context Menu Desktop Environments"
AC_SUBST(PACKAGE_SUMMARY)

dnl -----------------------------------------------
dnl Error Handler
dnl -----------------------------------------------
AC_DEFUN([AC_MISSING],AC_MSG_ERROR(["can not find $1 application"]))

dnl -----------------------------------------------
dnl make set requires
dnl -----------------------------------------------
AC_PROG_AWK
AC_PROG_SED
AC_PROG_MAKE_SET
AC_PROG_MKDIR_P
AC_PROG_LN_S
AC_PROG_INSTALL

dnl -----------------------------------------------
dnl KDE 4 Support
dnl -----------------------------------------------
AC_ARG_ENABLE([kde4],
[  --enable-kde4    Enable KDE4 Support],
[case "${enableval}" in
yes) kde4=true ;;
no)  kde4=false ;;
*) AC_MSG_ERROR([bad value ${enableval} for --enable-kde4]) ;;
esac],[kde4=false])

AC_CHECK_PROG([HAVE_KDEFOURCONFIG], [kde4-config kde-config4 kde-config-4 kde-config], yes, no)
AC_PATH_PROG([KDEFOURCONFIG], [kde4-config kde-config4 kde-config-4 kde-config], no)
if test "x$HAVE_KDEFOURCONFIG" = "xno"; then
    AC_MSG_WARN(kde4-config not found skipping kde4 ServiceMenu Support !)
    kde4=false
fi

AC_MSG_CHECKING([for kde4 servicemenu directory])
if test -x "$KDEFOURCONFIG" ; then
  KDE4_SERVICE_MENU_DIR=`$KDEFOURCONFIG --install services`ServiceMenus
fi
AC_MSG_RESULT([${KDE4_SERVICE_MENU_DIR}])
AC_SUBST(KDE4_SERVICE_MENU_DIR)
AM_CONDITIONAL(KDE4, test x$kde4 = xtrue)

dnl -----------------------------------------------
dnl Trinity Support
dnl -----------------------------------------------
AC_ARG_ENABLE([trinity],
[  --enable-tde   Enable TDE Support],
[case "${enableval}" in
yes) tde=true ;;
no)  tde=false ;;
*) AC_MSG_ERROR([bad value ${enableval} for --enable-tde]) ;;
esac],[tde=false])

AC_CHECK_PROG([HAVE_TRINITYCONFIG], [tde-config], yes, no)
AC_PATH_PROG([TRINITYCONFIG], [tde-config], no)
if test "x$HAVE_TRINITYCONFIG" = "xno"; then
    AC_MSG_WARN(tde-config not found skipping Trinity ServiceMenu Support !)
    tde=false
fi

AC_MSG_CHECKING([for tde servicemenu directory])
if test -x "$TRINITYCONFIG" ; then
  TRINITY_SERVICE_MENU_DIR=`$TRINITYCONFIG --prefix`/share/apps/konqueror/servicemenus
fi

AC_MSG_RESULT([${TRINITY_SERVICE_MENU_DIR}])
AC_SUBST(TRINITY_SERVICE_MENU_DIR)
AM_CONDITIONAL(TDE, test "x$tde" = xtrue)

dnl -----------------------------------------------
dnl Plasma Support
dnl -----------------------------------------------
AC_ARG_ENABLE([plasma],
[  --enable-plasma   Enable PLASMA KF5 Support],
[case "${enableval}" in
yes) plasma=true ;;
no)  plasma=false ;;
*) AC_MSG_ERROR([bad value ${enableval} for --enable-plasma]) ;;
esac],[plasma=false])

  PLASMA_SERVICE_MENU_DIR=${datadir}/kservices5/ServiceMenus/

AC_SUBST(PLASMA_SERVICE_MENU_DIR)
AM_CONDITIONAL(PLASMA, test "x$plasma" = xtrue)

dnl -----------------------------------------------
dnl Nautilus/Caja Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nautilus],
[  --enable-nautilus   Enable NAUTILUS/CAJA Support],
[case "${enableval}" in
yes) nautilus=true ;;
no)  nautilus=false ;;
*) AC_MSG_ERROR([bad value ${enableval} for --enable-nautilus]) ;;
esac],[nautilus=false])

  NAUTILUS_ACTIONS_DIR=${datadir}/file-manager/actions/

AC_SUBST(NAUTILUS_ACTIONS_DIR)
AM_CONDITIONAL(NAUTILUS, test "x$nautilus" = xtrue)

dnl -----------------------------------------------
dnl Nemo Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nemo],
[  --enable-nemo   Enable NEMO Support],
[case "${enableval}" in
yes) nemo=true ;;
no)  nemo=false ;;
*) AC_MSG_ERROR([bad value ${enableval} for --enable-nemo]) ;;
esac],[nemo=false])

  NEMO_ACTIONS_DIR=${datadir}/nemo/actions/

AC_SUBST(NEMO_ACTIONS_DIR)
AM_CONDITIONAL(NEMO, test "x$nemo" = xtrue)

dnl -----------------------------------------------
dnl Checks for required programs.
dnl -----------------------------------------------
AC_CHECK_PROG([HAVE_KDIALOG_BIN], [kdialog kdialog3 kdialog-3 kdialog4 kdialog-4], yes, no)
AC_PATH_PROG([KDIALOG_BIN], [kdialog kdialog3 kdialog-3 kdialog4 kdialog-4], no)
if test "x$HAVE_KDIALOG_BIN" = "xno"; then
    AC_MSG_WARN(kdialog not found!Kde/Plasma and Trinity support is disabled!)
    kde4=false
    plasma=false
    tde=false
fi

AC_CHECK_PROG([HAVE_ZENITY_BIN], [zenity], yes, no)
AC_PATH_PROG([ZENITY_BIN], [zenity], no)
if test "x$HAVE_ZENITY_BIN" = "xno"; then
    AC_MSG_WARN(zenity not found! GNOME/MATE/CINNAMON support is disabled!)
    nautilus=false
    nemo=false
fi
AC_PATH_PROGS([RPM2CPIO_BIN],[rpm2cpio rpm2cpio4 rpm2cpio5],[AC_MSG_ERROR(rpm2cpio not found!)])
AC_PATH_PROGS([RPM_BIN],[rpm rpm4 rpm5],[AC_MSG_ERROR(rpm package manager not found!)])
AC_PATH_PROGS([CPIO_BIN],[cpio cpio4 cpio5],[AC_MSG_ERROR(cpio not found!)])
AC_PATH_PROGS([MD5SUM_BIN],[md5sum],[AC_MSG_ERROR(md5sum not found!)])
AC_PATH_PROGS([TERMINAL],[konsole konsole3 konsole-3 konsole4 konsole-4 gnome-terminal mate-terminal],[AC_MSG_ERROR(A terminal emulator not found!)])

dnl -----------------------------------------------
dnl python-polib, gettext and intltool
dnl -----------------------------------------------
AM_PATH_PYTHON([2.7])

AX_PYTHON_MODULE([polib],[python-polib])

AC_CHECK_PROG(HAVE_GETTEXT, gettext.sh, yes, no)
AC_PATH_PROG(GETTEXT, gettext.sh, no)
if test "x$HAVE_GETTEXT" = "xno"; then
		AC_MSG_ERROR(you need to have gettext installed !)
fi dnl
AC_SUBST(GETTEXT)

AC_CHECK_PROG(HAVE_INTLTOOL, intltoolize, yes, no)
AC_PATH_PROG(INTLTOOL, intltoolize, no)
if test "x$HAVE_INTLTOOL" = "xno"; then
		AC_MSG_WARN(you need to have intltool installed !)
fi

AC_CHECK_PROGS([ENVSUBST],
  [envsubst],
  [AC_MSG_ERROR(["envsubst from gettext not found"])]
) dnl
AC_SUBST(ENVSUBST)

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
AC_CONFIG_FILES([kde/Makefile])
AC_CONFIG_FILES([actions/Makefile])
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

          bindir: $bindir
         locales: $localedir
   configuration: $sysconfdir/tuncel.conf
         datadir: ${datadir}/tuncel
         
install plasma service menu : $plasma
          plasma service dir: $PLASMA_SERVICE_MENU_DIR
          
install kde4 service menu : $kde4
          kde4 service dir: $KDE4_SERVICE_MENU_DIR
          
install trinity service menu : $tde
          trinity service dir: $TRINITY_SERVICE_MENU_DIR
          
install nautilus/caja actions : $nautilus
          nautilus actions dir: $NAUTILUS_ACTIONS_DIR
          
install nemo actions : $nemo
          nemo actions dir: $NEMO_ACTIONS_DIR
---------------------------------------------------------])

echo
echo " Now type 'make' then 'make install' as root or 'make DESTDIR=/tmp install'"
echo

dnl -----------------------------------------------
dnl eof
