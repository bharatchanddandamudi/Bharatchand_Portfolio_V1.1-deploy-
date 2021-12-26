[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT TITLE AND LOGO -->

# Django Portfolio Website

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li><a href="#about-this-project">About This Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About This Project

 [![Watch the video](https://img.youtube.com/vi/47AeB7AHozE/maxresdefault.jpg)](https://youtu.be/47AeB7AHozE)

           



      
         
 <!-- DESCRIPTION -->

### Description:

In this project I will be showing my step by step process for building a Django Portfolio Website. Django—an open-source web framework that's designed on top of Python—can help you quickly bring your website ideas to life. I plan to illustrate my undestanding of Django for web development, by building my own website from the ground up. I will create a database, design the layout for your website, and add and update URL paths. Then I will connect my Django portfolio website to Postgres, and add static files, URLs and more.

<!-- KEY OBJECTIVES -->

### Key objectives:

- Setting up URLs in Django project
- Creating models in Django
- Connecting Django project to Postgres
- Adding static images
- Designing the layout for website
- Creating object views
- Updating URL paths

<!-- GETTING STARTED -->

## Getting Started

Here are some instructions on how to get this project up and running. First you will need some some prerequsites to manage a local virtual environment. Bellow is a list of _'Bare Minimums'_ you need to follow along with this project.

- **[Python](https://www.python.org/downloads/)** 3.9.1
- **[Pip](https://pip.pypa.io/en/stable/installing/)** 21.0.1

### Here is how we install them:

- Check if `python` and `pip` are installed

  ```sh
  python --version
  python -m pip --version
  ```

- If `python` is notinstalled, you can download it from the [Python website](https://www.python.org/downloads/). If `pip` is not installed, run the following command or [check out](https://pip.pypa.io/en/stable/installing/)

  ```sh
  python get-pip.py pip==21.0.1
  ```

### Installations:

1. Create a directory for the project creating  run the following command in your terminal

   ```sh
   mkdir project
   cd project
    $ python -m django --version
    $ django-admin startproject portfolio
    $ python manage.py startapp job  
   ```
2. Runing commands  

   ```sh 
     $ python manage.py runserver
     $ python manage.py runserver 8080
     $ pythin manage.py makemigrations 
     $ pythin manage.py migrate 
     $ pythin manage.py show migrations  
   ```       

3. Install and activate the virtual environment, using `pip` as so

   ```sh
   python -m venv portfolio_website_environment
   source portfolio_website_environment/bin/activate
   python -m pip install requirements.txt
   pip list
   ```
