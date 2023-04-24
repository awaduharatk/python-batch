import configparser


class Properties:
    def __init__(self, config_file: str) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section: str, option: str) -> str:
        return self.config.get(section, option)
