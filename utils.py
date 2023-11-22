
def parse_lines(input_data):
    """ Parse l'input ligne par ligne. """
    return input_data.strip().split('\n')

def parse_comma_separated(input_data):
    """ Parse des données séparées par des virgules. """
    return [item.strip() for item in input_data.split(',')]

def parse_groups(input_data):
    """ Divise l'input en groupes séparés par des lignes vides. """
    return [group.split('\n') for group in input_data.strip().split('\n\n')]

def parse_key_value_pairs(input_data, separator=':'):
    """ Parse des paires clé-valeur. """
    return [line.split(separator) for line in input_data.strip().split('\n')]

def parse_lines_as_ints(input_data):
    """ Convertit les lignes de l'input en entiers. """
    return [int(line) for line in input_data.strip().split('\n')]

def parse_comma_separated_as_ints(input_data):
    """ Convertit des données séparées par des virgules en entiers. """
    return [int(item) for item in input_data.split(',')]
