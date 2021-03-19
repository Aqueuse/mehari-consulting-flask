import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:fastapp", host="95.142.160.136", port=3002, reload=True)
