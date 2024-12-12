from setuptools import setup, find_packages

setup(
    name='jarvis-installer',
    version='0.1.0',
    packages=find_packages(),
    description='Jarvis AI Assistant Installer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jarvis Development Team',
    author_email='dev@jarvis-assistant.com',
    url='https://github.com/plcpp-2/jarvis-assistant',
    install_requires=[
        'click>=8.0.0',
        'virtualenv>=20.13.0',
        'psutil>=5.9.0',
        'requests>=2.27.0',
    ],
    entry_points={
        'console_scripts': [
            'jarvis-install=jarvis_installer.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
)
