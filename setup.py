import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
    README = ''
    CHANGES = ''

setup(
    name='Flask-DebugToolbar-LineProfilerPanel',
    description="Panel for the Flask Debug toolbar to capture and view line-by-line profiling stats",
    version='0.0.1',
    url='https://github.com/phleet/flask_debugtoolbar_line_profiler_panel',

    author='Jamie Wong',
    author_email='jamie.lf.wong@gmail.com',
    long_description=README + '\n\n' + CHANGES,
    license='MIT',

    packages=(
        'flask_debugtoolbar_line_profiler_panel',
    ),
    package_data={'': [
        'templates/flask_debugtoolbar_line_profiler_panel/*',
    ]},
    install_requires=[
        'Flask-DebugToolbar>=0.7.1'
        'line-profiler>=1.0b3',
    ]
)