class NonEmptyIdBaseError(Exception):
    def __str__(self):
        return "NonEmptyIdBaseError : 'id base' must be empty in order to add a new line."

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