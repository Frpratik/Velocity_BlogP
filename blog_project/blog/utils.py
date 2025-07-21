from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {}

        if response.status_code == status.HTTP_404_NOT_FOUND:
            custom_response['error'] = 'The requested resource was not found.'
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            custom_response['error'] = 'You do not have permission to perform this action.'
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            custom_response['error'] = 'Authentication credentials were not provided or invalid.'
        else:
            custom_response = response.data

        return Response(custom_response, status=response.status_code)

    return response
