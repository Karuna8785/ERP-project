"""
SmartERP Enterprise Platform Launcher & Entry Point
"""
import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

try:
    from app.main import app
except ImportError:
    from backend.app.main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"Starting SmartERP Enterprise Platform on {host}:{port}...")
    uvicorn.run("backend.app.main:app" if os.path.exists("backend") else "app.main:app", host=host, port=port, reload=False)
