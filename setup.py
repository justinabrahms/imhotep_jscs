from setuptools import setup, find_packages

setup(
    name='imhotep_jscs',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/justinabrahms/imhotep_jscs',
    license='MIT',
    author='Justin Abrahms',
    author_email='justin@abrah.ms',
    description='An imhotep plugin for jscs validation',
    test_suite="imhotep_jscs",
    entry_points={
        'imhotep_linters': [
            '.js = imhotep_jscs.plugin:JSCS'
        ],
    },
)
