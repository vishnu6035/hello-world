# playbook for installing apache

- name: installing apache
  hosts: all
  become: yes
  tasks:
    - name: install apache
      apt:
        name: apache2
        state: present
