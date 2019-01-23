<p align="center"><img width=25% src="https://user-images.githubusercontent.com/6087486/51623212-7dc1e700-1f38-11e9-86ac-a4041dae99b3.png"></p>

## Basic Overview
D3P provides the tools to conduct in silico phenotyping experiment over typical sensors, including RGB/Multispectral camera and LiDAR.

## Install
**a. Install OpenAlea environment**

[OpenAlea](http://openalea.gforge.inria.fr/dokuwiki/doku.php) is a 3D plant modeling platform that includes modules to analyse, visualize and model the functioning and growth of plant architecture. To install OpenAlea, please ensure [Conda](https://conda.io) have been installed in your conmputer. Conda is an open source package management system and environment management system that can run in Windows, Linux, Mac.  Please use the Python 2.7 based installation ([Conda Download](https://conda.io/miniconda.html).

Create an environment named *openalea*:
Launch a console
    
    conda create -n openalea -c openalea openalea.plantgl openalea.lpy boost=1.66

Activate the *openalea* environment:

    [source] activate openalea

source should be written only on linux and macos.
Install the different packages

    conda install notebook=5.4 matplotlib pandas nbformat git

    conda install -c openalea openalea.mtg alinea.caribu openalea.plantscan3d openalea.visualea 

    conda install -c openalea -c conda-forge pvlib-python alinea.astk

b. Install POV-Ray

3) Install 

3) Install Phenotyping package
