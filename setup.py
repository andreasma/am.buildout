# -*- coding: utf-8 -*-
"""Installer for the collective.addons package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.md').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

setup(
    name='am.buildout',
    version='0.1.dev0',
    description="Plone buildout",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Buildout",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        ],
    keywords='Python Plone',
    author='Andreas Mantke',
    author_email='maand@gmx.de',
    url='https://github.com/andreasma/am.buildout',
    project_urls={
        'Source': 'https://github.com/andreasma/am.buildout',
        'Tracker': 'https://github.com/andreasma/am.buildout/issues',
        # 'Documentation':
        # 'https://collective.addons.readthedocs.io/en/latest/',
    },
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['am'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.addons.locales.update:update_locale
    """,
)
