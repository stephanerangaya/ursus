from setuptools import setup

setup(
    name='ursus',
    version='0.1',
    description='Static site generator',
    url='http://github.com/nicbou/ursus',
    author='Nicolas Bouliane',
    author_email='contact@nicolasbouliane.com',
    license='MIT',
    packages=['ursus'],
    scripts=['bin/ursus'],
    python_requires='>=3.10',
    install_requires=[
        'coloredlogs==15.0.1',
        'Jinja2==3.1.2',
        'Markdown==3.4.1',
        'MarkupSafe==2.1.1',
        'mdx_wikilink_plus==1.4.1',
        'ordered-set==4.1.0',
        'PyMuPDF==1.21.1',
        'Pillow==9.4.0',  # Pillow-simd is much faster, but requires binaries to be installed separately.
        'watchdog==2.2.1',
    ],
    zip_safe=False,
)
