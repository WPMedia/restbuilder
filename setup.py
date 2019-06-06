# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Sphinx_ extension to build reST (reStructuredText_) files.

This extension is in particular useful to use in combination with the autodoc
extension to automatically generate documentation for use by any rst parser
(such as the GitHub wiki).

In itself, the extension is fairly straightforward -- it takes the parsed reST 
file from Sphinx_ and outputs it as reST.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
'''

requires = ['Sphinx>=1.0']

setup(
    name='wapo-restbuilder',
    version='0.0.1',
    url='https://github.com/WPMedia/restbuilder',
    author='Arc Professional Services Team',
    description='Sphinx extension to output reST files.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
