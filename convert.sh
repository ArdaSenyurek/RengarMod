#!/bin/bash
# convert.sh
# Reconvert modified Python sources, with proper error logging

# Get modified tracked .py files (unstaged or staged)
pyfiles=$(git ls-files -m '*.py')

if [ -z "$pyfiles" ]; then
    echo "No modified Python files."
    exit 0
fi

errors=0
for f in $pyfiles; do
    echo "🔄 Converting $f with ritobin_cli.exe..."
    
    # Capture stdout+stderr
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

if [ $errors -gt 0 ]; then
    echo "⚠️ Conversion completed with $errors error(s)."
    exit 1
else
    echo "🎉 All conversions successful."
fi

