# Kirk Byers Free Python Course 2022
# Week 8, exercise 2
# Jaap de Vos
#
# ## 2A ## Create a new virtual environment on your system named 'test_venv'
# ## 2B ## Activate the virtual environment
# ## 2C ## Use 'which python' to see the path of the Python that you are using
# ## 2D ## Use 'pip list' to see the packages you have installed
# ## 2E ## Use pip to install Netmiko and the requests library
# ## 2F ## Use 'pip list' to see the updated list of installed packages
'''
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08 (week08)
$ mkdir venvs

jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08 (week08)
$ cd venvs/

jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ virtualenv test_env
created virtual environment CPython3.10.5.final.0-64 in 533ms

jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ source test_env/Scripts/activate

(test_env)
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ which python
/c/code/kirk-byers-free-python-course-2022/week08/venvs/test_env/Scripts/python

(test_env)
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ pip list
Package    Version
---------- -------
pip        22.2.1
setuptools 63.2.0
wheel      0.37.1

(test_env)
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ pip install netmiko
Collecting netmiko
  Using cached netmiko-4.1.1-py3-none-any.whl (192 kB)
Collecting paramiko>=2.7.2
  Using cached paramiko-2.11.0-py2.py3-none-any.whl (212 kB)
Collecting pyserial
  Using cached pyserial-3.5-py2.py3-none-any.whl (90 kB)
Collecting tenacity
  Using cached tenacity-8.0.1-py3-none-any.whl (24 kB)
Collecting textfsm>=1.1.2
  Using cached textfsm-1.1.3-py2.py3-none-any.whl (44 kB)
Collecting pyyaml>=5.3
  Using cached PyYAML-6.0-cp310-cp310-win_amd64.whl (151 kB)
Collecting scp>=0.13.3
  Using cached scp-0.14.4-py2.py3-none-any.whl (8.6 kB)
Collecting ntc-templates>=2.0.0
  Using cached ntc_templates-3.0.0-py3-none-any.whl (303 kB)
Requirement already satisfied: setuptools>=38.4.0 in c:\code\kirk-byers-free-python-course-2022\week08\venvs\test_env\lib\site-packages (from netmiko) (63.2.0)
Collecting six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting bcrypt>=3.1.3
  Using cached bcrypt-3.2.2-cp36-abi3-win_amd64.whl (29 kB)
Collecting pynacl>=1.0.1
  Using cached PyNaCl-1.5.0-cp36-abi3-win_amd64.whl (212 kB)
Collecting cryptography>=2.5
  Using cached cryptography-37.0.4-cp36-abi3-win_amd64.whl (2.4 MB)
Collecting future
  Using cached future-0.18.2.tar.gz (829 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting cffi>=1.1
  Using cached cffi-1.15.1-cp310-cp310-win_amd64.whl (179 kB)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Building wheels for collected packages: future
  Building wheel for future (setup.py): started
  Building wheel for future (setup.py): finished with status 'done'
  Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491058 sha256=0974babd7a2423337c9064f5164a93634037c1a68f1607a7469960094214d263
Successfully built future
Installing collected packages: pyserial, tenacity, six, pyyaml, pycparser, future, textfsm, cffi, pynacl, ntc-templates, cryptography, bcrypt, paramiko, scp, netmiko
Successfully installed bcrypt-3.2.2 cffi-1.15.1 cryptography-37.0.4 future-0.18.2 netmiko-4.1.1 ntc-templates-3.0.0 paramiko-2.11.0 pycparser-2.21 pynacl-1.5.0 pyserial-3.5 pyyaml-6.0 scp-0.14.4 six-1.16.0 tenacity-8.0.1 textfsm-1.1.3

(test_env)
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
$ pip list
Package       Version
------------- -------
bcrypt        3.2.2
cffi          1.15.1
cryptography  37.0.4
future        0.18.2
netmiko       4.1.1
ntc-templates 3.0.0
paramiko      2.11.0
pip           22.2.1
pycparser     2.21
PyNaCl        1.5.0
pyserial      3.5
PyYAML        6.0
scp           0.14.4
setuptools    63.2.0
six           1.16.0
tenacity      8.0.1
textfsm       1.1.3
wheel         0.37.1
(test_env)
jaap@bambo MINGW64 /c/code/kirk-byers-free-python-course-2022/week08/venvs (week08)
'''
