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

Las operaciones _push_ y _pull_ se ilustran en la {numref}`figure-git-push-pull`.

```{figure} img/git-push-pull.png
:name: figure-git-push-pull

Operaciones _push_ y _pull_. Imagen de [Melinda Higgins](https://www.coursera.org/learn/reproducible-templates-analysis/lecture/NGbQv/git-and-github-part-1).
```

Antes de un _push_, el usuario debe seleccionar los archivos que desea subir mediante el comando [git add](https://git-scm.com/docs/git-add), el cual pasa los archivos a un "área de espera" (_staging area_). Luego debe usarse el comando [git commit](https://git-scm.com/docs/git-commit) para "guardar" los cambios en el área de espera.

La relación entre estas operaciones de Git, se ilustra en la figura \@ref(fig:git-push-pull-commit).

```{r git-push-pull-commit, fig.cap='Operaciones de Git. Imagen de [Steven Klavins](https://medium.com/@stevenklavins94/version-control-part-4-c9387cf5b33e).', echo=FALSE}
knitr::include_graphics(rep("img/git-push-pull-commit.png"))
```

En la figura \@ref(fig:git-stage-commit-push) se muestra el funcionamiento de Git mediante una comparación con el procesamiento de una compra en línea.

```{r git-stage-commit-push, fig.cap='Operaciones de Git y compras en línea. Imagen de [Melinda Higgins](https://www.coursera.org/learn/reproducible-templates-analysis/lecture/NGbQv/git-and-github-part-2).', echo=FALSE}
knitr::include_graphics(rep("img/git-stage-commit-push.png"))
```

Otras operaciones de Git de uso frecuente son:

* [git config](https://git-scm.com/docs/git-config): para especificar opciones globales de la sesión de Git (ej. nombre del usuario, dirección de corre electrónico).
* [git clone](https://git-scm.com/docs/git-clone): para clonar (i.e. copiar) un repositorio remoto en la computadora local.
* [git status](https://git-scm.com/docs/git-status): para revisar el estado de los archivos y, por ejemplo, saber cuales deben pasarse al área de espera.

## Ejemplos de uso
### Clonación de un repositorio remoto y sincronización de los cambios efectuados localmente

Para seguir este ejemplo:

1. Bifurque (_fork_) a su cuenta en GitHub el repositorio localizado en la dirección [https://github.com/gf0604-procesamientodatosgeograficos/2022-i-tutorial-git-repo-ejemplo](https://github.com/gf0604-procesamientodatosgeograficos/2022-i-tutorial-git-repo-ejemplo).  
2. Con la opción *File - New Project - Version Control - Git* de RStudio, clone a su computadora el repositorio que acaba de bifurcar.
3. Con el editor de RStudio, abra el archivo ```README.md```, agregue una línea y guarde el archivo.  
4. Luego, ejecute los siguientes comandos desde la la ventana _Terminal_ de RStudio. Nota: las líneas que empiezan con  ```# ``` son comentarios.  

```shell
# 0. Especificación del nombre y de la dirección de correo del usuario.
# Debe modificar la dirección de correo y el nombre del usuario con sus propios datos.
$ git config --global user.email usuario@correo.com
$ git config --global user.name usuariogithub
# Para revisar:
$ git config --global --list
# 1. Revisión de los archivos con modificaciones.
$ git status
# 2. Adición de los archivos modificados al "área de espera".
# El punto (.) indica que se agregarán todos los archivos modificados.
$ git add .
# 3. Almacenamiento (commit) del conjunto de archivos modificados, junto con un mensaje explicativo.
$ git commit -m "Agregar línea 2"
# 4. "Subida" (push) de las modificaciones al repositorio remoto.
$ git push
```

Revise los cambios aplicados en el repositorio remoto en GitHub. Si se realizan nuevos cambios en el repositorio local, deben repetirse los pasos del 1 al 4. Los comentarios en el commando ```commit``` deben reflejar los cambios realizados.  

## Recursos de interés
*GitHub Archive Program*. (s. f.). GitHub Archive Program. Recuperado 10 de abril de 2022, de https://archiveprogram.github.com/

Higgins, M. (s. f.). *Reproducible Templates for Analysis and Dissemination*. Coursera. Recuperado 11 de abril de 2022, de https://www.coursera.org/learn/reproducible-templates-analysis

Klavins, S. (2020). *Version Control part 1*. Medium. https://stevenklavins94.medium.com/version-control-part-1-c5f1b43127f6
