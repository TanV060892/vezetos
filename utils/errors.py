from fastapi.responses import JSONResponse

'''
* name : process_error_response
* desc : function is specifically crafted to keep list of all possible errors and its specific messages need to responsd with
* input : error code -> string 
* return : error object -> json
'''
def process_error_response(error_code : str):
    if error_code == 'VZ4000':
        return JSONResponse(status_code=400, content={"status": False, "errors": [{"message": "Sorry unable to find details stored with the system.","code":error_code}]}) 
    elif error_code == 'VZ422':
        return JSONResponse(status_code=422, content={"status": False, "errors": [{"message": "Invalid Input.Unable to add details.Please contact admin.","code":error_code}]})
    elif error_code == 'VZ503':
        return JSONResponse(status_code=503, content={"status": False, "errors": [{"message": "Required permissions missing.","code":error_code}]})
    elif error_code == 'VZ409':
        return JSONResponse(status_code=409, content={"status": False, "errors": [{"message": "Unable to insert as record already exists.","code":error_code}]})
    else : 
        return JSONResponse(status_code=500, content={"status": False, "errors": [{"message": "Sorry due to some technical issue unable to get response.","code":'VZ500','reason':error_code}]})