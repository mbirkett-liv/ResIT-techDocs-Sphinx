6. Manipulating files and directories
*************************************

6.1 Copying, moving and deleting
================================

In Linux, a file can be copied to another file (possibly in a different directory) by using the cp (copy) command. This example will copy a file called plain_file to a new file called another_file in the course directory:

$ ls
c_code  plain_file  progs  r_code  text
$ cp plain_file another_file
$ ls
another_file  c_code  plain_file  progs  r_code  text

You can also use an absolute or a relative pathname to copy a file to another directory e.g.

$ ls -l text
total 32
-rw-r--r-- 1 ian ph  1503 Apr 27 11:19 hamlet.txt
-rw-r--r-- 1 ian ph  7581 Apr 27 11:12 ls_command
-rw-r--r-- 1 ian ph 20204 Apr 27 11:21 rhyme
$ cp plain_file text/more_text
$ ls -l text
total 36
-rw-r--r-- 1 ian ph  1503 Apr 27 11:19 hamlet.txt
-rw-r--r-- 1 ian ph  7581 Apr 27 11:12 ls_command
-rw-r--r-- 1 ian ph    23 May  4 12:00 more_text
-rw-r--r-- 1 ian ph 20204 Apr 27 11:21 rhyme

Unlike in Microsoft Windows, the cp command will not warn you if the "destination" file already exists and it will be overwritten e.g.

$ cp another_file text/more_text 
$ ls -l text
total 36
-rw-r--r-- 1 ian ph  1503 Apr 27 11:19 hamlet.txt
-rw-r--r-- 1 ian ph  7581 Apr 27 11:12 ls_command
-rw-r--r-- 1 ian ph    23 May  4 12:01 more_text
-rw-r--r-- 1 ian ph 20204 Apr 27 11:21 rhyme

It is possible to use the -i (inform) option to warn you about possible overwritting with cp and other commands (e.g. mv, rm). This is generally a bad habit to get into as one day you may forget to use it with disastrous consequences !

Instead of copying, files can also be moved from one directory to another using the mv (move) command e.g.

$ mv another_file text/another_file
$ ls text
another_file  command  hamlet.txt  more_text  rhyme
$ mv text/another_file another_file
$ ls 
another_file  c_code  plain_file  progs  r_code  text
$ ls text
command  hamlet.txt  more_text  rhyme

Where the same filename is used, there is a more succinct method using just the directory part that will save on typing:

$ mv another_file text
$ ls
c_code  plain_file  progs  r_code  text
$ ls text
another_file  hamlet.txt  ls_command  more_text  rhyme
$ mv text/another_file .
$ ls
another_file  c_code  plain_file  progs  r_code  text
$ ls text
hamlet.txt  ls_command  more_text  rhyme

Here the period "." in the second mv command is shorthand for "the current working directory".

Moving one file to another in the same directory has the effect of renaming it e.g.

$ ls 
another_file  c_code  plain_file  progs  r_code  text
$ mv another_file new_name_file
$ ls
c_code  new_name_file  plain_file  progs  r_code  text
$ mv new_name_file another_file
$ ls
another_file  c_code  plain_file  progs  r_code  text

The same comments about overwriting also apply to the mv command - it will not warn you if you are about to overwrite another file but will just go ahead and do it.

In Linux, files and directories can be removed (i.e. deleted) using the rm (remove) command for example:

$ ls
another_file  c_code  plain_file  progs  r_code  text
$ rm another_file
$ ls 
c_code  plain_file  progs  r_code  text

As with cp and mv, the rm command can be used with a pathname e.g.

$ ls text 
hamlet.txt  ls_command  more_text  rhyme
$ rm text/more_text 
$ ls text
hamlet.txt  ls_command  rhyme

What happens if you want to move or copy some files to a new directory ? In this case, you need to create the new directory first using the mkdir (make directory) command. Here's one to try:

$ mkdir new_dir
$ ls -l
total 24
drwxr-xr-x 2 ian ph 4096 Apr 27 11:28 c_code
drwxr-xr-x 2 ian ph 4096 Apr 28 11:52 new_dir
-rw-r--r-- 1 ian ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 ian ph 4096 Apr 27 11:33 progs
drwxr-xr-x 2 ian ph 4096 Apr 27 11:36 r_code
drwxr-xr-x 2 ian ph 4096 Apr 28 11:48 text
$ cp text/rhyme new_dir
$ ls -l new_dir
total 20
-rw-r--r-- 1 ian ph 20204 Apr 28 11:53 rhyme

To remove a directory, the rmdir (remove directory) command can be used however, the directory must be empty first. If the directory contains files (or other directories) you will get a warning as shown below:

$ rmdir new_dir
rmdir: failed to remove `new_dir': Directory not empty
$ rm new_dir/rhyme
$ rmdir new_dir/
$ ls -l
total 20
drwxr-xr-x 2 ian ph 4096 Apr 27 11:28 c_code
-rw-r--r-- 1 ian ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 ian ph 4096 Apr 27 11:33 progs
drwxr-xr-x 2 ian ph 4096 Apr 27 11:36 r_code
drwxr-xr-x 2 ian ph 4096 Apr 28 11:48 text

A more powerful way of removing unwanted directories and files is described in the next section.


6.2 Selecting multiple files using wildcards and recursion
==========================================================

The * wildcard
--------------

So far we have only dealt with copying, moving and removing files one file at a time however, it is always possible to replace a single file by a list of files in the cp, mv and rm commands. For example this will move two of the files in the course directory to the the text directory and back again:

$ mv another_file plain_file text
$ ls text
another_file  hamlet.txt  ls_command  plain_file  rhyme
$ ls
c_code  new_dir  progs  r_code  text
$ mv text/another_file text/plain_file .
$ ls text
hamlet.txt  ls_command  rhyme
$ ls 
another_file  c_code  new_dir  plain_file  progs  r_code  text

(Again, the period "." is shorthand for the current working directory).

This may be OK for small numbers of files but it is going to become very cumbersome if we want to manipulate large numbers of files. Fortunately Linux provides tools that allow us to select possibly thousands of files in a few keystrokes. These are called wildcards. The star "*" wildcard matches zero or more characters in a command so that a* would match all the files begining with the letter a (including just a on its own). The string *z would match all files ending in the letter z (including just z on it's on own) and a*z would match all files beginning with a and ending with z (including just az). A single * on its own will match all of the files in a directory. Here's a more concrete example to try:

The /dev directory contains numerous special files used by the Linux system. Try listing them now:

$ ls  /dev
autofs           fuse       md                  ram6      tty1   tty31  tty53    usbmon2
block            hidraw0    mem                 ram7      tty10  tty32  tty54    usbmon3
bsg              hidraw1    net                 ram8      tty11  tty33  tty55    usbmon4
btrfs-control    hugepages  network_latency     ram9      tty12  tty34  tty56    usbmon5
bus              hvc0       network_throughput  random    tty13  tty35  tty57    usbmon6
char             input      null                raw       tty14  tty36  tty58    usbmon7
console          ipmi0      nvram               root      tty15  tty37  tty59    usbmon8
core             kmsg       oldmem              rtc       tty16  tty38  tty6     vcs
cpu              log        port                rtc0      tty17  tty39  tty60    vcs1
cpu_dma_latency  loop0      ppp                 sda       tty18  tty4   tty61    vcs2
crash            loop1      ptmx                sda1      tty19  tty40  tty62    vcs3
disk             loop2      pts                 sda2      tty2   tty41  tty63    vcs4
...

(You can see the special nature of these files better by using the ls -l command. Note that the format is different to anything we've seen so far.)

Imagine that we want to select just those files starting with tty. Here's how using the * wildcard:

$ ls /dev/tty*
/dev/tty    /dev/tty16  /dev/tty24  /dev/tty32  /dev/tty40  /dev/tty49  /dev/tty57  /dev/tty8
/dev/tty0   /dev/tty17  /dev/tty25  /dev/tty33  /dev/tty41  /dev/tty5   /dev/tty58  /dev/tty9
/dev/tty1   /dev/tty18  /dev/tty26  /dev/tty34  /dev/tty42  /dev/tty50  /dev/tty59  /dev/ttyS0
/dev/tty10  /dev/tty19  /dev/tty27  /dev/tty35  /dev/tty43  /dev/tty51  /dev/tty6   /dev/ttyS1
/dev/tty11  /dev/tty2   /dev/tty28  /dev/tty36  /dev/tty44  /dev/tty52  /dev/tty60  /dev/ttyS2
/dev/tty12  /dev/tty20  /dev/tty29  /dev/tty37  /dev/tty45  /dev/tty53  /dev/tty61  /dev/ttyS3
/dev/tty13  /dev/tty21  /dev/tty3   /dev/tty38  /dev/tty46  /dev/tty54  /dev/tty62
/dev/tty14  /dev/tty22  /dev/tty30  /dev/tty39  /dev/tty47  /dev/tty55  /dev/tty63
/dev/tty15  /dev/tty23  /dev/tty31  /dev/tty4   /dev/tty48  /dev/tty56  /dev/tty7

To select all of the files ending in a 1 we could use:

$ ls /dev/*1
/dev/dm-1     /dev/lp1    /dev/sda1  /dev/tty11  /dev/tty41  /dev/ttyS1    /dev/vcsa1
/dev/hidraw1  /dev/ram1   /dev/sg1   /dev/tty21  /dev/tty51  /dev/usbmon1
/dev/loop1    /dev/ram11  /dev/tty1  /dev/tty31  /dev/tty61  /dev/vcs1

The ? wildcard
--------------

There is another wildcard which will match a single character in a filename - this is the ? wildcard. Say we wanted to list all of the files starting at tty20 and ending at tty29 inclusive. The ? wildcard provides a convenient way of doing this:

$ ls /dev/tty2?
/dev/tty20  /dev/tty22  /dev/tty24  /dev/tty26  /dev/tty28
/dev/tty21  /dev/tty23  /dev/tty25  /dev/tty27  /dev/tty29

Note that the * wildcard could not have been used as it would have matched tty2 as well (plus anything else beginning with tty2 had there been three digit suffixes or more):

$ ls /dev/tty2*
/dev/tty2   /dev/tty21  /dev/tty23  /dev/tty25  /dev/tty27  /dev/tty29
/dev/tty20  /dev/tty22  /dev/tty24  /dev/tty26  /dev/tty28

Wildcards can be used in any Linux command that expects a list of files. This example will copy only files starting with the letter c from the /bin directory (which contains system programs) to our own, newly created, directory (my_bin):

$ mkdir my_bin
$ cp /bin/c* my_bin
$ ls my_bin
cat         cgcreate  cgexec  cgset       chgrp  chown  cpio  cut
cgclassify  cgdelete  cgget   cgsnapshot  chmod  cp     csh

To delete those files starting with cg from my_dir, another wildcard could be used with the rm command:

$ rm  my_bin/cg*
$ ls my_bin
cat  chgrp  chmod  chown  cp  cpio  csh  cut

The rm command, when used with wildcards, can delete numerous files without the operating system giving any kind of warning so handle with care !

Recursion
---------

If you are familiar with using Windows Explorer in Microsoft Windows, you will probably know that it easy to copy or delete an entire folder and all the files and folders "below" it with a few mouse clicks. The same actions can also be performed in Linux using the recursive command option. We have already encountered an example of this earlier with the ls -R command e.g.

$ cd 
$ cd course
$ ls -R 
.:
another_file  c_code  my_bin  plain_file  progs  r_code  text

./c_code:
gif.c  hello.c  integrate.c

./my_bin:
cat  chgrp  chmod  chown  cp  cpio  csh  cut

./progs:
greeting.sh  hello  whats_my_name

./r_code:
initialise.R

./text:
hamlet.txt  ls_command  rhyme

The -R option causes the ls command to list the contents of each and every directory below the current working directory or a specified directory. The same idea can be employed with the cp command to make a copy of all the files below a given directory using the -r option. For example:

$ cp -r my_bin new_bin
$ ls new_bin
cat  chgrp  chmod  chown  cp  cpio  csh  cut

The -r option can also be used with the rm command to delete all of the files below a directory including the directory itself. Here this is used to remove the new_bin directory and all that it contains:

$ rm -r new_bin
$ ls new_bin
ls: cannot access new_bin: No such file or directory

Note that while the recursive option is -R with the ls command, it is -r with cp and rm.

Whilst using wildcards with the rm command can be slightly risky, reckless use of the -r option can be bordering on the suicidal as it possible to wipe out all of your files in a single keystroke (and without any warning being given). The golden rule is therefore:

Think very, very, very, very carefully before using rm -r !

You might be wondering if there is a -r option with the mv (move) command to move a set of files and directories. In fact this isn't usually needed as all that is required is to rename the "uppermost" directory. For example:

$ mv my_bin other_bin
$ ls
another_file  c_code  other_bin  plain_file  progs  r_code  text
$ ls -R other_bin/
other_bin/:
cat  chgrp  chmod  chown  cp  cpio  csh  cut

6.3 Summary
===========

    * In Linux, files and directories need to be removed, copied and moved/renamed using commands entered by the user as there is no graphical application similar to Windows Explorer to do the job. The cp command is used to copy files and the rm command used to remove (delete) files. Files and directories can be moved or renamed using the mv command.

    * For each command, either a relative or absolute pathname can be given and instead of a single file, multiple files (or directories) can be specified.

    * Multiple files can be selected using wildcard characters in file and directory names. The * wildcard matches zero or more characters and the ? wildcard matches a single character.

    * The -r (recursive) option can be used to select all of the files and directories below a named directory including that directory itself.

6.4 Command summary
===================

NOTE: Each file or directory can use a relative or absolute pathname e.g.

/a_dir/another_dir/file1
../another_dir/file2
/a_dir/another_dir/dir1
../parent_dir/dir2

Files in the current working directory do not need the pathname. File and directory names can also contain wildcards to select multiple files/directories.
Copying commands
Command 	Meaning
cp file1 file2 	copy the file file1 to another file file2
cp file1 dir 	copy the file file1 to the directory dir keeping the same filename
cp files dir 	copy the files listed in files (space-separated) to the directory dir keeping the same filenames
cp files . 	copy the files listed in files (space-separated) to the current working directory keeping the same filenames
cp file1 . 	copy the file file1 to the current working directory keeping the same filename
cp -r dir1 dir2 	copy everything in directory dir1 (including itself) to directory dir2
cp -r dir1/* dir2 	copy everything in directory dir1 (excluding itself) to directory dir2 i.e. make a complete copy of dir1
Moving commands
Command 	Meaning
mv file1 file2 	move the file file1 to another file file2 i.e. rename file1
mv file1 dir 	move the file file1 to the directory dir keeping the same filename
mv files dir 	move the files listed in files (space-separated) to the directory dir keeping the same filenames
mv file1 . 	move the file file1 to the current working directory (.) keeping the same filename
mv dir1 dir2 	rename dir1 to dir2 (same as moving everything in directory dir1 to directory dir2)
Removal (deletion) commands
Command 	Meaning
rm file1 	remove the file file1
rm files 	remove the files listed in files (space-separated)
rmdir dir1 	remove the directory dir1 - must be empty first
rm -r dir1 	remove the directory dir1 and everything "below" it. Use with care !!
Wildcards
* 	matches zero or more characters
? 	matches a single character


.. include:: ../shared/comments.rst