class NonEmptyIdBaseError(Exception):
    def __str__(self):
        return "NonEmptyIdBaseError : 'id base' must be empty in order to add a new line."


class NonEmptyIdPersonneError(Exception):
    def __str__(self):
        return "NonEmptyIdPersonneError : 'id personne' must be empty in order to add a new line."


class EmptyIdPersonneError(Exception):
    def __str__(self):
        return "EmptyIdPersonneError : 'id personne' must not be empty in order to add a new line."


class WrongIdPersonneTypeError(Exception):
    def __str__(self):
        return "WrongIdPersonneTypeError : 'id personne' must be a number."


class WrongIdBaseTypeError(Exception):
    def __str__(self):
        return "WrongIdBaseTypeError : 'id base' must be a number."


class EmptyIdBaseError(Exception):
    def __str__(self):
        return "EmptyIdBaseError : 'id base' must not be empty in order to modify a line."


class UnknownIdBaseError(Exception):
    def __str__(self):
        return "UnknownIdBaseError : this 'id base' does not exist in the database."


class UnknownIdPersonneError(Exception):
    def __str__(self):
        return "UnknownIdPersonneError : this 'id personne' does not exist in the database."


class MaccroError(Exception):
    def __init__(self, name, path):
        self.name = name
        self.source = path

    def __str__(self):
        return "MaccroError : an error has occurred while trying to run maccro : " + self.name + "in " + self.source


class IdUnknown(Exception):
    def __init__(self, primary_key):
        self.primary_key = primary_key

    def __str__(self):
        return "IdUnknown : id : " + self.primary_key + " is not a primary key of the database."
