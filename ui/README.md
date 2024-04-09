pyqt5 docs: https://doc.qt.io/qtforpython-5/modules.html

The .ui files are made with QtDesigner. pyqt5 should've been installed through the requirements.txt  
When in this directory do the following to generate a new `ui_main_window.py` file.

```
pyuic5 -o .\ui_main_window.py .\main_window.ui
```
