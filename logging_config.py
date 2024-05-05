import logging.config
import sys
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging
import time

logger = logging.getLogger(__name__)


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.perf_counter()
        req_format_log = {
            "req:": {"method": request.method, "url:": str(request.url)},
        }
        logging.info("Request: %s", req_format_log)
        response = await call_next(request)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        overall_status = (
            "successful" if response.status_code in [200, 201] else "failure"
        )
        res_format_log = {
            "res": {
                "status": overall_status,
                "status_code:": response.status_code,
                "time_taken": f"{execution_time:0.4f}s",
                # "body": resp_body,
            },
        }
        logging.info(f"Response: %s", res_format_log)
        return response


async def middleware_log(request: Request, call_next) -> Response:
    response = await call_next(request)
    logging.info(
        "Incoming Request",
        extra={
            "req:": {"method": request.method, "url:": str(request.url)},
            "res": {"status_code:": response.status_code},
        },
    )
    return response


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] [%(name)s] [%(module)s] [%(funcName)s] [%(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "default_formatter",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        },
        "rotate_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "./logs/app.log",
            "maxBytes": 100000,
            "backupCount": 25,
            "mode": "w",
            "level": "DEBUG",
            "formatter": "default_formatter",
        },
        "timed_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "./logs/api.log",
            "when": "d",
            "interval": 1,
            "level": "INFO",
            "backupCount": 25,
            "formatter": "default_formatter",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "rotate_file_handler",
            "timed_file_handler",
        ],
        "propogate": True,
    },
}


def init_log_config():
    logging.config.dictConfig(logging_config)
