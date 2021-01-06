import os
from distutils.core import setup
from setuptools.command.install import install
from shutil import copyfile

VERSION = '0.1.0'


local_path = os.path.dirname(__file__)
# Fix for tox which manipulates execution pathing
if not local_path:
    local_path = '.'
here = os.path.abspath(local_path)


# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def version():
    with open(here + '/ipypandex/_version.py', 'r') as ver:
        for line in ver.readlines():
            if line.startswith('version ='):
                return line.split(' = ')[-1].strip()[1:-1]
    raise ValueError('No version found in ipypandex/version.py')


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        try:
            from IPython.terminal.interactiveshell import TerminalInteractiveShell
            startup_dir = TerminalInteractiveShell.instance().get_ipython().profile_dir.startup_dir
            copyfile(
                os.path.join(here, 'ipypandex', '__init__.py'),
                os.path.join(startup_dir, '90-ipypandex.py'))
        except ModuleNotFoundError:
            raise RuntimeError("ipypandex requires an ipython installation to work")


setup(
    name='ipypandex',
    version=version(),
    description='A package for automatically turning on Data Explorer in Pandas for an IPython Jupyter kernel.',
    author='nteract contributors',
    author_email='nteract@googlegroups.com',
    license='BSD',
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='jupyter nteract notebook dataframe d3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nteract/ipypandex',
    packages=[],
    cmdclass={'install': PostInstallCommand},
    python_requires='>=3.6',
    install_requires=['pandas', 'ipython'],
    extras_require={
        'test': ['pytest'],
    },
    project_urls={
        'Funding': 'https://nteract.io',
        'Source': 'https://github.com/nteract/ipypandex/',
        'Tracker': 'https://github.com/nteract/ipypandex/issues',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
