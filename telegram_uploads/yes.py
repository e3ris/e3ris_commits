☞ BASH

• COMMAND:
pip install PyGithub 

• ERROR: 
WARNING: Ignoring invalid distribution -wh-idna (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-chardet (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-aiohttp (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-idna (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-chardet (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-aiohttp (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-idna (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-chardet (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-aiohttp (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-idna (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-chardet (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-aiohttp (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-idna (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-chardet (/usr/local/lib/python3.9/site-packages)
WARNING: Ignoring invalid distribution -wh-aiohttp (/usr/local/lib/python3.9/site-packages)

• OUTPUT:
Requirement already satisfied: PyGithub in /usr/local/lib/python3.9/site-packages (1.55)
Requirement already satisfied: deprecated in /usr/local/lib/python3.9/site-packages (from PyGithub) (1.2.12)
Requirement already satisfied: pynacl>=1.4.0 in /usr/local/lib/python3.9/site-packages (from PyGithub) (1.4.0)
Requirement already satisfied: requests>=2.14.0 in /usr/local/lib/python3.9/site-packages (from PyGithub) (2.25.1)
Requirement already satisfied: pyjwt>=2.0 in /usr/local/lib/python3.9/site-packages (from PyGithub) (2.1.0)
Requirement already satisfied: six in /usr/local/lib/python3.9/site-packages (from pynacl>=1.4.0->PyGithub) (1.16.0)
Requirement already satisfied: cffi>=1.4.1 in /usr/local/lib/python3.9/site-packages (from pynacl>=1.4.0->PyGithub) (1.14.5)
Requirement already satisfied: pycparser in /usr/local/lib/python3.9/site-packages (from cffi>=1.4.1->pynacl>=1.4.0->PyGithub) (2.20)
Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.9/site-packages (from requests>=2.14.0->PyGithub) (4.0.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/site-packages (from requests>=2.14.0->PyGithub) (1.26.5)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/site-packages (from requests>=2.14.0->PyGithub) (2021.5.30)
Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.9/site-packages (from requests>=2.14.0->PyGithub) (2.10)
Requirement already satisfied: wrapt<2,>=1.10 in /usr/local/lib/python3.9/site-packages (from deprecated->PyGithub) (1.12.1)