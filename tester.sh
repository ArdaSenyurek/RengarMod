#!/bin/bash
# Usage:
#   ./p.sh -isAt
#   ./p.sh -isAn SpellName
#   ./p.sh -isMo
#   ./p.sh -hasBuf BuffName
#   ./p.sh -flush

TEMPLATE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0_temp.py"
OUTFILE="/mnt/d/csLol/Mods/BinTests/Gitted/TestMod/data/characters/rengar/skins/skin0.py"

FLAG=$1
ARG=$2   # spell name or buff name

if [ -z "$FLAG" ]; then
    echo "Usage: $0 {-isAt|-isAn <Spell>|-isMo|-hasBuf <Buff>|-flush}"
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

    -flush)
        # Flush = copy template, but drop entire PersistentEffectConditions scope
        awk '
        BEGIN { skip=0; depth=0 }
        /PersistentEffectConditions: list2\[pointer\] = {/ {
            skip=1; depth=0
        }
        {
            if (skip) {
                # count braces to know when block ends
                for (i=1; i<=length($0); i++) {
                    c=substr($0,i,1)
                    if (c=="{") depth++
                    else if (c=="}") {
                        depth--
                        if (depth==0) { skip=0; next }
                    }
                }
                next
            }
        }
        !skip { print }
        ' "$TEMPLATE" > "$OUTFILE"
        echo "✅ Flushed: PersistentEffectConditions removed using $TEMPLATE → $OUTFILE"
        exit 0
        ;;

    *)
        echo "Unknown flag: $FLAG"
        exit 1
        ;;
esac

# For insertions: always regenerate from template
sed "/mDrivers: list\[pointer\] = {/r /dev/stdin" "$TEMPLATE" <<<"$INSERT" > "$OUTFILE"

echo "✅ Regenerated $OUTFILE with $FLAG ($ARG)"

