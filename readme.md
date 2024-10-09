
# BlogApp

This project to add the different blogs publishing over the internet

## Installation

Clone the project

```bash
  git clone krishna13052001/blogApp.git
```

Install python dependencies 

```bash
  pip install -r requirements.txt
``` 

Run the application
```bash
    uvicorn main:app --reload
```

In the above command main the file name, where ```FastAPI``` is initialized and app is the instance of FastAPI

Hear ```uvicorn``` acts as web server for the FastAPI application

Or running the application using the FastAPI command
Production Mode:
```bash
    fastapi run main.py
```
Development Mode:
```bash
    fastapi dev main.py
```