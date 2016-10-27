from fabric.api import run, sudo, settings, hide, cd
from fabric.contrib.files import exists
from termcolor import colored


def server():
    with settings(warn_only=False):
        sudo('yum install -y git python-devel epel-release python-pip')
        sudo('pip install --upgrade pip')
        sudo('pip install fabric')
        sudo('pip install termcolor')
        sudo('pip install iptools')
        sudo('pip install passlib')
        with cd('/home/vagrant'):
            if exists('/home/vagrant/proton', use_sudo=True):
                with cd('/home/vagrant/proton'):
                    sudo('fab -R local install_docker_centos7')
            else:
                run('git clone https://github.com/exequielrafaela/proton.git')
                with cd('/home/vagrant/proton'):
                    sudo('fab -R local install_docker_centos7')

        with cd('/lemp_dcker_demo'):
            run('docker-compose up -d')

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