# Dotfiles

Dotfiles are the config files that programs use to store preferences. 

This repository is a store of my dotfiles so I can replicate my preferences on a new machine with ease. 

## EditorConfig

My global editorconfig file that I can apply across projects to ensure a somewhat consistent style. 
Particularly with git.. Having whitespace changes can cause disgusting diffs.

Some people don't have this problem. I do.

I've started using [EditorConfig][1] to manage some base whitespace styling and it's been a blessing.

## GitConfig

My Git config file includes a couple of helpful things. 

* My name
* Force pull to only complete if it can `fast-forward`, to prevent undesired merges
* Aliases for `status` and `fetch`
* Setting for line endings

## Youtube-dl config

I use [youtube-dl][2] almost exclusively for music, so this file saves a bunch of typing.

The config file saves `128Kb m4a` audio files to the `~/Music` directory, including thumbnails and metadata. 

To ignore the config file, pass `--ignore-config`. 

# How to use

Clone the repo.

`git clone https://github.com/ScreamingHawk/dotfiles`

Navigate into the folder.

`cd dotfiles`

Run the corresponding shell/batch file to copy the files. 

[1]: http://editorconfig.org/
[2]: https://rg3.github.io/youtube-dl/