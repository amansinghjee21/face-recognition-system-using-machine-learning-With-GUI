#step 1 install the dependencies or library
#pip install cx_Freeze
#step 2 change executable name to your file name
import sys
from cx_Freeze import setup,Executable
import os
PYTHON_INSTALL_DIR=os.path.dirname(sys.executable)
os.environ['TCL_LIBRARYY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['Tk_LIBRARYY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')
include_files=[(os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),os.path.join('lib','tk86.dll')),
              (os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll'),os.path.join('lib','tcl86.dll'))]
base=None
if sys.platform=='win32':
    base='Win32GUI'
    #change here main1.py to your file name 
    # also you can change setup name or
    #  you can set icon overthere for icon icon= icon file
executables=[Executable('login.py',base=base,icon=r"face.ico",shortcutName='Face Recognation Attendance',shortcutDir="DesktopFolder")]
setup(name='Face Recognation Attendance Installer',Version='1.0',author='Aman Singh',description="This Application is made in low system configuration and it will better in high system",
options={'build_exe':{'include_files':include_files}},
executables=executables)
# paste this file where your main file exits
#for run command
# python Setup.py build for exe
#for application
#run this command
#python Setup.py bdist_msi
#enjoy
# Happy learing
