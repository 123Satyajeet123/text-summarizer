import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.1"
REPO_NAME = "text-summarizer"
AUTH_NAME = "Satyajeet"
SRC_REPO = "Text-Summarizer"

setuptools.setup(
    name=f"{REPO_NAME}-{AUTH_NAME}",
    version=version,
    author=AUTH_NAME,
    author_email="satyajeetdas225@gmail.com",
    description="A small package for text summarization",
    long_description=long_description,
)