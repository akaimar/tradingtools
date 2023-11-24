from setuptools import setup

APP = ['main_app.py']  # Replace with the name of your main python script
DATA_FILES = []  # Any additional data files
OPTIONS = {
    'argv_emulation': True,
    'packages': ['dearpygui'],  # Add any additional packages used
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)