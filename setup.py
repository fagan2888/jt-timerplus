"""
@author Neo
@time 2018/11/06
"""

from setuptools import setup, find_packages

setup(
    name='jt.timerplus',
    version='0.1.1',
    description="timer plus",
    author='Neo',
    author_email='neo.lin@jaspercapital.com',
    python_requires='>=3.6', 
    packages=find_packages('src'),
    package_dir={"": "src"},
    package_data={
        'jt.timerplus': [
            'cfg/*.yaml'
        ]        
    },    
    install_requires=[
        'apscheduler',
        'jt'
    ],
    zip_safe=False,
)
