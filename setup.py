from setuptools import setup

setup(
    name='tea-xyz1',
    version='1.0.1',
    description='A simple package for https://app.tea.xyz/',
    url='https://github.com/madest92/tea-xyz1',
    project_urls={
        'Homepage': 'https://github.com/madest92/tea-xyz1',
    },
    py_modules=['hello_tea'],
    entry_points={
        'console_scripts': [
            'hello-tea=hello_tea:hello_tea_func'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
