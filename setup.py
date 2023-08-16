from setuptools import setup, find_packages

setup(
    name="lambchop",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "colorama",
        "requests",
        "tweepy"
    ],
    entry_points={
        "console_scripts": [
            "lambchop=lambchop.__main__:main",
        ],
    },
    author="be0vlk",
    description="Create realistic user profiles for Read Team, OSINT, and testing using OpenAI's ChatGPT and DALL-E APIs.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/be0vlk/lambchop",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    python_requires=">=3.10",
)
