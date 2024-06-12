4 The Linux filesystem
**********************

4.1 Finding your way around the Linux filesystem
================================================

In Linux as with other operating systems such as Windows and Mac OS, data is stored in entities called files and these files are then held in other containers called directories (a directory is the Linux term for a folder). Directories can contain other directories so that files can be arranged in a hierarchical structure called a filesystem making it easier for the user to locate them. So far, so simple but in Linux every single file on the system is contained within the same overall hierarchy. This is in contrast to Windows where files located on different devices are labelled with a different drive letter. For example, files on your local hard disk are usually on the C: drive. If you insert a DVD or CD, the files on it may appear to be on the D: drive. Files on pen drives may be accessible through other drive letters such as E: and then there could be files located remotely on servers which use so-called "logical" drive letters - e.g. the M: drive used to store users' files on the MWS.

In Linux there are no drive letters and every file on the system (plus some things that don't actually seem to be files) is accessed through a common directory structure (a few examples will make this clearer in a minute). To beginners this may make the Linux filesystem seem a vast and confusing place where it's easy to get lost. Not to worry though, it is not necessary to understand the whole system to begin with and you can get to know it a small amount at time. Think of it in the same way as moving to a new town. There will be places you need to know how to get to (for example home and work), some places that are handy to know (e.g. where the shops are) and some places that you may rarely if ever need to go to (such at the refuse tip). Similarly in Linux, you will need to know where you can store your own files, possibly where to access other user's files and where you can store temporary files. Usually there is no need to concern yourself with the location of system files.

When using a Linux system via the command line, it is essential to know where you are in the filesystem and to be able to move around it by entering a few simple commands. This is because we do not have a nice graphical interface to find our way around as provided by, for example, Windows Explorer. Without further ado it's time to try out these commands.

If you are not already logged in to lxb, log back in again and try this command:

$ pwd

You should see something like:

/home/your-username

(Where your-username is the username you are logged in with).

The pwd stands for print working directory and this is the directory you are currently residing in. Any copying, moving or editing of files will, by default, act on files in the current working so it is clearly important to make sure that you are in the correct working directory before making any changes. The message printed in response to the pwd command is an example of a pathname which succinctly describes how to locate a given directory or file on the system from a fixed starting point.

Going back to the new town analogy, this is like asking for directions to where you want to want to go from a fixed starting point - say the main railway station. Instead of walking along various different streets to get to want, we move from one directory to another starting at a special directory called the root directory. The root directory is the only directory on a Linux system which is not contained in any other directory. Diagrammatically, the Linux filesystem has a tree like structure similar to that shown below.
filesystem (32K)

(This is a very much simplified version - to see this as a very broad and short tree you need to imagine it upside down ! A more more detailed diagram can be found here).

Only a few of the most important directories typically found are shown and of these we are just going to concentrate on the /home directory for now. This contains directories in which individual users (in this example abby27, biomech and crozon) can store their files and modify them at will and each user has their own home directory. When you first login to lxb, you will be placed in your home directory to begin with which is what the pwd command printed above. Try the command again:

$ pwd
 /home/your-username

What this is saying is that to reach your home directory we start at the root directory (labelled '/') move to the directory called /home and then move to /home/your-username. In other words this is the path from the root directory to your home directory hence the term pathname.

Note that in Linux the forward slash '/' is used to separate directories in pathnames whereas Windows/DOS uses the backslash '\'.

To list the files and directories in a directory, the ls (list) command is used. Try it now:

ls

Initially there will be no files of your own in your home directory so the response will be blank but we'll soon get to some more useful examples.

You can change your current working directory by using the cd (change directory) command. Try using this to move "up a level" and then use the ls command to see other users' home directories i.e.

$ cd /home
$ pwd
/home
$ ls 
abby27        cc0u8268  frant     jcsharp     mihasan   robertwi  sgjkella  slcouls
abdulkj       cc0u9274  fred      jflatley    mingli    robpoole  sgjmoffa  slurm
abisav4       cc0u9277  fsartor   jinzhou     mkidd     rsaleh    sgjmoral  smaskell
acarver       cdfsweb   gbarakos  jjangulo    momlejb2  rsavage   sgjzha21  smithic
...

(The output shown here has been truncated as denoted by the ellipses ...)

You should be able to see your own username in there. Now try moving to the root directory and seeing what's there:

$ cd /
$ pwd 
/
$ ls 
bin     deptbck2  etc   lib         media  net   rdfs  scratch  srv  usr       volatile2
boot    dev       gnu   lib64       misc   opt   root  selinux  sys  var
cgroup  dumpa     home  lost+found  mnt    proc  sbin  spool    tmp  volatile

(Most of these directories contain system files.)

Notice how each time you change directory, the command prompt will show you the final part of your current working directory (the tilde symbol (~) stands for your home directory).

So far we have been moving around the filesystem using something called an absolute path which is the list of "directions" starting from the root directory however, this isn't always the easiest way of finding our way around. Go back to the new town example again and imagine someone asking you for directions near where you live. Giving directions from say the main railway station (an absolute path) is not likely to be very useful and instead what's needed are directions from your current location. The Linux term for this is a relative path. Here's how we might get back to our home directory using relative pathnames and starting at the root directory:

$ cd /
$ pwd 
/
$ cd home
$ pwd 
/home
$ cd your-username
/home/your-username

Here we've moved a single directory at a time but we can move in as many or as few steps are we like. This does it on one:

$ cd /
pwd
/
$ cd home/your-username
$ pwd 
/home/your-username

At first sight the difference between an absolute and relative pathname might seem confusing but just remember this golden rule:

An absolute pathname gives the path to a file or directory from the root directory (/) and always starts with a forward slash (/),

A relative pathname gives the path to a file or directory from the current working directory and never starts with a forward slash (/).

There is another special relative pathname denoted by '..' which stands for the parent of the current working directory. This is easier to see with an example so here's one starting at your home directory:


$ cd /home/your-username
$ cd ..
$ pwd 
/home
$ cd ..
$ pwd
/

Each time the command cd .. is used, we move to the parent of the current working directory. You can think of this as moving "up a level" each time in the diagram shown above. As before you don't have to move one step at time. For example:


$ cd /home/your-username
$ cd ../..
$ pwd 
/

You can also combine the parent directory with the name of a directory contained in it e.g.

$ cd /volatile/your-username
$ pwd
/volatile/your-username
$ cd ../smithic
$ pwd 
/volatile/smithic

You can think of this as moving up a directory and then down one again but all in one step.

Armed with the cd, pwd, and ls commands, you should now be free to explore the Linux filesystem on your own so give it a try. Before that though, there is another cd command which will be useful which is just the cd command on its own i.e.

$ cd

Wherever you are in the filesystem, this will always return you to your home directory immediately. You may like to think of this and pwd as:

Help I'm lost - where am I ?

$ pwd

Help I'm lost - take me home straightaway

$ cd

There is actually another special pathname that can be useful. The tilde (~) represents your home directory and can be used to access files and directories there without typing the whole path. For example this would list files in a directory called mydir contained in your home directory: $ ls ~/mydir. This would be the same as: $ ls /home/your-username/mydir

Before leaving the cd command, there is one final feature of it that is also useful. The command cd - will return you to your previous current working directory. Again this is best shown by an example:


$ cd /home/your-username
$ pwd
/home/your-username
$ cd /bin
$ pwd
/bin
$ cd -
$ pwd
/home/your-username

... and so on and so on. You might like to think of this as working similarly to one of the buttons on a television remote control which flips back and forwards between channels (only here it is with directories).

Typing long filenames and directory names can be time consuming and error prone and so a keyboard short cut provides a way of cutting down on the typing. Try typing a command such as ls then the first couple of letters of a pathname or filename (you may need to prefix it by ./ for ones in your current working directory). Then press the [Esc] key twice i.e. type [Esc] [Esc]. The operating system will respond by completing the rest of the filename for you provided that it is a unique match. If there are multiple filenames with the same starting letters, as much of the filename as possible will be completed. By pressing [Esc] followed by =, you can see a list of all of the filenames which match and you can then type a few more letters before trying [Esc][Esc] again to complete the filename. Using a combination of [Esc] [Esc] and [Esc] = can make it much quicker to locate files especially where long pathnames are involved.

4.2 Summary
===========

    * In Linux, files are contained within directories (equivalent to folders in Windows) which themselves can contain directories. There is a single directory which is not contained in any other called the root directory and denoted by a forward slash: /

    * Files located on different disk drives and other devices appear under the same hierarchical structure and there is no concept of a drive letter as with Windows (e.g. the C: drive usually refers to the main hard disk).

    * The location of each file and directory is given by something called an absolute pathname which specificies which directories must be traversed in order to find it e.g. ::

		/a_directory/a_n_other_directory/a_file

    or

		/a_directory/a_n_other_directory/final_directory

    Absolute pathnames always begin with a forward slash (/).

    * A relative pathname gives the path to a file or directory from the current working directory and never starts with a forward slash (/) e.g. ::

		a_n_other_directory/final_directory

    or

		../a_directory/final_directory

    * By default all changes take effect in the current working directory which can be found using the pwd command.

    * Usually, users are placed in their home directory when they first log in. This is the area reserved for them for moving, copying, creating and modifying files and directories.

    * The current working directory can be changed by using the cd command.

    * Files and directories are listed using the ls command.

4.3 Command summary
===================

Command 	Meaning
pwd 	print working directory ("where am I ?")
ls 	list files and directories (by default in the current working directory)
cd pathname 	change working directory to pathname where pathname is an absolute or relative path
cd .. 	move to the parent directory ("go up a level")
cd ../dir 	move to a directory contained in the parent ("go up and then down a level")
cd 	change working directory to the home directory ("take me home")
cd - 	return to the previous working directory



.. include:: ../shared/comments.rst