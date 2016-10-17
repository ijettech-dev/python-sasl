#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from setuptools import setup, Extension

sasl_module = Extension('_saslwrapper',
                           sources=['saslwrapper/saslwrapper.cpp', "saslwrapper/saslwrapper_wrap.cxx"],
                           include_dirs=["saslwrapper"],
                           libraries=["sasl2"],
                           language="c++",
                           )
dist = setup (name = 'saslwrapper',
       version = '0.1.3',
       url = "https://github.com/ijettech-dev/python-sasl/tree/master",
       maintainer = "iJet Technologies",
       maintainer_email = "qa@ijettechnologies.com",
       description = """Cyrus-SASL bindings for Python forked from https://github.com/toddlipcon/python-sasl""",
       ext_modules = [sasl_module],
       py_modules = ["saslwrapper.saslwrapper"],
       include_package_data = True,
       )

