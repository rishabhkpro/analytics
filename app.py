from fastapi import FastAPI
import apis


def start_app():

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


app.include_router(apis.router)
