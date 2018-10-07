from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='microsoft-dynamics-auth',
    description='Microsoft Dynamics 365 authentication plugin for HTTPie.',
    long_description=open('README.md').read().strip(),
    version='0.0.2',
    author='Roshan Gautam',
    author_email='roshan.gautam@hotmail.com',
    license='MIT',
    url='https://github.com/roshangautam/microsoft-dynamics-auth',
    download_url='https://github.com/roshangautam/microsoft-dynamics-auth',
    py_modules=['microsoft-dynamics-auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'microsoft-dynamics-auth = auth:MsftDynamicsAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.9.9',
        'adal>=1.1.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
