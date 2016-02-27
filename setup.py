"""
labnote - HTML lab notebook generator
"""
DOCLINES = __doc__.split("\n")

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]

setup(
    author="Keith Hughitt",
    author_email="khughitt@umd.edu",
    classifiers=CLASSIFIERS,
    description=DOCLINES[0],
    install_requires=['beautifulsoup4', 'jinja2', 'PyYAML', 'setuptools-git'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    license="BSD",
    long_description="\n".join(DOCLINES[2:]),
    maintainer="Keith Hughitt",
    maintainer_email="khughitt@umd.edu",
    name="labnote",
    packages=find_packages(),
    platforms=["Linux", "Solaris", "Mac OS-X", "Unix"],
    provides=['labnote'],
    scripts=['bin/labnote'],
    zip_safe=False,
    url="https://github.com/khughitt/labnote",
    download_url="https://github.com/khughitt/labnote/tarball/0.6",
    version="0.6"
)

