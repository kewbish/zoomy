import setuptools

setuptools.setup(
    name="zoomy",
    version="0.1",
    author="Kewbish",
    author_email="kewbish@gmail.com",
    description="A Zoom utility for the terminal",
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
        zoomy=zoomy.zoomy:zoomy
    ''',
    python_requires='>=3.6',
)
