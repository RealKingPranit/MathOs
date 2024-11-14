import subprocess
import sys
import platform

def is_package_installed(package):
    """Check if a package is already installed."""
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "show", package])
        return True
    except subprocess.CalledProcessError:
        return False

def update_pip():
    """Function to update pip if needed."""
    print("Updating pip...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("pip updated successfully!")
    except subprocess.CalledProcessError:
        print("Failed to update pip. Please update pip manually.")

def install(package):
    """Function to install a package, with error handling and pip update if failed."""
    if is_package_installed(package):
        print(f"{package} is already installed. Skipping installation.")
        return
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")
        print("Attempting to update pip...")
        update_pip()
        print(f"Retrying installation of {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package} after updating pip.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package} again. Please check your internet connection or package name.")

def main():
    """Main function to handle dependencies installation."""
    # Check if we're on Windows and need to install windows-curses for 'curses'
    if platform.system() == 'Windows':
        print("Windows detected: installing 'windows-curses' for curses functionality.")
        install('windows-curses')
    
    # List of dependencies
    dependencies = [
        'curses',  # For Unix-based systems, curses is built-in, so this won't install anything.
        'importlib',  # In case of Python < 3.1, we install it, although it's built-in for newer versions.
        'pick',  # External package
    ]
    
    # Install the dependencies
    for package in dependencies:
        install(package)

    print("Installation complete!")

if __name__ == "__main__":
    main()
