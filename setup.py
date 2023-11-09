import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enhanced-plt-utils",
    version="0.0.1",
    author="Hamza",
    description="Package with basic some ploting utilities",
    url="https://github.com/BabaSanfour/plots-utils",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)