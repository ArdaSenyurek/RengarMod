#!/bin/bash
# Usage:
#   ./tester.sh -isAt
#   ./tester.sh -isAn SpellName

TEMPLATE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0_temp.py"
OUTFILE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0.py"

FLAG=$1
ARG=$2   # e.g. Spell5 (only for -isAn)

if [ -z "$FLAG" ]; then
    echo "Usage: $0 {-isAt|-isAn <SpellName>}"
    exit 1
fi

# Prevent overwriting existing skin0.py
if [ -f "$OUTFILE" ]; then
    echo "❌ Error: $OUTFILE already exists. Delete/move it first if you want to regenerate."
    exit 1
fi

case $FLAG in
    -isAt)
        INSERT='                        IsAttackingBoolDriver {}'
        ;;
    -isAn)
        if [ -z "$ARG" ]; then
            echo "❌ Error: you must provide a spell name for -isAn"
            echo "Example: $0 -isAn Spell5"
            exit 1
        fi
        INSERT=$(printf '%s\n' \
"                        IsAnimationPlayingDynamicMaterialBoolDriver {" \
"                            mAnimationNames: list[hash] = {" \
"                                \"$ARG\"" \
"                            }" \
"                        }")
        ;;
    *)
        echo "Unknown flag: $FLAG"
        exit 1
        ;;
esac

# Generate skin0.py from template
sed "/mDrivers: list\[pointer\] = {/r /dev/stdin" "$TEMPLATE" <<<"$INSERT" > "$OUTFILE"

echo "✅ Generated $OUTFILE with $FLAG ($ARG)"

