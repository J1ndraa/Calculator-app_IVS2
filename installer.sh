#!/bin/bash

# Destination folder provided as argument
destination_folder="$1"

# Check if the destination folder argument is provided
if [ $# -ne 1 ]; then
    echo "Base installation directory"
    destination_folder="../"
fi



# Check if the source file exists
if [ ! -f "./gui" ]; then
    echo "Source file '$source_file' not found. Aborting."
    exit 1
fi

# Check if the destination folder exists, if not, create it
if [ ! -d "$destination_folder" ]; then
    echo "Creating destination folder: $destination_folder"
    mkdir -p "$destination_folder"
fi
# Copy the file to the destination folder
cp "./gui" "$destination_folder/"

touch "$destination_folder/uninstall.sh"
echo '#!/bin/bash' > "$destination_folder/uninstall.sh"
echo "rm "./gui"" >> "$destination_folder/uninstall.sh"
echo "rm "./uninstall.sh"" >> "$destination_folder/uninstall.sh"
chmod +x "$destination_folder/uninstall.sh"

echo "Successfully installed "
