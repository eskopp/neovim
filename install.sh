#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v stow &>/dev/null; then
  echo "Error: GNU Stow is not installed." >&2
  echo "  Fedora/RHEL: sudo dnf install stow" >&2
  echo "  Ubuntu/Debian: sudo apt install stow" >&2
  echo "  macOS: brew install stow" >&2
  exit 1
fi

mkdir -p "$HOME/.config"

cd "$REPO_DIR"
stow --target="$HOME" nvim

echo "Done: ~/.config/nvim -> $REPO_DIR/nvim/.config/nvim"
