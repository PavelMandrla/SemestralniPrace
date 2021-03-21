import json


def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class ScannerSettings:
    """docstring for ScannerSettings."""

    def load_settings(self, srcFile):
        self.srcFile = srcFile
        with open(self.srcFile) as input:
            self.settings = json.load(input)

    def __getitem__(self,key):
        return self.settings[key]

settings = ScannerSettings()
