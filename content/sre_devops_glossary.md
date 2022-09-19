Title: Glosario DevOps
Date: June 15, 2020
Category: SRE
Tags: DevOps, IaC, CICD, PaaS, SRE
Summary: A Glossary of DevOps and SRE-related tools and terminology

## Los Conceptos

#### IaC

[Infrastructure as Code](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-infrastructure-as-code)

IaC se refiere a la definición en código de toda la infraestructura de sistemas, desde redes, load balancers, 
firewalls, servidores, cluster de Kubernetes, bases de datos, servicios, etc. Generalmente cuando decimos IaC hoy en 
dia nos referimos a Terraform pero igual puede ser Ansible, Cloud Formation, Azure Resource Manager / Bicep, etc.


#### Configuration Management

El manejo estructurado y deliberado de la configuración de un sistema (GNU Linux o Microsoft). Esto se realiza 
mediante algo como Ansible, Terraform y Git, Subversion. Es decir, la configuración se almacena en un repositorio 
dedicado a ese propósito y actualizado regularmente.

    
#### CICD  

Continuous Integration and Continuous Delivery, or Continous Deployment es la integración y distribución continua 
de un paquete de software. Abarca desde el git push inicial en Dev, hasta que el usuario puede interactuar o ver los 
resultados del cambio en código.

El objetivo central es lograr la agilidad, escala y confiabilidad para desplegar apps o microservicios en la nube 
altamente disponibles para un teórico público de millones y con varios equipos trabajando en diferenes componentes.

Un breve ejemplo: este sitio web está creado con [Netlify](http://www.netlify.com)

#### PaaS  

La Plataforma como un Servicio es un concepto que entra en su segunda década renovado con IaC/CICD/SDN y hasta IoT. 
En los remotos 2000, un PaaS significaba Debian, Ubuntu, CentOS o incluso Windows Server configurado en máquinas 
virtuales, con imágenes preconfiguradas para cada tech stack, y un paquete de scripts.  Es decir tenías C++, Java, 
Python, PHP, MySQL/Postgres, Javascript y alguna forma de crear/modificar un espacio de trabajo nuevo. Esto es un 
servicio utilizado por desarrolladores, para implementar o probar idea y prototipos.
   
   
#### IaaS

La infraestructura como servicio es el negocio de AWS, Goocle Cloud Platform, Azure, Rackspace, DigitalOcean y 
varios otros. Dejemos que ellos hagan lo suyo.

En realidad, cualquier organización puede tener IaaS, generalmente es equivalente al ingeniero de sistemas que 
configura todo.

#### DevOps  :loop:

La combinación de Desarollo y Operaciones. Por ejemplo, conjugar el Gitflow de ingenieros de software con el testing 
y QA, el monitoreo y el troubleshooting realizado por equipos de Operaciones, Soporte, Producto.

#### Gitflow :hourglass_flowing_sand:

Git flow es la práctica de gestionar el Unit Testing, Functional Testing o Continuous Integration de un paquete de 
software a partir de uno o varios repositorios de código que automáticamente generan pruebas y estatus a partir de 
cada Push de cambios. Esto se realiza con Webhooks estilo Github-Gitlab u otros mecanismos, la cosa es que sea 
automático, rápido y a prueba de balas :bullettrain_front: 

Generalmente, se utiliza en branches de desarrollo, prueba y staging para luego pasar el código 
verificado a main y ponerlo en producción mediante Continous Deployment.


####  SDN   

*Software Defined Networking* se refiera a eso, la definición de redes en software. 

A diferencia de IaC o la nube donde podemos definir, es cierto, recursos como un Firewall o un Router.

En SDN, la configuración de routers, switches, FW, balanceo de carga etc. se define en un código centralizado y manejado, ciertamente con Configuration Management.

#### Site Reliability Engineering (SRE)  

Site Reliability Engineering es la arquitectura de nube e infraestructura de software para resiliencia, 
disponibilidad, escalabilidad y observabilidad. Involucra desde las herramientas de desarrollo, el stack de software 
y componentes, hasta las bases de datos, las redes y VPC en la nube, peering, y el monitoreo de rendimiento mediante 
logs, trazas y alertas oportunas. 
     

## Las Herramientas

#### [Terraform](https://www.terraform.io/intro/index.html) :metal:

Terraform brinda un lenguaje de configuración [HCL](https://www.terraform.io/docs/configuration/syntax.html) 
abstracto encima de las API de proveedores de nube y datacenter comunes como AWS, Azure, GCP, VMWare, DigitalOcean, 
OpenStack.  Hashicorp Configuration Language o HCL es el idioma de Terraform y se parece algo a C en su syntaxis, y 
a Python en su lógica.

Por debajo, Terraform utiliza *providers* para cada nube, y está escrito en Go. 
    
#### [Ansible](https://www.ansible.com) :metal:
    
    Ansible permite actualizar y configurar servidores, dispositivos de red y nubes completas mediante ssh con una configuración sencilla basado en YAML, Jinja y GNU/Linux. 
 
    Está escrito en Python y utiliza Requests.   

#### [Chef](https://www.chef.io) :+1:

    Chef es un sistema de manejo de configuración en Ruby, basado en servidores que manejan un entorno (environment) y configuraciones, y agentes que los despliegan.

#### [Packer](https://www.packer.io) :+1:

    Packer de Hashicorp es una herramienta para crear imágenes AMI (AWS), OVF (VMware)...

    Se puede partir de un sistema vivo o un .iso y ejecutar un provisioner de forma similar a Terraform, que puede ser Ansible por ejemplo.

#### [Fabric](http://www.fabfile.org) :metal:
 
    Fabric es una librería completa en Python para configuración y automatización remota o local del sistema.  
 
#### Jenkins :point_up:

    El estándar industrial para la automatización del desarrollo. Jenkins inició como un soporte para pipelines de integración contínua en Java. Ahora corre la mitad del Internet
    
    ...  

#### [Travis CI](https://travis-ci.org/)

    Integración continua, como un servicio. Quizás, la alternativa más conocida a Jenkins.  

#### Kubernetes

Kubernetes es un software poderoso para orquestar o gestionar varios hasta miles de workloads de software 
simultáneamente, 
compartiendo recursos como ser VM's en la nube, bases de datos, espacio de red lógica y separando datos y flujos 
mediante namespaces. 
   
Kubernetes permite desarrollar rápidamente en base a microservicios o monolitos con múltiples instancias, abstraer 
la infrastructura de base como ser CPU, Memoria, IO y regular el uso de la misma en base a cuota y observación en 
tiempo real. Muchos o la mayoría de grandes servicios en Internet hoy en día corren sobre Kubernetes.

#### Nomad

Nomad es la antitesis de Kubernetes, es decir es un software para orquestrar microservicios y servicios a gran 
escala en base a un binario de menos de 100MB, contrapuesto a Kubernetes que son como 10 componentes.

Aún así, la idea básica es la misma, YAML para configuración, Consul o un service mesh para coordinar servicios y 
capacidad para distribuir la carga de varios servicios y paquetes en CPU, Memoria e IO compartida de nube.

#### Vagrant

Una herramienta para virtualizar o correr software de nube o servidor localmente para pruebas. Esto es similar a 
Minikube, Docker Compose, etc. que permiten correr contenedores Docker en VM o laptop. 

#### JSON

    Javascript Object Notation.  Así, feo como suena.

#### YAML       
       ---
        xid: 0
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
