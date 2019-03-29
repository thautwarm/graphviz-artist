from setuptools import setup, find_packages

with open('README.rst', 'r') as readme:
    readme = readme.read()


setup(
    name='graphviz-artist',
    version='0.1.2beta1',
    keywords="graphviz, graph-drawing, dsl", # keywords of your project that separated by comma ","
    description="A chance to focus on graph drawing itself, forget APIs and other stuffs.", # a conceise introduction of your project
    long_description=readme,
    license='mit',
    url='https://github.com/thautwarm/graphviz-artist',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=['graphviz_artist'],
    entry_points={"console_scripts": []},
    # above option specifies commands to be installed,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd.compiler"]}
    install_requires=["graphviz", "typing"],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
