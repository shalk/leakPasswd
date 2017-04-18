import leakPasswd

from distutils.core import setup

setup(
    name="leakPasswd",
    version=leakPasswd.__version__,
    packages=["leakPasswd"],
    package_dir={"leakPasswd": "leakPasswd"},
    description="This is the password leak query module",
    author="lauix",
    author_email="lauixData@gmail.com",
    url="https://github.com/lauixData/leakPasswd",
)
