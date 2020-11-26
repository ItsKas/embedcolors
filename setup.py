import setuptools
import embedtools

with open("README.md", "r") as fh:
    long_description = fh.read()

# python setup.py bdist_wheel --universal (BUILD)
# python -m twine upload dist/* (UPDATE)

setuptools.setup(
    name="embedtools",  # Replace with your own username
    version=embedtools.__version__,
    author="Lukas Canter",
    author_email="lilcanter07@gmail.com",
    description="Embed tools package for discord.py embeds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItsKas/embedcolors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
