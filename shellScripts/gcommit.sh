#!/bin/bash
# gcommit.sh
# Stage all changes and commit with a message

MSG="$*"

if [ -z "$MSG" ]; then
    echo "❌ Error: no commit message given."
    echo "Usage: $0 Commit message here"
    exit 1
fi

git add -A
git commit -m "$MSG"

echo "✅ Git commit done: $MSG"

