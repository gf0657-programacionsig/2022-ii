# Streamlit: marco de trabajo para desarrollo de aplicaciones web de ciencia de datos y aprendizaje automatizado


## Resumen
Se introduce el paquete Streamlit de Python, para el desarrollo de aplicaciones web.


## Características generales
[Streamlit](https://streamlit.io/) es un marco de trabajo (*framework*) para el desarrollo de aplicaciones web basadas en el lenguaje de programación [Python](https://www.python.org/). El desarrollo en Streamlit no requiere de conocimientos de tecnologías web como HTML, CSS o JavaScript.

La plataforma [Streamlit Cloud](https://streamlit.io/cloud) permite compartir y publicar aplicaciones Streamlit, conjuntamente con el mantenimiento del código fuente en [GitHub](https://github.com/). Las aplicaciones Streamlit también pueden ser puestas en producción en otras plataformas, como [Heroku](https://www.heroku.com/) y [AWS](https://aws.amazon.com/).

## Instalación
Puede instalarse mediante pip, conda o mamba:

```shell
# Con pip
pip install streamlit

# Con conda
conda install -c conda-forge streamlit

# Con mamba
mamba install -c conda-forge streamlit
```

También se recomienda instalar el paquete [streamlit-folium](https://github.com/randyzwitch/streamlit-folium) y el paquete [pygeos](https://pygeos.readthedocs.io/):

```shell
# Con pip
pip install pygeos streamlit-folium

# Con conda
conda install -c conda-forge pygeos streamlit-folium

# Con mamba
mamba install -c conda-forge pygeos streamlit-folium
```

## Recursos de interés
- [Sitio principal](https://streamlit.io/)
- [Guía de inicio](https://docs.streamlit.io/library/get-started)
- [Documentación](https://docs.streamlit.io/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Referencia del API](https://docs.streamlit.io/library/api-reference)
- [Galería de aplicaciones](https://streamlit.io/gallery)

## Ejemplo de aplicación Streamlit
En [https://mfvargas-ejemplo.streamlit.app/](https://mfvargas-ejemplo.streamlit.app/) se publicó una aplicación desarrollada, a modo de ejemplo, con Streamlit, la cual incluye visualizaciones de datos en formato tabular, gráfico y geoespacial.

El código fuente está disponible en [https://github.com/mfvargas/ejemplo-streamlit](https://github.com/mfvargas/ejemplo-streamlit).
