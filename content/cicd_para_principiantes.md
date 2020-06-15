Title: Glosario DevOps
Date: June 15, 2020
Category: SRE

# Glosario Devops

## IaC

[Infrastructure as Code](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-infrastructure-as-code)

IaC se refiere a la definición en código de toda la infraestructura de sistemas, desde redes, load balancers, firewalls, servidores, bases de datos SQL, NoSQL hasta  Elastic Search, Kafka, InfluxDB, etc.

## Herramientas
    
1. [Terraform](https://www.terraform.io/intro/index.html)

Terraform brinda un lenguaje de configuración [HCL](https://www.terraform.io/docs/configuration/syntax.html) abstracto encima de las API de proveedores de nube y datacenter comunes como AWS, Azure, GCP, VMWare, DigitalOcean, OpenStack.

...

Por debajo, Terraform utiliza *providers* para cada nube, y está escrito en Go. 


1. [Ansible](https://www.ansible.com)

Ansible permite actualizar y configurar servidores, dispositivos de red y nubes completas mediante ssh con una configuración sencilla basado en YAML, Jinja y GNU/Linux. 

Está escrito en Python y utiliza Requests.


1. [Chef](https://www.chef.io)

Chef es un sistema de manejo de configuración en Ruby, basado en servidores que manejan un entorno (environment) y configuraciones, y agentes que los despliegan.


1. [Packer](https://www.packer.io) 

Packer de Hashicorp es una herramienta para crear imágenes AMI (AWS), OVF (VMware)...

Se puede partir de un sistema vivo o un .iso y ejecutar un provisioner de forma similar a Terraform, que puede ser Ansible por ejemplo.


1. [Fabric](http://www.fabfile.org)  
 
Fabric es una librería completa en Python para configuración y automatización remota o local del sistema.  
 

1. Jenkins

...  


1. Travis CI  

...  

  
## Configuration Management

##CICD  

*Continuous Integration and Continuous Delivery*  



##PaaS  


##DevOps  

## SDN   

## Software Defined Networking  

##  Site Reliability Engineering (SRE)  

## YAML, JSON
