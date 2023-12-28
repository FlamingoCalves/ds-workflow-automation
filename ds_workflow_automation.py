import os
import subprocess

# Function to create a new folder inside the specified base path
def create_folder(base_path, folder_name):
    # Combine the base path and the new folder name
    new_path = os.path.join(base_path, folder_name)
    # Create the folder if it doesn't already exist
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

# Function to create new files in the specified folder
def create_files(folder_path):
    # Keep asking for file names until the user types 'END'
    while True:
        file_name = input("Enter a file name (or type 'END' to finish): ")
        if file_name == 'END':
            break
        # Create each new file
        open(os.path.join(folder_path, file_name), 'w').close()

# Function to set up a new virtual environment in the specified folder
def setup_venv(folder_path):
    # Ask the user for the name of the virtual environment
    env_name = input("Enter a name for the new virtual environment: ")
    env_path = os.path.join(folder_path, env_name)
    # Create the virtual environment using the venv module
    subprocess.run(["python3", "-m", "venv", env_path])
    print("\nVirtual environment created.")
    return env_path

# Function to prompt the user for packages to install
def prompt_packages():
    packages = input("Enter packages to install (separate by space, or leave blank if none): ")
    return packages.strip().split()

# Function to print the commands for the user to copy and paste into their Terminal
def print_activation_instructions(folder_path, env_path, packages):
    activate_command = f"source {env_path}/bin/activate"
    pip_install_command = f"pip install {' '.join(packages)}" if packages else "# No packages specified for installation"
    
    # Instructions for the user
    print("\nTo set up your project environment, copy and paste the following commands into your Terminal:")
    print("--------------------------------------------------")
    print(f"cd {folder_path}")
    print(activate_command)
    if packages:
        print(pip_install_command)
    print("code .")
    print("--------------------------------------------------")
    print("These commands will: change to the project directory, activate the virtual environment,")
    print("install the specified Python packages (if any), and open the folder in Visual Studio Code.")

# Main function to run the workflow
def main():
    # USER CONFIGURATION START
    # User should change this path to the desired default location
    default_base_path = os.path.expanduser('~/your_default_project_directory')
    # USER CONFIGURATION END
    
    # Ask the user for the new folder name
    folder_name = input("Enter the new folder name: ")
    new_folder_path = create_folder(default_base_path, folder_name)

    # Create files and set up the virtual environment
    create_files(new_folder_path)
    env_path = setup_venv(new_folder_path)
    
    # Prompt for packages and provide the setup instructions
    packages = prompt_packages()
    print_activation_instructions(new_folder_path, env_path, packages)

# Check if the script is being run directly
if __name__ == "__main__":
    main()
