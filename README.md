# terminal-journal
A way of journaling in the terminal

This journaling program uses openssl to encrypt the files it generates with aes-256-cbc standard, as bit64.
You'll need python 3 >


# How to use it

To start writing, run the script `start` with `w` as argument.
You can start a new paragraph with return.
When you are finished writing just type return leaving the string empty.

To read an specific day, just run the `start` script without arguments.

The files are saved at the `~/.entry`directory.
You don't need to create this folder, it is made for you.

I recommend adding an alias for quick access.
```
alias j="foo/journal/start"
alias jw="foo/journal/start w"
```
