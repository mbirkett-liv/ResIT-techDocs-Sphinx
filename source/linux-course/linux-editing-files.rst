7. More about files
*******************

7.1 Displaying and editing files
================================

For certain types of file such as text files and program code (e.g. R scripts), it is possible to display their contents directly on the screen using a command called cat (the strange name comes from the fact that is was originally designed to concatenate (join together) files). This example displays the contents of some small text files in the course directory:

$ cat plain_file 
Just a plain text file
$ cat text/hamlet.txt 
HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
....

If you try displaying a larger file, then the contents will probably scroll off the screen quickly before you have a chance to see them e.g.

$ cat text/rhyme
...
The Mariner, whose eye is bright,
Whose beard with age is hoar,
Is gone: and now the Wedding-Guest
Turned from the bridegroom's door.

He went like one that hath been stunned,
And is of sense forlorn:
A sadder and a wiser man,
He rose the morrow morn.

What is needed is to display the file a screenful at time and this is exactly what the more command does e.g.:

$ more text/rhyme
PART I
It is an ancient Mariner,
And he stoppeth one of three.
'By thy long grey beard and glittering eye,
Now wherefore stopp'st thou me?

The Bridegroom's doors are opened wide,
And I am next of kin;
The guests are met, the feast is set:
May'st hear the merry din.'

He holds him with his skinny hand,
'There was a ship,' quoth he.
'Hold off! unhand me, grey-beard loon!'
Eftsoons his hand dropt he.

He holds him with his glittering eye?
The Wedding-Guest stood still,
And listens like a three years' child:
The Mariner hath his will.

The Wedding-Guest sat on a stone:
He cannot choose but hear;
And thus spake on that ancient man,
The bright-eyed Mariner.

'The ship was cheered, the harbour cleared,
Merrily did we drop
Below the kirk, below the hill,
Below the lighthouse top.

The Sun came up upon the left,
Out of the sea came he!
And he shone bright, and on the right
Went down into the sea.

Higher and higher every dvery day,
--More--(4%)

Press the [space bar] repeatedly and the next screenful of the file will be displayed until we eventually get to the end of it:

...
The Mariner, whose eye is bright,
Whose beard with age is hoar,
Is gone: and now the Wedding-Guest
Turned from the bridegroom's door.

He went like one that hath been stunned,
And is of sense forlorn:
A sadder and a wiser man,
He rose the morrow morn.
$

If you find you are not really interested in the contents after all, just type [Ctrl] and c together ([Ctrl-c]) or type q to interrupt the output and get back to the command prompt.

As the name suggests, more only allows you to see more of the file each time the [space bar] is pressed but another program called less will allow you to scroll backwards by typing b as well as forwards using the [space bar] or by typing f. Try it now on the famous epic rhyme:

$ less text/rhyme

You can also scroll backwards and forwards a line at a time by using the [up arrow] and [down arrow] keys. To move to the end of the file, type G (i.e. [SHIFT] and g together) and to move to the begininng of the file, type 1G (in fact any number followed by G will take you to that line number and typing [Ctrl-g] will display the current line number).

It would seem that if less can do all that more can, why have the more command. The answer is that in the past more would be guaranteed to be available on every Linux system but not less. Unlike Oliver Twist, in Linux you can always have more but possibly not less.

There are two other related programs for displaying the contents of a file which can come in useful. The head command will display the first few lines of a file and the tail command the last few lines.

Linux systems generally come with a variety of editors which can be used for editing text files and program code but unfortunately none of them are exactly user-friendly. On lxb (and other systems), the nano editor can be used to make small changes to files and create new ones e.g.

$ nano new_file

Here there really isn't space to cover nano in detail so please refer to this beginners guide online (don't let the title put you off!). If you aim to do a lot of editing - particularly of program code and scripts etc - you may be better off with the nedit editor. This is described in Appendix B.

7.2 Filenames and types in Linux
================================

The Linux restrictions on the file naming can be summed up pretty much as "anything goes" and there are very very few constraints on what you can call a file (or equivalently a directory). This, as in real life, is sometimes a dangerous idea and can, in some cases, lead to files that are difficult to copy and even remove. One example of this, which confuses a lot of Microsoft Windows users, is the use of spaces in filenames. This is an extremely bad idea in Linux as spaces are used to separate options in Linux commands and so the golden rule is:

Never use spaces in filenames or directory names.

(Ideally, use the underscore "_" or hyphen "-" instead)

The following example illustrates the point. Start in the course directory again and create a file with a space in its name thus:

$ echo some text > "single file"

You can examine the contents using the cat command:

$ cat  "single file"
some text

Notice how we need to put the name of the file in quotes in order to preserve the space in the name. If we go away and come back later having forgotten about the spaces in the name this leads to all sorts of confusion. For example, it now looks like we have created two files called single and file:

$ ls
another_file  c_code  new_dir  plain_file  progs  r_code  single file  
text

Now try getting rid of them:

$ rm single file
rm single file
rm: cannot remove `single': No such file or directory
rm: cannot remove `file': No such file or directory

What is needed are the quotes again:

$ rm "single file"
rm "single file"
$ ls
another_file  c_code  new_dir  plain_file  progs  r_code  text

There are also some characters which have a special meaning in Linux and which are best avoided. Here are some (but possibly not all) of them:

! " $ % ^ & * ( ) # | / \ < > ` ' { } ; 

In short, it is safest to stick to upper and lower case letters, numbers, underscores, hyphens and periods i.e. A-Z a-z 0-9 _ - .

Files in Linux are just a collection of bytes of data referenced by a particular filename and there is no significance attached to them by the operating system. This is in marked contrast to Microsoft Windows where the operating system, the applications and the files are closely linked together. In Windows, some file types are associated with particular applications depending on their three (or four) letter filename extension so for example by double-clicking on a file with .doc extension, the file will automatically be opened in Microsoft Word.

In Linux, there are no file extensions as such and it is down to the user to work out how to open a particular file. Having said that there are some conventions used in naming files, for example, filenames ending in .c contain C program code whereas files ending in .sh are special command programs (scripts). These are just conventions though and users are free to chose whatever "extensions" they like. The operating system can make a guess at what a particular file contains by using the file command. Try this one:

$ file c_code/hello.c 
 c_code/hello.c: ASCII C program text

and this one:

$ file text/hamlet.txt 
text/hamlet.txt: ASCII English text

Notice that the .txt "extension" (which is used for Notepad files in Windows) is irrelevant though and another text file without it gives similar results:

$ file text/ls_command 
text/ls_command: UTF-8 Unicode English text

The contents of all of these files could be displayed using the cat command or more/less but there are some files which you should be careful about displaying or editing. These are actual programs themselves which the operating system refers to as executables: e.g.

$ file progs/hello
progs/hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), 
dynamically linked (uses shared libs), for GNU/Linux 2.6.18, 
not stripped

If you try to list the contents of this using using the cat, you will be greeted with screenfuls of gibberish, random beeps possibly and you may even have to login again to get a usable terminal window back. If you have an adventurous streak, you can try it it but don't say you weren't warned :-)

There is actually another type of executable called a shell script which contains Linux commands and can be edited using the likes of the nano editor. Here is an example:

$ file progs/greeting.sh 
progs/greeting.sh: Bourne-Again shell script text executable
$ cat progs/greeting.sh 
#!/bin/bash

echo "Hello ! You are logged in as `whoami` on `date`."

We'll say more about running executable programs and scripts in a later section.

7.3 Controlling the output from Linux commands
==============================================

In the section on displaying and editing files we met the Linux more and less programs which can be used to scroll through a file, displaying its contents a screenful at a time. These programs are actually general purpose tools and are not restricted to just displaying files but can be used to "pause" the output from any Linux command. If we revisit the example of the long running ls command you can see this for yourself. Try this:

$ ls -lR /

This will give a long listing of every file and directory on the Linux system and the output will whizz past before you have chance to see it. Type [Ctrl] and c together (i.e. [Ctrl-c]), or just q, to interrupt the command and then try this instead:

$ ls -lR / | more

The output will now pause after a screenful has been displayed and you can press the [space bar] to advance the output a screenful at a time. It will take a very long time to get through all of the output so type [Ctrl-c] when you've had enough.

The vertical bar | is called a pipe in Linux and it takes the output from a command or program and feeds it to the input of another. You can think of this like a water pipe taking water from a source to a destination only here it is data that is flowing along the pipe. Pipes are a very important part of Linux but, this is the only time we'll use them here. Suffice it to say, the output of any Linux command can always be controlled by sending it via a pipe to the more program. As well as the more program, we can use less instead to scroll backwards as well as forwards through the output e.g.

$ ls -lR / | less

Remember that in order to scroll backwards type b and to go forwards type f or press the [space bar] (the [up arrow] and [down arrow] keys can also be used to move a line at a time).

Try using the more and less on some of your own commands.

You should now be able to see that using:

$ more filename

is actually just a short hand way of using:

$ cat filename | more

7.4 Summary
===========

    * Text files can be displayed on the terminal window in Linux using a variety of commands. For short files, the cat command will display the entire file in one go whereas, for longer files, the more and less commands commands can be used to scroll through a file.

    * Files that contain executable program code should not be displayed as they can mess up the terminal window.

    * The output from any Linux command can be controlled by feeding it to ether the more or less programs using a pipe (denoted by a vertical bar |).

7.5 Command summary
===================

Command 	Meaning
cat filename 	Display the contents of filename.
more filename 	Display the contents of filename a screenful at a time (scroll forward only).
less filename 	Display the contents of filename a screenful at a time (scroll forward or backwards).
head filename 	Display the first few lines of of filename.
tail filename 	Display the last few lines of of filename.
file filename 	Find out when the likely file type filename

more/less key 	Function
[space bar] or f 	scroll forward a screen
b 	scroll backward a screen
[down arrow] 	move forward one line
[up arrow] 	move backward one line
1G 	go to the first line
G 	go to the last line
NG 	go to line number N
[Ctrl-g] 	print current file position
q or [Ctrl-c] 	quit

.. include:: ../shared/comments.rst