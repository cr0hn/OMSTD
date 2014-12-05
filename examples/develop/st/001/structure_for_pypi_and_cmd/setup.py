import os

from setuptools import setup, find_packages

_required = []

try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt")) as f:
        _required = f.read().splitlines()
    _required = list(filter(None, _required))  # Remove empty values
except IOError:
    print("requirements.txt file not found")

setup(
    name='PROGRAM_NAME',  # TODO
    version='0.1.2',  # TODO
    packages=find_packages(),
    url='https://YOUR_SITE',  # TODO
    license='BSD',
    install_required=_required,
    entry_points={
        'console_scripts': [
            # 'your-binary-name = your_package.main:main',  # TODO
            'omstd-st-001 = omstd_st_001.st_001:main',
            ],
    },
    author='YOU',  # TODO
    author_email='YOUR@MAIL.COM',  # TODO
    description='DESCRIPTION',  # TODO
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        ],
)

