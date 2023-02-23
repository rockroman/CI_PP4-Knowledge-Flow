![Mockup image](readme/misc/mock-up.png)


[View live website](https://pic-pals-pp4.herokuapp.com/)

## Table of Contents
0. [About](#about)
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Project Structure](#project-structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
    1. [Agile Design](#agile-design)
    2. [CRUD Functionality](#crud-functionality)
4. [Technologies Used](#technologies-used)
    1. [Coding Languages](#coding-languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
5. [Features](#features)
6. [Future implementation](#future-implementation)
    1. [Future Features](#future-features)
    2. [Improvements](#improvements)
7. [Validation](#validation)
    1. [HTML](#html-validation)
    2. [CSS](#css-validation)
    3. [Javascript](#javascript-validation)
    4. [Python](#python-validation)
    5. [Chrome Dev Tools Lighthouse](#chrome-dev-tools-lighthouse-validation)
    6. [WAVE Validation](#wave-validation)
8. [Testing](#testing)
    1. [Device Testing](#device-testing)
    2. [Browser Compatibility](#browser-compatibility)
    3. [Manual Testing](#manual-testing)
    4. [Automated Testing](#automated-testing)
9. [Bugs](#bugs)
10. [Configuration](#configuration)
    1. [Google emails](#google-emails)
11. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Tutorial](#tutorials)
    2. [Code](#code)
    3. [Literature](#literature)
    4. [Misc](#misc)
13. [Acknowledgements](#acknowledgements)

## About

The Knowledge Flow is a Learning and Blogging application that allows users to post blogs  in
a chosen categories add comments, learn from the content of a blog or a comment and find out a mentor available 
for each category and reach out and connect with them.

***
## Project Goals
Primary goals of the Project(web app):
- Give users  an online solution to Learn  or Teach 
 in a certain category
- Enable users to express themselves through a written form
in comfort of their environment and provide or get some 
valuable information that will help them or others develop more
knowledge. 
  

### User Goals
- Ability to create content
- Be able to share content and give an opinion on a topic
- Ability to amend and update content
- Chance to connect with a variety of interesting individuals. 


## User Experience

### Target Audience
- People with a desire to teach and share their knowledge
- Individuals that want to learn and expand the knowledge
- People who's wants to be productive and save time while learning 


### User Requirements and Expectations

- Application with a clear purpose
- Easy and intuitive user interface that allows quick and efficient navigation
- Responsive and visually good design
- Engaging content within the limit of set categories
- Way to engage with a team or a developer

##### Back to [top](#table-of-contents)

### User stories

1. As an authenticated user I would like to see a home page and have an Idea what the application is about
2. As an authenticated user I would like to be able to choose a way to get benefit from the app with choosing the right role
3. As an authenticated user I would like to have a full access to the content of an web app
4. As an authenticated user I would like a functionality to create profile(account)
5. As an authenticated user I would like functionality to upload a supporting image to my profile and change it when I desire
6. As an authenticated user I would like a functionality to update or delete profile (account) if not planning to use web app anymore
7. As an authenticated user I would like functionality to pick different types of learning categories in my profile and change them later
8. As an authenticated user I would like functionality to see and read blog posts that other users created
9. As an authenticated user I would like functionality to leave a comment on a blog post 
10. As an authenticated user I would like functionality to add blog post and share it with other users
11. As an authenticated user I would like functionality to support my blog post with a cover image and change it later if needed.
12. As an authenticated user I would like to upload a blog in a selected category
13. As an authenticated user I would like the functionality for each category page to have a list of mentors avaliable 
14. As a user I would like web app to be fully responsive and to have the same experience when using
on any device 
15. As an returning user user I would like functionality to set a new password and use the web app even if I forgot the old password
16.  As an returning user user I would like functionality to leave a feedback or send a mesage to a site owner or a web app Team

### Site Owner Stories

1. As a Site Owner I would like that every un-authenticated user has  limited
functionality of a website  until he is registered.
2. As a Site Owner I would like that authenticated users have full access to web app and its functionality
3. As a Site Owner I would like that each data entry is validated before stored in database
4. As a Site Owner I would like that users an leave a message or feedback via contact form or 
5. As a Site Owner I would like that users have more than one way of comunicating with team or myself
6. As a Site Owner I would like that each 'Mentor' user cant see himself on the list of available mentors for his respective category(user wont be contacting himself)
7. As a Site Owner I would like that each authenticated user gets prompt messages when performing CRUD(Create,Read,Update,Delete) operations when using web app.
8. As a Site Owner I would like that each authenticated user has option to get access to an app if he forgots password for any reason via (Reset password functionality)




## Design
***
### Colours
Web app is utilizing  dark theme with black and blue colors, it is enhancing user experience by reducing eye strain and improving visibility in low-light environments.

The Color pallet was created using [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="docs/readme/color-pallet-PP4.png">
</details>

### Fonts
Google fonts "'Rubik', sans-serif" modern and versatile font were used for this project as it offers  clean and legible design, which makes it easy to read on screens of different sizes and resolutions. It has a neutral appearance and doesn't have any distracting features that can make it difficult to read.
<details><summary>See Rubik font</summary>
<img src="docs/readme/color-pallet-PP4.png">
</details>


## Project Structure 

#### Web app  pages
Clean dark theme was used troughout entire project, intuitive and simple navigation and 
clear message about value of knowledge was main driver for delivering the project.

#### sections:
1.  Home page divided into 6 sections with simple and intuitive navigation
- Hero Section with supporting image and clear call to action
- Bottom hero that's going deeper with an hero headline and displays some benefits and ways to use the web app
- Team section that presents members responsible for delivering a fnished project
- About section with a quote
- Contact section  with a simple form and a web app banner
- Footer with some navigation social media links
2. Blog Page where user can see latest blogs posted with links to a more detail vie of each blog
3. Add blog page with a simple form 
4. Profile page where all the data about user is stored
5. 3 Category pages
- Personal finance
- Leadership
- Time management 
- each page consists of headline, supporting image , sections that describes category, describes importance ,benefits and section where user can see available mentors for that category.
then section with blogs related to that category

### Code structure
Project code structure is organized and divided into various application folders and constructed using Django Framework 
#### Project Apps:
- Home app - constructed to deliver basic information for the User about the app via Home page with simple an intuitive navigation(links in nav-bar and footer to navigate throughout app), basic contact form for user feedback and footer

- Siteusers app- this app provide user authentication and profile management functionality,full CRUD functonality, so user can create a an account, select a role that provides further functionality and usage, update profile, upload supporting images for a profile

- flow_blog app - constructed to deliver CRUD functions of a blogging app, where  structure includes the necessary files for running the application, including the views, models, and templates required to create, read, update, and delete blog posts and comments 

- categories app - delivers  functionality for users to select and manage learning categories for their profile and blog posts. The app includes views and templates for displaying a list of available categories and enabling users to select which learning categories they want to be associated with their profile and blog posts. 

#### Other django apps:
- **settings.py**: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- **Procfile**: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- **static**: This directory contains the base CSS and JavaScript files 
- **templates**- base level folder with basic templates extended throughout other templates like : base.html, navbar.html, footer.html, also templates for user authentication and also each app has its own templates folder with html files to support the app functinalit and reusability
- **requirements.txt**: This file lists the dependencies required for  Django project to run.
- **env.py**: This file is used to store environment variables for a Django project or application, such as database connection details or API keys. best practice is including this file into th gitignore file so  the values can be easily accessed and used by the project without being exposed in the code or configuration files.



