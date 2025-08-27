#!/bin/bash
# run_rt_modified.sh
# Run "rt {file}.py" for each recently modified Python file

# 1. Find modified *.py files according to Git
files=$(git ls-files -m "*.py")

# 2. If none, exit
if [ -z "$files" ]; then
    echo "No modified Python files."
    exit 0
fi

# 3. Loop and run rt
for f in $files; do
    echo "Running rt on $f..."
    /mnt/d/csLol/Tools/ritobin/bin/ritobin_cli.exe "$f"
done

