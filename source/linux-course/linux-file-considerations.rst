8. Other file considerations
****************************

8.1 Home and temporary filestores
=================================

So far we've outlined how to list files, how to move, copy and remove them and how to display and modify files. However, there are some other important things to consider in a Linux system which which supports several simultaneous compared to a single user PC.This includes where users are allowed to store their files, how much space is reserved for them and what permission they have to access other users' files.

Users are typically assigned an area of the overall filesystem where they can store their files called their home filestore. After logging in, users are usually placed in the "root directory" of this which is called their home directory. From here, they can create directories and files at will.

Home filestores are ultimately stored on one or more hard disks which obviously have only finite space available. This is shared between users and often each user is allocated a fixed portion of the overall space called their disk quota. The quota allocated to each user varies from system to system (contact your system administrator for details) but is typically only on the order of a few GB. The home filestore on lxb is actually physically on a different server and is shared with lxc and several other Linux systems, that is transparent to, but convenient for, most users.

On most of the centrally managed Linux servers, and particularly on the HTCondor and Barkla systems, the home filestore quota is no way near enough to accomodate the large files that are used in a typical application and for this reason a special "alternative home directory" is available for your use. On the HTCondor system, the pathname for this is /condor_data/your-username. On all of the other centrally managed systems, the pathname for this is /volatile/your-username. On lxb, this sits on a fairly large (9.5 TB) and fast disk which is ideal for application data. In summary then:

Do not use your home filestore for HTCondor jobs, use the HTCondor data disk
(/condor_data/your-username) instead.

Do not use your home filestore for lxb/lxc or Barkla jobs, use the volatile area instead:
(/volatile/your-username) instead.

There are no per-user limits on the amount of space on /condor_data or /volatile that users can take up but please do not abuse this liberal approach and always...

Remove any files you no longer need in /condor_data/your-username and /volatile/your-username .

If you are unsure about how much space you are using or how much is available, the following commands are useful. To find how much space is available on a filesystem use:

$ df -vh directory_name

e.g.

$ df -vh /condor_data/your-username

$ df -vh /volatile/your-username

To see all of the filesystems, just omit the directory_name.

The amount of storage you are currently using can be found with this command:

$ df -vh /condor_data/your-username

$ df -vh /volatile/your-username

This may take a while to complete if you have a large amount of files while it works its way through them, adding up the sizes.

A good way of remembering these commands is:

df - amount of disk free
du - amount of disk used

On most systems, users' home filestores are safely backed up so that if you accidently delete or overwrite a file, the original can be recovered from the backup (contact your local system administrator for details). On HTCondor however, because the HTCondor data disk is so large, backups are not kept of it. Similarly, on Barkla, because /volatile is so large, backups are not kept of it on any of the systems - hence the name "volatile". Bearing this in mind it is important to:

Keep a backup of any important results you have in /condor_data/your-username or /volatile/your-username in a safe place.

As well as your home filestore, most Linux systems provide another area of storage where users can store files temporarily. This is the /tmp (short for temporary) filesystem, If you think of your home filestore as an area of land reserved solely for your own use, then /tmp is analagous to common land that all users have access to. Although all users can copy files to /tmp or create new ones there, the operating system will prevent you from deleting or overwriting files owned by others.

Typically /tmp may only hold a few GB of data of storage and /tmp filesystems are not backed up as they are only intended for the short term storage of files. These should of course be deleted when you no longer need them to free space for others.

8.2 Permissions
===============

In a system that supports multiple users it important that users cannot, accidently or otherwise, delete or alter files owned by others. Furthermore, there may be files that users do not want others to be able to read and system files that only the system administrator should have access to. Conversely, there may be files and programs which users wish to share with others - perhaps other members of their research group.

In Linux, these conflicting demands are met by permissions which govern which users have access to files and directories and the type of access granted to them. This could be the ability to read a file/directory, modify/delete a file/directory or run a program. Earlier we briefly mentioned permissions in the section on listing files. To recap, go back to the course directory and try listing the files there using the long format:

$ cd ~/course
$ ls -l
-rw-r--r-- 1 smithic ph   23 May  4 11:59 another_file
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:28 c_code
drwxr-xr-x 2 smithic ph 4096 May  5 14:29 other_bin
-rw-r--r-- 1 smithic ph   23 Apr 27 11:22 plain_file
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:33 progs
drwxr-xr-x 2 smithic ph 4096 Apr 27 11:36 r_code
drwxr-xr-x 2 smithic ph 4096 May  5 10:45 text

The very first character in the first column shows whether the name on the right corresponds to a file (indicated by a dash -) or a directory (indicated by a d). The next nine characters are the permissions which are grouped into three sets of three (see figure). The first set are the so-called user permissions which are the permissions the owner of the file/directory has. The middle set of three characters are the group permissions which control how users in your group can access the file/directory (more about groups below) and the final set of set of three characters are the others permissions i.e. the access rights for everyone else on the system outside the owner and the group.

The characters in each set of three always come in the same order which is rwx and the presence of a letter means that permission is granted whereas a dash means that it is denied. A typical example is shown in the figure below:
permissions (20K)

The letters have slightly different interpretations for files and directories which are summarised below:

File permissions
----------------

letter	permission	meaning
r 	read permission 	able to display the contents of a file but not necesarily change it
w 	write permission 	able to modify a file or overwrite it
x 	execute permission 	able to run an executable program

Directory permissions
---------------------

letter	permission	meaning
r 	read permission 	able to list the contents of a directory
w 	write permission 	able to delete/modify files in a directory or add files to it
x 	execute permission 	able to access files in a directory

In order to a read file in a particular directory, you will need read permission on that file plus read and execute permission on the directory (in fact you will need this on all of the parent directories as well).

If you are getting a migraine with all of this, then a few examples should make things clearer. Look at the files in the course example and in particular the one called plain_file which has these permissions: -rw-r--r--

This means that you can modify or delete the file and read it since the user permissions are rw-. People in your group could possibly read the file as the group permissions are r--. The same goes for other users outside the group whose permissions are again r--. In reality, you as the owner are the only user able to read this file as ultimately the permissions are restricted by those of your home directory:

ls -ld ~
drwx------. 68 your_username ph 4096 Jun 23 14:55 /home/your_username

(the d option is used to show information about the directory itself rather than the files in it).

Notice that while you can do anything you want under your home directory (as shown by the rwx), no one else has permission to do anything (as shown by the two sets of --- for the group and others permissions).

Executable programs need the execute permission (x) set which you can see in this example from the course directory.

$ ls -l progs
-rwxr--r-- 1 smithic ph    69 Apr 27 11:33 greeting.sh
-rwxr-xr-x 1 smithic ph  6417 Apr 27 11:29 hello
-rwxr-xr-x 1 smithic ph 26280 Apr 27 11:30 whats_my_name

(Stictly speaking you need read permission set as well for shell script programs such as greeting.sh).

Try running one of the programs now (more on this later) e.g.

$ progs/hello
Hello World

Remember the /tmp directory that all users have access to ? Here's its permissions:

$ ls -ld /tmp
drwxrwxrwt. 15 root root 4096 Jun 23 06:14 /tmp

This shows that everyone can do anything here as the user, group and others permissions are all rwx. (The t at the end, sometimes called the sticky bit, stops this being a free-for-all and means that you cannot delete or modify another user's files in /tmp).

To find out which group(s) you belong to, use the id (identity) command e.g.

$ id
uid=41269(smithic) gid=15(man) groups=15(man),65533(condor)

(uid stands for user ID and gid for group ID. The numbers can be ignored).

You can be a member of several groups at the same time but only one primary group which is shown in the gid field above. All HTCondor users are members of the condor group which is grants them access to the server. The permissions on /condor_users/your_username are the same as for your ordinary home filestore so other users cannot access your HTCondor job files. If you would like your group membership changed, you will need to contact your system administrator.

The permissions of any files that you own can be altered by using the chmod command (unfortunately this is one of those command names that seems to have been plucked out the air with no sensible way of remembering it). The general format of the command is:

$ chmod permissions_options file_or_directory

One of three characters is used to represent the set of users the command applies to which are:
letter	meaning	applies to
u 	user 	the file owner
g 	group 	members of the same group
o 	other 	users outside of the owner and group

A plus sign + is used to add permissions and minus sign - is used to remove them. For example, to allow read access to other members of your group you would use:

$ chmod g+r file_or_directory

To remove write pemission for users outside of your group use:

$ chmod o-w file_or_directory

You can also set the permissions explicitly. For example to allow read and write permission for yourself to a file, use:

$ chmod u=rx file

To set read-only permission for your group members:

$ chmod g=r file_or_directory

The chmod command can be tricky to master at first so do experiment with it on a few files/directories and check that the permissions are set correctly using ls -l (or ls -ld).

8.3 Running programs
====================

So far we have not really mentioned how to run programs in detail but infact most, if not all, of the commands we have come across so far correspond to actual programs which have been written by software developers and incorporated into the operating system. You can find out the actual location of the program file corresponding to a command by using the which command e.g.

$ which pwd
/bin/pwd
$ which du
/usr/bin/du

If you get a long listing of these files, you should see that they have the executable and read permissions set for all users:

$ ls -l /bin/pwd
-rwxr-xr-x 1 root root 31656 Oct 14  2014 /bin/pwd
$ ls -l /usr/bin/du
-rwxr-xr-x 1 root root 99168 Oct 14  2014 /usr/bin/du

(Note that only the system administrator who has the user name root can modify these files).

A few things that seem like commands do not correspond to actual programs at all but are just short cuts to real commands. Thse are called aliases. You can get a list of them using the alias command (ll is common one for long listing). Some command programs are also included in the command line interpreter and are called shell built-ins.

How does the operating system know where to find these programs when you enter a command ? The answer is that it searches a preset list of directories called the search path. You can see this list by using this command:

$ echo $PATH
/sbin:/bin:/usr/sbin:/usr/bin:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin

(This is for lxb - the search path is likely to be different on other systems).

The search path on lxb/lxc (and Barkla) can be altered so that users can access particular application software (e.g. MATLAB, ABAQUS) using the module command. The web page on lxb software has more details but try typing module avail to see what is available.

Notice how both the /bin and /usr/bin directories are contained in the search path which are the locations of the pwd and du commands used above. Normallly there is no need to worry about the search path but if you want to run your own program(s), you will need to give the path to the program explicitly as either a relative or absolute pathname. This is because it will not be included in the default search path. Here are some examples:

$  ~/course/progs/greeting.sh
Hello ! You are logged in as your_username on Thu Jun 30 14:54:33 BST 2016.

(remember the ~ is shorthand for your home directory)

$ cd ~/course
$ progs/whats_my_name your_username

To run a program in your current working directory you will still need a pathname to it e.g.:

$ cd ~/course/progs
$ ./hello
Hello World

(Remember that "." is shorthand for the current working directory.)

This trips up many users accustomed to Windows since Windows always includes the current working directory in the search path. If you try to run any of these programs without specifying the path to them you will get an error e.g.:

$ hello
-bash: hello: command not found

As mentioned earlier, you need to have both read and execute permission on the file containing the program to be able to run it. You can add these permissions with:

$ chmod u+rx my_program

(This is easy to forget !).

8.4 Transferring files to/from a Linux machine
==============================================

As a Linux user doing real work, you will typically be running programs that take in data from one or more input files, process it and then write the results to one or more output files. This being the case, you will need some way of uploading the input files to the Linux machine and downloading the output to your desktop. This is provided by something called secure file transfer protocol (SFTP) or by secure copy (SCP).

Here, a protocol is just a set of rules for exchanging data and secure means that the data are sent in an encrypted ("scrambled") format to prevent eavesdropping.

The easiest way to use scp (or sftp) on Windows is to use the built-in command. To do this, first open a Command Prompt by clicking on the icon on the desktop or by searching for it by typing cmd in the search box in the lower left hand corner of the desktop. You can also click [Windows]+r then type cmd.

The general form of the command is:

scp remote-username@remote-hostname:remote-filename local-filename

to download a file or to upload a file:

scp local-filename remote-username@remote-hostname:remote-filename

For example this would download the file hello from the folder ~/c_course/progs/ on lxb to the local folder \download on the M: drive (recall that the tilde ~ stands for the home directory).

Note that the Duo two-factor authentication is needed in this case. Here is another example where a file called main.py is uploaded from the
folder \python_test on the M: drive to the directory ~/python on lxb.

You can also download and upload multiple files at once by using the wildcard ("*") character to match their names.

If you have a lot of files in different locations to transfer, then it probably quicker to use the sftp command in the Command Prompt. This has the general form:

sftp remote-username@remote-hostname

There isn't space to describe to operation of this fully here but you can get a list of commands by typing help once connected. There is also a guide available here.

Both scp and sftp can be used on a Mac or on any Linux system. A more powerful graphical interface for transferring files is available on Windows called MobaXterm which is described below. This has other functionality including a way of logging into systems using the X Windows graphical interface and is available on Install University Apps.

MobaXterm
---------

MobaXterm can be downloaded and installed from:

http://mobaxterm.mobatek.net

or installed directly on the MWS from Install University Apps via:

Start -> Install Uni Apps -> Utilities -> MobaXterm 21.1

A MobaXterm icon should then appear on your desktop. Start MobaXterm by double-clicking on the icon and the following window should appear:

To use the SFTP client, click on Session icon in the upper left corner of the window (highlighted below) and then click on the SFTP icon as indicated below:

In the Remote Host box, type the name of the server you wish to connect to, for example condor.liv.ac.uk and enter your username in the Username box...

...and you will then be prompted for your password

You can then transfer files to/from condor by highlighting them and dragging them to/from the local PC and remote host panes as shown below:

Unfortunately MobaXterm appears not to be working on lxb or lxc due to problems with Duo authentication.

Bundling files for uploading and downloading
--------------------------------------------

If you have a large amount of input and/or output files to transfer between your PC and a remote machine such as HTCondor, then selecting each of them can be cumbersome and prone to error. Here it is often easier to bundle the files together into a ZIP format file which can be uploaded or downloaded in one action.

For example, say you have a number results files called results0.mat, results1.mat, restults2.mat ... which are to be downloaded. These could first be bundled into a single ZIP file (say all_results.zip) using a command similar to this:

$ zip all_results.zip results*.txt

The ZIP format file can then be downloaded easily and the individual files extracted. To extract the files in Windows, select the ZIP file in Windows Explorer then right-click and select Extract All...

A similar method can be used to upload the input files. First copy the input files to an empty folder on the PC. Then right-click on the folder name and select Send To | Compressed (zipped) folder and enter the ZIP file name. After uploading the ZIP format file, the individual files can be extracted with the unzip command e.g.

$ unzip input_files.zip

Mac and Linux users should find that the zip and unzip programs are available from the command line and there may be other graphical tools to do the job as well.

8.5 Summary
===========

    * On shared Linux systems, users are generally allocated a fixed portion of the overall storage available called their home filestore which is usually in /home/your-username. This is unsuited to HTCondor and users should treat /condor_data/your-username as their home filestore for HTCondor jobs. Similarly on Barkla, /volatile/your-username should be used for data files.
    
    * On many systems, users' home filestore is periodically backed up safely so that deleted files can be recovered. On HTCondor backups of the HTCondor data disk are not kept so users should ensure that they have their own backups of important data in /condor_data/your-username. Similarly on Barkla, lxb and lxc, users should keep a copy of any important data held on /volatile/your-username .

    * Access to other user's files (including programs) is governed by file permissions. By changing these file permissions using the chmod command, users can allow or deny access to files to other users.

    * All users belong to at least one Linux group to allow sharing of files amongst members. Only your system administrator can change or add to your group membership.

    * To run a program in Linux, you will in general need to have read and execute permission on the file containing it. System programs can be run without the need to specify a path to them (as there is a default search path to them) however, to run your own programs you will need prefix it with an absolute or relative path (use ./my_program_name to run programs in your current working directory).

    * Files can be transferred to and from a Linux server by using a piece of software called a secure file transfer protocol (SFTP) client. On Windows this is provided by via the Command Prompt as the scp and sftp commands and a graphical interface called MobaXterm is available on MWS. Mac and Linux users can make use of the command line sftp program or there may be other graphical applications available.

    * If you wish to move large numbers of files, it may be easier to bundle them into a ZIP file first. The zip and unzip Linux command can be used to create and extract ZIP files respectively.

8.6 Command summary
===================

Command 	Meaning
df -vh 	show how much space is free on all filesystems
df -vh directory 	show how much space is free on the filesystem containing directory
df -vh ~ 	show how much space is free on the filesystem containing your home filestore
du -sh directory 	show how space is used by all files below directory
du -sh ~ 	show how much space has been used in your home filestore
echo $PATH 	show the search path
id 	show your group membership (identity)
chmod permissions_options file_or_directory 	change permissions on the file_or_directory (see below for an explanation of the options)
zip zip_file files 	create a ZIP file called zip_file from the list of files given in files (can contain wildcards)
unzip zip_file 	extract zip_file
unzip -l zip_file 	list the contents of zip_file without extracting it (useful for checking first)

chmod options

chmod commands have the general form:

chmod <applicability><action><permissions> file(s)_or_directory(s)

<applicability> contains one or more of these characters:
u 	applies only to the owner ("user")
g 	applies to members of the group
o 	applies to everyone outside the group ("others")

<action> consists of one of these symbols:
+ 	add permission(s)
- 	remove permission(s)
= 	set permission(s)

<permissions> contains one or more of these characters:
r 	read permission
w 	write permission
x 	execute permission


.. include:: ../shared/comments.rst
