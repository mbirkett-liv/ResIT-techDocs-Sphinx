2. First steps
**************

2.1 Introduction and Registration
=================================

The main general purpose Linux service provided by IT Services is based on two servers designated lxb.liv.ac.uk and lxc.liv.ac.uk (lxb and lxc for short). These systems are basically identical and each contain two 8 core processors with 256 GB of memory. If one seems to be running slowly then try logging in to the other one. The service is primarily aimed at staff and postgrads and to access it, you will first need to register. To do this, open a web browser and go to the Service Now portal at:

https://liverpool.service-now.com/sp

Click on the Request icon:

Then enter "Unix" in the search box at the top.

You should then see a link marked "Unix request for staff and research students" so click on this and enter your details.


Alternatively you can try this direct link: Unix request for staff and research students

The Research IT division provides two special purpose platforms for postgrads and staff namely the Barkla Cluster for high performance computing and the HTCondor service for high throughput work. These also require users to register before use. To do this, again go to the Service Now portal and click the Request icon as above. Then search for "high performance".

Click on the link marked "Application to access high performance/throughput computing facilities (staff)":

Then enter your details:

Alternatively you can try this direct link: Application to access high performance/throughput computing facilities (staff)

Note that "Parallel Linux cluster" refers to the Barkla HPC cluster. A central Linux service account (lxb/lxc) should be set up automatically for you when applying for these systems so there is no need to register separately.

2.2 Logging in
==============

Microsoft Windows
-----------------

There a number of ways you can login to a remote Linux server under Windows but by far the easiest is to use the built in Windows ssh client. To use this, first open a Command Prompt by clicking on the icon on the desktop or by searching for it by typing cmd in the search box in the lower left hand corner of the desktop. You can also click [Windows]+r then type cmd.

At the command prompt you will need to type in a command to login to the required server. This has the general form:

ssh remote-username@remote-hostname

where remote-username is your username on the remote server - this will usually be the same as your standard MWS username, in which case it may be omitted. For example, to login to lxb.liv.ac.uk:

If you see a warning such as this, just type yes.

The lxb and lxc hosts employ Duo two-factor authentication and so require an additional step to login:

To login to the one of the other systems, use one of the following commands as appropiate (replace username with your own username):

ssh username@lxc.liv.ac.uk
ssh username@condor.liv.ac.uk
ssh username@barkla.liv.ac.uk

The built-in ssh client described above works well in most circumstances but you may want to move to a more powerfull application once you've gained confidence with Linux. This is called a terminal emulator because it mimics the actions of an old style "dumb" terminal used to access UNIX systems (unfortunately Linux still doesn't understand how to talk to a PC properly). There are a range of these available however, the one we will use here is called PuTTY (we'll cover a more advanced one called MobaXterm in a later section). If you are on a Managed Windows System PC, you can install this directly by clicking:

(Start) -> Install University Apps -> Internet -> PuTTy 0.77

or if you are off-campus, you can install it from the web at:

http://www.putty.org/

Once PuTTY has been installed, you should see a PuTTY icon appear on the desktop. Double-click on it to start a PuTTY "session" and the following Window should appear:
puty_grab (50K)

In the box marked "Host Name", enter the host name of the system you wish to connect to. (this is for lxb but you could enter lxc.liv.ac.uk, condor.liv.ac.uk or barkla.liv.ac.uk for other systems). A terminal window as shown below should appear and you will now be prompted for your username and password. These will usually be the same as for your MWS/email account.

terminal (12K)

Using a Mac or a Linux/UNIX machine
-----------------------------------

If you are using a Mac or a Linux (or other UNIX) based machine then there is no need to install a terminal emulator and you can login straight away using a built in program called ssh (secure shell). To do this, open a terminal window end enter the a command such as:

$ ssh -l your-username@condor.liv.ac.uk

where your-username is your standard MWS username. You will then be prompted for your password which will be the same as for the MWS.

Access from off-campus
----------------------

Accessing HTCondor and Barkla (and most local systems) from outside the campus firewall is slightly more difficult as direct connections are not allowed for security reasons. There are three ways around this, namely:

    connect firstly to lxb.liv.ac.uk or lxc.liv.ac.uk and then ssh to the local system
    use Apps Anywhere
    establish a virtual private network (VPN) connection first

Details of how to use Apps Anywhere are available on the CSD website at:

https://www.liverpool.ac.uk/csd/apps-anywhere

Once you have logged in to Apps Anywhere, add PuTTY to your applications group (if necessary) and start the PuTTY app. You can then login as above. Incidently, if you see a security warning about an untrusted certificate pop up, just click on the "Yes" option.

If Apps Anywhere is not available, you can still login by establishing a virtual private network (VPN) connection first and then logging in as above. Details of how to use the VPN are available on the CSD website at:

https://www.liverpool.ac.uk/csd/vpn/

2.3 Logging out
===============

To logout of Condor and finish your Linux "session", use the following command:

$ exit

It is also possible to end your session by simply closing the terminal window however this is bad practise and should be avoided. You may read in some texts that it's also possible to logout by typing [Ctrl] and d together (i.e. [Ctrl-d]). This is also best avoided although it's something to be aware of in the unlikely case that you do it accidently.

2.4 Summary
===========

    The easiest way to access a Linux server using a Microsoft Windows based machine is to open a Command Prompt and use the ssh command.,

    A terminal emulator such as PuTTY provides a more flexible and powerful interface on Windows but needs to be installed first.

    A terminal emulator is not necessary for the Mac or if you are already logging in from a Linux or other UNIX system. Instead, the ssh command can be used instead.

    Local systems can be accessed from off-campus but you will need to use Apps Anywhere or set up a virtual private network (VPN) connection first.

    To logout and end your Linux sesssion, type exit.

2.5 Command summary
Command 	Meaning
ssh 	login to a remote Linux system
exit 	end your Linux session - i.e. logout


.. include:: ../shared/comments.rst