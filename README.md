# Data Science Workflow Automation Script (Visual Studio Code)

This Python script streamlines the setup process for new data science projects. It automates the creation of a new project directory, file creation within that directory, setting up a Python virtual environment, and installing initial packages. It also provides the commands to activate the virtual environment and open the project in Visual Studio Code.

## Features

- Interactive prompts for custom folder and file creation.
- Virtual environment setup using Python's built-in `venv` module.
- Ability to specify initial Python packages for installation.
- Copy-paste commands for easy environment activation and package installation.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3
- [Visual Studio Code](https://code.visualstudio.com/)

Additionally, make sure the `code` command is installed in your PATH to enable opening Visual Studio Code from the terminal. This can typically be done from within VS Code by opening the Command Palette (`Shift+Cmd+P`), typing `Shell Command: Install 'code' command in PATH`, and executing this command.

## Configuration

Before using the script, some environment setup is necessary:

1. If you are using `zsh` (the default shell on recent macOS versions), you will need to add the following lines to your `~/.zshrc` file to ensure that the `pyenv` and `pyenv-virtualenv` commands work correctly:

    ```zsh
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    ```

    After adding these lines, apply the changes with the command `source ~/.zshrc`.

2. Modify the default path for new projects by editing the script:

    ```python
    default_base_path = os.path.expanduser('~/your_default_project_directory')
    ```

    Replace `'~/your_default_project_directory'` with the path where you want your new data science projects to be located.

## Usage

To get started with this script:

1. Clone this repository or download the `ds_workflow.py` file to your local machine.
2. Open the script in a text editor or IDE of your choice.
3. Modify the `default_base_path` in the script to the directory where new projects should be created.
4. Save the script and run it using the following command in your terminal:

    ```bash
    python3 ds_workflow.py
    ```

5. Follow the interactive prompts in the terminal to specify your new project's details.

After running the script, you will be provided with a set of commands that you can copy and paste into your terminal to complete the environment setup.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.
