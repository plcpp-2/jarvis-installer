import platform
import psutil
import sys

def validate_system_requirements():
    """
    Validate system requirements for Jarvis AI Assistant
    
    Returns:
        bool: True if system meets requirements, False otherwise
    """
    checks = [
        check_python_version,
        check_memory,
        check_disk_space,
        check_cpu
    ]
    
    return all(check() for check in checks)

def check_python_version():
    """
    Check Python version compatibility
    
    Returns:
        bool: True if Python version is compatible
    """
    min_version = (3, 9)
    current_version = sys.version_info
    
    if current_version < min_version:
        print(f"❌ Unsupported Python version. Minimum required: {'.'.join(map(str, min_version))}")
        return False
    
    return True

def check_memory(min_ram_gb=8):
    """
    Check system memory
    
    Args:
        min_ram_gb (int): Minimum RAM required in GB
    
    Returns:
        bool: True if system has sufficient memory
    """
    total_ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    
    if total_ram < min_ram_gb:
        print(f"❌ Insufficient RAM. Minimum required: {min_ram_gb} GB")
        return False
    
    return True

def check_disk_space(min_space_gb=20):
    """
    Check available disk space
    
    Args:
        min_space_gb (int): Minimum disk space required in GB
    
    Returns:
        bool: True if sufficient disk space is available
    """
    disk_usage = psutil.disk_usage('/')
    available_space = disk_usage.free / (1024 ** 3)  # Convert to GB
    
    if available_space < min_space_gb:
        print(f"❌ Insufficient disk space. Minimum required: {min_space_gb} GB")
        return False
    
    return True

def check_cpu(min_cores=4):
    """
    Check CPU cores
    
    Args:
        min_cores (int): Minimum number of CPU cores required
    
    Returns:
        bool: True if system has sufficient CPU cores
    """
    cpu_count = psutil.cpu_count(logical=True)
    
    if cpu_count < min_cores:
        print(f"❌ Insufficient CPU cores. Minimum required: {min_cores}")
        return False
    
    return True

def get_system_info():
    """
    Retrieve comprehensive system information
    
    Returns:
        dict: System information details
    """
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
        "total_ram": psutil.virtual_memory().total / (1024 ** 3),
        "available_ram": psutil.virtual_memory().available / (1024 ** 3),
        "total_disk_space": psutil.disk_usage('/').total / (1024 ** 3),
        "available_disk_space": psutil.disk_usage('/').free / (1024 ** 3),
        "cpu_cores": psutil.cpu_count(logical=True),
        "cpu_frequency": psutil.cpu_freq().current
    }
