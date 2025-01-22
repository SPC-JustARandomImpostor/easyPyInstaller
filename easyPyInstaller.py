import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    print("Please open a Python file to convert it to an executable.")
    
    # Open file dialog to select a Python file
    Tk().withdraw()  # Hide the root Tkinter window
    file_path = askopenfilename(filetypes=[("Python Files", "*.py")])
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    # Confirm the selected file
    print(f"Selected file: {file_path}")
    
    # Ask for options
    one_file = input("Do you want to bundle it into a single file? (yes/no): ").strip().lower() == "yes"
    no_console = input("Do you want to hide the console window? (yes/no): ").strip().lower() == "yes"
    extra_args = input("Enter any additional PyInstaller arguments (or press Enter to skip): ").strip()
    
    # Build the command
    command = ["python", "-m", "PyInstaller", file_path]
    if one_file:
        command.append("--onefile")
    if no_console:
        command.append("--noconsole")
    if extra_args:
        command.extend(extra_args.split())
    
    # Print the final command for confirmation
    print("\nExecuting the following command:")
    print(" ".join(command))
    
    # Run the command
    try:
        subprocess.run(command, check=True)
        print("\nBuild process completed successfully!")
    except subprocess.CalledProcessError as e:
        print("\nAn error occurred during the build process.")
        print(e)

if __name__ == "__main__":
    main()
