# Vagrant_PyFab-Docker
*_Basic Fabric implementation usign Vagrant to deploy a VM equiped with a Docker Toolbox in place Docker Engine + Docker Compose + Docker Machine._*

*In this repo you'll find the Vagrant file and its python fabric provisioning file.*

<p align="center">
  <b>Some Related Links:</b><br>
  <a href="#">https://docs.docker.com/engine/installation/</a> |
  <a href="#">https://docs.docker.com/compose/install/</a> |
  <a href="#">https://docs.docker.com/machine/install-machine/</a> |
  <a href="#">http://docs.fabfile.org/en/1.12/</a>
  <br><br>
  <img src="https://github.com/exequielrafaela/Vagrant_PyFab-Fabric/blob/master/Figures/fabric_pyenv.png" img>
  <img src="https://github.com/exequielrafaela/Vagrant_PyFab-Docker/blob/master/Figures/Docker-logo-and-type.png" img> 
</p>

Also refer for the standard vagrant docker provision and docker-compose plugin provision in the this repo: https://github.com/exequielrafaela/Vagrant_Docker-LocalDev for a better understanding. What we have add here is the provisioning of this docker modules with our configuration management tool PROTON (https://github.com/exequielrafaela/proton). We make use of the function install_docker_centos7 => Install Docker Engine, docker-compose, docker-machine.


