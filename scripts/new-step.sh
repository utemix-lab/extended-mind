#!/usr/bin/env bash
set -euo pipefail

repo_root="$(pwd)"
steps_dir="$repo_root/docs/steps"
template_path="$steps_dir/_template.step.md"

mkdir -p "$steps_dir"

if [[ ! -f "$template_path" ]]; then
  echo "Template not found: $template_path" >&2
  exit 1
fi

date_str="$(date +"%Y-%m-%d")"
existing_count=$(ls "$steps_dir"/step-"$date_str"-*.step.md 2>/dev/null | wc -l | tr -d ' ')
next=$(printf "%02d" $((existing_count + 1)))

step_id="S-$date_str-$next"
file_name="step-$date_str-$next.step.md"
target_path="$steps_dir/$file_name"

sed "s/S-YYYY-MM-DD-XX/$step_id/" "$template_path" > "$target_path"
echo "$target_path"
