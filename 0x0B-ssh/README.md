### introduction

# SSH

SSH (Secure Shell) is a network protocol used to securely connect to a remote server and interact with it as if you were sitting in front of it. This means you can run commands on a remote server as if you were logged into it.

The SSH protocol uses a client-server architecture, where the client is the machine you're using to connect to the server, and the server is the machine you're connecting to.

The SSH client is responsible for connecting to the server, authenticating the user, and then establishing a secure connection between the client and server. Once this is done, the client can run commands on the server, and the output from those commands will be sent back to the client.

The SSH server is responsible for authenticating the user, and then allowing the user to run commands on the server.

In this project, we'll be implementing an SSH client that can connect to an SSH server and run commands on that server.

## Resources

# Read or watch:

[What is a (physical) server - text](https://www.linode.com/docs/platform/billing-and-support/linode-beginners-guide/#what-is-a-server)
[What is a (physical) server - video](https://www.youtube.com/watch?v=lDojBPZ77Z8)
[SSH essentials](https://www.ssh.com/ssh/essentials/)
[SSH Config File](https://linuxize.com/post/using-the-ssh-config-file/)
[Public Key Authentication for SSH](https://www.ssh.com/ssh/public-key-authentication/)
[How Secure Shell Works](https://www.ssh.com/ssh/how-it-works/)
[SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)](https://www.youtube.com/watch?v=hTCHv6BT6ZA)

# For reference:

[Understanding the SSH Encryption and Connection Process](https://www.ssh.com/ssh/encryption/)
[Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
[IETF RFC 4251 (Description of the SSH Protocol)](https://tools.ietf.org/html/rfc4251)
[Internet Engineering Task Force](https://www.ietf.org/about/about-ietf/about-ietf-org)
[Request for Comments](https://www.rfc-editor.org/about/rfc-index.html)
[man or help: ssh](https://linux.die.net/man/1/ssh)
[man or help: ssh-keygen](https://linux.die.net/man/1/ssh-keygen)
[env](https://www.computerhope.com/unix/uenv.htm)

## General

What is a server
Where servers usually live
What is SSH
How to create an SSH RSA key pair
How to connect to a remote host using an SSH RSA key pair
The advantage of using #!/usr/bin/env bash instead of /bin/bash

# Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

# General

Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
The second line of all your Bash scripts should be a comment explaining what is the script doing
