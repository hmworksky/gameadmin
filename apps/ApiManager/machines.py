#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


class Machine(object):

    def __init__(self):
        self.user = self.get_user
        self.ip = self.get_ip
        self.cpuinfo = {
            "cpu_used": self.cpu_used,
        }

    @property
    def get_user(self):
        return self.result('whoami')

    @staticmethod
    def result(cmd):
        return os.popen(cmd).read()

    @property
    def get_ip(self):
        return self.result("ifconfig eth0 |grep 'inet' |awk '{print $2}'")

    @property
    def cpu_used(self):
        return self.result("top -n 1 |grep 'Cpu'|awk '{print $2}'|cut -d '%' -f1")


if __name__ == "__main__":
    m = Machine()
    print(m.user)
    print(m.ip)
