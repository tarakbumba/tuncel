#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# This script is a bit modified version of desktoppo.py, 
# which is created by Yuri Chornoivan <yurchor@ukr.net> for 
# Mageia GNU/Linux software desktop files translations.
# Source: http://gitweb.mageia.org/software/i18n/tools/tree/desktop
#
#  This script is free software. They come without any warranty, to
#  * the extent permitted by applicable law. You can redistribute it
#  * and/or modify them under the terms of the Do What The Fuck You Want
#  * To Public License, Version 2, as published by Sam Hocevar. See
#  * http://sam.zoy.org/wtfpl/COPYING for more details.

import errno, glob, polib, re, os, getopt, sys
from time import strftime

def usage():
    print '\nUsage: python %s [OPTION]' %os.path.basename(sys.argv[0])
    print '       generate pot catalogs and updates po files for desktop resources in the specified directory'
    print 'Options: -h, --help                              : usage'
    print '         -d <directory>, --directory <directory> : directory with desktop files'
    sys.exit(2)
try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "directory="])
except getopt.GetoptError:
    usage() # print help information and exit

directory='.'
for o,a in opts:
    if o in ("-h", "--help"):
        usage()
    if o in ("-d", "--directory"):
        directory=a
        
directory = directory.rstrip('/')

if (directory != '') and (os.path.isdir(directory) == False):
    sys.exit('Specified directory does not exist')

# Find all desktop files
files = []
for rootdir, dirnames, filenames in os.walk(directory):
    files.extend(glob.glob(rootdir + "/*.desktop"))

# Define Templates and po directory name
messagetemplate='(?<=\n)Name=.*?\n|Comment=.*?\n|ToolbarLabel=.*?\n|X-KDE-Submenu=.*?\n'
mpattern=re.compile(messagetemplate,re.DOTALL)
translationtemplate='(?<=\n)Name\[.*?\n|Comment\[.*?\n|ToolbarLabel=\[.*?\n|X-KDE-Submenu=\[.*?\n'
tpattern=re.compile(translationtemplate,re.DOTALL)
podir = 'po'

# Write POT file
pot = polib.POFile('',check_for_duplicates=True)
potcreationtime = strftime('%Y-%m-%d %H:%M%z')
pot.metadata = {
  'Project-Id-Version': 'Tuncel desktop files translation',
  'Report-Msgid-Bugs-To': 'https://github.com/tarakbumba/tuncel/issues',
  'POT-Creation-Date': potcreationtime,
  'PO-Revision-Date': 'YEAR-MO-DA HO:MI+ZONE',
  'Last-Translator': 'FULL NAME <EMAIL@ADDRESS>',
  'Language-Team': 'LANGUAGE <LL@li.org>',
  'MIME-Version': '1.0',
  'Content-Type': 'text/plain; charset=UTF-8',
  'Content-Transfer-Encoding': '8bit',
  }

for langfile in files:
  langfiledir = langfile.replace('.desktop', '')
  langfilename = langfiledir.rpartition('/')[2]
  # Create localization directories if needed
  try:
    if directory == os.path.dirname(__file__):
            os.makedirs(podir)
    else:
            os.makedirs(directory +"/" + "po")
  except OSError, e:
    if e.errno != errno.EEXIST:
        raise
  #open desktop file
  text = open(langfile,"r").read()

  # Parse contents and add them to POT
  for mblock in mpattern.findall(text):
    mblock_stripped = mblock.strip('\n')
    message_comment, message_id = mblock.strip('\n').split('=')
    potentry = polib.POEntry(
      msgctxt = message_comment,
      msgid = message_id.decode('utf-8'),
      msgstr = '',
      occurrences=[(langfile,'')]
      )
    if message_id != '':
      try:
	pot.append(potentry)
      except ValueError:
	print 'The entry already exists'
pot.save(directory + '/po/tuncel_desktop.pot')

# Merge translations
for pofile in glob.glob(podir + '/*.po'):
  lang = pofile[:-3].rsplit('/',1)[1]
  pofilename = pofile
  po = polib.pofile(pofilename)
  po.merge(pot)
  po.save(pofilename)

for langfile in files:
  #open desktop file
  deskfile = open(langfile,"r")
  text = deskfile.read()
  deskfile.close()
  deskfile = open(langfile,"w")
  for transblock in tpattern.findall(text):
    text = text.replace(transblock, '')

  # Parse PO files
  for pofile in sorted(glob.glob(podir + '/*.po'), reverse = True):
    lang = pofile[:-3].rsplit('/',1)[1]
    pofilename = pofile
    po = polib.pofile(pofilename)
    for entry in po.translated_entries():
      if entry.msgid.encode('utf-8') in text:
	origmessage = ('\n' + entry.msgctxt + '=' + entry.msgid + '\n').encode('utf-8')
	origandtranslated = ('\n' + entry.msgctxt + '=' + entry.msgid + '\n' + entry.msgctxt + '[' + lang + ']=' + entry.msgstr + '\n').encode('utf-8')
	text = text.replace(origmessage, origandtranslated)

  deskfile.write(text)
  deskfile.close()

