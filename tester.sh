#!/bin/bash
# Usage:
#   ./p.sh -isAt
#   ./p.sh -isAn SpellName
#   ./p.sh -isMo
#   ./p.sh -hasBuf BuffName

TEMPLATE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0_temp.py"
OUTFILE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0.py"

FLAG=$1
ARG=$2   # For spell/buff names

if [ -z "$FLAG" ]; then
    echo "Usage: $0 {-isAt|-isAn <Spell>|-isMo|-hasBuf <Buff>}"
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

    -isMo)
        INSERT='                        IsMovingBoolDriver {}'
        ;;

    -hasBuf)
        if [ -z "$ARG" ]; then
            echo "❌ Error: you must provide a buff name for -hasBuf"
            echo "Example: $0 -hasBuf rengarpassivebuff"
            exit 1
        fi
        INSERT=$(printf '%s\n' \
"                        HasBuffDynamicMaterialBoolDriver {" \
"                            mScriptName: string = \"$ARG\"" \
"                        }")
        ;;

    *)
        echo "Unknown flag: $FLAG"
        exit 1
        ;;
esac

# Always regenerate output from template
sed "/mDrivers: list\[pointer\] = {/r /dev/stdin" "$TEMPLATE" <<<"$INSERT" > "$OUTFILE"

echo "✅ Regenerated $OUTFILE with $FLAG ($ARG)"

