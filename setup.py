import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='recast',
    version='0.1.0',
    author='Phil Dreizen,Miccah Castorina',
    author_email='dreizen@kupad.net,m.castorina93@gmail.com',
    description='python bit recaster',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kupad/recast',
    project_urls={
        'Bug Tracker': 'https://github.com/kupad/recast/issues',
    },
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
