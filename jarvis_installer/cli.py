import click
import sys
import os
import subprocess
import platform

from .dependency_manager import check_dependencies, install_dependencies
from .environment_setup import create_virtual_environment
from .system_checks import validate_system_requirements

@click.group()
def main():
    """Jarvis AI Assistant Installer"""
    pass

@main.command()
@click.option('--python-version', default=f"{sys.version_info.major}.{sys.version_info.minor}", help='Python version to use')
@click.option('--venv-path', default='jarvis_venv', help='Path to create virtual environment')
def install(python_version, venv_path):
    """Install Jarvis AI Assistant"""
    click.echo("🚀 Starting Jarvis AI Assistant Installation")

    # System Requirements Check
    if not validate_system_requirements():
        click.echo("❌ System does not meet minimum requirements.")
        sys.exit(1)

    # Check and Install System Dependencies
    if not check_dependencies():
        click.confirm("Some dependencies are missing. Do you want to install them?", abort=True)
        install_dependencies()

    # Create Virtual Environment
    venv_path = os.path.abspath(venv_path)
    if create_virtual_environment(venv_path, python_version):
        click.echo(f"✅ Virtual environment created at {venv_path}")

        # Activate Virtual Environment and Install Jarvis
        activate_script = os.path.join(venv_path, 'Scripts' if platform.system() == 'Windows' else 'bin', 'activate')
        pip_path = os.path.join(venv_path, 'Scripts' if platform.system() == 'Windows' else 'bin', 'pip')
        
        install_commands = [
            f"{pip_path} install --upgrade pip",
            f"{pip_path} install jarvis-installer jarvis-core"
        ]

        for cmd in install_commands:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                click.echo(f"❌ Installation failed: {result.stderr}")
                sys.exit(1)

        click.echo("🎉 Jarvis AI Assistant successfully installed!")
    else:
        click.echo("❌ Failed to create virtual environment.")
        sys.exit(1)

@main.command()
def update():
    """Update Jarvis AI Assistant"""
    click.echo("🔄 Updating Jarvis AI Assistant")
    # Implement update logic

@main.command()
def uninstall():
    """Uninstall Jarvis AI Assistant"""
    click.echo("🗑️ Uninstalling Jarvis AI Assistant")
    # Implement uninstall logic

if __name__ == '__main__':
    main()
