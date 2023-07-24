#!/bin/bash

#colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Function to execute Python files
execute_python_files() {
    for file in *.py; do
        if [[ -f "$file" ]]; then
            echo -e "${GREEN}Executing $file...${NC}"
            python3 "$file"
            echo -e "${GREEN}Finished executing $file${NC}"
            echo -e "${MAGENTA}---------------------------------${NC}"
        fi
    done
}

# Beautified messages
echo -e "${YELLOW}Executing Python files in the current directory:${NC}"
execute_python_files

echo -e "${YELLOW}Executing Python files in the parent directory:${NC}"
pushd .. # Move to the parent directory
execute_python_files
popd # Move back to the original directory
