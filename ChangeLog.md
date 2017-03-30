## tuncel 2.0  (2017-03-30)

Bugfix:

    - Updated configure.ac and Makefile.am scripts for better building
    - Removed unnecessary programs checking for plasma
    - Remove nemo-actions from runtime dependencies part. There is no such tool, nemo supports actions natively :)


New:
    - Require Python 2.7
    - Added Trinity Desktop and KF Plasma support.
    
Deprecated:
    - Kde3 support is dropped.    
    

## tuncel 1.6  (2014-06-13)

Bugfix:

    Fix openHomepage option which was not work with https URLs

    -Fix python-polib requirement at buildtime


## tuncel 1.5  (2014-06-12)

Bugfix:

    - Fix configure checks for prerequisties
    
New:

    - Make Nemo actions use translations from Actions directory
    - Merge translations at build time

## tuncel 1.4  (2014-06-11)

Bugfix:

    - Fix Nemo support: It wasn't installed correct path and didn't work
    
New:
    
     - Added Romanian, Spanish and Greek translations from transifex
       Thanks to respective translators :)

## tuncel 1.3  (2014-04-07)

Bugfix:
    - Fixed configure.ac: Default behaviour is enabling feature when requirements met
    - Fixed typo in po/LINGUAS file which broke package building.
    - Fixed Makefile doesn't copy Copying, ChangeLog, Readme

New:
    - Add maintaniers directory
    - Merge nautilus and nemo directories into one "actions" directory
    - Merge kde3 and kde4 directories into one "kde" directory
    - Add gettext po translation files for both kde and actions .desktop files.
    - Add autogen.sh script to create configure and makefile scripts easily
    - Add actions and kde Turkish translation


Updates:
    - Update .desktop file strings and create new po files from them
    - Updated translations from Transifex

## tuncel 1.2  (2013-12-23)

New:

    - Make configure.ac builds all without --enable-future flag

Update:

    - Update README for changed build instructions

## tuncel 1.1  (2013-12-19)

Bugfix:

    - Fixed actions desktop files: use %f not %u
    - Fixed textdomaindirs
    - Fix rpm specfile: error with nautilus-data package

New:

    - Add Turkish translation to kde desktop files
    - Add translatable rpm querytags

Updated:

    - Update translation catalogs

## tuncel 1.0  (2013-12-12)

New:
    - Initial Release

