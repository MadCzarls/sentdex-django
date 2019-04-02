[WIP]

Repository created codeing-along with sentdex in:
https://www.youtube.com/watch?v=yD0_1DPmfKM

Some changes/additions made to this tutorial:
- added virtualenv - https://virtualenv.pypa.io/en/latest/
- moved all secret/custom/unique-per-workstation data to external file using python-decouple - check it here: https://pypi.org/project/django-decouple/

SETUP
In root directory create file '.env' (DOT-ENV) and put inside:
<file>
SECRET_KEY = <YOUR SECRET KEY> <-- get it from example here: https://www.miniwebtool.com/django-secret-key-generator/
DEBUG=<BOOLEAN IF DEBUG SHOULD BE ENABLED>
</file>
example file:

<file>
SECRET_KEY = 'k#gbxd4-(6nf_@lo=1$k_2$a%cqrs0^sio1nby7b6bu1n06rrq'
DEBUG=True
</file>


- use python from virtualenv in repository; to activate it run in root dir:
source sentdex-django/bin/activate

- to deactivate run:
deactivate