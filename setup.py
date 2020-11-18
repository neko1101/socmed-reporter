from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="socmed-reporter",
    version="0.0.2",
    description="Social media tool",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/neko1101/socmed-reporter",
    author="Neko1101",
    author_email="fizdotcom@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["socmed_reporter"],
    include_package_data=True,
    install_requires=[
            "beautifulsoup4==4.9.3",
            "bs4==0.0.1",
            "collection==0.1.6",
            "google==3.0.0",
            "soupsieve==2.0.1",
        ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },
)