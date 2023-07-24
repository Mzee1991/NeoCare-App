#!/bin/bash

# colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Function to execute Python files in the current directory
execute_python_files() {
    for file in ./*.py; do
        if [[ -f "$file" ]]; then
            echo -e "${GREEN}Executing $file...${NC}"
            python3 "$file"
            echo -e "${GREEN}Finished executing $file${NC}"
            echo -e "${MAGENTA}---------------------------------${NC}"
        fi
    done
}

# Function to execute Python files in the given directory
execute_python_files_in_folder() {
    local folder="$1"
    pushd "$folder" > /dev/null
    folder_name=$(basename "$folder")
    echo -e "${YELLOW}Executing Python files in the '$folder_name' directory:${NC}"
    execute_python_files
    echo -e "${YELLOW}${folder_name} district and its constituencies have been installed!${NC}"
    popd > /dev/null
}

# Beautified messages
execute_python_files_in_folder "./" # Execute Python files in the current directory

# Loop through folders in the current directory
for folder in ./*/; do
    execute_python_files_in_folder "$folder"
done
