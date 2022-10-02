# Example Project to Create Executable of Python Program
### Prerequisite
1. [Python 3](https://www.python.org/downloads/)
### Create Virtual Environment
It is recommended to use virtual environment but not necessary. You need to run only setupVenv.bat to create virtual environment and move to next section.
1. **setupVenv.bat:** creates virtual environment (venv folder) in same folder where batch file is present. Installs libraries from requirements.txt.
2. **activateVenv.bat:** It activates virtual environment in your command line.
3. **deactivateVenv.bat:** It deactivates virtual environment in your command line.
4. **deleteVenv.bat:** It deletes venv folder which contained all required files to activate virtual environment.
5. **updatePythonLibraries.bat:** It updates libraries of virtual environment using requirements.txt.
6. **exportRequirements_txt.bat:** It updates requirements.txt file as per updated libraries used virtual environment.
### How to Run the Program
1. Open CMD inside project folder and run activateVenv.bat file (activates virtual environment in command line)
2. Move to program directory with command `cd program`
3. Run the program with command `python main.py`
4. It will ask for images folder. Please press ENTER to select default path.

### Create Executable with Supporting Files
1. Open CMD inside project folder and run activateVenv.bat file (activates virtual environment in command line)
2. Run buildExec.bat file. It will create build and dist folder inside executable folder.
3. You can run main.exe file inside executable/dist/main folder.
4. It will ask for images path, so press ENTER to select default path.

### Create Single Executable
1. Open CMD inside project folder and run activateVenv.bat file (activates virtual environment in command line)
2. Run buildExecOnefile.bat file. It will create build and dist folder inside executableOnefile folder.
3. You can run mainOnefile.exe file inside executableOne/dist folder.
4. It will create a temporary folder with name _MEIxxxxx (**Example:** _MEI93842).
5. It will ask for images path, so press ENTER to select default path. Now the default path will be images folder inside temporary folder with name _MEIxxxxx.

### Create Installer
1. You need to complete *Create Installer with Supporting Files* section.
2. Install [Inno Setup](https://jrsoftware.org/isdl.php) in your system.
3. Go to Installer folder and open installer.iss file using *Inno Setup Compiler* App.
4. Now run the script using F9 and it will create Image_viewer.exe inside Installer folder.