# terminal-journal
A way of journaling in the terminal

This journaling program uses openssl to encrypt the files it generates with aes-256-cbc standard, as bit64.

# How to use it

To start writing start the script.py with `w`as argument.
You can start a new paragraph with return.
When you are finished writing just type return leaving the string empty.

To read an specific day, just run script.py without arguments.

The files are saved at the `~/.entry`directory.
