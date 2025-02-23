import os
import subprocess
import sys
from pathlib import Path
import shutil
import stat

# Get the current script's directory and go up one level to the setup directory
setup_dir = Path(__file__).parent.parent

# Define GitHub repository URLs
REPOSITORIES = {
    "web-app": "https://github.com/BetterGR/betterGR-web-app.git",
    "api-gateway": "https://github.com/BetterGR/api-gateway.git",
    "keycloak": "https://github.com/BetterGR/keycloak-instance.git",
    "homework": "https://github.com/BetterGR/homework-microservice.git",
    "students": "https://github.com/BetterGR/students-microservice.git",
    "courses": "https://github.com/BetterGR/course-microservice.git",
    "staff": "https://github.com/BetterGR/staff-microservice.git",
    "grades": "https://github.com/BetterGR/grades-microservice.git"
}

def check_prerequisites():
    """Check if required tools are installed"""
    requirements = ['git', 'docker', 'docker-compose']
    
    for tool in requirements:
        if shutil.which(tool) is None:
            print(f"Error: {tool} is not installed")
            sys.exit(1)

def clone_repositories():
    """Clone all required repositories"""
    services_dir = setup_dir / "services"
    services_dir.mkdir(exist_ok=True)
    os.chdir(str(services_dir))
    
    for name, url in REPOSITORIES.items():
        if not os.path.exists(name):
            print(f"Cloning {name}...")
            subprocess.run(["git", "clone", url, name], check=True)
        else:
            print(f"{name} directory already exists, pulling latest changes...")
            os.chdir(name)
            subprocess.run(["git", "pull"], check=True)
            os.chdir("..")

def setup_environment():
    """Setup environment variables"""
    if not os.path.exists(setup_dir / ".env"):
        shutil.copy(setup_dir / ".env.example", setup_dir / ".env")
        print("Created .env file from template. Please update with your configurations.")

def start_services():
    """Start all services using docker-compose"""
    try:
        os.chdir(str(setup_dir))  # Change back to setup directory
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("All services started successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error starting services: {e}")
        sys.exit(1)

def clean():
    """Clean up all services and Docker resources"""
    print("Cleaning up...")
    
    # Stop and remove all Docker containers
    try:
        os.chdir(str(setup_dir))
        subprocess.run(["docker-compose", "down", "-v"], check=True)
    except subprocess.CalledProcessError:
        print("Warning: Error stopping Docker containers")
    
    # Remove services directory
    services_dir = setup_dir / "services"
    if services_dir.exists():
        print("Removing services directory...")
        shutil.rmtree(str(services_dir))
    
    # Remove .env file
    env_file = setup_dir / ".env"
    if env_file.exists():
        print("Removing .env file...")
        env_file.unlink()
    
    print("Cleanup completed!")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean()
        return
        
    print("Starting BetterGR setup...")
    
    check_prerequisites()
    clone_repositories()
    setup_environment()
    start_services()
    
    print("""
Setup completed!
Access points:
- Web App: http://localhost:3000
- Keycloak: http://localhost:8080
- API Gateway: http://localhost:1234
    """)

if __name__ == "__main__":
    main()
