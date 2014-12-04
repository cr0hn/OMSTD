import os

from distutils.core import setup

_required = []
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "omstd_bh_001/requirements.txt")) as f:
    _required = f.read().splitlines()
_required = list(filter(None, _required))  # Remove empty values

setup(
    name='OMSTD-BH-001',
    version='0.1',
    packages=['omstd_bh_001', 'omstd_bh_001.framework', 'omstd_bh_001.framework.tasks'],
    url='http://omstd.readthedocs.org/develop/behavior.html',
    license='BSD',
    entry_points={
        'console_scripts': [
            'omstd-bh-001 = omstd_bh_001.start:main',
            ],
        },
    package_data={'omstd_bh_001': ['requirements.txt']},
    install_requires=_required,
    author='cr0hn',
    author_email='cr0hn<-at->cr0hn.com',
    description='OMSTD BH-001 study case: Basic structure to working with Celery framework and taskes.',
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
