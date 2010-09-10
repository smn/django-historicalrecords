from setuptools import setup, find_packages

setup(
    name = "django-historicalrecords",
    version = "0.1",
    url = 'http://github.com/smn/django-historicalrecords',
    description = "Marty Alchin's HistoricalRecords from the ProDjango book.",
    author = 'Marty Alchin',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['django',],
)

