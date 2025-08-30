#!/bin/bash
# convert.sh
# Convert modified Python files (or their paired bins) with ritobin_cli.exe

# 1. Collect changed .py and .bin files (staged + unstaged vs HEAD)
changed=$(git diff --name-only HEAD -- '*.py' '*.bin')
changed_staged=$(git diff --cached --name-only HEAD -- '*.py' '*.bin')
changed="$changed $changed_staged"

# 2. Build list of .py files to convert
pyfiles=""
for f in $changed; do
    if [[ $f == *.py ]]; then
        echo "📌 Found modified Python file: $f"
        pyfiles="$pyfiles $f"
    elif [[ $f == *.bin ]]; then
        dir=$(dirname "$f")
        candidate=$(ls "$dir"/*.py 2>/dev/null | head -n 1)
        if [ -n "$candidate" ]; then
            echo "📌 Found modified BIN file: $f → will convert sibling $candidate"
            pyfiles="$pyfiles $candidate"
        else
            echo "⚠️  Found modified BIN file: $f but no sibling .py in $dir"
        fi
    fi
done

# 3. Deduplicate
pyfiles=$(printf "%s\n" $pyfiles | sort -u)

# 4. Exit early if nothing
if [ -z "$pyfiles" ]; then
    echo "No modified Python files."
    exit 0
fi

# 5. Run conversions
errors=0
for f in $pyfiles; do
    echo "🔄 Converting $f with ritobin_cli.exe..."
    output=$(/mnt/d/csLol/Tools/ritobin/bin/ritobin_cli.exe "$f" 2>&1)
    status=$?
    if [ $status -ne 0 ] || echo "$output" | grep -q "Error:"; then
        echo "❌ Error converting $f"
        echo "$output"
        errors=$((errors+1))
    else
        echo "✅ Converted $f"
    fi
done

# 6. Final summary
if [ $errors -gt 0 ]; then
    echo "⚠️  Conversion finished with $errors error(s)."
    exit 1
else
    echo "🎉 All conversions successful."
fi

