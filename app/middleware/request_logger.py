from fastapi import Request
import logging

logging.basicConfig(level=logging.INFO)


async def log_request(request: Request, call_next):
    method = request.method
    url = request.url.path
    headers = dict(request.headers)
    body = await request.body()

    logging.info(f"Request Method: {method}")
    logging.info(f"Request URL: {url}")
    logging.info(f"Request Headers: {headers}")
    logging.info(f"Request Body: {body.decode('utf-8') if body else 'No Body'}")

    response = await call_next(request)

    return response