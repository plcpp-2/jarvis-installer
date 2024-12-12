import platform
import subprocess
import sys

def check_dependencies():
    """Check system dependencies"""
    dependencies = {
        'Windows': ['powershell', 'git'],
        'Linux': ['apt', 'git'],
        'Darwin': ['brew', 'git']
    }
    
    system = platform.system()
    missing_deps = []
    
    for dep in dependencies.get(system, []):
        if not is_command_available(dep):
            missing_deps.append(dep)
    
    return len(missing_deps) == 0

def is_command_available(command):
    """Check if a command is available"""
    try:
        subprocess.run([command, '--version'], 
                       stdout=subprocess.DEVNULL, 
                       stderr=subprocess.DEVNULL, 
                       check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_dependencies():
    """Install system dependencies"""
    system = platform.system()
    
    dependency_installers = {
        'Windows': install_windows_dependencies,
        'Linux': install_linux_dependencies,
        'Darwin': install_mac_dependencies
    }
    
    installer = dependency_installers.get(system)
    if installer:
        installer()
    else:
        print(f"Unsupported operating system: {system}")
        sys.exit(1)

def install_windows_dependencies():
    """Install dependencies on Windows"""
    print("Installing Windows dependencies...")
    try:
        # Check and install Chocolatey if not present
        subprocess.run(['powershell', '-Command', 
                        'Set-ExecutionPolicy Bypass -Scope Process -Force; ' +
                        '[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; ' +
                        'iex ((New-Object System.Net.WebClient).DownloadString("https://community.chocolatey.org/install.ps1"))'], 
                       check=True)
        
        # Install Git and other dependencies
        subprocess.run(['choco', 'install', 'git', '-y'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def install_linux_dependencies():
    """Install dependencies on Linux"""
    print("Installing Linux dependencies...")
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def install_mac_dependencies():
    """Install dependencies on macOS"""
    print("Installing macOS dependencies...")
    try:
        subprocess.run(['brew', 'update'], check=True)
        subprocess.run(['brew', 'install', 'git'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def get_python_dependencies():
    """Return core Python package dependencies"""
    return [
        'dynaconf',
        'azure-identity',
        'openai',
        'langchain',
        'fastapi',
        'uvicorn',
        'pydantic'
    ]
