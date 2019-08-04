#! /bin/sh -e

dest="$1"
src="$2"

d=$(dirname "$dest")
mkdir -p "$d"
ln -snf $(realpath "$src") "$d"/
cd "$d"
exec python3 $(basename "$src")
