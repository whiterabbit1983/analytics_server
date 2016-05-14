import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages


setup(
    name="analytics-server",
    version="0.1.0",
    author="Dmitry A. Paramonov",
    author_email="asmatic075@gmail.com",
    entry_points = {
        'console_scripts': [
            'analytics_server = analytics_server.scripts.analytics_server:run'
        ],
        'setuptools.installation': [
            'eggsecutable = analytics_server.scripts.analytics_server:run',
        ]
    },
    packages=find_packages(
        exclude=[
            "*test*",
            "*build*",
            "*__pycache__*"
        ]
    ),
    include_package_data=True,
    description="Analytics server"
)
