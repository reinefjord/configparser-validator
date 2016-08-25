def validate_config(config, template):
    """Validates ConfigParser and returns errors.
    Compares a ConfigParser with a template dict or ConfigParser 
    and returns errors if there are invalid sections, invalid keys,
    or values of wrong type.
    """
    errors = []
    config_get_map = {str: config.get,
                      int: config.getint,
                      float: config.getfloat,
                      bool: config.getboolean}

    for section in config.sections():
        if section not in template:
            errors.append("Invalid section in config: '{}'".format(section))
            continue

        for conf_key, conf_val in config.items(section):
            if conf_key not in template[section]:
                errors.append("Invalid key in section '{section}': '{key}'"
                              .format(section=section, key=conf_key))
                continue

            template_val_type = type(template[section][conf_key])
            try:
                config_get_map[template_val_type](section, conf_key)
            except ValueError:
                errors.append(
                        ("Invalid value for key '{key}' in section "
                         "'{section}': '{val}'")
                        .format(section=section, key=conf_key, val=conf_val))
    return errors
