#! /usr/bin/env sh
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


