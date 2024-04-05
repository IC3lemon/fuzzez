#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

useradd -m ansible
echo "ansible:ansible_test" | chpasswd

mkdir -p /home/ansible/syzkaller
mkdir -p /home/ansible/Kernel
mkdir -p /home/ansible/Img
mkdir -p /home/ansible/config
chown -R ansible:ansible /home/ansible

usermod -aG kvm ansible

echo "User ansible created with password ansible_test, necessary folders created, and added to kvm group for qemu access."
