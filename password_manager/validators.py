from rest_framework.exceptions import NotFound

from utils.custom_exceptions import EmptyValueException


def validate_get_parameters(*parameters):
    for param in parameters:
        if param is None:
            raise NotFound
        elif param == '':
            raise EmptyValueException
