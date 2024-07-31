from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, ErrorDetail


def extract_error_details(error):
    error_details = []
    if isinstance(error, ValidationError):
        for field, details in error.detail.items():
            for detail in details:
                error_details.append({
                    'field': field,
                    'message': detail if isinstance(detail, str) else detail[0],
                    'code': detail.code
                })
    return error_details










def custom_exception_handler(exc, context):
    res = {}
    response = exception_handler(exc, context)
    
    if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:
        error_details = extract_error_details(exc)
        for detail in error_details:
            res.update({"Field":detail['field'], "Message": detail['message'], "Code": detail['code']})
            break
        custom_response_data = {
            "status": False,
            "message": res.get("Message"),
            "key":res.get("Field"),
            "status": 400,
            'data':[]
        }

        response.data = custom_response_data

    return response