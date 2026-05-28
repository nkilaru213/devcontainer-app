# Python Flask Web App with Devcontainer

This is a small sample web application using Python Flask and a VS Code Dev Container.

## Run in VS Code Dev Containers

1. Install Docker Desktop.
2. Install the VS Code extension: **Dev Containers**.
3. Open this folder in VS Code.
4. Press `Cmd + Shift + P`.
5. Select **Dev Containers: Reopen in Container**.
6. Wait for dependencies to install.
7. Run:

```bash
python app.py
```

8. Open:

```text
http://localhost:5000
```

## API Endpoints

```text
GET  /api/health
GET  /api/tasks
POST /api/tasks
```

## Run without Devcontainer

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
