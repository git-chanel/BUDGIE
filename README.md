# BUDGIE

Simple budgeting app

## Setup

This project uses Python 3.12.  
Setting up the virtual environment ([why?](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments))  
Ensure virtualenv is installed:

```
py -3.12 -m pip install --upgrade pip virtualenv
```

Setup virtualenv in this folder:

```
py -3.12 -m venv ./venv
```

Run virtualenv:
Linux or GitBash:

```
source ./venv/scripts/activate
```

Windows/Powershell

```
./venv/scripts/activate
```

might need to do this: shift + right-click windows button, and select admin powershell.  
```
set-executionpolicy remotesigned
Y
```

Install all the packages:

```
pip install -r requirements.txt
```

Run the cli with:
```
py test.py
```

Run the app GUI with:
```
py app.py
```

## pyqt5 tools & designer

Uses pyqt5 for UI. If you want to use the [QT designer](https://realpython.com/qt-designer-python/), install [pyqt5-tools](https://pypi.org/project/pyqt5-tools/).
Use Python 3.11, as it errors out with 3.12. Below will install it in your global python 3.11 folder.

```
py -3.11 -m pip install pyqt5-tools
```

Then in your `Python3.11/Scripts/` folder you can find and launch `pyqt5-tools.exe designer`, or `pyqt5-tools.exe --help` for more options.

The .ui files are made with QtDesigner. pyqt5 should've been installed through the requirements.txt  
When in the "./ui/" directory do the following to generate a new ui_main_window.py file.
```
pyuic5 -o .\ui_main_window.py .\main_window.ui
```