#!/bin/bash
# update.sh
# Run ritobin_cli.exe on modified .py files, then git add+commit with message.

# 1. Grab commit message from arguments
commit_msg="$*"

if [ -z "$commit_msg" ]; then
    echo "❌ Error: No commit message provided."
    echo "Usage: up Commit message here"
    exit 1
fi

# 2. Find modified .py files
files=$(git ls-files -m "*.py")

# 3. Run ritobin_cli.exe on them if any
if [ -n "$files" ]; then
    for f in $files; do
        echo "Running ritobin_cli.exe on $f..."
        /mnt/d/csLol/Tools/ritobin/bin/ritobin_cli.exe "$f"
    done
else
    echo "No modified Python files to process."
fi

# 4. Add all changes (including untracked) and commit
git add -A
git commit -m "$commit_msg"

