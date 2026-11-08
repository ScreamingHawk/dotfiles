# Dotfiles

Dotfiles are the config files that programs use to store preferences.

This repository is a store of my dotfiles so I can replicate my preferences on a new machine with ease.

## Layout

* `shared/` — platform-independent configs (EditorConfig, youtube-dl)
* `linux/` — Linux-only configs; subfolders map to `~/.config/<name>/` (e.g. `kitty/`)
* `windows/` — Windows-only configs
* `work/` — job-specific configs; prompt-declined when moving between jobs

## EditorConfig

My global editorconfig file that I can apply across projects to ensure a somewhat consistent style.
Particularly with git.. Having whitespace changes can cause disgusting diffs.

Some people don't have this problem. I do.

I've started using [EditorConfig][1] to manage some base whitespace styling and it's been a blessing.

## Youtube-dl config

I use [youtube-dl][2] almost exclusively for music, so this file saves a bunch of typing.

The config file saves `128Kb m4a` audio files to the `~/Music` directory, including thumbnails and metadata.

To ignore the config file, pass `--ignore-config`.

# How to use

Clone the repo.

`git clone https://github.com/ScreamingHawk/dotfiles`

Navigate into the folder.

`cd dotfiles`

Run the copy script.

`python copy.py`
