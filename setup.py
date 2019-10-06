import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SealTeamTools",
    version="0.0.1",
    author="GDASL",
    author_email="author@example.com",
    description="Collection of CTF tools (WIP)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gdasl/STT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
