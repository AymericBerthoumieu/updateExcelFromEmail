class WrongData(Exception):
    def __init__(self, expected):
        self.expected = expected

    def __str__(self):
        msg_format = """WrongData : You didn't gave the good number of argumets. The data expected is {exp}
        """
        msg = msg_format.format(exp=self.expected)
        return msg


class UnunderstandableSubject(Exception):
    def __str__(self):
        return "UnunderstandableSubject: Sorry but the command in subject is not understood by the automaton."

class GmailAddressesOnly(Exception):
    def __str__(self):
        return "GmailAddressesOnly: Sorry but only Gmail addresses can launch a command."
