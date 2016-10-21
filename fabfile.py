from fabric.api import run, sudo, settings, hide
from termcolor import colored


def server():
    with settings(warn_only=False):

        print colored('################################################################', 'red', attrs=['bold'])
        print colored('################################################################', 'red', attrs=['bold'])


        print colored(' ____             _               ____                           ', 'blue', attrs=['bold'])
        print colored('|  _ \  ___   ___| | _____ _ __  / ___|  ___ _ ____   _____ _ __ ', 'blue', attrs=['bold'])
        print colored('| | | |/ _ \ / __| |/ / _ \  __| \___ \ / _ \  __\ \ / / _ \  __|', 'blue', attrs=['bold'])
        print colored('| |_| | (_) | (__|   <  __/ |     ___) |  __/ |   \ V /  __/ |   ', 'blue', attrs=['bold'])
        print colored('|____/ \___/ \___|_|\_\___|_|    |____/ \___|_|    \_/ \___|_|   ', 'blue', attrs=['bold'])

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('                                 xMMMMMMc', 'cyan')
        print colored('                                 xMMMMMMc', 'cyan')
        print colored('                                 xMMMMMMc', 'cyan')
        print colored('                  ......  ...... ;dddddd ', 'cyan')
        print colored('                 oWWWWWWo0NNNNNN,dNNNNNN:                     dOl.', 'cyan')
        print colored('                 dMMMMMMdXMMMMMM,xMMMMMMc                    kMMMWd.', 'cyan')
        print colored('                 dMMMMMMdXMMMMMM,xMMMMMMc                   cMMMMMMO.', 'cyan')
        print colored('                ,,,,,, :xxxxxx;oxxxxxx.:xxxxxx .,,,,,,.           xMMMMMMMO. ....', 'cyan')
        print colored('                .XMMMMMW,dMMMMMMdXMMMMMM,xMMMMMMckMMMMMMc           lMMMMMMMMXNWMWWX0x:.', 'cyan')
        print colored('        .XMMMMMW,dMMMMMMdXMMMMMM,dMMMMMMckMMMMMMc           .0MMMMMMMMMMMMMMMMK.', 'cyan')
        print colored('        .XMMMMMW,dMMMMMMdXMMMMMM,xMMMMMMckMMMMMMc            ;NMMMMMMMMMMMMMWk.', 'cyan')
        print colored(',;;;;;;:dddddddclddddddloddddddclddddddcoddddddl;;;;;;:cldOKWMMMMMMMMMWXOdc.', 'cyan')
        print colored('WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWc''..', 'cyan')
        print colored('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc', 'cyan')
        print colored('WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN;', 'cyan')
        print colored('0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.', 'cyan')
        print colored(':WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd', 'cyan')
        print colored(' dMMMMMMMMMMMMMMMMMMW0KxKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:', 'cyan')
        print colored('  dMMMMMMMMMMMMMMMMMNOKO0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,', 'cyan')
        print colored('   oWMMMMMMMMMWWX0ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.', 'cyan')
        print colored('    .d0o .......    0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc.', 'cyan')
        print colored('      .dOl.          lNMMMMMMMMMMMMMMMMMMMMMMMMMNOc.', 'cyan')
        print colored('        .:odo:.       .lKWMMMMMMMMMMMMMMMMMWKxc,.', 'cyan')
        print colored('            .;dxxxoc:;, .ckXMMMMMMMMWX0xo: .', 'cyan')
        print colored('                     cxOKNWWWWWWNXKOxo; .', 'cyan')

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('              cd.                                ,dc', 'blue')
        print colored('              XMo                                kMW.', 'blue')
        print colored('     .,:cc: . XMo     .;ccc;.           :ccc;.   kMW.   ;;       :llc;.         . ;:,', 'blue')
        print colored('   c0WW0OOKWW0WMo  .dXMN0OOXMNx.    ,OWWKOO0NW:  kMW..dNMO   ,OWMKOk0NMKl.    :0WWK0x', 'blue')
        print colored('  OMXc     .cXMMo  NMO,      xWN;  oMNo.         kMWONWk,   oWNl.     xMMK  .0MK:.', 'blue')
        print colored(' cMW         .WMo OMk         oMN.,MM:           kMMWx.    ;MM;    .lKM0l.  dMX.', 'blue')
        print colored(' cMN.        .NMl 0Mx         lMW.,MM,           kMMWl     :MM,  ,OWM0;     kM0', 'blue')
        print colored(' .KMO'      '0MK. :WWo.      cNMd  xMK;          kMMXMXl.   xMKl0WXd        kM0', 'blue')
        print colored('  .xWMKdooxKMWd.   ,0MWOdlokNMX:    lNMNkdodOK;  kMW.;0MNo   cXMMNxoxOK:    kM0', 'blue')
        print colored('    .;ldxxdl,        .:oxxxo:.        ,ldxxdo;   ,dl    do      cdxxxo;     ;x:', 'blue')

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('                                                                  ', 'blue')
        print colored('                                                                  ', 'blue')

        print colored('===================================================================', 'blue')
        print colored('DEPENDENCIES PROVISIONING                          ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        sudo('yum clean all')
        sudo('yum update')
        sudo('yum install -y gcc glibc glibc-common gd gd-devel wget net-tools git')
        sudo('yum install -y python-devel vim net-tools')
        sudo('yum install -y epel-release')

        print colored('===================================================================', 'blue')
        print colored('INSTALLING PYTHON FABRIC                           ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        sudo('yum install -y python-pip')
        sudo('pip install --upgrade pip')
        sudo('pip install fabric')
        sudo('pip install termcolor')
        sudo('pip install iptools')
        sudo('pip install passlib')

        print colored('===================================================================', 'blue')
        print colored('DOCKER ENGINE PROVISIONING                         ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')

        with settings(warn_only=True):
            docker_version = run('docker -v')
            docker_version.strip()
            if "Docker version" not in docker_version:
                # Run the Docker installation script.
                sudo('curl -fsSL https://get.docker.com/ | sh')
            else:
                print colored('===================================================================', 'blue')
                print colored('DOCKER '+ docker_version + ' INSTALLED          ', 'blue', attrs=['bold'])
                print colored('===================================================================', 'blue')

        # Enable the service.
        sudo('systemctl enable docker.service')
        # Start the Docker daemon.
        sudo('systemctl start docker')
        #Verify docker is installed correctly by running a test image in a container.
        sudo('docker run --rm hello-world')

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