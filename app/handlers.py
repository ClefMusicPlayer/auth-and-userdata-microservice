from flask import request, Response

from .views import app


@app.after_request
def _after_request(response: Response):

    request_closure = request.__dict__.copy()

    @response.call_on_close
    def on_close_handler():
        print(request_closure)
        # Do things here like log traffic, message log aggregator etc
        ...

    return response