import os
import sys
import subprocess
import platform
import venv

def create_virtual_environment(venv_path, python_version=None):
    """
    Create a virtual environment for Jarvis AI Assistant
    
    Args:
        venv_path (str): Path to create virtual environment
        python_version (str, optional): Specific Python version to use
    
    Returns:
        bool: True if virtual environment created successfully
    """
    try:
        # Ensure the directory exists
        os.makedirs(venv_path, exist_ok=True)
        
        # Create virtual environment
        venv.create(venv_path, with_pip=True)
        
        # Determine pip path based on platform
        if platform.system() == 'Windows':
            pip_path = os.path.join(venv_path, 'Scripts', 'pip')
        else:
            pip_path = os.path.join(venv_path, 'bin', 'pip')
        
        # Upgrade pip
        subprocess.run([pip_path, 'install', '--upgrade', 'pip'], check=True)
        
        return True
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        return False

def activate_virtual_environment(venv_path):
    """
    Activate the virtual environment
    
    Args:
        venv_path (str): Path to virtual environment
    """
    if platform.system() == 'Windows':
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        subprocess.run([activate_script], shell=True, check=True)
    else:
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        subprocess.run(['source', activate_script], shell=True, check=True)

def install_requirements(venv_path, requirements_file=None):
    """
    Install requirements in the virtual environment
    
    Args:
        venv_path (str): Path to virtual environment
        requirements_file (str, optional): Path to requirements file
    
    Returns:
        bool: True if requirements installed successfully
    """
    try:
        # Determine pip path based on platform
        if platform.system() == 'Windows':
            pip_path = os.path.join(venv_path, 'Scripts', 'pip')
        else:
            pip_path = os.path.join(venv_path, 'bin', 'pip')
        
        # Install requirements
        if requirements_file and os.path.exists(requirements_file):
            subprocess.run([pip_path, 'install', '-r', requirements_file], check=True)
        else:
            # Install core dependencies
            subprocess.run([pip_path, 'install', 'jarvis-core'], check=True)
        
        return True
    except Exception as e:
        print(f"Error installing requirements: {e}")
        return False
