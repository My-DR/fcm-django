#!/usr/bin/env python
import fcm_django

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = "3.0.0"

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name="fcm-django",
    packages=[
        "fcm_django",
        "fcm_django/api",
        "fcm_django/migrations",
    ],
    python_requires=">=2.7",
    install_requires=["msgpack==0.5.6", "firebase-admin==3.0.0", "Django"],
    author=fcm_django.__author__,
    author_email=fcm_django.__email__,
    classifiers=CLASSIFIERS,
    description="Send push notifications to mobile devices & browsers through "
    "FCM in Django.",
    long_description="",
    url="https://github.com/lisufoxu/fcm-django",
    version=VERSION,
)
