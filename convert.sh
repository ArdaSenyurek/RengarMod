#!/bin/bash
# convert.sh
# Reconvert only if .py or .bin in the folder changed (working dir check)

# Get modified tracked .py or .bin files (unstaged or staged)
changed=$(git ls-files -m '*.py' '*.bin')

if [ -z "$changed" ]; then
    echo "No modified .py or .bin files."
    exit 0
fi

# Collect corresponding .py sources
pyfiles=""
for f in $changed; do
    if [[ $f == *.py ]]; then
        pyfiles="$pyfiles $f"
    elif [[ $f == *.bin ]]; then
        # find a .py in the same directory (if any)
        dir=$(dirname "$f")
        candidate=$(ls "$dir"/*.py 2>/dev/null | head -n 1)
        if [ -n "$candidate" ]; then
            pyfiles="$pyfiles $candidate"
        fi
    fi
done

# Deduplicate
pyfiles=$(echo "$pyfiles" | tr ' ' '\n' | sort -u)

if [ -z "$pyfiles" ]; then
    echo "No .py sources found to convert."
    exit 0
fi

errors=0
for f in $pyfiles; do
    echo "🔄 Converting $f with ritobin_cli.exe..."
    /mnt/d/csLol/Tools/ritobin/bin/ritobin_cli.exe "$f"
    status=$?
    if [ $status -ne 0 ]; then
        echo "❌ Error: ritobin_cli.exe failed on $f (exit code $status)"
        errors=$((errors+1))
    else
        echo "✅ Converted $f"
    fi
done

if [ $errors -gt 0 ]; then
    echo "⚠️ Conversion completed with $errors error(s)."
    exit 1
else
    echo "🎉 All conversions successful."
fi

