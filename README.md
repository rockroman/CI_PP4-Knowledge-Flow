# Knowledge Flow
(Developer: Roman Rakic)

![Mockup image](docs/features/first-one.png)


[View live website](https://knowledge-flow.herokuapp.com/)

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
    7. [Agile Design](#agile-design)
4. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries and Tools](#libraries--tools)
5. [Features](#features)
6. [Future Features](#future-features)
    
7. [Validation](#validation)
    1. [CSS](#css)
    2. [Html](#html)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Chrome Dev Tools Lighthouse](#lighthouse)
    6. [WAVE Validation](#wave)  
8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## About

Knowledge Flow is a learning and blogging application that allows users to post blogs in
chosen categories, Add comments, learn from the content of a blog or a comment, and find a mentor available.
for each category and reach out and connect with them.

***
## Project Goals
Primary goals of the project (web app):
- Give users  an online solution to learn or teach
 in a certain category
- Enable users to express themselves through a written form,
in the comfort of their environment and provide or get some
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
- Individuals that want to learn and expand their knowledge
- People who want to be productive and save time while learning


### User Requirements and Expectations

- Application with a clear purpose
- An easy and intuitive user interface that allows quick and efficient navigation
- Responsive and visually good design
- Engaging content within the limits of set categories
- Ways to engage with a team or a developer

##### Back to [top](#table-of-contents)

### User stories

0. As a user I want to navigation to be intuitive and user-friendly so that I'm able to easily navigate through the app content.
1. As a  user I want to know Important info on what the app is about so that I can use its functionality for mutual benefit
2. As an authenticated user I would like to be able to choose a way to get benefits from the app by choosing the right role
3. As an authenticated user I would like to have full access to the content of a web app
4. As an authenticated user I would like the functionality to create a profile(account)
5. As an authenticated user I would like the functionality to upload a supporting image to my profile and change it when I desire
6. As an authenticated user I would like the functionality to update or delete profile (account) if not planning to use the web app anymore
7. As an authenticated user I would like the functionality to pick different types of learning categories in my profile and change them later
8. As an authenticated user I would like functionality to see and read blog posts that other users created
9. As an authenticated user I would like to upload a blog in a selected category so that I can share my knowledge, opinion, and information
10. As an authenticated user I would like the functionality to delete or update my blog post I I find it no longer relevant
11. As an authenticated user I would like the functionality to leave a comment on a blog post
12. As an authenticated user I would like functionality to support my blog post with a cover image and change it later if needed.
13. As an authenticated user I would like the functionality for each category page to have a list of mentors available and their contact info
14. As a user I would like a web application to be fully responsive and to have the same experience when using
on any device
15. As a returning user I would like the functionality to set a new password if I forget the old one so that I can still use the web app
16. As a User I would like a functionality to contact the app owner or a team so that I can leave a suggestion or express my opinion about the web app
17. As a user I would like a functionality to update or delete a comment Iposted to a blogpost so that if any mistake was made or new information is acquired anyone reading will be up to date

### Site Owner Stories

18. As a site owner I want to restrict access to sections of an app to unauthenticated users so that basic standards of data protection are met
19. As a Site Owner I would like that authenticated users have full access to web app and its functionality
20. As a Site Owner I would like that each data entry is validated before stored in database
21. As a Site Owner I would like that users an leave a message or feedback via contact form or 
22. As a Site Owner I would like that users have more than one way of comunicating with team or myself
23. As a Site Owner I would like that each 'Mentor' user cant see himself on the list of available mentors for his respective category(user wont be contacting himself)
24. As a Site Owner I would like that each authenticated user gets prompt messages when performing CRUD(Create,Read,Update,Delete) operations when using web app.
25. As a Site Owner I would like that each authenticated user has option to get access to an app if he forgots password for any reason via (Reset password functionality)




## Design
***
### Colours
Web app is utilizing  dark theme with black and blue colors, it is enhancing user experience by reducing eye strain and improving visibility in low-light environments.

The Color pallet was created using [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="docs/features/color_palete.png">
</details>

### Fonts
Google fonts "'Rubik', sans-serif" modern and versatile font were used for this project as it offers  clean and legible design, which makes it easy to read on screens of different sizes and resolutions. It has a neutral appearance and doesn't have any distracting features that can make it difficult to read.
<details><summary>See Rubik font</summary>
<img src="docs/features/fonts.png">
</details>


## Project Structure 

#### Web app  pages
Clean dark theme was used troughout entire project, intuitive and simple navigation and 
clear message about value of knowledge was main driver for delivering the project.

#### sections:
1.  Home page divided into 6 sections with simple and intuitive navigation
- Hero Section with supporting image and clear call to action
- Bottom hero that's going deeper with a hero headline and displays some benefits and ways to use the web app
- Team section that presents members responsible for delivering a finished project
- About section with a quote
- Contact section  with a simple form and a web app banner
- Footer with  navigation and social media links
2. Blog Page where user can see the latest blogs posted with links to a more detailed view of each blog
3. Add blog page with a simple form
4. The profile page where all the data about the user is stored
5. 3 Category pages
- Personal Finance
- Leadership
- Time management
- each page consists of a headline, supporting image, sections that describe the category, describe its importance and benefits,  and a section where user can see available mentors for that category.
then section with blogs related to that category

### Code structure
Project code structure is organized and divided into various application folders and constructed using Django Framework 
#### Project Apps:
- Home app - constructed to deliver basic information for the User about the app via Home page with simple an intuitive navigation(links in nav-bar and footer to navigate throughout the app), basic contact form for user feedback and a footer


- Siteusers app- this app provides user authentication and profile management functionality, full CRUD functionality, so user can create an account, select a role that provides further functionality and usage, update profile, upload supporting images for a profile


- flow_blog app - constructed to deliver CRUD functions of a blogging app, where  the structure includes the necessary files for running the application, including the views, models, and templates required to create, read, update, and delete blog posts and comments.


- categories app - delivers functionality for users to select and manage learning categories for their profile and blog posts. The app includes views and templates for displaying a list of available categories and enabling users to select which learning categories they want to be associated with their profile and blog posts.

#### Other django apps:
- **settings.py**: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- **Procfile**: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- **static**: This directory contains the base CSS and JavaScript files
- **templates**- base-level folder with basic templates extended throughout other templates like: base.html, navbar.html, footer.html, also templates for user authentication. and also each app has its own templates folder with HTML files to support the app's functionality and reusability
- **requirements.txt**: This file lists the dependencies required for the Django project to run.
- **env.py**: This file is used to store environment variables for a Django project or application, such as database connection details or API keys. the best practice is to include this file into th gitignore file so the values can be easily accessed and used by the project without being exposed in the code or configuration files.

##### Back to [top](#table-of-contents)

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

- Profile model is constructed as an extension of  user model  and there for has an <strong>one to one</strong> relationship with User model.also it related via <strong>Many To Many</strong> field with a Learning category model. it contains further data about authenticated user and has following fields:

- ROLE = (
        ('Mentor', 'Mentor'),
        ('Student', 'Student')
    ) 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | OneToOneField|  User, on_delete=models.CASCADE|
|  image       |  image     |CloudinaryField | 'image', default='placeholder'  |
| first_name| first_name  | CharField | max_length=20    |
| last_name| last_name  | CharField | max_length=20    |
|  email   | email  | EmailField  | max_length=100  |
| category      | category    |ManyToManyField|LearningCategory, related_name='user_learning_categoy'      |
|  website_url    | website_url      | URLField  |  max_length=100, default='https:// www.google.com/'  |
|  linkedIn_url    | linkedIn_url | URLField  |  max_length=100, default='https:// www.linkedin.com/'   |
|  bio    | bio      | DateTimeField   | auto_now_add=True    |
|  role     | role      | CharField | max_length=20, choices=ROLE    |
|  created_on     | crested_on      | DateTimeField   | auto_now_add=True    |
|  updated_on     | updated_on      | DateTimeField   | auto_now_add=True    |


#### BlogPost model

- BlogPost model is model used for each blogpost uploaded by the user,it has foreign key to the User model to associate each post with the author who created it, and another foreign key to the Category model to organize posts by topic or theme.By using foreign keys to establish these relationships model is associated with valid users and categories in the system. it consists of the 
following fields:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| title        | title      | CharField| max_length=200, unique=True  |
| creator        | creator       |ForeignKey   | User, on_delete=models.CASCADE  |
| category| category  | ForeignKey   | LearningCategory, on_delete=models.PROTECT, null=True     |
|  slug   | slug   | SlugField   | max_length=100, unique=True  |
| body       | body     |TextField |      |
|  cover_image     | cover_image      | CloudinaryField  | 'image', default='placeholder'   |
|  created_on     | created_on      | DateTimeField   | auto_now_add=True    |
|  updated_on     | updated_on      | DateTimeField   | auto_now_add=True    |


#### Comment model

- Comment model is used for any user comment on particular blog post there are 2 foreign keys one associated to a user and the other to a blog post fields of this model are:

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author         |  author          | ForeignKey | User, on_delete=models.CASCADE   |
| created        | created       | DateTimeField    | auto_now_add=True   |
| blogpost| blogpost   | ForeignKey   | BlogPost, on_delete=models.CASCADE, related_name='comments'     |
| content    | content    | TextField    | max_length=500   |
| status       | status      |BooleanField | max_length=255, default=True     |


#### LearningCategory model 

- LearningCategory model is used as an designed to provide a predefined list of categories that users can select from in their profile to indicate their areas of interest for learning, and also to serve as a set of categories that bloggers can assign to their posts to help other users discover relevant content. by using one model to represent both user interests and blog categories, the app can ensure consistency and avoid duplication in the category list. it has foreign key associated with a User. model fields are as follows: 

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| maker          | user          | OneToOneField | User, on_delete=models.PROTECT    |
| name           | name        | CharField    | max_length=50     |
| category image| category_image   | CloudinaryField   | 'image', default='placeholder'      |
| Start Quote    | start_quote    | CharField    |max_length=255, null=True    |
| Description       | description       |TextField  |       |
| Importance of category      |importance_of_category      | TextField    | null=True    |

##### Back to [top](#table-of-contents) 

### Wireframes

<details><summary>Big screens - laptop & desktop</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home-desk-wireframe.png" >

</details>

<details><summary>authentication pages(Login,register,logout,password reset and password reset done)</summary>
<img src="docs/wireframes/authentication-pages.png">
</details>

<details><summary>Set role</summary>
<img src="docs/wireframes/set-role.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/PROFILE.png">
</details>

<details><summary>Edit profile</summary>
<img src="docs/wireframes/PROFILE-BLOG-UPDATE.png">
</details>

<details><summary>Delete profile</summary>
<img src="docs/wireframes/DELETE-PROFILE.png">
</details>

<details><summary>Blog</summary>
<img src="docs/wireframes/blog-page.png">
</details>

<details><summary>Blog detail</summary>
<img src="docs/wireframes/BLOG-DETAIL.png">
</details>

<details><summary>Blog edit, Blog add</summary>
<img src="docs/wireframes/PROFILE-BLOG-UPDATE.png">
</details>

<details><summary>Category</summary>
<img src="docs/wireframes/category-page.png">
</details>

</details>

***

<details><summary>Medium screens - tablet</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home-tablet.png" >

</details>

<details><summary>authentication pages(Login,register,logout,password reset and password reset done)</summary>
<img src="docs/wireframes/authentication-tablet.png">
</details>

<details><summary>Set role</summary>
<img src="docs/wireframes/set-role-tablet.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/PROFILE-tablet.png">
</details>

<details><summary>Edit profile</summary>
<img src="docs/wireframes/blog-profile-update-add-tablet1.png">
</details>

<details><summary>Delete profile</summary>
<img src="docs/wireframes/delete-profile-tablet1.png">
</details>

<details><summary>Blog</summary>
<img src="docs/wireframes/blog-tablet1.png">
</details>

<details><summary>Blog detail</summary>
<img src="docs/wireframes/blog-detail-tablet1.png">
</details>

<details><summary>Blog edit, Blog add</summary>
<img src="docs/wireframes/blog-profile-update-add-tablet1.png">
</details>

<details><summary>Category</summary>
<img src="docs/wireframes/category-tablet.png">
</details>
</details>

***

<details><summary>Small screens - mobile</summary>

<details><summary>Home page</summary>
<img src="docs/wireframes/home-mob-wireframe.png" >

</details>

<details><summary>authentication pages(Login,register,logout,password reset and password reset done)</summary>
<img src="docs/wireframes/authentication-pages-mob.png">
</details>

<details><summary>Set role</summary>
<img src="docs/wireframes/set-role-mob.png">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/PROFILE-MOB.png">
</details>

<details><summary>Edit profile</summary>
<img src="docs/wireframes/profile-blog-update-mob.png">
</details>

<details><summary>Delete profile</summary>
<img src="docs/wireframes/delete-profile-mob.png">
</details>

<details><summary>Blog</summary>
<img src="docs/wireframes/blog-page-mob1.png">
</details>

<details><summary>Blog detail</summary>
<img src="docs/wireframes/blog-detail-mob.png">
</details>

<details><summary>Blog edit, Blog add</summary>
<img src="docs/wireframes/profile-blog-update-mob.png">
</details>

<details><summary>Category</summary>
<img src="docs/wireframes/category-mob.png">
</details>


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

### Epics
- Using the GitHub 'Milestones' and Linking the user stories with the tasks I created a 5 epics for this project
<details><summary>See epics</summary>
<img src="docs/features/new-epic.png">
</details>

### User stories
- using Github issues first I created the template for a user story that was later used to
create user stories. at a later date user stories were edited since at the start they were just a rough sketch or a guideline that later became a full user story
<details><summary>See User story template</summary>
<img src="docs/features/user-story-template.png">
</details>
<details><summary>See User story ticket</summary>
<img src="docs/features/user-story-ticket.png">
</details>
<details><summary>See user story</summary>
<img src="docs/features/user-story.png">
</details>

### Kanban Board
- As a visual representation of the project's status, showing what tasks are in progress, what tasks are waiting, and what tasks have been completed.Each task is represented as a card on the board, and the cards can be moved from one column to another to show progress.  Kanban board is an excelent tool and since it was my first time using I didnt get the  full benefits of using it ,since it wasnt used as often as it should, but since completing the project I m more aware of its great purpose and im sure it will be utilized more and more in the future 
[Link to project Kanban board.](https://github.com/users/rockroman/projects/5)
<details><summary>See Kanban board</summary>
<img src="docs/features/kanban-board.png">
</details>

### Moscow prioritisation
- The Moscow prioritization technique is used to prioritize project requirements based on their importance and urgency. Although it's my first time using this technique and the implementation may not be perfect, it allowed me  to effectively prioritize my project requirements and ensure the most critical ones were addressed first.

<details><summary>See image</summary>
<img src="docs/features/moscow.png">
</details>

### Sprints 

- Using Agile sprints , time-boxed iterations in which a team works on a set of prioritized user stories to deliver a potentially shippable product increment. Although the initial implementation may not have been successful as using it for the first time , the experience provided valuable insights and learning opportunities for future sprints to improve. and to improve  overall implementation of the Agile methodology.

#### 1st Sprint
 - Tasks and User stories in first sprint
    - Create new django project and app (dev task)
    - install django and supporting libraries (dev task)
    - Deploy empty project to heroku (dev task)
    - USER STORY: 1 (dev task)
 - development time : 7 days


#### Closing words on agile:
- As a solo developer using Agile for the first time, the learning curve was steep, but the experience gained from the process is invaluable. Although the initial implementation may have not been great ,but  it will serve as a foundation for implementing Agile more effectively in future projects.

##### Back to [top](#table-of-contents)    
***


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


## Features

***
### Nav-bar and Logo

- this feature is present throughout entire project except on a page where user is prompt to define his profile role for using the app, and since the incentive is to pick the role as its vital part of a user functionality of the web app I decided to not incude this feature in this part of the project.

- Nav-bar consists of a links to a blog page, profile page, each of 3 learning category pages and link to about us section
    - authenticated user has his username visible on the navbar and dropdown extends to a link to profile page
    - unaithenticated user cant see (name link to profile) and blog page dropdown is restricted so he dont have access to CRUD functionality of a blog section while authenticated user has dropdown link to add blog.

- Feature is fully responsive and on smaller screen sizes it coverts into a 'Hamburger menu'
- User Story covered with this feature: 0,1

<details><summary>See Nav-bar and Logo</summary>

![Logo and navbar](docs/features/nav_bar_logged_in.png)
![Logo and navbar](docs/features/nav_bar_Mobile.png)
![Logo and navbar](docs/features/nav_bar_Not_logged_in.png)

</details>

### Back to top Button

- This button is present an all pages
- Makes navigating the page easier and its enhancing the user experience 
- User Story covered with this feature: 0
<details><summary>See Back to top Button</summary>

![Home page](docs/features/back-to-top.png)
</details>


### Homepage

<details><summary>See Homepage</summary>

![Home page](docs/features/home-page.png)
![Home page](docs/features/home-page-mob.png)

</details>

- this feature is First point of contact with a user, it consist of:
 - hero section with a CTA(call to action button)
    - CTA guides user depending if user is authenticated or not
    - Authenticated user is redirected to see latest blogs and find his preferrence
    - Unauthnticated user is redirected to a signup page.
    - User Story covered with this feature:1,14,15,19

    <details><summary>See Hero section</summary>

    ![Hero section](docs/features/hero-section.png)
    </details>

- Featured section as an extension of a hero section with introduction to web app and small list 
  of benefits when using the web app.
  - User Story covered with this feature:1,2

    <details><summary>See Featured section </summary>

    ![Featured section](docs/features/feature-section.png)
    </details>


- Team Section that presents the team who delivered the app
    - User Story covered with this feature:1,2,22

    <details><summary>See Team Section</summary>

    ![Team Section](docs/features/team-section.png)
    </details>

- About section with a famous quote is delivering a small peek into reasons for delivering the
   app while effectively communicating  brand's values and invites users to engage with web app
   - User Story covered with this feature:1

    <details><summary>See About section </summary>

    ![About section ](docs/features/about-section.png)
    </details>

- Contact section with a web app logo and small contact form this section purpose is to  
  establish visual identity of a web app and to provide a convenient way for users to get in touch with a Team
  - User Story covered with this feature:21,16 

    <details><summary>See Contact section</summary>

    ![Contact section](docs/features/contact-section.png)
    </details>

- Footer is intended to be extension of a nav-bar with links to home page, about us setion and blog page, links to social media pages to ensure multple ways that user can communicate with a team and one added detail of a developer git-hub page link with a timeframe ofproject development.
    - User Story covered with this feature:0,1,14,22 

    <details><summary>See Footer </summary>

    ![Team Section](docs/features/footer_section.png)
    </details>

***

 ### Register(sign up) Page

 - This feature is presenting sign up form wich is par of django-allauth and for 
 unauthenticated users CTA button from the home page is linked to this page so incentive is to get users registered so that they can experience the full benefits of th web app
 - For registering User must provide a username and strong enough password(for any errors user is prompted) 
 - User Story covered with this feature:3,4,18,19 

<details><summary>See Register Page</summary>

![Register Page](docs/features/sign_up_page.png)
![Register Page](docs/features/sign_up_mobile.png)
</details>

### Login page 

 - Returning users with created Profile(account) can get back and use the web app
 - user must provide valid username and password
 - User Story covered with this feature: 18,19,3

<details><summary>See Login Page</summary>

![Login Page](docs/features/login_page.png)
![Login Page](docs/features/login_mobile.png)
</details>

### Logout page
- This feature is presenting logout form wich is par of django-allauth library
- Authenticated user can click on a nav-bar link and 
he is redirected to a logout page where ho confirms that he wants to logout
- User Story covered with this feature:3,19

<details><summary>See Logout page Page</summary>

![Logout page](docs/features/logout.png)
![Logout page](docs/features/logout_modal.png)
</details>




### Forgot password page
 - This feature is also part of (django-allauth) and its included to help users
 start process of setting the new password if they forgot their password
  - User Story covered with this feature: 25,15

<details><summary>See Forgot password Page</summary>

![Forgot password Page](docs/features/forgot-password.png)
</details>




### Reset password finished
- after user puts his valid email to forgot password page he is redirected to this page and now can check his email for further directions
  - User Story covered with this feature:25,15 

<details><summary>See Forgot password finished Page</summary>

![Forgot password finished Page](docs/features/pass-reset-finish.png)
![Forgot password finished Page](docs/features/pass-reset-finish-mob.png)
</details>


### Set role page

- After successful registration user is redirected  to this page that gives the Mentor or Student functionality of a web app
- User can register as a Student or mentor.
- Each card presented gives a brief description of a role selected
and upon clicking the user profile role is set
- User Story covered with this feature: 2

<details><summary>See Set role Page</summary>

![Set role Page](docs/features/set-role.png)
![Set role Page](docs/features/set-role-mob.png)
</details>

### Create profile page
User is presented with a form
- User is filling out the form and all the information is stored in the database
- User must choose the category that he is interested in
- Its mandatory to provide the email address
- Its required filling all the fields except website and linkedIn url
- User is given the option to upload a supporting image to his profile
- User Story covered with this feature:4,3,20 

<details><summary>See Create profile Page</summary>

![Create profile Page](docs/features/create-profile.png)
![Create profile Page](docs/features/create-pofile-mob.png)
</details>

### Profile page
- This feature is a summary of info provided in create profie page 
structured nicely into simple jet effective profile page example
- User can updatehis profile by clickin on a update profile button
- user can delete profile by cicking on delete profile button
- User Story covered with this feature: 4,6,7

<details><summary>See Profile Page</summary>

![Profile Page](docs/features/profile-page.png)
![Profile Page](docs/features/see-profile-mob.png)
</details>

### Update Profile page
- User presented with a same form from create profile page
- User can update his profile info and all the datais updated in a database
- User Story covered with this feature:5,6,7
 <details><summary>See Update Profile Page</summary>

![Update Profile Page](docs/features/update-profile.png)
![Update Profile Page](docs/features/update-profile-mob.png)
</details>


### Delete Profile page
- User is presented with two options
- User can Delete his profile(he cant register with a same username again)
- User can go back to profile page
- User Story covered with this feature:6,7
 <details><summary>See Delete Profile Page</summary>

![Delete Profile Page](docs/features/delete-profile.png)
![Delete Profile Page](docs/features/delete-profile-mob.png)
</details> 

### Blog page
- Latest Blogs published are presented on this page
- Blogs are displayed using a cards elements(blog card)
- User Story covered with this feature:8,10
 <details><summary>See blog Card</summary>

![blog card page](docs/features/blog-card.png)
</details>

- Basic info about blogpost displayed on a blog card:
    - title of a blog
    - Creator of a blog
    - Date of publishing
    - Category of a blog

- User Story covered with this feature:8,10
 <details><summary>See Blog page</summary>

![Blog Page](docs/features/blog-page.png)
![Blog Page](docs/features/blog-page-mob.png)
</details> 

### Blog detail page
- User must be authenticated to get access to a blog detail page
- User can see full cntent of a blog post , all the comments posted for
that blog post
- User Story covered with this feature: 10,11
 <details><summary>See Blog detail Page</summary>

![Blog detail Page](docs/features/blog-detail1.png)
![Blog detail Page](docs/features/blog-detail1-mob.png)

</details> 

- If the user is the creator of a blog two icons are displayed, one for updating and the other one
for deleting a blog
- The user has the functionality to post a comment under the blog.
- Two icons are also displayed under each comment that logged in user-posted so he got options to delete or update a comment
- User Story covered with this feature:10,12
 <details><summary>See Comment section</summary>

![Comment section](docs/features/blog-detail2.png)
![Comment section](docs/features/blog-detail2-mob.png)
</details> 

### Delete blog (modal)
- User is presented with a pop up modal
- Two options in a modal one to delete a blogpost or to go back
- User Story covered with this feature:10
 <details><summary>See Delete blog(modal)</summary>

![Delete blog](docs/features/delete-blog-modal.png)
</details> 

### Add blog page
- User is presented with add blog form
- User can add title, supporting image for a blog, and body of a blog
- Only one of the categories selected in user profile can be selected as a category of a blogpost 
- User Story covered with this feature:9,12
 <details><summary>See Add blog page</summary>

![Add blog page](docs/features/add-blog.png)
![Add blog page](docs/features/add-blog-mob.png)
</details>

### Update comment page
- User is redirected to a page where a comment modal is
displayed so he can update his comment or go back
- User Story covered with this feature:17
 <details><summary>See Update comment page</summary>

![Update comment page](docs/features/update-comment.png)
![Update comment page](docs/features/update-comment-mob.png)
</details>

### Delete comment (modal)
- User is presented with a pop-up modal where he has two options.
 to delete the comment or go back
- User Story covered with this feature:17
 <details><summary>See Delete comment (modal)</summary>

![Delete comment](docs/features/delete-coment-modal.png)
![Delete comment](docs/features/delete-coment-modal-mob.png)
</details>

### Learning Category page (x3)
- This page contains information about each learning category.
- Users can read about benefits when gaining knowledge about each category.
- User can see mentors available by category and mentors' basic information and contact details.
- Blogs related to the category are displayed on the page.
- User Story covered by this feature:8,13,23,1
 <details><summary>See Learning Category page</summary>

![Learning Category page](docs/features/category-page.png)

![Learning Category page](docs/features/category-mentor.png)
</details>

 <details><summary>See Mentor section of category page</summary>

![Mentor section](docs/features/category-mentor.png)
![Mentor section](docs/features/cat-mentor-mob.png)
</details>


### Error handling pages
- Making the user experience good by handling errors that users can encounter
(404, 403, and 500 errors)
- User Story covered by this feature:18,19
 <details><summary>See Error pages</summary>

![404-page](docs/features/404-page.png)
![404-page](docs/features/404-mob.png)
![403-page](docs/features/403-page.png)
![403-page](docs/features/403-mob.png)
![500-page](docs/features/500-page.png)
![500-page](docs/features/500-mob.png)
</details>


## Future Features
***
For further releases of this web, there is a plan to implement new and improve
some of the existing features

1. Implement email validation before registering new users.
2. Dynamically updating comments
3. Implement replies for a comment section.
4. Enable the mentor user to add new learning categories with administrator approval.
5. Implement an internal messaging system between users (inbox).

##### Back to [top](#table-of-contents)

## Validation:
***

### CSS
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)was used  to validate the css in the project
    - web app passed validator with no errors. 
    <details><summary>Style.css</summary>
    <img src="docs/validation/html-css/valid-css.png" width="800">
    </details>

### Html
- [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project

- Note : all info on validator pages are related with using cloudinary template tags for rendering user uploaded images and there for trailing slash cant be removed
    

<details><summary>Home</summary>
<img src="docs/validation/html-css/home-html-valid.png" width="800" >
</details>

<details><summary>Register</summary>
<img src="docs/validation/html-css/signup-valid.png" width="800" >
</details>

<details><summary>Login</summary>
<img src="docs/validation/html-css/login-valid.png" width="800" >
</details>

<details><summary>password reset</summary>
<img src="docs/validation/html-css/password-reset-valid.png" width="800" >
</details>

<details><summary>password reset done</summary>
<img src="docs/validation/html-css/password-reset-done.png" width="800" >
</details>

<details><summary>Set role</summary>
<img src="docs/validation/html-css/set-role-valid.png" width="800" >
</details>

<details><summary>Set Profile</summary>
<img src="docs/validation/html-css/set-profile.png" width="800"  >
</details>

<details><summary>Profile</summary>
<img src="docs/validation/html-css/profile-valid.png" width="800" >
</details>

<details><summary>Edit profile</summary>
<img src="docs/validation/html-css/profile-edit-valid.png" width="800">
</details>

<details><summary>Delete profile</summary>
<img src="docs/validation/html-css/profile-delete-valid.png" width="800" >
</details>

<details><summary>Blog</summary>
<img src="docs/validation/html-css/blog.png" width="800" >
</details>

<details><summary>Blog add</summary>
<img src="docs/validation/html-css/blog-add.png" width="800" >
</details>

<details><summary>Blog detail</summary>
<img src="docs/validation/html-css/blog-detail-valid.png" width="800" >
</details>

<details><summary>Blog edit</summary>
<img src="docs/validation/html-css/blog-edit.png" width="800">
</details>

<details><summary>Category</summary>
<img src="docs/validation/html-css/category-valid.png" width="800" >
</details>


   
### Javascript
- [JShint](https://jshint.com/) was used to validate custom script file

    <details><summary>Js file</summary>
    <img src="docs/validation/python-js/custom-js.png" width="800" >
    </details>

### Python
- [CI Python Linter](https://pep8ci.herokuapp.com/) to check  Python code for validity and conventions

    <details><summary>Home app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/home-views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/home-url.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python-js/home-forms.png" width="800" >
    </details>



    <details><summary>tests_views.py</summary>
    <img src="docs/validation/python-js/home-test-views.png" width="800" >
    </details>

 
    </details>

    ***

    <details><summary>flow_blog app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/blog-views2.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/blog-urls.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python-js/blog-forms.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python-js/blog-models.png" width="800" >
    </details>

    <details><summary>tests_views.py</summary>
    <img src="docs/validation/python-js/blog-test-views.png" width="800" >
    </details>

    <details><summary>tests_models.py</summary>
    <img src="docs/validation/python-js/blog-test-models.png" width="800" >
    </details>

    <details><summary>tests_forms.py</summary>
    <img src="docs/validation/python-js/blog-test-forms.png" width="800" >
    </details>  
    </details>

    ***


    <details><summary>siteusers app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/siteusers-views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/siteusers-url.png" width="800" >
    </details>

    <details><summary>forms.py</summary>
    <img src="docs/validation/python-js/siteusers-forms.png" width="800" >
    </details>

    <details><summary>models.py</summary>
    <img src="docs/validation/python-js/siteusers-models.png" width="800" >
    </details>

    <details><summary>tests_views.py</summary>
    <img src="docs/validation/python-js/siteusers-test-views.png" width="800" >
    </details>

    <details><summary>tests_models.py</summary>
    <img src="docs/validation/python-js/siteusers-test-models.png" width="800" >
    </details>

    <details><summary>tests_forms.py</summary>
    <img src="docs/validation/python-js/siteusers-test-forms.png" width="800" >
    </details>  

    </details>

    ***

    <details><summary>categories app</summary>

    <details><summary>views.py</summary>
    <img src="docs/validation/python-js/categories-views.png" width="800" >
    </details>

    <details><summary>urls.py</summary>
    <img src="docs/validation/python-js/category-url.png" width="800" >
    </details>


    <details><summary>models.py</summary>
    <img src="docs/validation/python-js/categories-models.png" width="800" >
    </details>

    <details><summary>tests_views.py</summary>
    <img src="docs/validation/python-js/categories-test-views.png" width="800" >
    </details>

    <details><summary>tests_models.py</summary>
    <img src="docs/validation/python-js/categories-test-models.png" width="800" >
    </details>

  

    </details>

    ***   

### Lighthouse

- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance, accessibility, progressive web apps, SEO analysis of the project code here are the results:

- Note: Lighthouse results of testing the project may be inconsistent due to the functionality of user-uploaded images,Hosting project on Heroku may affected the results (server response time, caching, and network latency), But since Lighthouse scores are not the only measure of a website's performance and user experience, other factors such as functionality, accessibility, and usability should also be considered when determining the overall performance score of the project.
 
<details><summary>Home Desktop-screen</summary>
<img src="docs/validation/lighthouse/home-desk.png" >

</details>
<details><summary>Home Mobile-screen</summary>
<img src="docs/validation/lighthouse/Home-mob.png" >
</details>

<details><summary>Register page Desktop-screen</summary>
<img src="docs/validation/lighthouse/register-desk.png">
</details>
<details><summary>Register page Mobile-screen</summary>
<img src="docs/validation/lighthouse/register-mob.png">
</details>

<details><summary>Login Desktop-screen</summary>
<img src="docs/validation/lighthouse/login-desk.png" >
</details>

<details><summary>Login page Mobile-screen</summary>
<img src="docs/validation/lighthouse/login-mob.png">
</details>

<details><summary>password reset Desktop-screen</summary>
<img src="docs/validation/lighthouse/password-reset-desk.png">
</details>

<details><summary>password reset Mobile-screen</summary>
<img src="docs/validation/lighthouse/password-reset-mob.png">
</details>

<details><summary>password reset done Desktop-screen</summary>
<img src="docs/validation/lighthouse/pass-reset-done-desk.png">
</details>

<details><summary>password reset done Mobile-screen</summary>
<img src="docs/validation/lighthouse/pass-reset-done-mob.png">
</details>

<details><summary>Set role Desktop-screen</summary>
<img src="docs/validation/lighthouse/set-role-desk.png">
</details>

<details><summary>Set role Mobile-screen</summary>
<img src="docs/validation/lighthouse/set-role-mob.png">
</details>

<details><summary>Set Profile Desktop-screen</summary>
<img src="docs/validation/lighthouse/set-profile-desk.png">
</details>

<details><summary>Set Profile Mobile-screen</summary>
<img src="docs/validation/lighthouse/set-profile-mob.png">
</details>

<details><summary>Profile Desktop-screen</summary>
<img src="docs/validation/lighthouse/profile-desk.png">
</details>

<details><summary>Profile Mobile-screen</summary>
<img src="docs/validation/lighthouse/profile-mob.png">
</details>

<details><summary>Edit profile Desktop-screen</summary>
<img src="docs/validation/lighthouse/update-profile-desk.png">
</details>

<details><summary>Edit profile Mobile-screen</summary>
<img src="docs/validation/lighthouse/update-profile-desk.png">
</details>

<details><summary>Delete profile Desktop-screen</summary>
<img src="docs/validation/lighthouse/delete-profile-desk.png">
</details>

<details><summary>Delete profile Mobile-screen</summary>
<img src="docs/validation/lighthouse/delete-profile-mob.png">
</details>

<details><summary>Blog Desktop-screen</summary>
<img src="docs/validation/lighthouse/blog-desk.png">
</details>

<details><summary>Blog Mobile-screen</summary>
<img src="docs/validation/lighthouse/blog-mob.png">
</details>

<details><summary>Blog add Desktop-screen</summary>
<img src="docs/validation/lighthouse/add-blog-desk.png">
</details>

<details><summary>Blog add Mobile-screen</summary>
<img src="docs/validation/lighthouse/add-blog-mob.png">
</details>


<details><summary>Blog detail Desktop-screen</summary>
<img src="docs/validation/lighthouse/blog-detail-desk.png">
</details>

<details><summary>Blog detail Mobile-screen</summary>
<img src="docs/validation/lighthouse/blog-detail-mob.png">
</details>

<details><summary>Blog edit Desktop-screen</summary>
<img src="docs/validation/lighthouse/blog-edit-desk.png">
</details>

<details><summary>Blog edit Mobile-screen</summary>
<img src="docs/validation/lighthouse/blog-edit-mob.png">
</details>

<details><summary>Comment edit Desktop-screen</summary>
<img src="docs/validation/lighthouse/comment-edit-desk.png">
</details>

<details><summary>Comment edit Mobile-screen</summary>
<img src="docs/validation/lighthouse/comment-edit-mob.png">
</details>

<details><summary>Category Desktop-screen</summary>
<img src="docs/validation/lighthouse/category-desk.png">
</details>

<details><summary>Category Mobile-screen</summary>
<img src="docs/validation/lighthouse/category-mob.png">
</details>




### Wave
 [Wave Validator](https://wave.webaim.org/) to evaluate accessibility

- NOTE : Alerts in Wave Validator are connected with the "alt" attribute of images uploaded by
the user. they needed to be put as generic since  user cant put alt text for the image 

<details><summary>Home</summary>
<img src="docs/validation/wave/home-pg.png" width="800" height="1200" >
</details>

<details><summary>Register</summary>
<img src="docs/validation/wave/register-pg.png" width="800" height="1200">
</details>

<details><summary>Login</summary>
<img src="docs/validation/wave/login-pg.png" width="800" height="1200">
</details>

<details><summary>password reset</summary>
<img src="docs/validation/wave/password-reset.png" width="800" >
</details>

<details><summary>password reset done</summary>
<img src="docs/validation/wave/pass-reset-done.png" width="800" >
</details>

<details><summary>Set role</summary>
<img src="docs/validation/wave/set-role-pg.png" width="800" >
</details>

<details><summary>Set Profile</summary>
<img src="docs/validation/wave/create-profile.png" width="800"  >
</details>

<details><summary>Profile</summary>
<img src="docs/validation/wave/see-profile.png" width="800" >
</details>

<details><summary>Edit profile</summary>
<img src="docs/validation/wave/edit-profile.png" width="800">
</details>

<details><summary>Delete profile</summary>
<img src="docs/validation/wave/delete-profile.png" width="800" >
</details>

<details><summary>Blog</summary>
<img src="docs/validation/wave/blog.png" width="800" >
</details>

<details><summary>Blog add</summary>
<img src="docs/validation/wave/add-blog.png" width="800" >
</details>

<details><summary>Blog detail</summary>
<img src="docs/validation/wave/blog-detail.png" width="800" >
</details>

<details><summary>Blog edit</summary>
<img src="docs/validation/wave/blog-edit.png" width="800">
</details>

<details><summary>Category</summary>
<img src="docs/validation/wave/category-pg.png" width="800" >
</details>

## Testing
***

- Knowledge flow was tested during and post development and all
results for 
    - Device Testing
    - Browser Compatibility
    - Manual Testing
    - Automated Testing

    are contained in TESTING.md file that you can see [here.](https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/docs/TESTING.md)

## Bugs
***
- following Bugs are found during the development of this project
1. Migration error
   <details><summary>see bug</summary>
    <img src="docs/bugs/migration-error1.png" width="800">
    </details>

2. Bad request(Heroku) images issue
   <details><summary>see bug</summary>
    <img src="docs/bugs/bad-request-image-issue.png" width="800">
    </details>


3. Prepopulated comment form
   <details><summary>see bug</summary>
    <img src="docs/bugs/bug3.png" width="800">
    </details>

4. only last object deleted
   <details><summary>see bug</summary>
    <img src="docs/bugs/bug4.png" width="800">
    </details>


5. missing alt text for "cloudinary tag images" 
   <details><summary>see bug</summary>
    <img src="docs/bugs/bug5.png" width="800">
    </details>


6. Button outlined after click 
   <details><summary>see bug</summary>
    <img src="docs/bugs/bug6.png" width="800">
    </details>

7. not redirected properly after submitting the form 
   <details><summary>see bug</summary>
    <img src="docs/bugs/bug7.png" width="800">
    </details>


## Deployment
***
- During the initial phases of development, Knowledge Flow was deployed on Heroku. To avoid any potential deployment issues near the app's release, I made sure that the database and static files were accessible right from the start of the project.

###  Creating Database ==> ElephantSQL
1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.
    <details><summary>See Image</summary>

    ![ElephantSQL](docs/deployment/elephant.png)
    </details>

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'
    <details><summary>See Image</summary>

    ![ElephantSQL](docs/deployment/tiny-turtle.png)
    </details>

3. Select your preferred region and create the database instance.
    After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.
    <details><summary>See Image</summary>

    ![ElephantSQL](docs/deployment/instance.png)
    </details>

### Heroku Deployment

- Before deploying to Heroku there are a few things to have ready
ElephantSQL Database url, SECRET_KEY variable(generate key different from provided one), CLOUDINARY_URL variable(after logging in the Cloudinary website copy the 'cloudinary url' from your account dashboard as the value of a variable )
- Create env.py (at the root level of your project) This file contains the above mentioned
variables in a form of:
- os.environ['DATABASE_URL'] = 'value of ElephantSQL Database url'
        <details><summary>See Image</summary>
        ![DATABASE_URL](docs/deployment/url.png)
        </details>

- os.environ['SECRET_KEY'] = 'value of secret key'
    secret key could be generated [here](https://miniwebtool.com/django-secret-key-generator/)
        <details><summary>See Image</summary>
        ![SECRET_KEY](docs/deployment/key.png)
        </details>

-  os.environ['CLOUDINARY_URL'] = 'value of 'cloudinary url' from your  
   account dashboard'
   cloudinary url can be found [here](https://console.cloudinary.com/)
        <details><summary>See Image</summary>
        ![CLOUDINARY_UR](docs/deployment/cloudinary.png)
        </details> 

1. First, sign up or sign in to your Heroku account. Next, create a new app from the Heroku dashboard.
        <details><summary>See Image</summary>
        ![heroku](docs/deployment/heroku-app.png)
        </details>

2. Choose a unique name for your app and enter the region.Then, click on the 
    'Create App' button.
    Once your app has been created, select the 'Settings' tab from the dashboard and navigate to 'Reveal Config Vars'. From there, paste the: 
    - ElephantSQL Database URL into the DATABASE_URL environment variable.
    - SECRET_KEY variable  into the SECRET_KEY environment variable.
    - CLOUDINARY_URL variable  into the CLOUDINARY_URL environment variable.
    - add DISABLE_COLLECTSTATIC variablewith value of 1 (for initial deployment, later this variable can be removed)
    - add variable named PORT with value of 8000

    <details><summary>See Images</summary>

    ![heroku](docs/deployment/heroku2.png)
    ![heroku](docs/deployment/heroku3.png)
    </details>

3. Select Deploy option from the 'tabs'
     <details><summary>See Image</summary>

    ![heroku](docs/deployment/heroku4.png)
    </details>

4. From Deployment method section choose Connect to GitHub and click on it
     <details><summary>See Image</summary>

    ![heroku](docs/deployment/heroku-deploy-meth.png)
    </details>

5. Find your github repository by name and connect
     <details><summary>See Image</summary>

    ![heroku](docs/deployment/heroku-repo-connected.png)
    </details>

6. At the bottom of the page choose either automatic deployment manual 
   deployment(deploy by branch)
     <details><summary>See Image</summary>

    ![heroku](docs/deployment/manual-auto-deploy.png)
    </details> 

7. Click on the option you want, and you should be able to see the boiler process.
    and after a while, your app should be deployed.
         <details><summary>See Image</summary>

    ![heroku](docs/deployment/build.png)
    ![heroku](docs/deployment/build-finish.png)
   
    </details> 


### Forking the GitHub Repository

1. Login or Signup to [Github](https://github.com/)
2. Navigate to  the GitHub repository link  https://github.com/rockroman/CI_PP4-Knowledge-Flow
2. Click on the Fork button in the top right corner

<img src="docs/deployment/git-fork.png">

3. Copy of the repository will be in your own GitHub account.


### Clone a GitHub Repo

1. Go to the GitHub repository  https://github.com/rockroman/CI_PP4-Knowledge-Flow
2. Locate the Code button above the list of files (next to 'Add file') and click it

<img src="docs/deployment/clone.png">

3. choose a preferred cloning option by selecting either HTTPS or GitHub CLI.
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone



## Credits

### Code

- The code for building nav-bar component was taken and adjusted to my project needs from [here](https://getbootstrap.com/)
- The code for building footer and profile page component  was taken and adjusted to my project needs from [here](https://mdbootstrap.com/)
- The code for building team section component was taken and adjusted to my project needs from [here](https://codepen.io/search/pens?q=team+section&cursor=ZD0xJm89MCZwPTQ=)
- The code for building back to top button functionality component was taken and adjusted to my project needs from [here](https://mdbootstrap.com/docs/standard/extended/back-to-top/)
- The code for building allauth forms components was taken and adjusted to my project needs from [here](https://blog.nirmites.com/)

## Tutorials 

- [This](https://www.youtube.com/watch?v=S9-Bt1JgRjQ) tutorial helped me understand django  Context Processors functionality
- [This](https://www.youtube.com/watch?v=FdVuKt_iuSI) tutorial helped me solidify my knowledge of Django views, forms, and templates


### Imagery

- Hero image  taken from [here](https://unsplash.com/@greg_rosenke)
- Team section images are taken from  [here] (https://www.pexels.com/) 
- Mentor role image is taken from [here](https://pixabay.com/users/harishs-3407954/)
- Student role image is taken from[here](https://pixabay.com/users/geralt-9301/)
- Default blog post  image taken from [here](https://unsplash.com/s/photos/cup)
- Leadership learning category image is taken from[here](https://pixabay.com/users/mohamed_hassan-5229782/) 
- Personal-finance learning category image is taken from [here](https://pixabay.com/users/mohamed_hassan-5229782/) 
- Time-management learning category image is taken from [here](https://pixabay.com/users/mohamed_hassan-5229782/) 

- All other images are uploaded by the users of the website


## Acknowledgements

***
I would like to take a few moments to say Thank you to the following people:

- First, I would like to thank my wife Una, and my daughter Tara for their continuous support and understanding while working on the development of this project.

-  I would like to thank my Mentor Mo.Shami for his support, insight expertise, and guidance.

-  Awesome Code Institute Slack community for being there