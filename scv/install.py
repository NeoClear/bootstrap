import shutil

from installer.fedora_installer import FedoraInstaller

def install():
    if shutil.which("dnf"):
        FedoraInstaller().install()
    else:
        print("Platform is not supported yet")
