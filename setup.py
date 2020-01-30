from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30830",
      url="",
      author="Sachin Soman",
      author_email="sachin.soman@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
        }
      )

print("Fred")
