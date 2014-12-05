from distutils.core import setup
setup(
    name='OMSTD-hh-001',
    version='0.1.1',
    packages=['omstd_hh_001', 'omstd_hh_001.lib'],
    url='http://omstd.readthedocs.org/hacking/hh_001.html',
    license='BSD',
    entry_points={
        'console_scripts': [
            'omstd-hh-001 = omstd_hh_001.hh_001:main',
            ],
    },
    author='cr0hn',
    author_email='cr0hn<-at->cr0hn.com',
    description='OMSTD HH-001 study case: High performance TCP port scanner nmap friendly.',
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

