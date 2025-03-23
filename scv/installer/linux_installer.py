from .installer import DependencySequenceInstaller, ScriptInstaller


class OllamaInstaller(ScriptInstaller):
    OLLAMA_INSTALL_COMMAND = "curl -fsSL https://ollama.com/install.sh | sh"
    OLLAMA_WEBSITE_URL = "https://ollama.com/download/linux"

    def __init__(self):
        super().__init__(command=self.OLLAMA_INSTALL_COMMAND, link=self.OLLAMA_WEBSITE_URL)

class LinuxInstaller(DependencySequenceInstaller):
    def __init__(self):
        super().__init__(installers=[
            OllamaInstaller()
        ])
