import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoomy",
    version="0.5",
    author="Kewbish",
    author_email="kewbish@gmail.com",
    description="A Zoom utility for the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kewbish/zoomy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Education"
    ],
    entry_points='''
        [console_scripts]
        zmy=zoomy.zoomy:zoomy
    '''
)
