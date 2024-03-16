from setuptools import setup, find_packages

setup(
    name='injury_data_regression',
    version='0.0.1',
    author='Nathan Schaaf',
    author_email='nathan.rocky.schaaf@gmail.com',
    packages=find_packages(),
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NRSchaaf/injury_data_regression.git',
    license='none',
    #classifiers=[
    #    'Development Status :: 3 - Alpha',
    #    'Intended Audience :: Developers',
    #    'License :: OSI Approved :: MIT License',
    #    'Programming Language :: Python :: 3',
    #    'Programming Language :: Python :: 3.6',
    #    'Programming Language :: Python :: 3.7',
    #    'Programming Language :: Python :: 3.8',
    #    'Programming Language :: Python :: 3.9',
    #], 
   
    install_requires=[ 
        'pandas', 'numpy', 'seaborn'
    ],
    #python_requires='>=3.6',
)