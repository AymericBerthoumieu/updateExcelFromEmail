from emailManager.errors import *


def format_data(message_body: str, headers: list):
    """
    :param message_body: body of e-mail message
    :param headers: data to find in e-mail body
    :return: dict with data
    """
    splited = message_body.split('#')
    formatted_data = {}
    try:
        for inde, header in enumerate(headers):
            if splited[inde] != '':
                formatted_data[header] = splited[inde]
    except:
        raise WrongData
    return formatted_data


def format_error_response(message, error):
    msg_format = """ An error as occurred:
    {error_str}
    ===================
        Your e-mail
    ===================
    Subject : {subject}
    Body :
    {body}
    """
    msg = msg_format.format(error_str=error.__str__(), subject=message['Subject'], body=message['body'])
    return msg


def format_done(message):
    msg_format = """ Done with request
    ===================
        Your e-mail
    ===================
    Subject : {subject}
    Body :
    {body}
    """
    msg = msg_format.format(subject=message['Subject'], body=message['body'])
    return msg


def format_done_and_id(message, id_personne):
    msg_format = """ Done with request. New id personne is : {id_personne}
    ===================
        Your e-mail
    ===================
    Subject : {subject}
    Body :
    {body}
    """
    msg = msg_format.format(id_personne=id_personne, subject=message['Subject'], body=message['body'])
    return msg
