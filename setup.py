#!/usr/bin/env python

from distutils.core import setup

setup(
        name='jupyter_extension_publish',
        version='0.1',
        description='jupyter extension for publish notebook',
        author='Keunhui Park',
        author_email='keunhui.park@gmail.com',
        packages=['jupyter_extension_publish'],
        include_package_data=True,
        )