import setuptools

with open('README.md', 'r') as in_:
    long_description = in_.read()

setuptools.setup(
    name='deploynow',
    version='1.0.0',
    author='Anushka Yohan',
    author_email='anushka.yohan@pearson.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnushkaYohan/code-deploy-now',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"
                 ],
    scripts=['deploynow']
)
