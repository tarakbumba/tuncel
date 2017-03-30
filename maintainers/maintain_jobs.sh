#! /usr/bin/env sh

update_desktop () {
directories="actions kde"
for i in $directories; do
    echo "Entering into $i directory...
"
    cp tuncel_desktop2po.py ../"$i"/ 
    pushd ../"$i"
    python2 tuncel_desktop2po.py
    mv po/tuncel_desktop.pot po/tuncel_"$i"_desktop.pot
    rm -fr python2 tuncel_desktop2po.py
    popd
done

}

update_changelog () {
pushd ../
if test -d ".git"; then
    git log --date-order --date=short | \
    sed -e '/^commit.*$/d' | \
    awk '/^Author/ {sub(/\\$/,""); getline t; print $0 t; next}; 1' | \
    sed -e 's/^Author: //g' | \
    sed -e 's/\(.*\)> \([0-9]*-[0-9]*-[0-9]*\)/\2 \1>/g' | \
    sed -e 's/^\(.*\) \(\)\t\(.*\)/\3    \1    \2/g' > ChangeLog
else
    echo "No git repository present."
fi
popd

}

OPTION="$1"
case $OPTION in
    *p* ) update_desktop; shift
    ;;
    *c* ) update_changelog;shift
    ;;
    -* )  echo "Unrecognized option: $OPTION" && exit 1
    ;;
esac

