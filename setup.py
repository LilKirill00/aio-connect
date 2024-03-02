from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='aio-1c-connect',
    version='0.0.2',
    author='LilKirill00',
    author_email='pc.browsers.1@gmail.com',
    description='This is a library for creating bots in the 1C-Connect environment',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/LilKirill00/aio-connect',
    packages=find_packages(),
    install_requires=[
        "magic-filter>=1.0.12,<1.1",
        "aiofiles~=23.2.1",
        'aiohttp~=3.9.0',
        'pydantic>=2.4.1,<2.6'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: AsyncIO",
        "Typing :: Typed",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
    ],
    keywords='1C-Connect',
    project_urls={
        'GitHub': 'https://github.com/LilKirill00/aio-connect'
    },
    python_requires='>=3.8'
)
