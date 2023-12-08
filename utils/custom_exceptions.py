from rest_framework import status
from rest_framework.exceptions import APIException


class EmptyValueException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Пустое значение недопустимо'
    default_code = 'empty_value_exception'
