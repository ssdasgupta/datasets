from setuptools import setup, find_packages

install_requires =['cachetools==3.1.1','allennlp>=0.9.0',
 'certifi==2019.9.11',
 'chardet==3.0.4',
 'filelock==3.0.12',
 'gdown==3.8.3',
 'google-api-python-client==1.7.11',
 'google-auth==1.6.3',
 'google-auth-httplib2==0.0.3',
 'httplib2==0.14.0',
 'idna==2.8',
 'nlp_utils @ git+https://github.com/dhruvdcoder/nlp-utils.git',
 'numpy==1.17.2',
 'oauth2client==4.1.3',
 'pyasn1==0.4.7',
 'pyasn1-modules==0.2.6',
 'PyDrive==1.3.1',
 'PyYAML==5.1.2',
 'requests==2.22.0',
 'rsa==4.0',
 'six==1.12.0',
 'torch>=1.2.0',
 'torchtext==0.4.0',
 'tqdm==4.36.1',
 'uritemplate==3.0.0',
 'urllib3==1.25.6']

setup(
    name='datasets',
    version='0.0.1',
    description='AllenNLP style data pipeline for KB Completion',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'datasets': ['py.typed']},
    install_requires=install_requires,
    zip_safe=False)
