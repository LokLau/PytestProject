import configparser


def read_config(section,keyword):
    config = configparser.ConfigParser()
    config.read("../Configuration/config.ini")
    return config.get(section,keyword)