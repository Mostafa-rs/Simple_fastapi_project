from fastapi.responses import JSONResponse


def get_response(data=None, msg=None, status_code=200, errors=None):
    if errors is None:
        success = True
    else:
        success = False
        status_code = 400

    return JSONResponse(
        {
            'success': success,
            'msg': msg,
            'errors': errors,
            'data': data,
        }, status_code=status_code
    )
