from fastapi import FastAPI
import apis
from logging_config import init_log_config, LogMiddleware
from fastapi.middleware.cors import CORSMiddleware


def start_app():
    init_log_config()

    fastapi_app = FastAPI(
        title="Analytics",
        description="This app is to develope API's for analytics",
        summary="Appliction analytics by logging each event",
        version="0.0.1",
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        contact={
            "name": "Rishabh Kumar",
            "email": "rishabh.kumar94@outlook.com",
        },
    )
    return fastapi_app


app = start_app()
app.add_middleware(LogMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apis.router)
