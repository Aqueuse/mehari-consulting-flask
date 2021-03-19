import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:fastapp", host="127.0.0.1", port=5000, reload=True)
