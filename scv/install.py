import shutil
import argparse

from fedora_installer import FedoraInstaller

def install(verbose: bool, dry_run: bool):
    if shutil.which("dnf"):
        FedoraInstaller().install(verbose=verbose, dry_run=dry_run)
    else:
        print("Platform is not supported yet")


parser = argparse.ArgumentParser(description="Install programs for the brand-new OS")
parser.add_argument('-d', '--dry-run', type=bool, default=True)
parser.add_argument('-v', '--verbose', type=bool, default=False)

args = parser.parse_args()

install(verbose=args.verbose, dry_run=args.dry_run)
