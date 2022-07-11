#!/bin/bash

for file in old_site/*.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "old_site/$name.html"
done