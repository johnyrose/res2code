from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='res2code',
    version='0.1.0',
    author='John Rose',
    author_email='johnyrose@example.com',
    description='A CLI tool for applying code changes specified in a JSON file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/johnyrose/res2code',
    packages=find_packages(),
    install_requires=[
        'pydantic==2.8.2',
        'typer==0.12.3',
    ],
    entry_points={
        'console_scripts': [
            'res2code=res2code.cli:app',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
