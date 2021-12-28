#!bin/bash
systemctl unset-environment MYSQLD_OPTS
systemctl restart mysqld
exit