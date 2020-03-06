import yaml

config_path = '/var/config/authentication.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    try:
        with open(config["keys"]["location"]) as f:
            config["keys"]["private"] = f.read()
    except:
        raise FileNotFoundError("No private key file provided")
    return config


config = get_config(config_path)
