5. Files and directories
************************

5.1 Getting more information about files and directories
========================================================

So far we have only dealt with files in passing and have been more concerned with navigating our way around the Linux filesystem. Now though it's time to look at files and directories in more detail so we can see when they were modified, how big they are and who they are owned by (amongst other things). Rather than relying on system files as examples we are going to start with some previously created files which have been bundled together into a ZIP file (ZIP files should be familiar from Windows where they are sometimes referred to as compressed folders). To start with, move to your home directory and unpack the ZIP file using the unzip command (more on this later):

On lxb.liv.ac.uk:

$ cd
$ unzip /opt/software/local/unix_course/files.zip 
Archive:  /opt/software/local/unix_course/files.zip
   creating: course/
 extracting: course/plain_file       
   creating: course/r_code/
  inflating: course/r_code/initialise.R  
   creating: course/progs/
  inflating: course/progs/greeting.sh  
  inflating: course/progs/hello      
  inflating: course/progs/whats_my_name  
...

On condor.liv.ac.uk:

$ cd
$ unzip /opt1/unix_course/files.zip
Archive:  /opt1/unix_course/files.zip
   creating: course/
 extracting: course/plain_file
   creating: course/r_code/
  inflating: course/r_code/initialise.R
   creating: course/progs/
  inflating: course/progs/greeting.sh
  inflating: course/progs/hello
  inflating: course/progs/whats_my_name
...

You can also download this ZIP bundle from this link (42 kbyte).

(If you accidently delete any of the unpacked files while working through these examples, just repeat the above commands to reinstate everything).

The unzip command shows all of the files and directories that have been created as the ZIP file was unpacked. Here everything has been placed "below" the directory called course. To see what's in there, move to the course directory and list its contents:

$ cd course
$ ls
c_code  plain_file  progs  r_code  text

There are actually three directories and one file here although it may not be clear which is which. To see the bigger picture, get a long listing by using the -l (long) option with the ls command:

$ ls -l
total 20
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:28 c_code
-rw-r--r-- 1 smithic ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:33 progs
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:36 r_code
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:22 text

[You should see you own username and group instead of 'smithic' and 'ph' here.]

There is a lot of information presented here which at first sight may seem overwhelming but, by breaking it down bit by bit, things should be come clearer. The first thing to notice is that the very first character on each line which (in this case) is either a 'd' or a dash '-'. This indicates whether the name on the far right corresponds to a file or a directory. A 'd' indicates a directory whereas a dash corresponds to an ordinary file (there are actually other letters which can appear at the start of the line which indicate other special types of file but we won't cover them here).

The next six characters are made up of a combination of 'r', 'w', 'x', and '-' and are called the permissions. These control who can read, modify and delete files and directories. We won't cover this in detail here but will return to it later. The second column, which here contains a 1 or a 2, can also be skipped over the time being. The third column shows the owner of the file (which should should be yourself) and the fourth column indicates the group that the file belongs to.

The size of the file (or directory) in bytes is shown in column five. For large files this can sometimes be difficult to interpret so there is another ls option, namely -h, which will print file sizes in a more human readable format when combined with the -l option e.g.

$ ls -lh
total 20K
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:28 c_code
-rw-r--r-- 1 smithic ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:33 progs
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:36 r_code
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:22 text

K stands for kilobytes, M for Megabytes, and G for Gigabytes. If you see a T, you've got a very big file - it's a Terabyte !!.

The information in columns 6-8 is called the timestamp and shows the time at which the file or directory was last modified (e.g. by editing a file).

The ls command can be used with a pathname (relative or absolute) to list other directories or files. For example, this lists the contents of the directory called text:

$ ls -l text
total 32
-rw-r--r-- 1 smithic ph  1503 Apr 27 11:19 hamlet.txt
-rw-r--r-- 1 smithic ph  7581 Apr 27 11:12 ls_command
-rw-r--r-- 1 smithic ph 20204 Apr 27 11:21 rhyme

By default, ls will sort files and directories alphabetically but,you can also sort by file size using the -S (Size) option e.g.

$ ls -lS text
total 32
-rw-r--r-- 1 smithic ph 20204 Apr 27 11:21 rhyme
-rw-r--r-- 1 smithic ph  7581 Apr 27 11:12 ls_command
-rw-r--r-- 1 smithic ph  1503 Apr 27 11:19 hamlet.txt
$ ls -lSh text
total 32K
-rw-r--r-- 1 smithic ph  20K Apr 27 11:21 rhyme
-rw-r--r-- 1 smithic ph 7.5K Apr 27 11:12 ls_command
-rw-r--r-- 1 smithic ph 1.5K Apr 27 11:19 hamlet.txt

(Note that you can group options together with the ls command so that ls -lSh is equivalent to ls -l -S -h. This is true of most other commands.)

It also possible to sort by modification time using the -t (time) option e.g.

$ ls -l c_code
total 88
-rw-r--r-- 1 smithic ph   190 Apr 27 11:27 gif.c
-rw-r--r-- 1 smithic ph    71 Apr 27 11:28 hello.c
-rw-r--r-- 1 smithic ph 76993 Apr 27 11:26 integrate.c
$ ls -lt c_code
total 88
-rw-r--r-- 1 smithic ph    71 Apr 27 11:28 hello.c
-rw-r--r-- 1 smithic ph   190 Apr 27 11:27 gif.c
-rw-r--r-- 1 smithic ph 76993 Apr 27 11:26 integrate.c

In each case, the sorting order can be reversed using the -r (reverse) option. For example, this would list the most recently modified file last instead of first.

ls -ltr c_code
total 88
-rw-r--r-- 1 smithic ph 76993 Apr 27 11:26 integrate.c
-rw-r--r-- 1 smithic ph   190 Apr 27 11:27 gif.c
-rw-r--r-- 1 smithic ph    71 Apr 27 11:28 hello.c

Before leaving the ls command for now, there is one other important option that may come in useful. The -R (recursive) option will list all of the files and directories in the hierarchy below the current working directory. This is easier to see than to describe, so try this:

$ ls -R
.:
c_code  plain_file  progs  r_code  text

./c_code:
gif.c  hello.c  integrate.c

./progs:
greeting.sh  hello  whats_my_name

./r_code:
initialise.R

./text:
hamlet.txt  ls_command  rhyme

The period "." is shorthand for "the current working directory", so below ".:" are the contents of the current directory, below "./c_code:" are the contents of the c_code directory and so on. The -R option can be combined with other options for example:

$ ls -lhR
.:
total 20K
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:28 c_code
-rw-r--r-- 1 smithic ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:33 progs
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:36 r_code
drwxr-xr-x 2 smithic ph 4.0K Apr 27 11:22 text

./c_code:
total 88K
-rw-r--r-- 1 smithic ph 190 Apr 27 11:27 gif.c
-rw-r--r-- 1 smithic ph  71 Apr 27 11:28 hello.c
-rw-r--r-- 1 smithic ph 76K Apr 27 11:26 integrate.c

./progs:
total 40K
-rwxr--r-- 1 smithic ph   69 Apr 27 11:33 greeting.sh
-rwxr-xr-x 1 smithic ph 6.3K Apr 27 11:29 hello
-rwxr-xr-x 1 smithic ph  26K Apr 27 11:30 whats_my_name

./r_code:
total 4.0K
-rw-r--r-- 1 smithic ph 330 Apr 27 11:36 initialise.R

./text:
total 32K
-rw-r--r-- 1 smithic ph 1.5K Apr 27 11:19 hamlet.txt
-rw-r--r-- 1 smithic ph 7.5K Apr 27 11:12 ls_command
-rw-r--r-- 1 smithic ph  20K Apr 27 11:21 rhyme

Note the ls command uses a capital R for the recursive option whereas other commands use a lower case r.

5.2 Summary
===========

    * The ls (list command) is used to list the contents of directories and, by default, shows the contents of the current working directory. By following the ls command with an absolute or relative pathname, the contents of other directories can be displayed.

    * The -l option is used to display a long listing which contains much more information about file attributes e.g. size and modification time. A number of options can be used to control the way information is displayed in the long listing (see below).

5.3 Command summary
===================

Command 	Meaning
ls 	list the contents of current working directory
ls pathname 	list the contents of the directory (or file) specified by pathname

ls option 	Meaning
-h 	display file sizes in human readable format
-S 	sort by file size
-t 	sort by modification time
-r 	reverses the sorting order
-R 	get a "recursive" listing i.e. list all files and directories below the current working directory (default) or a specified directory


.. include:: ../shared/comments.rst