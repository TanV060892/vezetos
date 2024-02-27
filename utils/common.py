import re
import json

from datetime import datetime,timedelta
from fastapi.responses import JSONResponse
from utils import errors

def check_required_fields_and_types(field_types, body):
    type_errors = []
    for field, expected_type in field_types.items():
        if field not in body:
            type_errors.append({"message": field + " is required", "code": "VZ422"})
        elif not isinstance(body[field], expected_type):
            type_errors.append({"message": field + " should be of type " + str(expected_type), "code": "VZ422"})    
    if type_errors:
        return {"status": False, "errors": type_errors}
    else:
        return True


def process_success_response(response_to_send : dict):
    return JSONResponse(status_code=200, content={"status": True, "data": response_to_send})

def process_error_response(error_code : str):
    return errors.process_error_response(error_code)

def to_camel_case(input_string: str):
    words = input_string.replace("_", " ").replace("-", " ").split()
    return ' '.join(word.title() for word in words)

def to_first_upper_case(input_string: str):
    return input_string.capitalize()

def convert_to_dict(json_str: str):
    data_dict = json.loads(json_str)
    return data_dict


def convert_to_dict_from_list(ip_list_value: list):
    json_data = json.dumps(ip_list_value)
    return json_data


def read_content_from_file(file_path):
    with open(file_path, "r") as file_details:
       return file_details.read()


def remove_all_special_characters(ip_string: str) -> str:
    string = ip_string.replace(' ', '-')
    return re.sub(r'[^A-Za-z0-9]', '', string)