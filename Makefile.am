##
##   Copyright (C) 2007 by Juergen Heinemann http://tuncel.hjcms.de
##   Copyright (C) 2013 Atilla ÖNTAŞ https://github.com/tarakbumba/zeynep
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2 of the License, or
##   (at your Argument) any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
##
##   You should have received a copy of the GNU General Public License
##   along with this program; if not, write to the
##   Free Software Foundation, Inc.,
##   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
##
AUTOMAKE_OPTIONS = foreign 1.4
ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}
#### Taken from the autoconf scripts Makefile.am ####
edit = sed \
	-e 's|@localedir[@]|$(localedir)|g' \
	-e 's|@sysconfdir[@]|$(sysconfdir)|g' \
	-e 's|@localstatedir[@]|$(localstatedir)|g' \
	-e 's|@pkgdatadir[@]|$(pkgdatadir)|g' \
	-e 's|@prefix[@]|$(prefix)|g'

.PHONY: SCRIPT

SCRIPT: 
	./desktop_translations.sh all
	
prerequisites: SCRIPT

target: prerequisites 

SUBDIRS = po \
	kde \
    actions \
    nemo

bin_SCRIPTS = tuncel

cfgdir = $(sysconfdir)
cfg_DATA = tuncel.conf

docdir = $(datadir)/doc/tuncel

EXTRA_DIST = 			\
	COPYING \
	INSTALL \
	ChangeLog

MAINTAINERCLEANFILES = \
	aclocal.m4 \
	config.guess \
	config.sub \
	depcomp \
	configure \
	INSTALL \
	install-sh \
	ltmain.sh \
	missing \
	m4/libtool.m4 \
	m4/ltoptions.m4 \
	m4/ltsugar.m4 \
	m4/ltversion.m4 \
	m4/lt~obsolete.m4 \
	`find "$(srcdir)" -type f -name Makefile.in -print`

all: target UPDATE_PO GIT_CHANGELOG
	
UPDATE_PO:
	$(MAKE) -C po update-gmo
	
GIT_CHANGELOG:
	@if test -d "$(srcdir)/.git"; \
	then \
		echo Creating ChangeLog && \
		(GIT_DIR=$(top_srcdir)/.git \
		  ./missing --run git log --stat -M -C --name-status  --date=short --no-color) | \
		  fmt --split-only > ChangeLog.tmp \
		&& mv -f ChangeLog.tmp $(top_srcdir)/ChangeLog \
		|| ( rm -f ChangeLog.tmp ; \
		  echo Failed to generate ChangeLog >&2 ); \
	else \
		echo A git clone is required to generate a ChangeLog >&2; \
	fi

-include $(top_srcdir)/git.mk

.PHONY: UPDATE_PO GIT_CHANGELOG



##eof

