# trivia

## Description 

Small trivia app

## Connecting WSL to VSCode
If you are using WSL as a Linux subsystem of Windows, you will need to ensure your VSCode workspace is connected to your WSL instance. To do this, begin by clicking the two arrows in the bottom left corner. This will open a tab near the top of the window that will prompt you to select an option; select `New WSL Window` and open the folder in which your project is located.

## WSL VSCode Python Configuration
If you are struggling with your python configuration with VSCode ("unable to find import" errors, ex), you will need to select your Python interpreter
To begin, ensure you are using VSCode in a WSL instance. 
Next, ensure you are on a virtual environment. In the terminal, run `which python3`. This will show you the location of your Python3 interpreter. Press `CTRL+Shift+P` to open the VSCode preferences search and type `interpreter`, selecting the option that says `Python: Select Interpreter`. Click `enter interpreter path`, and find the file that was shown with the `which python3` command. Once you select this, your Python interpreter should correctly recognize imports.

## Selecting a Linter
For Python, we will be using Pylint as our interpreter. This will help us with code consitency across our project. To select your interpreter, ensure you are on a WLS instance (if you are using WSL) and type `CTRL+Shift+P` to open the VSCode preferences search. Type `linter` and select the option that says `Python: Select Linter`. Select `pylint` at the bottom. You may get a warning that you have not installed pylint; if so, click "install".