import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="jukebox",
    py_modules=["jukebox"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)
python jukebox/sample.py --model=5b_lyrics --name=yeniden_baslasin_nu_disco --lyrics="Ajda Pekkan yeniden başlasın" --genre="nu-disco" --levels=3 --sample_length_in_seconds=30 --total_sample_length_in_seconds=180 --sr=44100
