3. The Linux command line
*************************

3.1 Entering and editing Linux commands
=======================================

We've already encountered one Linux command in the form of exit but now it's time to try a few more so log back into lxb (or any other system you want to use). You should see something like this displayed in the terminal window::

	[smithic@lxb ~]$

Try pressing the [Return] key a few times and you should see this repeated::

	[smithic@lxb ~]$
	[smithic@lxb ~]$
	[smithic@lxb ~]$

This is called a command prompt and whenever you see some text followed by the dollar sign ($), it means that the operating system is waiting for you to type in a command to tell it what to do next. The details of the text will differ between systems but in this case the following are displayed: your username (mine is "smithic") followed by the name of the system. Finally the working current working directory is printed (more about this later). Since just pressing the [Return] key doesn't actually tell the operating system to do anything, it will just come back begging for more like an obedient hound dog.

Here are a couple of commands to try out that will actually do something (no need to memorise them - they are just for practise). First, to see who is currently logged into the system, type who followed by [Return] i.e. ::

	$ who

(Note that you must press [Return] after typing each command for it to be "sent" to the operating system. Also remember not to type the $ as it's just a convention).

At the time of writing, I get this output but you will probably see a lot more users::

	smithic      tty1         2016-03-11 11:54
	smithic      pts/0        2016-04-11 14:47 (uxa.ac.uk)

To find out the current date and time, try this::

	$ date

Here's couple of other commands to try - can you tell what they do? ::

	$ whoami
	$ uname
	$ uptime

ANSWERS HERE

You can now see that Linux commands are generally concise and often somewhat cryptic. This is because they were designed to be easy to type rather than easy to remember. Linux systems also support a large number of commands (lxb has 2132!) and it can be difficult to find meaningful names for all of them. This may seem off-putting but most non-specialist Linux users can probably get by with a couple of dozen commands or less which are fairly easy to remember.

Most Linux commands you use will actually consist of the command name itself and then one or more options. Try using the --help option with the who command to see what options are available::

	$ who --help

(We'll cover more about getting online help in a later section).

If you happen to mistype a command (and assuming the typo doesn't correspond to another valid command), the operating system will reply with something like::

	$ whomia
	-bash: whomia: command not found  

It is however possible to correct commands before pressing [Return] if you spot the mistake first. To do this you can use the [left arrow] and [right arrow] keys to move the cursor and the [Del] or [backspace] key to remove characters before inserting others (by default the terminal should be in "insert" mode rather than "overtype"). The [Home] key can be used to move to the beginning of the command and the [End] key to the end of it. If you make a complete mess of a command, it is possible to erase the entire line by typing [Ctrl] and u together (i.e. [Ctrl-u]). Try correcting the above mistyped command or try correcting some of your own.

If you see a series of gibberish symbols when using any of the cursor keys then something is wrong with your setup and you should contact your system administrator.

Having to type in the same or similar commands over and over again can become labourious so Linux makes it easy to recall and reuse previous commands by pressing the [up arrow] key (remember that you can edit the command before pressing [Return] to create a command similar to a previous one). Try pressing the [up arrow] key to recall previous commands and enter them by pressing [Return], then try editing them before pressing [Return]. You can "scroll" back and forwards through your command "history" by using the [up arrow] and [down arrow] keys. Only a limited number of commands are stored (which varies from system to system) so eventually they will start to repeat. To see a list of recently entered commands use this command::

	$ history

Linux can actually do a lot more with the command history and here's another tip if you are feeling ambitious. Type [Crtl] and r together (i.e. [Ctrl-r]) and then the first few letters of a previously entered command. Once the operating system finds an unambiguous match for the letters you have typed in so far, it will complete the rest of the command for you. This is very useful for recalling commands without having to scroll back through the entire history.

We are not going to cover all of the command editing and recall features of Linux here and there is just one more important feature to be aware of before we complete this section. Imagine you are running a program or a Linux command which is taking an extremely long time to complete (maybe it has a bug and is stuck in an infinite loop) and you wish to stop it. To do this type [Ctrl] and c together (i.e. [Ctrl-c]) to interrupt the program and have Linux return you to the command prompt where you can continue typing in other commands.

Some users may be tempted to just shut down the terminal window and then log back in and start again. This is very bad practise as the command/program may continue to run even after you have terminated your Linux session

Here's a quick example to help illustrate the point. Try entering this command::

	ls -lR /

This will attempt to list every single file on the Linux system which will take an EXTREMELY long time to complete. You should see screenfulls of filenames scolling by and to interrupt this and get back to the command prompt type [Ctrl-c].

The [Ctrl-c] interrupt has another use where an incomplete command has been entered and Linux is waiting for the user to type in the rest of it. This is easier to show than explain so try typing this command::

	$ echo "here is some text to be printed"

you should see::

	here is some text to be printed

(this may seem a fairly pointless command but it is useful in Linux command programs called scripts).
Now try just typing the first part of the command followed by [Return] and you should get something like this::

	echo "here is some
	>

The greater than (>) symbol is called the secondary command prompt and means that the system is waiting for the rest of a command to be entered before it can continue. You now have two choices: either enter the rest of the command or type [Ctrl-c] to interrupt it and get back to the (primary) command prompt. Here's what you should get in both cases with the [Ctrl-c] one second::

	$ echo "here is some
	> text to be printed"
	here is some
	text to be printed
	$

	echo "here is some
	> ^C
	$

(^C is where [Ctrl-c] was typed)

This is fairly trivial example but as a new user you may find that it is sometimes difficult to figure out what it is that Linux is expecting in order to complete a command. No need to worry though - typing [Ctrl-c] will always get you out of trouble!

3.2 Summary
===========

    * In Linux, commands are typed in a terminal window to tell the operating system what it is you want done rather than clicking on icons and menu items as in Microsoft Windows etc.

    * When the command prompt ($) is displayed, it means that the operating system is waiting for instructions from the user. If it disappears, then this means that Linux is busy for example running a program or command.

    * Linux commands can be edited using the standard cursor control keys used for word processing i.e. the arrow keys, the [Del] and [backspace] keys and the [Home] and [End] keys. Editing is done in "insert mode" by default.

    * You can erase a command completely by typing [Ctrl] and u together (i.e. [Ctrl-u]).

    * Previously entered commands can be recalled with the [up arrow] key. Use the [up arrow] and [down arrow] keys to "scroll" back and forwards through the list of previous commands.

    * To see a list of previously entered commands, use the history command.

    * Long running commands or programs can be interrupted by typing [Ctrl] and c together (i.e. [Ctrl-c)]) to return you to the command prompt. This can also be used to abandon an incomplete command where Linux is waiting for the rest of it to be entered (this is indicated by the > prompt).

3.3 Command summary
===================

Command 	Meaning
history 	display a list of previously entered commands

.. include:: ../shared/comments.rst