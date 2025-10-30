#!/usr/bin/env python3
"""Move and Rename Files with shutil"""

import shutil  # For moving and renaming files
import os  # For directory operations

def main():
    """Main logic"""
    # Ensure the script starts in the correct directory
    os.chdir("/home/student/mycode/")

    # Move Raynor to battlecruiser
    shutil.move("raynor.obj", "battlecruiser/")

    # Prompt for Kerrigan's new name
    xname = input("What is the new name for kerrigan.obj? ")

    # Rename Kerrigan
    shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()

