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

AC_PREREQ([2.69])

AC_INIT([tuncel], [1.5], [https://github.com/tarakbumba/tuncel])

AM_INIT_AUTOMAKE([1.9 tar-ustar dist-xz foreign no-dist-gzip])

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
  [AS_HELP_STRING([--enable-kde4=@<:@yes/no@:>@],
  [Enable kde4 @<:@default=yes@:>@])],
  [ac_cv_with_kde4=no],
  [ac_cv_with_kde4=yes]
)

AC_CHECK_PROG([HAVE_KDEFOURCONFIG], [kde4-config kde-config4 kde-config-4 kde-config], yes, no)
AC_PATH_PROG([KDEFOURCONFIG], [kde4-config kde-config4 kde-config-4 kde-config], no)
if test "x$HAVE_KDEFOURCONFIG" = "xno"; then
    AC_MSG_WARN(kde4-config not found skipping kde4 ServiceMenu Support !)
    ac_cv_with_kde4=no
fi

ac_cv_kde4_servicedir=
if test -x "$KDEFOURCONFIG" ; then
  ac_cv_kde4_servicedir=`$KDEFOURCONFIG --install services`ServiceMenus
fi
AC_SUBST([KDE4_SERVICE_MENU_DIR],"$ac_cv_kde4_servicedir")
AM_CONDITIONAL(KDE4_SERVICE_SUPPORT, test "x$ac_cv_with_kde4" = xyes)

dnl -----------------------------------------------
dnl KDE 3 Support
dnl -----------------------------------------------
AC_ARG_WITH([kde3],
  [AS_HELP_STRING([--enable-kde3=@<:@yes/no@:>@],
  [Enable kde3 @<:@default=no@:>@])],
  [ac_cv_with_kde3=yes],
  [ac_cv_with_kde3=no]
)
AC_CHECK_PROG([HAVE_KDETHREECONFIG], [kde3-config kde-config3], yes, no)
AC_PATH_PROG([KDETHREECONFIG], [kde3-config kde-config3], no)
if test "x$HAVE_KDETHREECONFIG" = "xno"; then
    AC_MSG_WARN(kde3-config not found skipping kde4 ServiceMenu Support !)
    ac_cv_with_kde3=no
fi
ac_cv_kde3_servicedir=
if test -x "$KDETHREECONFIG" ; then
  ac_cv_kde3_servicedir=`$KDETHREECONFIG --prefix`/share/apps/konqueror/servicemenus
fi
AC_SUBST([KDE3_SERVICE_MENU_DIR],"$ac_cv_kde3_servicedir")
AM_CONDITIONAL(KDE3_SERVICE_SUPPORT, test "x$ac_cv_with_kde3" = xyes)

dnl -----------------------------------------------
dnl Nautilus/Caja Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nautilus],
  [AS_HELP_STRING([--enable-nautilus=@<:@yes/no@:>@],
  [Enable nautilus @<:@default=yes@:>@])],
  [ac_cv_with_nautilus=no],
  [ac_cv_with_nautilus=yes]
)
ac_cv_nautilus_actionsdir=${datadir}/file-manager/actions/

AC_SUBST([NAUTILUS_ACTIONS_DIR],"$ac_cv_nautilus_actionsdir")
AM_CONDITIONAL(NAUTILUS_ACTIONS_SUPPORT, test "x$ac_cv_with_nautilus" = xyes)

dnl -----------------------------------------------
dnl Nemo Support
dnl -----------------------------------------------
AC_ARG_ENABLE([nemo],
  [AS_HELP_STRING([--enable-nemo=@<:@yes/no@:>@],
  [Enable nemo @<:@default=yes@:>@])],
  [ac_cv_with_nemo=no],
  [ac_cv_with_nemo=yes]
)
ac_cv_nemo_actionsdir=${datadir}/nemo/actions/

AC_SUBST([NEMO_ACTIONS_DIR],"$ac_cv_nemo_actionsdir")
AM_CONDITIONAL(NEMO_ACTIONS_SUPPORT, test "x$ac_cv_with_nemo" = xyes)

dnl -----------------------------------------------
dnl Checks for required programs.
dnl -----------------------------------------------
AC_CHECK_PROG([HAVE_KDIALOG_BIN], [kdialog kdialog3 kdialog-3 kdialog4 kdialog-4], yes, no)
AC_PATH_PROG([KDIALOG_BIN], [kdialog kdialog3 kdialog-3 kdialog4 kdialog-4], no)
if test "x$HAVE_KDIALOG_BIN" = "xno"; then
    AC_MSG_WARN(kdialog not found!Kde support is disabled!)
    ac_cv_with_kde4=no
    ac_cv_with_kde3=no
fi

AC_CHECK_PROG([HAVE_ZENITY_BIN], [zenity], yes, no)
AC_PATH_PROG([ZENITY_BIN], [zenity], no)
if test "x$HAVE_ZENITY_BIN" = "xno"; then
    AC_MSG_WARN(zenity not found! GNOME/MATE/CINNAMON support is disabled!)
    ac_cv_with_nautilus=no
    ac_cv_with_nemo=no
fi
AC_PATH_PROGS([RPM2CPIO_BIN],[rpm2cpio rpm2cpio4 rpm2cpio5],[AC_MSG_ERROR(rpm2cpio not found!)])
AC_PATH_PROGS([RPM_BIN],[rpm rpm4 rpm5],[AC_MSG_ERROR(rpm package manager not found!)])
AC_PATH_PROGS([CPIO_BIN],[cpio cpio4 cpio5],[AC_MSG_ERROR(cpio not found!)])
AC_PATH_PROGS([MD5SUM_BIN],[md5sum],[AC_MSG_ERROR(md5sum not found!)])
AC_PATH_PROGS([TERMINAL],[konsole konsole3 konsole-3 konsole4 konsole-4 gnome-terminal mate-terminal],[AC_MSG_ERROR(A terminal emulator not found!)])

dnl -----------------------------------------------
dnl python-polib, gettext and intltool
dnl -----------------------------------------------
AM_PATH_PYTHON([2.5])

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

          bindir: \$(DESTDIR)$bindir
         locales: \$(DESTDIR)$localedir
   configuration: \$(DESTDIR)$sysconfdir/tuncel.conf
         datadir: \$(DESTDIR)${datadir}/tuncel
         
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
