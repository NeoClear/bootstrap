OS=`uname -s`
COMMON=''
SPECIFIC=''

if [ -e ./packages/common/extra.txt ]
then
    COMMON=`cat ./packages/common/extra.txt | xargs echo`
else
    COMMON=''
fi

if [ $OS = Darwin ]
then
    if [ -e ./packages/darwin/extra.txt ]
    then
        SPECIFIC=`cat ./packages/darwin/extra.txt | xargs echo`
    fi
elif [ $OS = Linux ]
then
    if [ -e ./packages/linux/extra.txt ]
    then
        SPECIFIC=`cat ./packages/linux/extra.txt | xargs echo`
    fi
fi

if [ $OS = Darwin ]
then
    if [ ! -z $COMMON ]
    then
        brew install --cask `echo $COMMON`
    fi
    if [ ! -z $SPECIFIC ]
    then
        brew install --cask `echo $SPECIFIC`
    fi
elif [ $OS = Linux ]
then
    # TODO
    echo PLACEHOLDER
fi
