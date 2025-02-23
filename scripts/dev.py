import os
import subprocess
import sys
from typing import List, Dict
import signal
import time

# Define commands to run services in development mode
# Note: These run directly on the host machine, not in containers
SERVICES = {
    "web-app": "npm run dev",  # Runs Next.js with hot-reload
    "api-gateway": "go run cmd/api-gateway/main.go",  # Runs Go service directly
    "homework": "go run server/main.go",
    "students": "go run server/main.go",
    "courses": "go run server/main.go",
    "staff": "go run server/main.go",
    "grades": "go run server/main.go"
}

# Store running processes for management
processes = {}

def load_env():
    """Load environment variables from .env file"""
    if not os.path.exists(".env"):
        print("Error: .env file not found. Run setup.py first.")
        sys.exit(1)
    
    with open(".env") as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

def start_service(name: str, command: str):
    """
    Start a service in development mode
    Unlike setup.py which uses Docker, this runs services directly
    enabling faster development cycles and easier debugging
    """
    try:
        # Run process in the background with output visible
        process = subprocess.Popen(
            command.split(),
            cwd=f"services/{name}",
            env=os.environ.copy()
        )
        processes[name] = process
        print(f"Started {name} in development mode")
    except Exception as e:
        print(f"Error starting {name}: {e}")

def stop_all_services():
    """
    Gracefully stop all running services
    This is important for development to ensure proper cleanup
    """
    for name, process in processes.items():
        print(f"Stopping {name}...")
        process.terminate()
    
    # Give processes time to terminate gracefully
    time.sleep(2)
    
    # Force kill any remaining processes
    for name, process in processes.items():
        if process.poll() is None:
            process.kill()

def signal_handler(sig, frame):
    """
    Handle Ctrl+C gracefully
    This ensures all services are properly stopped
    """
    print("\nStopping all development services...")
    stop_all_services()
    sys.exit(0)

def main():
    print("Starting services in development mode...")
    
    # Ensure environment is set up
    load_env()
    
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start all services in development mode
    for name, command in SERVICES.items():
        start_service(name, command)
    
    print("\nAll services started in development mode. Press Ctrl+C to stop.")
    print("\nAccess points:")
    print("- Web App: http://localhost:3000")
    print("- API Gateway: http://localhost:1234")
    print("- Keycloak: http://localhost:8080")
    
    # Keep the script running and monitoring services
    while True:
        # Check if any service has crashed
        for name, process in processes.items():
            if process.poll() is not None:
                print(f"\nWarning: {name} has stopped. Exit code: {process.poll()}")
        time.sleep(1)

if __name__ == "__main__":
    main() 