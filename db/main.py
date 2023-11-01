from fastapi import FastAPI

from routers import (
    appointment,
    agent,
    client,
    event,
)
import uvicorn
import os


def create_app():
    app = FastAPI()

    app.include_router(appointment.router)
    app.include_router(agent.router)
    app.include_router(client.router)
    app.include_router(event.router)

    return app


app = create_app()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT")), reload=True)
