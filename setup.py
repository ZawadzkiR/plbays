from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]


setup(
    name='plbdays',
    version='1.1.1',
    author='Robert Zawadzki',
    author_email='r.zawadzki96@gmail.com',
    description='Business days in Poland',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/ZawadzkiR/plbays/',
    project_urls = {
        "Bug Tracker": "https://github.com/ZawadzkiR/plbays/issues"
    },
    License='MIT',
    packages=find_packages(),
    keywords = 'business days'
)
