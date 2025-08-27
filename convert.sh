#!/bin/bash
# convert.sh
# Convert all modified Python files with ritobin_cli.exe

# Find modified tracked .py files
files=$(git ls-files -m "*.py")

if [ -z "$files" ]; then
    echo "No modified Python files to convert."
    exit 0
fi

for f in $files; do
    echo "🔄 Converting $f with ritobin_cli.exe..."
    /mnt/d/csLol/Tools/ritobin/bin/ritobin_cli.exe "$f"
done

echo "✅ Conversion finished."

