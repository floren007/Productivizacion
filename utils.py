import yaml
def read_yaml():
    with open("config.yml","rb") as file:
        config = yaml.safe_load(file)
    return config