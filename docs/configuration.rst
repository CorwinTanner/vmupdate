#############
Configuration
#############

Configuration is at the root of **vmupdate** and as a user you can override virtually all of the utility's
functionality to suit your needs. For most purposes setting up the `Credentials`_ will be sufficient. To
override the configuration (including ``Credentials``) for specific VM's see `Machines`_.

You can pass a custom config file as follows:

.. code-block:: bash

    $ vmupdate --config "/path/to/config/vmupdate.yaml"

.. note:: Nested keys will be merged, but values will be replaced. Thus, when modifying a list make sure
    to include any original list items that you wish to keep.

*************
Specification
*************

===========
Credentials
===========

The ``Credentials`` section is used for options relating to authentication and access. These options will be used
for all VM's unless specifically overridden (see `Machines`_).

.. code-block:: yaml

    Credentials:
      Username: myuser
      Password: mypass
      Use Keyring: true
      Run As Elevated: true

Username
    The username used to authenticate with the VM. Defaults to ``root``.
Password
    The password used to authenticate with the VM. Defaults to ``null``.
Use Keyring
    Whether to use the host's keyring to access the password. See `Using the Keyring`_ for more details. Defaults to
    ``true``.
Run As Elevated
    Whether to use an elevated user mode when running commands against the VM. This will be required by most guest
    operating system configurations. Defaults to ``true``.

.. warning:: Setting a password in plaintext is generally insecure. Use of the keyring is encouraged.

=======
General
=======

The ``General`` section is used for miscellaneous options.

.. code-block:: yaml

    General:
      Wait After Start: 30
      Wait Before Stop: 10

Wait After Start
    Time in seconds to wait after starting the VM. Defaults to ``30``.

Wait Before Stop
    Time in seconds to wait before stopping the VM. Defaults to ``10``.

=======
Network
=======

The ``Network`` section is used for options relating to SSH endpoints. These are advanced options and generally don't
need to be modified.

.. code-block:: yaml

    Network:
      SSH:
        Guest:
          Port: 22
        Host:
          Ports:
            Min: 49152
            Max: 65535

----
SSH
----

Guest Port
    SSH port of the guest. Defaults to ``22``.
Host Ports
    Range of ports to be used on the host for forwarding SSH to the guest. Defaults to ``49152 - 65535``.

================
Package Managers
================

The ``Package Managers`` section is used for configuring package managers on guest operating systems. These are advanced
options and generally don't need to be modified.

.. code-block:: yaml

    Package Managers:
      Ubuntu:
        apt-get:
          - update -y -u -q
          - upgrade -y -u -q

This example configures the utility to run ``apt-get`` with the ``update`` and ``upgrade`` commands on guests
running ``Ubuntu``.

======
Shells
======

The ``Shells`` section is used for configuring :mod:`~vmupdate.shells` for communicating with the guest operating system. These are
advanced options and generally don't need to be modified.

.. code-block:: yaml

      Shells:
        Ubuntu: Posix

This example configures the utility to use the :class:`~vmupdate.shells.Posix` shell to communicate with guests
running ``Ubuntu``.

========
Machines
========

The ``Machines`` section is used for overriding the configuration for specific virtual machines.

.. code-block:: yaml

      Machines:
        My Machine:
          Username: myuser
          Password: mypass
          Use Keyring: true
          Run As Elevated: true
          Shell: Posix
          Ignore: false

Username
    The username used to authenticate with the VM.
Password
    The password used to authenticate with the VM.
Use Keyring
    Whether to use the host's keyring to access the password. See `Using the Keyring`_ for more details.
Run As Elevated
    Whether to use an elevated user mode when running commands against the VM. This will be required by most guest
    operating system configurations.
Shell
    Which shell to use for communicating with the guest operating system.
Ignore
    Whether to skip the machine for updating. Defaults to ``false``.

``My Machine`` is the name of the virtual machine as listed in the virtualizer.

============
Virtualizers
============

The ``Virtualizers`` section is used for configuring :mod:`~vmupdate.virtualizers` that may be found on the host. These
are advanced options and generally don't need to be modified.

.. code-block:: yaml

    Virtualizers:
      Windows:
        VirtualBox:
          - $PROGRAMW6432\Oracle\VirtualBox\VBoxManage.exe
          - $PROGRAMFILES\Oracle\VirtualBox\VBoxManage.exe

This example configures the utility to search for :class:`~vmupdate.virtualizers.VirtualBox` on ``Windows`` hosts
at the listed paths. The first path found will be used.

.. note:: ``$[ENVAR]`` in the paths will be expanded using environment variables on the host.

********
Examples
********

=================
Using the Keyring
=================

The keyring of your host is the most secure place to store the password(s) used by the utility.

.. note:: Keyring lookup is by label and username. Both must match to retrieve the password.

-------------------
General Credentials
-------------------

In your config file:

.. code-block:: yaml

    Credentials:
      Username: myuser
      Use Keyring: true

Then in your keyring provider, set the password using the label ``vmupdate`` and your chosen username. This will act as
the default authentication profile for all virtual machine connections.

-------------------
Machine Credentials
-------------------

You may have different credentials for a specific machine.

In your config file:

.. code-block:: yaml

    Machines:
      My Machine:
        Username: myuser
        Use Keyring: true

Then in your keyring provider, set the password with the label as your machine name (``My Machine`` in the example).
This will override the authentication profile for this machine.
