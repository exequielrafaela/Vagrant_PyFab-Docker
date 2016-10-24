from fabric.api import run, sudo, settings, hide, cd
from fabric.contrib.files import exists
from termcolor import colored


def server():
    with settings(warn_only=False):
        with cd('/home/vagrant'):
            if exists('/home/vagrant/proton', use_sudo=True):
                with cd('/home/vagrant/proton'):
                    sudo('fab -R local install_docker_centos7')
            else:
                with cd('/home/vagrant/proton'):
                    run('git clone https://github.com/exequielrafaela/proton.git')
                    sudo('fab -R local install_docker_centos7')

        print colored('===================================================================', 'blue')
        print colored('FIREWALL - NAT TABLE STATUS:                       ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            fw = sudo('iptables -t nat -L')
        print colored(fw, 'red')

        print colored('===================================================================', 'blue')
        print colored('FIREWALL - FILTER TABLE STATUS:   ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            fw = sudo('iptables -L')
        print colored(fw, 'red')

        print colored('===================================================================', 'blue')
        print colored('## NETWORK CONFIGURATION #', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            netconf = sudo('ip addr show')
        print colored(netconf, 'yellow')