###############
Troubleshooting
###############

****
SSH
****

SSH is used to communicate with VM's so you will need an SSH server enabled on each virtual machine. This is
often the case by default with many *\*nix* installations, but may have to be installed separately.

***************
Port Forwarding
***************

An attempt will be made to forward the configured guest SSH port on each VM to a unique port on the host if such a port
forwarding does not already exist. This only needs to be done once per virtual machine and can only occur if the VM is
in a *stopped* state. If the automatic port forwarding fails, you can configure it yourself using your virtualizer.

*************
Elevated User
*************

Most guests will require elevated access (i.e. *sudo*) to run updates. Make sure the account you use can run as an
elevated user.

****************
PyCrypto Install
****************

If you get a PyCrypto build error during installation please see the `paramiko install docs
<http://www.paramiko.org/installing.html#pycrypto>`_.
