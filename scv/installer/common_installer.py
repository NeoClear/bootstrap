from .installer import DependencySequenceInstaller
from .installer import ScriptInstaller

class SshKeyInstaller(ScriptInstaller):
    SSH_KEYGEN_COMMAND = "ssh-keygen -t ed25519 -C 'neoclear@outlook.com'"

    def __init__(self):
        super().__init__(command=self.SSH_KEYGEN_COMMAND, link="")

class MiseInstaller(ScriptInstaller):
    MISE_INSTALL_COMMAND = "curl https://mise.run | sh"
    MISE_WEBSITE_URL = "https://mise.jdx.dev/getting-started.html"

    def __init__(self):
        super().__init__(command=self.MISE_INSTALL_COMMAND, link=self.MISE_WEBSITE_URL)

class RustInstaller(DependencySequenceInstaller):
    class RustupInstaller(ScriptInstaller):
        RUSTUP_INSTALL_COMMAND = "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
        RUSTUP_WEBSITE_URL = "https://rustup.rs/"

        def __init__(self):
            super().__init__(command=self.RUSTUP_INSTALL_COMMAND, link=self.RUSTUP_WEBSITE_URL)

    class RustAnalyzerInstaller(ScriptInstaller):
        RUST_ANALYZER_INSTALL_COMMAND = "rustup component add rust-analyzer"

        def __init__(self):
            super().__init__(command=self.RUST_ANALYZER_INSTALL_COMMAND, link="")

    def __init__(self):
        super().__init__(installers=[
            self.RustupInstaller(),
            self.RustAnalyzerInstaller()
        ])

class SpacemacsInstaller(ScriptInstaller):
    SPACEMACS_INSTALL_COMMAND = "git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d"

    def __init__(self):
        super().__init__(command=self.SPACEMACS_INSTALL_COMMAND, link="")

class CommonInstaller(DependencySequenceInstaller):
    def __init__(self):
        super().__init__(installers=[
            SshKeyInstaller(),
            MiseInstaller(),
            RustInstaller(),
            SpacemacsInstaller()
        ])
