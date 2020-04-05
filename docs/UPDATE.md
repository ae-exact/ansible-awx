---
sidebarDepth: 3
---

# Backup & Restore

## Why

Users with experience in Ansible Tower Automation operation and maintenance understand the truth: "IT systems can't maintain 100% stability for a long time. Any system may fail, but the probability of failure is different and the degree of harm is different."

When system failure, we first seek the help of a professional to quickly repair and recovery it, but unfortunately, some failure cannot be solved smoothly or even in the expected time period.

Obviously, there is a backup is so important, it can guarantee that the system can be restored to the normal state through the existing backup file when the failure occurs, which means that the huge loss due to the unrecoverable can be avoided.

> Must develop the habit of backup, there is no luck

## How

From the specific backup object, due to the existence of four backup objects on the server: **operating system, environment software, database and application**, each object may have unpredictable failures that cannot be solved as expected.

Based on the backup object, we believe that the following two backup measures are necessary:

### Automation Backup for Instance

Automation Backups for Instance is using the **Snapshot** or **Cloud Server Backup Service** on your Cloud Platform, A snapshot is a full, read-only copy of a disk. You can take a snapshot of an OS or data disk to use as a backup, or to troubleshoot instance issues.

```
- Backup scope: All data on a Disk
- Backup effect: Very Good
- Backup frequency: Automatic backup per hour if you need
- Recovery methond: One key recovery on Cloud platform
- Skill requirement: Very easy 
- Automation or Manual: Fully automated on backup strategy
```

For VM spapshots, refer to RHEV Virtualization Guide.

### Manual backup for application

Manual backup for application is based on the **Exporting source code and database of application** to achieve a minimized backup scheme.

```
- Backup scope: Source code and database of application
- Backup effect: Good
- Backup frequency: You can operate when you need
- Recovery methond: Import
- Skill requirement: Easy 
- Automation: manual
```
The general manual backup operation steps are as follows:

1. Just compression and download the entire **[AWX storage directory](/stack-components.md#awx)** by SFTP 
2. Export AWX's database (Container postresql
docker-compose exec postgres pg_dumpall -U postgres --clean to file ~/awx_pgdumpall_2018-12-14.sql)
3. Backup awx configuration with Tower CLI 
4. Put the source code file and database file in the same folder, named according to the date
5. Backup completed


### Backup awx configuration with Tower CLI 
tower-cli config host http://old-awx-host.example.com
tower-cli config verify_ssl false
tower-cli config username user
tower-cli config password pass
tower-cli receive --all > backup.json


### Export AWX's database 
Container postresql
docker-compose exec postgres pg_dumpall -U postgres --clean to file ~/awx_pgdumpall_2018-12-14.sql

Or separate postresql server
sudo su - postgres
pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

Check pg_hba.conf to match docker ips
/etc/init.d/postgresql restart


##Management, Maintenance and Repair
AWX should self-maintain using the beuilt-in management tasks. However, sometimes manual intervention is required.

### Update  AWX 
Upgrading to a New Version
AWX is frequently updated and not always stable. To work around this, the installation is pinned to a known-good version and should not be updated without testing the new version first. If there is a need to upgrade the version, change the version number in the awx installer/inventory file.

### Cleanup (remove old awx)
Clearing Docker Images
After a failed migration, it is a good idea to clean up all of the old docker images that have been downloaded. Running the following commands will stop the docker containers, remove them, and purge the images from which they were created.

docker stop postgres awx_task awx_web memcached rabbitmq
docker rm -f postgres awx_task awx_web memcached rabbitmq
rm -rf /tmp/awx*

Extra run:
docker stop $(docker ps -q -a)
docker rm $(docker ps -q -a)
docker rmi $(docker images  -q)


--- Upgrade ---
make a new folder for awx installation
mkdir new-awx

cd new-awx
git clone https://github.com/ansible/awx.git

cd awx/installer
pip install docker-compose

ansible-playbook -i inventory install.yml

###  Import data
tower-cli config host http://new-awx-host.example.com
tower-cli config username user
tower-cli config password pass
tower-cli send assets.json

### Links:
https://github.com/ansible/awx/blob/d...
https://tower-cli.readthedocs.io/en/l...
awx migrate tool:
https://github.com/autops/awx-migrate