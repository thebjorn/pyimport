
from setuptools import setup

setup(
    name='pyimport',
    version='0.1',
    description='pyimport',
    url='https://github.com/thebjorn/pyimport.git,
    author='thebjorn',
    license='MIT',
    packages=['src'],
    entry_points={
        'console_scripts': """
            do_daily = src.do_daily:do_daily_fn
        """
    },
    zip_safe=False
)
