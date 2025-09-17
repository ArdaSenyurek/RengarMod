#!/bin/bash
# cs.sh — build & run overlay; kill any previous run first

set -euo pipefail

MODTOOLS="mod-tools.exe"

MODS_DIR='D:\csLol\Mods\BinTests\Gitted'
PROFILE_DIR='D:\csLol\cslol New new\cslol-manager\profiles\ProfileForRengar'
CONFIG_INI='D:\csLol\cslol New new\cslol-manager\config.ini'
GAME_PATH='D:\Riot Games\League of Legends\Game\DATA\FINAL\..\..'   # resolves to ...\Game
MODS_LIST='RengarMod'
EXTRA_FLAGS='--ignoreConflict --noTFT'

kill_modtools() {
  # kill any old session (Windows process from WSL)
  taskkill.exe /F /IM mod-tools.exe >/dev/null 2>&1 || true
  # wait until it’s really gone (max ~3s)
  for _ in {1..30}; do
    if ! tasklist.exe | grep -i 'mod-tools.exe' >/dev/null 2>&1; then
      break
    fi
    sleep 0.1
  done
}

# Ensure we also clean up if THIS script is interrupted
trap 'taskkill.exe /F /IM mod-tools.exe >/dev/null 2>&1 || true' INT TERM

echo "[PREP] Killing any existing mod-tools.exe..."
kill_modtools

echo "[MK] Building overlay..."
"$MODTOOLS" mkoverlay "$MODS_DIR" "$PROFILE_DIR" --game:"$GAME_PATH" --mods:$MODS_LIST $EXTRA_FLAGS

echo "[RUN] Running overlay (will wait until you press Enter)..."
"$MODTOOLS" runoverlay "$PROFILE_DIR" "$CONFIG_INI" --game:"$GAME_PATH"

echo "[DONE] Overlay run finished."

