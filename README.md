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
5. It will ask for images path, so please enter relative path (**Example:** ./_MEI93842/images/).
>Note: Default path won't work here.