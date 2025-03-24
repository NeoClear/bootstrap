import os
import sys
from typing import List, override, final

class Installer:
    def run_install_command(self, verbose: bool, dry_run: bool) -> bool:
        """Returns true if command is successful.
        Derived class should always override this method
        """
        raise RuntimeError("Unimplemented")

    @final
    def install(self, verbose: bool, dry_run: bool) -> bool:
        """Returns true if installation is successful.
        If the installation failed, it would return false.
        This method is final.
        """
        print(f"Starting {type(self).__name__}")
        if verbose:
            self.show_verbose_description()
        else:
            self.show_description()

        # dry_run is not handled here, as a dry_run still needs to reach
        # all terminal installers. dry_run is handled in [run_install_command]
        # methods of terminal installers.

        success = True

        if not self.run_install_command(dry_run=dry_run, verbose=verbose):
            print(f"\033[91;1mFAILURE\033[0m: {type(self).__name__}", file=sys.stderr)
            self.show_reference()
            success = False

        print(f"Exiting {type(self).__name__}")

        return success

    def show_description(self) -> None:
        """Displays description before installation if no verbose is set
        """
        pass

    def show_verbose_description(self) -> None:
        """Displays verbose description of the install. Only one of
        [description] and [verbose_description] would happen
        """
        pass

    def show_reference(self) -> None:
        pass


class SequenceInstaller(Installer):
    """Runs a sequence of installers.
    Any installation failure would abort the entire install
    """
    def __init__(self, installers: List[Installer], stop_on_error=True):
        self.installers = installers
        self.stop_on_error = stop_on_error

    @override
    def run_install_command(self, verbose=False, dry_run=True) -> bool:
        failed_installers = []

        for installer in self.installers:
            if not installer.install(verbose=verbose, dry_run=dry_run):
                failed_installers.append(installer)

                if self.stop_on_error:
                    return False

            # if not installer.install(verbose=verbose, dry_run=dry_run):
            #     return False

        return True

class PackageManagerInstaller(Installer):
    def __init__(self, command, packages):
        """command should look like [sudo dnf install %s].
        packages is a list of strings.
        """
        self.command = command
        self.packages = packages

    @override
    def run_install_command(self, verbose=False, dry_run=True) -> bool:
        if dry_run:
            return True

        if os.system(self.command % " ".join(self.packages)) != 0:
            return False

        return True

class ScriptInstaller(Installer):
    def __init__(self, command, link):
        self.command = command
        self.link = link

    @override
    def run_install_command(self, verbose: bool, dry_run: bool) -> bool:
        if dry_run:
            return True

        if os.system(self.command) != 0:
            return False

        return True

    @override
    def show_reference(self):
        print(f"Script failed, please visit {self.link}")
