OS=`uname -s`
COMMON=''
SPECIFIC=''

if [ -e ./packages/common/base.txt ]
then
    COMMON=`cat ./packages/common/base.txt | xargs echo`
else
    COMMON=''
fi

if [ $OS = Darwin ]
then
    if [ -e ./packages/darwin/base.txt ]
    then
        SPECIFIC=`cat ./packages/darwin/base.txt | xargs echo`
    fi
elif [ $OS = Linux ]
then
    if [ -e ./packages/linux/base.txt ]
    then
        SPECIFIC=`cat ./packages/darwin/base.txt | xargs echo`
    fi
fi

if [ $OS = Darwin ]
then
    brew install $COMMON
    brew install --cask $SPECIFIC
elif [ $OS = Linux ]
then
    # TODO
    echo PLACEHOLDER
fi
