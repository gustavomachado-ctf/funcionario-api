import uvicorn

from api.asgi import app


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", reload=True)


if __name__ == "__main__":
    main()
