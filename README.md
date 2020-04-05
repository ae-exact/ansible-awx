# AWX automated installation and deployment

Description for Ansible Tower Community Edition[AWX](https://github.com/ansible/awx) automated installer development of language is Ansible. Using this project, users only need to run a command on Linux to automatically install AWX, making the original complicated installation process without any technical threshold. 

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

This project is an open source project, using LGPL3.0 open source agreement.

## Configuration requirements

Install this project to ensure that the following conditions are met:

| condition       | Details       | Note  |
| ------------ | ------------ | ----- |
| operating system       | RHEL 7.x, CentOS7.x, Ubuntu18.04      |    |
| Virtualization|  KVM, VMware, VirtualBox, OpenStack |  |
| server configuration | Minimum 1 core 1G, bandwidth required for installation is not less than 10M |  100M bandwidth is recommended|

## Component

The core components included are: AWX, Docker, Node.jS, etc.

For more information, please see [Parameter Table] (/docs/zh/stack-components.md)

## Is the latest version of AWX installed in this project?

This project uses the official Docker installation method. The official regularly releases the latest Docker image. Deploying this project is the latest stable version officially released by AWX.

We will regularly test this project to ensure that users can install it smoothly.  

The latest version number of AWX [View Address] (https://github.com/ansible/awx/releases)

## Installation Guide

Log in to Linux and run the following ** command script ** to start the automated deployment, and then wait patiently until the installation is successful.

```
#After logging in as a non-root user, you need to be elevated to root first
sudo su-

#Automated installation commands
wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/master/scripts/install.sh; bash install.sh -r awx

```

** Notes during installation: **   

1. Inadvertent operation or changes in the network may cause the SSH connection to be interrupted and the installation will fail. Please reinstall at this time
2. The installation is slow, stagnant or unreasonably interrupted, mainly due to the download problem caused by the network failure (or the network speed is too slow), please reinstall at this time

There are many reasons why it cannot be installed smoothly, please use the deployment method of [AWX image] (https://apps.websoft9.com/awx) that we released on the public cloud


## Documentation

Documentation link: https://support.websoft9.com/docs/awx/zh

## FAQ

-What is the difference between command script deployment and image deployment? Please refer to [image deployment-vs-script deployment] (https://support.websoft9.com/docs/faq/zh/bz-product.html#image deployment-vs-script deployment)
-Does this project support running on Ansible Tower? stand by

## To do

* Random passwords for applications and databases
* Supports deployment on Amazon Linux
