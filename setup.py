from setuptools import setup

# before loosening requirements it should be tested first

install_requires = [
    'djangorestframework==3.7.7',
]

setup(
    name="django-admin-webapi",
    version="0.1",
    license='UNLINCENSE',
    description="Admin WebAPI based on Django Rest Framework",
    author='Daniel Boczek',
    packages=['admin_webapi'],
    package_dir={'': '.'},
    install_requires=install_requires,
    zip_safe=False,
)
