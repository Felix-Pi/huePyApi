import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huePyApi-Felix-Pi",
    version="0.0.1",
    author="Felix Pieschka",
    author_email="felix@felixpi.de",
    description="Python module for controlling Philips Hue lights, groups, scenes and sensors by using the Hue rest API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Felix-Pi/huePyApi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.5',
)