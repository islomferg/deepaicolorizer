from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='deepaicolorizer',
    version='0.0.1',
    author='Islomferg',
    packages=['colorizer'],
    description='Colorizer your bw photos',
    zip_safe=False,
    author_email='usfvouhd@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/islomferg/deepaicolorizer',
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)