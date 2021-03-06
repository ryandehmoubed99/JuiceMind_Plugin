from setuptools import setup

setup (
        name="thonny-JuiceMind",
        version="1.0.0",
        description="Enhanced JuiceMind features for Thonny",
        long_description="""JuiceMind plug-in which adds JuiceMind theme, automatic polling for ESP32 connection, and easy switching between computer and ESP32.
More info about JuiceMind: www.JuiceMind.com.""",
        url="https://github.com/ryandehmoubed99/thonny-JuiceMind",
        #download_url="https://github.com/ryandehmoubed99/thonny-JuiceMind/archive/v0.0.8.tar.gz",
        author="Ryan Dehmoubed",
        author_email="r.dehmoubed99@gmail.com",
        license="MIT",
        classifiers=[
          "Environment :: MacOS X",
          "Environment :: Win32 (MS Windows)",
          "Environment :: X11 Applications",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: End Users/Desktop",
          "License :: Freeware",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: MacOS",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: POSIX",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Topic :: Education",
          "Topic :: Software Development",
          "Topic :: Software Development :: Embedded Systems",
        ],
        keywords="IDE education programming  Thonny JuiceMind",
        platforms=["Windows", "macOS", "Linux"],
        requires_dist=["thonny (>=3.2.1)"],
        python_requires=">=3.5",
        package_data={'thonnycontrib.JuiceMind': ['res/*']},
        install_requires=["thonny >= 3.2.1"],
        include_package_date = True,
        packages=["thonnycontrib.JuiceMind"],
)
