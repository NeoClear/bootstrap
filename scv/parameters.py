import os

# Provides parameters to the scv module. It is to separate sensative information from the codebase
class Parameters:
    instance = None

    def __init__(self):
        self.params = {}

    @staticmethod
    def get_instance():
        if Parameters.instance is None:
            Parameters.instance = Parameters()

        return Parameters.instance

    def get(self, key):
        if key not in self.params:
            if key in os.environ:
                self.params[key] = os.environ[key]
            else:
                self.params[key] = input(f"Please provide value for {key}: ").strip()

        return self.params[key]
