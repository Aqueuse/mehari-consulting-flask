import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:fastapp", host="mehari-consulting.com", port=3002, reload=True)
