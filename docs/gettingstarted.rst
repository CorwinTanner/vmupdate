###############
Getting Started
###############

************
Installation
************

The recommended installation tool is **pip**:

.. code-block:: bash

    $ pip install vmupdate

*************
Configuration
*************

Create a custom configuration file *vmupdate.yaml*:

.. code-block:: yaml

    Credentials:
      Username: myuser
      Password: mypass

.. note:: This method is included for simplicity, but is not recommended due to the inherent insecurity
    of a plaintext password. See :doc:`configuration` for more options.

*******
Command
*******

And pass the path to the utility:

.. code-block:: bash

    $ vmupdate --config "/path/to/config/vmupdate.yaml"
