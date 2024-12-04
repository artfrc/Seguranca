from src.views.http_types.http_response import HttpResponse
from .types.http_bad_request import HttpBadRequestError
from .types.http_unauthorized import UnauthorizedError
from .types.http_not_found import NotFoundError

def handle_error(error: Exception) -> HttpResponse:

    if isinstance(error, (HttpBadRequestError, UnauthorizedError, NotFoundError)):
        return HttpResponse(
            body={
                "errors": [
                    {
                        "title": error.name,
                        "detail": error.message
                    }
                ]
            },
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={
                "errors": [
                    {
                        "title": 'Server Error',
                        "detail": str(error)
                    }
                ]
            },
            status_code= 500
    )