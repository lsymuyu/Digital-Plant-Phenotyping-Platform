<p align="center"><img width=25% src="https://user-images.githubusercontent.com/6087486/51623212-7dc1e700-1f38-11e9-86ac-a4041dae99b3.png"></p>

## Basic Overview
D3P provides the tools to conduct in silico phenotyping experiment over typical sensors, including RGB/Multispectral camera and LiDAR.

## Install
1) Install OpenAlea environment

Note that please ensure [Conda](https://conda.io) have been installed in your conmputer that is an open source package management system and environment management system. [Conda Download](https://conda.io/miniconda.html). Use the Python 2.7 based installation (Windows, Linux, Mac).

Create an environment named *openalea*:
Launch a console (See Anaconda Prompt in Start menu on windows)
    
    conda create -n openalea -c openalea openalea.plantgl openalea.lpy boost=1.66

Activate the *openalea* environment:

    [source] activate openalea

source should be written only on linux and macos.
Install the different packages

    conda install notebook=5.4 matplotlib pandas nbformat git

    conda install -c openalea openalea.mtg alinea.caribu openalea.plantscan3d openalea.visualea 

    conda install -c openalea -c conda-forge pvlib-python alinea.astk

2) Install POV-Ray

3) Install 

3) Install Phenotyping package
