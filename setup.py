from setuptools import setup, find_packages

with open('README.md', 'r') as in_:
    long_description = in_.read()

setuptools.setup(
    name='deploynow',
    author='Anushka Yohan',
    author_email='anushka.yohan@pearson.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnushkaYohan/code-deploy-now',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"
    ],
    install_requires=['boto3'],
    scripts=['deploynow']
    packages=find_packages(),
    include_package_data=True,
    version="1.5.0",
)