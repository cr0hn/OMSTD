from distutils.core import setup
setup(
    name='OMSTD-ch-001',
    version='0.1',
    packages=['omstd_ch_001', 'omstd_ch_001.lib'],
    url='http://omstd.readthedocs.org/cracking/ch_001.html',
    license='BSD',
    entry_points={
        'console_scripts': [
            'omstd-ch-001 = omstd_ch_001.ch_001:main',
            ],
    },
    author='cr0hn',
    author_email='cr0hn<-at->cr0hn.com',
    description='OMSTD CH-001 study case: cracking MD5 password using online resolver services.',
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

