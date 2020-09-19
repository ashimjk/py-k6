import setuptools

setuptools.setup(
    name='gitter-pkg',
    version='1.0.0',
    author='Ashim Jung Khadka',
    author_email='ashim.jung.khadka@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['PyYAML', 'dataclasses-json', 'pyinstaller'],
    scripts=['scripts/gitting'],
    # entry_points={
    #     'console_scripts': [
    #         'gitting=gitter.entrypoint:main'
    #     ]
    # }
)
