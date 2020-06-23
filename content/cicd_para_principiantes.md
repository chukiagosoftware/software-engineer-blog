Title: Glosario DevOps
Date: June 15, 2020
Category: SRE

## Glosario Devops


### Los Conceptos


#### IaC

[Infrastructure as Code](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-infrastructure-as-code)

IaC se refiere a la definición en código de toda la infraestructura de sistemas, desde redes, load balancers, firewalls, servidores, bases de datos SQL, NoSQL hasta  Elastic Search, Kafka, InfluxDB, etc.


#### Configuration Management

El manejo estructurado y deliberado de la configuración de un sistema (GNU Linux o Microsoft)

    
#### CICD  

   *Continuous Integration and Continuous Delivery*  
   
   La integración y distribución continua y abarca desde el git push, hasta que el usuario puede ver o utilizar los resultados del cambio en código.
   
   El objetivo central es lograr la agilidad, escala y confiabilidad para desplegar apps o microservicios en la nube, altamente disponibles para un teórico público de millones.
   
   Un breve ejemplo: este sitio web está creado con [Netlify](http://www.netlify) 


#### PaaS  

   La Plataforma como un Servicio es un concepto que entra en su segunda década renovado con IaC/CICD/SDN y hasta IoT.  
   
   En los remotos 2000, un PaaS significaba Debian, Ubuntu, CentOS o incluso Windows Server configurado en máquinas virtuales, con imágenes preconfiguradas para cada tech stack, y un paquete de scripts.  Es decir tenías C++, Java, Python, PHP, MySQL/Postgres, Javascript y alguna forma de crear/modificar un espacio de trabajo nuevo. 
   
   Esto es un servicio utilizado por desarrolladores, para implementar/arquitectar/probar sistemas.
   
   
#### IaaS

   La infraestructura como servicio es el negocio de AWS, Goocle Cloud Platform, Azure, Rackspace, DigitalOcean y varios otros.  Dejemos que ellos hagan lo suyo.
   
   En realidad, cualquier organización puede tener IaaS, generalmente es equivalente al ingeniero de sistemas que configura todo.

#### DevOps  

   La combinación de Desarollo y Operaciones.  Podemos escribir un libro, pero nah.


####  SDN   

*Software Defined Networking* se refiera a eso, la definición de redes en software. 

A diferencia de IaC o la nube donde podemos definir, es cierto, recursos como un Firewall o un Router.

En SDN, la configuración de routers, switches, FW, balanceo de carga etc. se define en un código centralizado y manejado, ciertamente con Configuration Management.

#### Site Reliability Engineering (SRE)  

Oof  :laughing: 

Todo lo anterior, y lo de abajo también. Lo principal es que no duermes mucho.        
     
     
### Las Herramientas
    
1. [Terraform](https://www.terraform.io/intro/index.html) :metal:

    Terraform brinda un lenguaje de configuración [HCL](https://www.terraform.io/docs/configuration/syntax.html) abstracto encima de las API de proveedores de nube y datacenter comunes como AWS, Azure, GCP, VMWare, DigitalOcean, OpenStack.

    ...

    Por debajo, Terraform utiliza *providers* para cada nube, y está escrito en Go. 
    
1. [Ansible](https://www.ansible.com) :metal:
    
    Ansible permite actualizar y configurar servidores, dispositivos de red y nubes completas mediante ssh con una configuración sencilla basado en YAML, Jinja y GNU/Linux. 
 
    Está escrito en Python y utiliza Requests.   
    
1. [Chef](https://www.chef.io) :+1:

    Chef es un sistema de manejo de configuración en Ruby, basado en servidores que manejan un entorno (environment) y configuraciones, y agentes que los despliegan.

1. [Packer](https://www.packer.io) :+1:

    Packer de Hashicorp es una herramienta para crear imágenes AMI (AWS), OVF (VMware)...

    Se puede partir de un sistema vivo o un .iso y ejecutar un provisioner de forma similar a Terraform, que puede ser Ansible por ejemplo.

1. [Fabric](http://www.fabfile.org) :metal:
 
    Fabric es una librería completa en Python para configuración y automatización remota o local del sistema.  
 
1. Jenkins :point_up:

    El estándar industrial para la automatización del desarrollo. Jenkins inició como un soporte para pipelines de integración contínua en Java. Ahora corre la mitad del Internet
    
    ...  

1. Travis CI :hand:

   Integración continua, como un servicio. Quizás, la alternativa más conocida a Jenkins.
   [https://travis-ci.org/](https://travis-ci.org/)

1. Kubernetes

   Algo sobre orquestas y containers y YAML.
   
1. Nomad

   Más containers, más YAML. O JSON, alguien quiere JSON?

1. Vagrant

   ...
   
1. JSON

   Javascript Object Notation.  Así, feo como suena.

1. YAML :notes:
        
       id: 0
       name: un archivo YAML contiene datos
       que_no_es: "Yaml Ain't a Markup Language"
       url: "https://yaml.org"
       una_lista: 
         - Los Beatles
         - Radiohead
         - Rolling Stones
         - Café Tacuba
       diccionario:
         calle13: Residente
         cadillacs: Vicentico
       muchas_lineas: |
         "En la Escuela de Computación Poética de Nueva York no importan 
         los resultados, sino la experimentación. 'Hardware', programación
         y arte son los tres pilares de este centro educativo en el que la
         poesía se fusiona con el código." 
       linea_larga: >
         Marx
         Keynes
         Friedman
         esto es
         todo
         la misma 
         linea?