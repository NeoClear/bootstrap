# Copy common dotfiles into home directory
cp -r ./dotfiles/common/home/.??* ~

OS=`uname -s`

if [ $OS = Darwin ]
then
    if [ -e ./dotfiles/darwin ]
    then
        cp -r ./dotfiles/darwin/home/.??* ~
    fi
elif [ $OS = Linux ]
then
    if [ -e ./dotfiles/linux ]
    then
        cp -r ./dotfiles/linux/home/.??* ~
    fi
fi
