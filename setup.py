from setuptools import setup, find_packages

version = '0.1'

setup(name='fluegelform',
      version=version,
      description="Dexterity-based form generator for Plone.",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        ],
      keywords='plone form ploneformgen dexterity',
      author='David Glick',
      author_email='dglick@gmail.com',
      url='http://github.com/davisagli/fluegelform',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.dexterity',
          'zope.interface',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
