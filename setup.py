import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='plbdays',
    version='0.0.1',
    author='Robert Zawadzki',
    author_email='r.zawadzki96@gmail.com',
    description='Business days in Poland',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ZawadzkiR/plbays/',
    project_urls = {
        "Bug Tracker": "https://github.com/ZawadzkiR/plbays/issues"
    },
    license='MIT',
    packages=['plbdays'],
    install_requires=['datetime'],
)