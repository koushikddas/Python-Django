import configparser


def createconfig(path):
    config = configparser.ConfigParser()
    config.add_section("Setting")
    config.set("settings", "font", "times")
    config.set('settings', 'color', 'blue')
    config.set("Settings", "font_size", "10")

    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    createconfig(path)
