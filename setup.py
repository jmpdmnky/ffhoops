import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# with open("version.txt", "r", encoding="utf-8-sig") as fh:
#     version = fh.read()
#     print(version)

setuptools.setup(
    name="ffhoops",
    version='0.0.3',#version,
    author="RW Hooper",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    #packages=setuptools.find_namespace_packages(include=['hoops.*'])
    python_requires=">=3.6",
)