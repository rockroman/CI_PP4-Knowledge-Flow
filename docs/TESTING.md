# TESTING





## Table of Contents

1. [Device Testing](#device-testing)
2. [Browser Compatibility](#browser-compatibility)
3. [Manual Testing](#manual-testing-of-user-stories)
4. [Automated Testing](#automated-testing)


***
## Device testing
***

### Mobile devices 

- project was tested during and post development on following  devices

#### Samsung A52
- Results are here:

    <details><summary>Screenshot</summary>
    <img src="./device-testing/samsung1.jpg" >
    <img src="./device-testing/samsung2.jpg" >
    <img src="./device-testing/samsung3.jpg" >
    <img src="./device-testing/samsung4.jpg" >
    <img src="./device-testing/samsung5.jpg" >
    <img src="./device-testing/samsung6.jpg" >
    <img src="./device-testing/samsung7.jpg" >

    </details>

#### Iphone 13 mini 
- Results are here:

    <details><summary>Screenshot</summary>
    <img src="./device-testing/iphone1.png" >
    <img src="./device-testing/iphone2.png" >
    <img src="./device-testing/iphone3.png" >
    <img src="./device-testing/iphone4.png" >
    <img src="./device-testing/iphone5.png" >
    <img src="./device-testing/iphone6.png" >
    
    </details>


#### Ipad 3rd generation 
- Results are here:

    <details><summary>Screenshot</summary>
    <img src="./device-testing/ipad1.jpg" >
    <img src="./device-testing/ipad2.jpg" >
    <img src="./device-testing/ipad3.jpg" >
    <img src="./device-testing/ipad4.jpg" >
    <img src="./device-testing/ipad5.jpg" >
    <img src="./device-testing/ipad6.jpg" >
    
    </details>


***
## Browser compatibility
***
Testing was conducted on the following browsers;

- Chrome;

<details><summary>Screenshot</summary>
    <img src="./browser-compatibility/chrome1.png" >
    <img src="./browser-compatibility/chrome2.png" >    
    <img src="./browser-compatibility/chrome3.png" >    
</details>

- Firefox;

<details><summary>Screenshot</summary>
    <img src="./browser-compatibility/fox1.png" >
    <img src="./browser-compatibility/fox2.png" >    
    <img src="./browser-compatibility/fox3.png" >    
</details>

- Microsoft Edge;

<details><summary>Screenshot</summary>
    <img src="./browser-compatibility/edge1.png" >
    <img src="./browser-compatibility/edge2.png" >    
    <img src="./browser-compatibility/edge3.png" >    
</details>




## Manual testing of user stories
***
WAS = Works as expected


0. As a user I want to navigation to be intuitive and user-friendly so that Im able to easily navigate through the app content.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigating to :https://knowledge-flow.herokuapp.com/ | home page loads | WAS |
User scrolls through the home page | Content of the page is presented | WAS |
User click on a Link in the nav bar | user taken to desired part of the web app | WAS |



 <details><summary>Screenshot</summary>
<img src="./user-story-test/story1new.png" >
<img src="./user-story-test/story00.png" >
<img src="./user-story-test/story00a.png" >
<img src="./user-story-test/story00d.png" >
<img src="./user-story-test/story00ad.png" >

</details>

1. As a user I want to know Important info on what the app is about so that I can use it's functionality on mutual benefit

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigating to :https://knowledge-flow.herokuapp.com/ | home page loads | WAS |
User scrolls through the home page | Content of the page is presented | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story1.png" >
<img src="./user-story-test/story1a.png" >
<img src="./user-story-test/story1m.png" >
<img src="./user-story-test/story1ma.png" >

</details>

2. As an authenticated user I would like to be able to choose a way to get benefit from the app with choosing the right role

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Register" link in a nav bar | Loads register form | WAS |
User is filling out form correctly| set role page loads with success message | WAS |
User reads brief info about 2 roles presented and clicks on "Mentor" button | Set profile page is loaded anduser profile role is set as "Mentor"  | WAS |
after setting up profile user clicks "set profile" button  |User email is available on a category page for student users to see along with website and linkedIn url if they have been set  | WAS |
User reads brief info about 2 roles presented and clicks on "Student" button | Set profile page is loaded anduser profile role is set as "Student"  | WAS |

 <details><summary>Screenshots</summary>
<img src="./user-story-test/story2da.png" >
<img src="./user-story-test/story2db.png" >
<img src="./user-story-test/story2dc.png" >
<img src="./user-story-test/story2dd.png" >
<img src="./user-story-test/story2de.png" >
<img src="./user-story-test/story2ma.png" >
<img src="./user-story-test/story2mb.png" >
<img src="./user-story-test/story2mc.png" >
<img src="./user-story-test/story2md.png" >
<img src="./user-story-test/story2me.png" >

</details>



3. As an authenticated user I would like to have a full access to the content of an web app

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Register" link in a nav bar | Loads register form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
User navigates to a "Login" link in a nav bar | Loads Login form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
User clicks on a link in the nav bar |user taken to desired part of the web app  | WAS |


 <details><summary>Screenshots</summary>
<img src="./user-story-test/story2da.png" >
<img src="./user-story-test/story2db.png" >
<img src="./user-story-test/story3db.png" >
<img src="./user-story-test/story3dc.png" >
<img src="./user-story-test/story00.png" >
<img src="./user-story-test/story00d.png" >
<img src="./user-story-test/story2ma.png" >
<img src="./user-story-test/story2mb.png" >
<img src="./user-story-test/story3mb.png" >
<img src="./user-story-test/story3mc.png" >
<img src="./user-story-test/story00a.png" >
<img src="./user-story-test/story00ad.png" >

</details>



4. As an authenticated user I would like a functionality to create profile(account)

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to register link on a navbar| registration form loads | WAS |
Fill out registration form with all required data|form submmited with succes message  | WAS |
Click on desired profile role|choose role page  displayed with 2 options   | WAS |
Inputing required data into a create profile form| form is submited with a success message that profile is created | WAS |


<details><summary>Screenshots</summary>
<img src="./user-story-test/story2dd.png" >
<img src="./user-story-test/story2de.png" >
<img src="./user-story-test/story2md.png" >
<img src="./user-story-test/story2me.png" >
</details>

5. As an authenticated user I would like functionality to upload a supporting image to my profile and change it when I desire

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "profile" link in the nav bar| loads profile page | WAS |
Click "update profile" button| loads profile form | WAS |
Click on the choose file button | window with local files open so file can be uploaded after successful upload succes message is rendered | WAS |
 


 <details><summary>Screenshots</summary>
<img src="./user-story-test/story5da.png" >
<img src="./user-story-test/story5db.png" >
<img src="./user-story-test/story5dc.png" >
<img src="./user-story-test/story5ma.png" >
<img src="./user-story-test/story5mb.png" >
<img src="./user-story-test/story5mc.png" >
</details>

6. As an authenticated user I would like a functionality to update or delete profile (account) if not planning to use web app anymore

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigte to a profile link in the nav bar | profile page loads | WAS |
Click on update profile button| update profile form is displayed | WAS |
Click on any field change the data and click updaate profile | user redirected to profile page with successs message that profile is updated   | WAS |
Click on delete profile|delete profile page loads  | WAS |
Click on delete button| user is redirected to home page and his profile deleted | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story5da.png" >
<img src="./user-story-test/story6db.png" >
<img src="./user-story-test/story6dc.png" >
<img src="./user-story-test/story6da.png" >
<img src="./user-story-test/story5ma.png" >
<img src="./user-story-test/story6mb.png" >
<img src="./user-story-test/story6mc.png" >
<img src="./user-story-test/story6ma.png" >
</details>

7. As an authenticated user I would like functionality to pick different types of learning categories in my profile and change them later

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigte to a profile link in the nav bar | profile page loads | WAS |
Click on update profile button| update profile form is displayed | WAS |
Click on category to tick the multiple selection box if category is to be added or click on ticked box for category to be removed|depending on action user is redirected to profile page and category is set  | WAS |


 <details><summary>Screenshot</summary>
 <img src="./user-story-test/story5da.png" >
 <img src="./user-story-test/story7da.png" >
 <img src="./user-story-test/story7db.png" >
 <img src="./user-story-test/story7dc.png" >
 <img src="./user-story-test/story7dd.png" >
<img src="./user-story-test/story5ma.png" >
<img src="./user-story-test/story7ma.png" >
<img src="./user-story-test/story7mb.png" >
<img src="./user-story-test/story7mc.png" >

</details>

8. As an authenticated user I would like functionality to see and read blog posts that other users created

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to a blog link in the nav bar or click "SEE BLOGS" in the hero section| Loads blogs page | WAS |
Click on a blog title or "Read the blog" button| blog detail page is loaded | WAS |


<details><summary>Screenshot</summary>
<img src="./user-story-test/story8da.png" >
<img src="./user-story-test/story8db.png" >
<img src="./user-story-test/story8dc.png" >
<img src="./user-story-test/story8ma.png" >
<img src="./user-story-test/story8mb.png" >
<img src="./user-story-test/story8mc.png" >
</details>


9. As an authenticated user I would like to upload a blog in a selected category so that I can share my knowledge,opinion and informations

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "Add Blog" link in the nav bar and click on it |The "Create Blog" form is loaded| WAS |
Enter relevant data for posting the blog| Form is populated with user data | WAS |
From the drop-down category menu, select category |Categories that are chosen during the profile set up are displayed in the drop-down menu  | WAS |
 Click the "Post" button|user is redirected to blog page with success message that "YOU ADDED A NEW BLOG" | WAS |


 <details><summary>Screenshot</summary>
 <img src="./user-story-test/story9da.png" >
 <img src="./user-story-test/story9db.png" >
 <img src="./user-story-test/story9dc.png" >
<img src="./user-story-test/story9ma.png" >
<img src="./user-story-test/story9mb.png" >
<img src="./user-story-test/story9mc.png" >
</details>

10. As an authenticated user I would like functionality to delete or update my blog post i I find it no longer relevant

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "Blog" link in the nav bar and click on it |page with latest blogs is loaded| WAS |
Find the blog you want to update and click on update(pencil) icon |Blog form with blog data is displayed | WAS |
Enter new relevant data for your blog and press "Post" button |blog page loads with success message and your blog is updated  | WAS |
Navigate to "Blog" link in the nav bar and click on it |page with latest blogs is loaded| WAS |
Find the blog you want to delete and click on delete(trash-can) icon |pop up modal shows and asking user to confirm that he wants to delete blog | WAS |
Press "delete" button|blogs page loads with success message"your blog post is deleted | WAS |


 <details><summary>Screenshot</summary>
 <img src="./user-story-test/story10da.png" >
 <img src="./user-story-test/story10db.png" >
 <img src="./user-story-test/story10dc.png" >
 <img src="./user-story-test/story10dd.png" >
 <img src="./user-story-test/story10de.png" >
 <img src="./user-story-test/story10df.png" >
 <img src="./user-story-test/story10g.png" >

</details>

11. As an authenticated user I would like functionality to leave a comment on a blog post

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to a blog link in the nav bar or click "SEE BLOGS" in the hero section| Loads blogs page | WAS |
click on a blog title or read the blog button| blog detail page is loaded | WAS |
scroll to the end of a blog | comment section is displayed | WAS |
enter your comment text and press green button|success message is displayed and you can see your comment in comment section  | WAS |

 <details><summary>Screenshot</summary>
  <img src="./user-story-test/story11a.png" >
  <img src="./user-story-test/story11b.png" >
  <img src="./user-story-test/story11c.png" >
  <img src="./user-story-test/story11d.png" >
</details>

12. As an authenticated user I would like functionality to support my blog post with a cover image and change it later if needed.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "Add Blog" link in the nav bar and click on it |The "Create Blog" form is loaded| WAS |
Enter relevant data for posting the blog| Form is populated with user data | WAS |
From the drop-down category menu, select category |Categories that are chosen during the profile set up are displayed in the drop-down menu  | WAS |
Click "Choose file" under image section of blog form |window with local files is displayed  | WAS |
Click on image you want to be the blog cover image |name of the image is displayed in the image section  | WAS |
 Click the "Post" button|user is redirected to blog page with success message that "YOU ADDED A NEW BLOG" | WAS |


 <details><summary>Screenshots</summary>
  <img src="./user-story-test/story12a.png" >
  <img src="./user-story-test/story12b.png" >
  <img src="./user-story-test/story12c.png" >
</details>

13. As an authenticated user I would like the functionality for each category page to have a list of mentors avaliable and their contact info

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "Learning categories" link in the nav bar and click on it| dropdown menu is displayed | WAS |
Click on a category you want to display|Selected category page is displayed | WAS |
Navigate to a "mentors available section" click on it|cards with available mentors is displayed   | WAS |


 <details><summary>Screenshots</summary>
<img src="./user-story-test/story13a.png" >
<img src="./user-story-test/story13b.png" >
<img src="./user-story-test/story13c.png" >
</details>

14. As a user I would like web app to be fully responsive and to have the same experience when using on any device

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Change device screen size using chrome dev tools |Web app ux and designs remains consistent on various screen sizes | WAS |
Change device with any extension(mobile simulaor) that simulates devices screes| Web app ux and designs remains consistent on various screen sizes| WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story14a.png" >
<img src="./user-story-test/story14b.png" >
<img src="./user-story-test/story14c.png" >
<img src="./user-story-test/story14d.png" >
<img src="./user-story-test/story14e.png" >
<img src="./user-story-test/story14f.png" >
</details>

15. As an returning user user I would like functionality to set a new password if I forgot the password so that I can still use the web app

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Login" link in a nav bar | Loads Login form | WAS |
Click on a "forgot password" link at the bottom of the form| password reset page loads| WAS |
Enter the valid email address that was used in setting up the profile and press "reset my password"|password reset done page is displayed and email with reset link is sent  | WAS |
Open your email inbox and reset password mail with a link should be there|link takes user through a process of setting a new pasword  | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story15a.png" >
<img src="./user-story-test/story15b.png" >
<img src="./user-story-test/story15c.png" >
</details>

16. As a User I would like a Functionality to contact the app owner or a team so that I can leave a suggestion or express my opinion about the web app

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Register" link in a nav bar | Loads register form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
User navigates to a "Login" link in a nav bar | Loads Login form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
Navigate to "About us" link in a navbar | Page scrolls to about section with a form | WAS |
Scroll to the "About us" section of the page| Contact form is displayed | WAS |
User is filling out form correctly and pressing "Send" button|User taken to top of the page and succes message"Thank you for your message" is displayed  | WAS |

 <details><summary>Screenshot</summary>
<img src="./user-story-test/story16a.png" height="600" >
<img src="./user-story-test/story16b.png" height="600" >
<img src="./user-story-test/story16c.png" height="600" >
<img src="./user-story-test/story16d.png" height="600" >
<img src="./user-story-test/story16e.png" height="600" >
<img src="./user-story-test/story16f.png" height="600" >
</details>

17. As a user I would like a Functionality to update or delete a comment I posted to a blogpost so that if any mistake was made or new information is acquired anyone reading will be up to date

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to a "blog" link in the nav bar or click "SEE BLOGS" in the hero section| Loads blogs page | WAS | 
Click on a blog title or "Read The blog" button of a blog that the comment is posted for| Blog detail page is loaded | WAS |
Scroll to comment you posted ad to update click on a "pencil" button | Update comment page loads  | WAS |
Click on the comment field update the comment and press "update " button  | comment is updated and success message is displayed  | WAS |
 Click on a "trash" button to delete comment and in a pop up modal press "delete"| delete modal pops up and after delete is pressed comment is deleted with a success message  | WAS |
 

 <details><summary>Screenshot</summary>
<img src="./user-story-test/story17a.png">
<img src="./user-story-test/story17b.png">
<img src="./user-story-test/story17c.png">
<img src="./user-story-test/story17d.png">
<img src="./user-story-test/story17e.png">

</details>

18. As a site owner I want to restrict access to sections of an app to unauthenticated users so that basic standards of data protection are met

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Not logged in user Clicks on "Learning category" link | dropdown with categories is displayed | WAS |
Not logged in user Clicks on any category | Login page loads | WAS |
Not logged in user Clicks on a "Blogs" link in a navbar | Blog page loads  | WAS |
Not logged in user Clicks on a title or "Read The blog" button |Login page loads  | WAS |
Not logged in user scrolls to a contact form and after filling it out clicks a "send" button | user taken to top of the page with a warnning message "needs to be logged in to send message"  | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story18a.png" height="600" >
<img src="./user-story-test/story18b.png" height="600" >
<img src="./user-story-test/story18c.png" height="600" >
<img src="./user-story-test/story18d.png" height="600" >
<img src="./user-story-test/story18e.png" height="600" >
</details>

19. As a Site Owner I would like that authenticated users have full access to web app and its functionality

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to "About us" link in a navbar | Page scrolls to about section with a form | WAS |
Scroll to the "About us" section of the page| Contact form is displayed | WAS |
User is filling out form correctly and pressing "Send" button|User taken to top of the page and succes message"Thank you for your message" is displayed  | WAS |
Navigate to "Add Blog" link in the nav bar and click on it |The "Create Blog" form is loaded| WAS |
Enter relevant data for posting the blog| Form is populated with user data | WAS |
From the drop-down category menu, select category |Categories that are chosen during the profile set up are displayed in the drop-down menu  | WAS |
 Click the "Post" button|user is redirected to blog page with success message that "YOU ADDED A NEW BLOG" | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story16d.png" height="600" >
<img src="./user-story-test/story16e.png" height="600" >
<img src="./user-story-test/story16f.png" height="600" >
<img src="./user-story-test/story19a.png" height="600" >
<img src="./user-story-test/story19b.png" height="600" >
<img src="./user-story-test/story19c.png" height="600" >
</details>

20. As a Site Owner I would like that each data entry is validated before stored in database

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigte to a profile link in the nav bar | profile page loads | WAS |
Click on update profile button| update profile form is displayed | WAS |
Fill fill the form and try to leave empty any field except website and linkedIn url fields and press update | form error message is displayed "please fill out this field"   | WAS |
Navigate to "Add Blog" link in the nav bar and click on it |The "Create Blog" form is loaded| WAS |
Enter relevant data for posting the blog but dont add category| Form is populated with user data | WAS |
click "post" button | message is displayed to select the item from the list and blog is not posted | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story20a.png">
<img src="./user-story-test/story20b.png">
<img src="./user-story-test/story20c.png">
<img src="./user-story-test/story20d.png">
</details>

21. As a Site Owner I would like that users an leave a message or feedback via contact form or

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Register" link in a nav bar | Loads register form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
User navigates to a "Login" link in a nav bar | Loads Login form | WAS |
User is filling out form correctly| Home page loads with success message | WAS |
Navigate to "About us" link in a navbar | Page scrolls to about section with a form | WAS |
Scroll to the "About us" section of the page| Contact form is displayed | WAS |
User is filling out form correctly and pressing "Send" button|User taken to top of the page and succes message"Thank you for your message" is displayed  | WAS |

 <details><summary>Screenshot</summary>
<img src="./user-story-test/story16d.png" height="600" >
<img src="./user-story-test/story16e.png" height="600" >
<img src="./user-story-test/story16f.png" height="600" >
</details>

22. As a Site Owner I would like that users have more than one way of comunicating with team or     myself
    - NOTE: SINCE THIS IS THE PROJECT FOR EDUCATIONAL PURPOSES AT THE MOMENT LINKS IN TEAM SECTION
    ARE TAKING USER TO A LOGIN SOCIAL MEDIA PAGE(NOT ACTUAL TEAM MEMMBER PAGE)

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User scrolls to the bottom of the website| website footer is presented | WAS |
User clicks on a github icon| site owner github page opens in a new window | WAS |
User scrolls to the bottom of the website| website footer is presented | WAS |
User clicks on a LinkedIn icon |site owner LinkedIn page opens in a new window  | WAS |
User scrolls to the team section  and click on any social media icon on a team member card | Social media page of a team member opens  | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story22a.png" height="600" >
<img src="./user-story-test/story22c.png" height="600" >
</details>

23. As a Site Owner I would like that each 'Mentor' user cant see himself on the list of available mentors for his respective category(user wont be contacting himself)

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Register" link in a nav bar | Loads register form | WAS |
User is filling out form correctly| set role page loads with success message | WAS |
User reads brief info about 2 roles presented and clicks on "Mentor" button | Set profile page is loaded anduser profile role is set as "Mentor"  | WAS |
after setting up profile user clicks "set profile" button  |User email is available on a category page for student users to see along with website and linkedIn url if they have been set  | WAS |
User navigates to his Learning category page (selected in profile) and clicks on available mentors link | Users data is not displayed to himself | WAS |


 <details><summary>Screenshot</summary>
  <img src="./user-story-test/story23.png" >
  <img src="./user-story-test/story23b.png" >

</details>

24. As a Site Owner I would like that each authenticated user gets prompt messages when performing CRUD(Create,Read,Update,Delete) operations when using web app.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to a blog link in the nav bar or click "SEE BLOGS" in the hero section| Loads blogs page | WAS |
click on a blog title or read the blog button| blog detail page is loaded | WAS |
scroll to the end of a blog | comment section is displayed | WAS |
enter your comment text and press green button|success message is displayed and you can see your comment in comment section  | WAS |
Navigte to a profile link in the nav bar | profile page loads | WAS |
Click on update profile button| update profile form is displayed | WAS |
Click on any field change the data and click updaate profile | user redirected to profile page with successs message that profile is updated   | WAS |

 <details><summary>Screenshot</summary>
<img src="./user-story-test/story11a.png" >
<img src="./user-story-test/story11b.png" >
<img src="./user-story-test/story11c.png" >
<img src="./user-story-test/story11d.png" >
<img src="./user-story-test/story5ma.png" >
<img src="./user-story-test/story6mb.png" >
<img src="./user-story-test/story6mc.png" >
</details>


25. As a Site Owner I would like that each authenticated user has option to get access to an app if he forgots password for any reason via (Reset password functionality)

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User navigates to a "Login" link in a nav bar | Loads Login form | WAS |
Click on a "forgot password" link at the bottom of the form| password reset page loads| WAS |
Enter the valid email address that was used in setting up the profile and press "reset my password"|password reset done page is displayed and email with reset link is sent  | WAS |
Open your email inbox and reset password mail with a link should be there|link takes user through a process of setting a new pasword  | WAS |


 <details><summary>Screenshot</summary>
<img src="./user-story-test/story15a.png" >
<img src="./user-story-test/story15b.png" >
<img src="./user-story-test/story15c.png" >
</details>


## Automated testing


Automated testing was conducted utilizing the "unittest" module from the Python standard library, which is integrated with Django's unit tests. Subsequently, reports were generated by utilizing the coverage tool.
and results are here:

- Whole  project:

<img src="./automated-testing/project-coverage1.png">
<img src="./automated-testing/project-coverage2.png">
<img src="./automated-testing/project-tests.png">



- Home app:

<img src="./automated-testing/home-test.png">
<img src="./automated-testing/home-coverage.png">

- categories app:

<img src="./automated-testing/categories-test.png">
<img src="./automated-testing/categories-coverage.png">

- flow_blog app:

<img src="./automated-testing/flow_blog-test.png">
<img src="./automated-testing/flow-blog-coverage.png">

- siteusers app:

<img src="./automated-testing/siteusers-test.png">
<img src="./automated-testing/siteusers-coverage.png">