#! /usr/bin/env sh
set -x
#directories="actions kde nemo"
#cp actions/po/*.po nemo/po/
#for i in $directories; do
#    echo "Entering into $i directory...
#"
#    cp maintainers/tuncel_desktop2po.py "$i"/ 
#    pushd "$i"
#    python2 tuncel_desktop2po.py
#    mv po/tuncel_desktop.pot po/tuncel_"$i"_desktop.pot
#    rm -fr tuncel_desktop2po.py
#    popd
#done

nemo () {
cp actions/po/*.po nemo/po/
cp maintainers/tuncel_desktop2po.py nemo/
pushd nemo
#for i in po/*.po; do sed -i 's|ToolbarLabel|Comment|g' po/$i && do sed -i 's|.desktop|.nemo_action|g' po/$i; done
python2 tuncel_desktop2po.py
for i in *.desktop; do mv $i $(echo "$i" | cut -d "." -f1).nemo_action; done
rm -fr tuncel_desktop2po.py
popd

}

actions () {

cp maintainers/tuncel_desktop2po.py actions/
pushd actions
python2 tuncel_desktop2po.py
rm -fr tuncel_desktop2po.py
popd

}

kde () {

cp maintainers/tuncel_desktop2po.py kde/
pushd kde
python2 tuncel_desktop2po.py
rm -fr tuncel_desktop2po.py
popd

}


while [[ $1 ]]; do
  case "$1" in
    nemo)		nemo;;
    actions)	actions;;
    kde)		kde;;
    all)		nemo;actions;kde;;
    *)          echo -n "Not valid option" && exit 1 ;;
  esac
  shift
done

