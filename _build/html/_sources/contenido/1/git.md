# Git - sistema de control de versiones


## Trabajo previo

### Tutoriales
Abba, I. V. (2021). *Git and GitHub Tutorial – Version Control for Beginners*. FreeCodeCamp.Org. https://www.freecodecamp.org/news/git-and-github-for-beginners/

### Otros
Instale en su computadora el sistema de control de versiones [Git](https://git-scm.com/downloads).


## Descripción general
[Git](https://git-scm.com/) es un sistema de [control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones) diseñado para "rastrear" cambios en el código fuente durante el proceso de desarrollo de software. Sin embargo, puede ser utilizado para llevar el control de los cambios en cualquier conjunto de archivos (ej. [documentación](https://guides.github.com/features/wikis/), [música](https://techcrunch.com/2013/10/09/splice-music/)). 

Un sistema de control de versiones proporciona, entre otras ventajas:

* La capacidad de recuperar versiones anteriores de los archivos.
* La capacidad de integrar modificaciones efectuadas por varias personas en el mismo conjunto de archivos.
* La capacidad de mantener varias "ramas" (_branches_) de un producto (ej. "estable", "evaluación", "inestable", como en el caso de [Debian Linux](https://www.debian.org/releases/), [GRASS GIS](https://grass.osgeo.org/download/software/sources/) y muchos otros proyectos de software libre).
* Facilidades para mantener redundancia y respaldos de los archivos (ej. [Programa de respaldos de GitHub](https://archiveprogram.github.com/)).

Git fue diseñado por Linus Torvalds en 2005 durante del desarrollo del _kernel_ del sistema operativo Linux. Se caracteriza por ser un [sistema de control de versiones distribuido](https://es.wikipedia.org/wiki/Control_de_versiones_distribuido), lo que significa que el código fuente puede estar alojado en la estación de trabajo de cualquier miembro del equipo de desarrollo (i.e. no tiene que existir un repositorio central).

El protocolo de Git es utilizado en varios sitios que proveen servicios de alojamiento de software, entre los que están [SourceForge](https://sourceforge.net/), [Bitbucket](https://bitbucket.org/), [GitLab](https://about.gitlab.com/) y [GitHub](https://github.com/).

## ¿Como funciona Git?
Desde el punto de vista de un usuario de Git (ej. un programador), Git se utiliza para sincronizar la versión local de un conjunto de archivos, llamado proyecto o repositorio, con la versión que está alojada en un sistema remoto (ej. GitHub). Cada repositorio se almacena en un directorio (carpeta) del sistema operativo. La sincronización se realiza principalmente a través de dos operaciones:

* **_push_**: para "subir" al repositorio remoto los cambios realizados en el repositorio local. Esta operación se realiza mediante el comando [git push](https://git-scm.com/docs/git-push). Es probable que el sistema remoto le solicite al usuario algún tipo de autenticación (ej. nombre de usuario y clave).
* **_pull_**: para "bajar" al repositorio local los cambios realizados en el repositorio remoto. Esta operación se realiza mediante el comando [git pull](https://git-scm.com/docs/git-pull).

