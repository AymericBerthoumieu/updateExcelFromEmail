class WrongData(Exception):
    def __init__(self, instruction, expected):
        self.expected = expected
        self.instruction = instruction

    def __str__(self):
        msg_format = """WrongData : The data given in mail for instruction {inst}.
        Expected : {exp}.
        """
        msg = msg_format.format(inst=self.instruction, exp=self.expected)
        return msg


class UnunderstandableSubject(Exception):
    def __str__(self):
        return "UnunderstandableSubject: Sorry but the command in subject is not understood by the automaton."

class GmailAddressesOnly(Exception):
    def __str__(self):
        return "GmailAddressesOnly: Sorry but only Gmail addresses can launch a command."
