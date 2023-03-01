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

## Database
***
<details><summary>(ERD)Physical database model</summary>
<img src="docs/Knowledge-Flow-diagram2.jpeg">
</details>

- For this Django app I ve used PostgreSQL relational database management system.
- model showed on the diagram visually represents the structure of a PostgreSQL database, including tables, columns, relationships, and constraints, that is actually stored in the database itself.

### Data Models

#### User model

- User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
username, password,email

#### Profile model

- Profile model is constructed as an extension of  user model  and there for has an <strong>one to one</strong> relationship with User model.also it related via <strong>Many To Many</strong> field with a Learning category model. it contains further data about authenticated user and has following fields: Image,first_name, last_name,email,category,website_url,linkedIn_url,bio,role,created_on,updated_on

#### BlogPost model

- BlogPost model is model used for each blogpost uploaded by the user,it has foreign key to the User model to associate each post with the author who created it, and another foreign key to the Category model to organize posts by topic or theme.By using foreign keys to establish these relationships model is associated with valid users and categories in the system. it consists of the 
following fields:title,creator,category,slug,body,cover_image,created_on,updated_on

#### Comment model

- Comment model is used for any user comment on particular blog post there are 2 foreign keys one associated to a user and the other to a blog post fields of this model are:author,created,blogpost,content,status

#### LearningCategory model 

- LearningCategory model is used as an designed to provide a predefined list of categories that users can select from in their profile to indicate their areas of interest for learning, and also to serve as a set of categories that bloggers can assign to their posts to help other users discover relevant content. by using one model to represent both user interests and blog categories, the app can ensure consistency and avoid duplication in the category list. it has foreign key associated with a User. model fields are as follows:  maker,name,category_image,start_quote,description,importance_of_category.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| maker          | user          | OneToOneField | User, on_delete=models.PROTECT    |
| name           | name        | CharField    | max_length=50     |
| category image| category_image   | CloudinaryField   | 'image', default='placeholder'      |
| Start Quote    | start_quote    | CharField    |    |
| Description       | description       |TextField ManyToManyField | max_length=255, null=True       |
| Importance of category      |importance_of_category      | TextField    | null=True    |

##### Back to [top](#table-of-contents) 

### Wireframes

<details><summary>Big screens - laptop & desktop</summary>
<img src="docs/wireframes/wireframes-desktop.png">
</details>
<details><summary>Medium screens - tablet</summary>
<img src="docs/wireframes/wireframes-tablet.png">
</details>
<details><summary>Small screens - mobile</summary>
<img src="docs/wireframes/wireframes-mobile.png">
</details>

***

## Agile design

### About
- When I first tried to implement Agile methodology in my Django app, I found it challenging to balance the iterative development approach with the need for a solid plan and clear requirements.
While I faced some setbacks and had to adjust my process along the way, the experience taught me valuable lessons about the importance of flexibility, communication, and continuous improvement in software development, and prepared me to approach future projects with a more agile mindset.
usage of Milestones,Issues GitHub Projects and  Boards led to organizing the development in User Stories, Epics, Sprints

- With my first try of using Agile methodology Im aware that planing and execution of agile could be better and would speed up the development procces but since its basicaly coomprehended to be collaborative,fast paced cyclical approach it felt odd to be implemented as a solo developer 

- When faced with unexpected changes or challenges during development, I learned to be flexible and adjust my plan accordingly, often by reorganizing cards on my Kanban board and prioritizing tasks based on their importance and impact.
This allowed me to respond more effectively to change, stay focused on the most critical issues, and ensure that my development process remained agile and adaptable




## Technologies Used

### Languages & Frameworks

- HTML 
- CSS
- Javascript
- Boostrap 4
- Python 3.10.2
- Django 3.2

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was usedfor creating the multi-device mock-up at the top of this README.md file
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap 4.2](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Pagination, Navbar)
- [Cloudinary](https://cloudinary.com/) to store static files
- [Lucidcharts](https://lucid.app/) has been used in  project to design and document  data model architecture.
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Boostrap icons](https://fontawesome.com/) - Icons from Boostrap icons  were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Looka](https://looka.com/)- for making the custom website logo


- Validation:
    - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) to validate the css in the project
  - [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project
 
  - [JShint](https://jshint.com/) to validate custom script file
  <!-- - [PEP8](http://pep8online.com/) to check code against Python conventions -->
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance, accessibility, progressive web apps, SEO analysis of the project code
  - [Wave Validator](https://wave.webaim.org/) to evaluate accessibility



