from setuptools import setup, find_packages

setup(
    name="stack_analyzer",
    version="0.1.1",
    author="dimeloper",
    author_email="dkiriakakis@gmail.com",
    description="A library to analyze GitHub repositories and determine their tech stack.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/warestack/stack-analyzer",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "python-dotenv>=0.19.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
