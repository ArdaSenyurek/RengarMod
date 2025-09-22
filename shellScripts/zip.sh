#!/bin/sh
# Usage: ./shellScripts/zip.sh <folder> [archive.zip]
# Example: ./shellScripts/zip.sh RengarMod RengarMod.zip

FOLDER="$1"
ARCHIVE="$2"

if [ -z "$FOLDER" ]; then
    echo "Usage: $0 <folder> [archive.zip]"
    exit 1
fi

# If no archive name is given, default to <folder>.zip
if [ -z "$ARCHIVE" ]; then
    ARCHIVE="${FOLDER}.zip"
fi

# Run the zip inside the folder in a subshell
(
  cd "$FOLDER" || exit 1
  # write the archive one level up, relative to Gitted/
  zip -r "../$ARCHIVE" .
)

