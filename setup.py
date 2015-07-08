from setuptools import setup, find_packages, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name='imhotep_jscs',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/justinabrahms/imhotep_jscs',
    license='MIT',
    install_requires=['imhotep>=0.4.0'],
    tests_require=['mock', 'pytest'],
    author='Justin Abrahms',
    author_email='justin@abrah.ms',
    description='An imhotep plugin for jscs validation',
    entry_points={
        'imhotep_linters': [
            '.js = imhotep_jscs.plugin:JSCS'
        ],
    },
    cmdclass={'test': PyTest},
)
