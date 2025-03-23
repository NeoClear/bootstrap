from typing import override

from installer.package_list import COMMON_PACKAGES, LINUX_PACKAGES
from .installer import DependencySequenceInstaller, PackageManagerInstaller

class DnfInstaller(PackageManagerInstaller):
    def __init__(self, packages=[]):
        super().__init__(command="sudo dnf install --skip-unavailable %s", packages=packages)

    @override
    def show_description(self):
        print("Installs fedora packages via dnf")

class FedoraPackageInstaller(DnfInstaller):
    def __init__(self):
        super().__init__(packages=COMMON_PACKAGES + LINUX_PACKAGES)

class FedoraDropboxInstaller(DnfInstaller):
    FEDORA_DROPBOX_PACKAGE_URL = "https://www.dropbox.com/download?dl=packages/fedora/nautilus-dropbox-2024.04.17-1.fc39.x86_64.rpm"

    def __init__(self):
        super().__init__(packages=[self.FEDORA_DROPBOX_PACKAGE_URL])

class Fedora1PasswordInstaller(DnfInstaller):
    FEDORA_1PASSWORD_PACKAGE_URL = "https://downloads.1password.com/linux/rpm/stable/x86_64/1password-latest.rpm"

    def __init__(self):
        super().__init__(packages=[self.FEDORA_1PASSWORD_PACKAGE_URL])

class FedoraInstaller(DependencySequenceInstaller):
    def __init__(self):
        super().__init__(installers=[
            FedoraPackageInstaller(),
            FedoraDropboxInstaller(),
            Fedora1PasswordInstaller()
        ])
