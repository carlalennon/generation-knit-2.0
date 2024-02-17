# Generation Knit 

## Overview

Generation Knit is a pattern charing website, built to address the need for a modern, responsive and accesbile website in the online knitting space. It provides a space for users to upload and share pattterns for knitting and crochet 

[Screenshot of Generation Knit home page]

## Project Goals 

For my fourth portfolio projects, I wanted to create a project that both showcased my proficiency with databases, Bootstrap and Django. My project goal is to show that I can use these tools effectively in a creative way.

Generation Knit serves as a platform to both share and find knitting patterns. The goal was to create a platform that stores the information that comes with a knitting pattern and display it back to the user in an attractive and intuitive. The largest community based knitting website on the internet has long been criticized for its confusing layout and lack of accessibilty for visually impaired users. My website aims to address these issues.

## Contents: 

- What happened to Generation Knit 1.0? 
- UX Design
- Accessibilty Focus
- User Avatar
- Site Goals
- Agile Method
- Wireframes
- Data Modelling Relationships
- Structure
- - Features
- - Future Features
- Design 
- - Colours 
- - Typography 
- Languages 
- - Django 
- - JavaScript
- - Bootstrap
- Deployment
- Linting 
- Error Hall of Fame
- Citations 


## What happened to Generation Knit 1.0? 

I started work on the first version of this project in October 2023. After multiple issues with Codeanywhere, I was advised by Code Institute to start again from scratch on Gitpod. I quickly rebuilt my project as Generation Knit 2.0. The original project can be viewed [here](https://github.com/carlalennon/portfolio-project-4). I started this current project again in January 2024. 

In my job, I do a lot of overtime. This restart was daunting to me, but by working on the project every day I slowly built up a new project from scratch. 

## UX Design

I wanted a simple home page to let the images speak for themselves. Looking at the images is the most pleasurable part of browsing knitting patterns, it should no be marred by stray information all over the page.

For the feed, I settled with having the absolute bare minimum of information available so the picture stand out on their own. This is in direct opposition to other knitting websites, where the tendency is to have information everywhere cluttering up the page and affecting the enjoyment of the browsing experience. 

I created many wireframes for this project, some just to get the look of the site down, and more practical ones. They are included in the wireframe section below. 

I endevoured to create a site that adhered to UX principles. Information is neatly stored and displayed upon request. The website is laid out in a way that is easy to use. 

I created hand-drawn logo and icons for the nav bar, to create some personality for the site 

## Accessibilty Focus

The largest knitting website on the web often receives criticism for its lack of accessibilty to vision-impaired crafters. This is expecially bad when so many elderly people knit, and can be vision impaired. My site is laid out in a way that colourblind users can still use the site. The icons in the nav bar are designed to be distincy from each other so vision impaired users will not have any problems differentiating them. I have also tried to adhered to accessibility guidelines from W3 Schools to improve the site experience for the visually impaired.


## User Avatar

My site user avatar: 
- Young person looking for a modern knitting site
- Like fibre craft, dislikes cluttered UI of extant sites
- Is challenged in finding and sharing knitting patterns in existing social media platforms
- Wants to upload patterns or share those they've found online


## Site Goals

My site goals are as follows: 

- Provide a modern responsive interface for users
- Provide a place for users to discover new patterns
- Provide a place for users to share new patterns they write 
- Provide a place for user to share patterns they find
- Allow users to search patterns by keyword and category
- Allow users to create and customise a profile to showcase their personality 

## Agile Method

I used the agile method to develop my project. I wrote [user stories](https://github.com/carlalennon/generation-knit-2.0/issues?q=is%3Aopen%20is%3Aissue%20project%3Acarlalennon%2F4) and mapped them to a [kanban board](https://github.com/users/carlalennon/projects/4/views/1). I then broke my user stories into tasks and completed the tasks one by one. I also assigned labels to my issues so I can see what they are better.


### User Stories

For Agile development, user stories are an important part of the process. They allow developers to plan according to the needs of the user. This ensures that important steps for the user's experience aren't overlooked in developement. 

On my kanban board, user stories are marked as Must Have, Could Have, or Beautify. Beautify is for styling that doesn't affect functionality.

My user stories are as follows: 

- Users Story: Registration
- User Story: Homepage/Feed
- User Story: Pattern Detail Page
- User Story: User Profile
- User Story: Search for patterns
- User Story: Navigation Bar
- User Story: Upload a Pattern

This can be viewed in closer detail in the [issues section of this project](https://github.com/carlalennon/generation-knit-2.0/issues).

  <details>
    <summary> User stories on Kanban board</summary>
    <IMG src="templates/assets/images/readme/readme-user-stories.png"  alt="User stories on Kanban board"/>
    </details>


## Wireframes

### Early Wireframes to get the "Vibe"

  <details>
    <summary> Early wireframe for the hamburger menu</summary>
    <IMG src="templates/assets/images/readme/wireframe-hamburger-menu.png"  alt="Early wireframe for the hamburger menu"/>
    </details>
    
  <details>
    <summary>Early wireframe for the home feed</summary>
    <IMG src="templates/assets/images/readme/wireframe-home-feed.png"  alt="Early wireframe for the home feed"/>
    </details>

  <details>
    <summary> Early wireframe for login page</summary>
    <IMG src="templates/assets/images/readme/wireframe-log-in.png"  alt="Early wireframe for login page"/>
    </details>

  <details>
    <summary> Wireframe for a pattern generation tool</summary>
    <IMG src="templates/assets/images/readme/wireframe-pattern-generator.png"  alt="Wireframe for a pattern generation tool"/>
    </details>


### Search Wireframes
  <details>
    <summary> Large Wireframe</summary>
    <IMG src="templates/assets/images/readme/wireframe-search-desktop.png"  alt="large wireframe for search page"/>
    </details>

  <details>
    <summary> Small Wireframe</summary>
    <IMG src="templates/assets/images/readme/wireframe-search-mobile.png"  alt="small wireframe for search page"/>
    </details>

  <details>
    <summary> Search result preview for large screen</summary>
    <IMG src="templates/assets/images/readme/wireframe-search-result.png"  alt="Search result preview for large screen"/>
    </details>

  <details>
    <summary> Search result preview for small screen</summary>
    <IMG src="templates/assets/images/readme/wireframe-search-result-bar.png"  alt="Search result preview for small screen"/>
    </details>
    
  ### Profile Wireframes

  <details>
    <summary> User Profile on large screen</summary>
    <IMG src="templates/assets/images/readme/wireframe-profile-large.png"  alt="User Profile on large screen"/>
    </details>

  <details>
    <summary> User Profile on small screen</summary>
    <IMG src="templates/assets/images/readme/wireframe-profile-small.png"  alt=" User Profile on small screen"/>
    </details>

### Feed Wireframes

  <details>
    <summary> Large Wireframe</summary>
    <IMG src="templates/assets/images/readme/wireframe-feed-large.png"  alt="large wireframe for home page"/>
    </details>

  <details>
  <summary> Small Wireframe</summary>
    <IMG src="templates/assets/images/readme/wireframe-feed-small.png"  alt="large wireframe for home page"/>
    </details>

## Data Modelling Relationships

I mapped out the relationships between my data models and used these to build my models. I have added a diagram below.
 
  <details>
  <summary> ERD diagram</summary>
    <IMG src="templates/assets/images/readme/readme-entity-relationship-database.png"  alt="ERD diagram"/>
    </details>


## Structure

My project is structured with gknit as the main app and feed, pattern, profiles, and search as installed apps. 
### Features
###  Future Features

- Add multiple image uploads to patterns
- Add Cloudinary upload widget to forms for ease of use for user
- Give user the option to change a pdf to an external link or vice versa after pattern is posted
- Allow users to add custom alt text to images they upload
## Design 
### Colours 
Anything over 7 is very accesible 
My accessible colours:

#F9F4BA  18.68:1
#F6EE9A  17.61:1
#f0e332  15.74:1
#d9c626  12.06:1
#c2a91a  8.98:1


### Typography 

## Languages

### Git 

I used git for version control on this project. Version control allows me to track and control changes to the project. It also allows me to restore older versions of the project should something go wrong. 

I tracked my project using git. I wrote a small descriptive note for each commit to github.

### Django 

I used Django to build my project. Django is a Python framework for developing web apps. Django comes with security features built in to keep sensitive data hidden. It is a popular framework and is widely used in professional development settings. 

I especially liked the tag system, as the tags can accept logical arguments. These can be used to determine whether to show certain HTML or iterate over database entries.


### JavaScript

I used Javascript in combination with Bootstrap to make my website neater and more responsive to the user. A javascript feature of note is the hambuger menu in which the navigation tags are hidden. This allows less visual clutter on the page for the user. It is especially effective for mobile users.

Javascript is not installed in this project, rather it is loaded in using a tag in base.html. The tag is based on the bottom of the page to improve loading times.

![My javascript tag](/workspace/generation-knit-2.0/templates/assets/images/readme/readme-javascript.png)

### Bootstrap

I used Bootstrap to design the HTML of my website. 

Bootstrap is a 

### CSS 

I used a small amount of custom CSS to style certain aspects of my project. To serve the CSS, each change to custom.css had to be made in VS Code on my PC, saved, uploaded to Cloudinary and refreshed on prder to show changes.

## Testing and Validation

### Manual Testing 

Manual testing was carried out on User Stories: 

<details>
  <summary> Manual Testing Table </summary>

| User Story                      | Acceptance Criteria                                                                | Action                                                                                                  | Result                                                                                                                                    |      |
|---------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------|
| Upload a Pattern                | Users can upload a pattern when logged in                                          | Upload a pattern to the site when logged in                                                             | I can upload a pattern to Generation Knit                                                                                                 | Pass |
|                                 | The pattern contains at least one image of the garment                             | Look at uploaded pattern and check to see if a garnment picture is uploaded                             | There is a picture attached to the pattern that displays in thumbnails and on the pattern information page                                | Pass |
|                                 | The pattern contains specifications on the pattern eg. yarn weight and needle type | Check "Pattern information" section to check that spec is present                                       | The pattern's spec is present and displays correctly in the table in the "Pattern Information" tab                                        | Pass |
|                                 | The pattern can be found by other users using search                               | Search for this pattern using the search function                                                       | Placing a key word that matches the pattern in the search bar returns a pattern                                                           | Pass |
|                                 | Users can download or travel by hyperlink to the pattern                           | Click on "download PDF" and "Link to pattern" buttons to check they function correctly                  | Both pattern and link buttons lead to their desired pages                                                                                 | Pass |
|                                 | Users can delete a pattern they created                                            | Delete a created pattern and verify it no longer exists                                                 | The pattern is deleted from the database and the user gets a message that says "Your pattern was deleted"                                 | Pass |
| User Story: Search for patterns | Users can access a search bar                                                      | Navigate to the search page using the link in the nav bar                                               | Clicking "Search" in the nav bar loads the search page                                                                                    | Pass |
|                                 | Users can enter a keyword to query                                                 | Enter a keyword into the search bar and press "Go"                                                      | Patterns that match the key word are returned                                                                                             | Pass |
|                                 | A paginated list of results is returned                                            | Enter a query that returns enough results for pagination and check that it's working                    | Fail - there are not enough patterns on Generation Knit at present to test this                                                           | Pass |
|                                 | Results are matched by title or author                                             | Enter an author name and a title name to check for matches                                              | Patterns are returned when a username is typed in and the user has uploaded patterns. Patterns are returned when a title match is entered | Fail |
|                                 | User can filter patterns by criteria                                               | Filter all results by a criteria and press "Go"                                                         | Patterns with a matching criteria to that entered in the dropdowns are returned                                                           | Pass |
| User Story: Pattern Detail Page | Each pattern has it's own pattern page                                             | Click into different patterns and make sure they each have their own page                               | Each pattern has a unique pattern detail page using pattern ID                                                                            | Pass |
|                                 | Pattern page shows image(s) of pattern                                             | Check each pattern has an image                                                                         | Each pattern has it's own unique image                                                                                                    | Pass |
|                                 | Pattern page shows fibre weight and needle size of pattern                         | Check each pattern displays pattern spec                                                                | Each pattern has it's spec displayed in the tab "Pattern Information"                                                                     | Pass |
|                                 | Pattern page provides either a link to pattern or direct PDF download              | Check that buttons are displayed for either a link or PDF for each pattern                              | Each pattern has button(s) available for user to get the pattern                                                                          | Pass |
| User Story: Homepage/Feed       | Feed acts as a home page / index for Gknit                                         | Go to / and make sure the correct HTML is rendered                                                      | / brings the user to the feed page                                                                                                        | Pass |
|                                 | Feed displays patterns uploaded to gknit by users                                  | Check that a list of patterns by gknit users are on home page                                           | The page displays a list of pattern previews by users                                                                                     | Pass |
|                                 | Posts in feed show the project's title, a thumbnail and the pattern author         | Check that each post shows title, pattern thumbnail, and pattern author                                 | Each post displays the title, pattern thumbnail and author, along with user icon                                                          | Pass |
|                                 | Feed updates as new patterns are added                                             | Create a new post and check it's at the top of the feed page                                            | The new post is first in the feed                                                                                                         | Pass |
| User Story: Navigation Bar      | Navigation bar is clearly displayed                                                | Go to all pages on Gknit and ensure navigation bar is displayed                                         | The nav bar is displayed on all pages on gknit                                                                                            | Pass |
|                                 | The links in the bar describe the page they take the user to                       | Click on all navbar links and make sure they go to the correct page                                     | All nav bar links bring the user to the correct page                                                                                      | Pass |
|                                 | The user can access the navigation bar at all times                                | Make sure hamburger menu works on all pages                                                             | The hamburger menu is working on all pages                                                                                                | Pass |
|                                 | The site logo brings the user to home page                                         | Click the logo on small and large screens                                                               | The logo brings the user to the home feed on small and large screens                                                                      | Pass |
|                                 | The navbar displays the login state of the user                                    | Log out and in and check the top right of the nav bar                                                   | The navbar displays the username and icon when logged in and a "Login" button when logged out                                             | Pass |
|                                 | The user icon in the top right brings the user to their profile                    | Click the user icon                                                                                     | The username and icon bring the user to their profile page when logged in                                                                 | Pass |
| User Story: User Profile        | Profile has a profile picture                                                      | Open the user profile and check for a picture                                                           | The profile displays a large version of the user icon                                                                                     | Pass |
|                                 | User can optionally add a short biography                                          | Create an account with no biography, and then add one in                                                | Users are permitted to not have a biography, and can edit the biography after                                                             | Pass |
|                                 | Profile shows the patterns uploaded by the user                                    | Go to a user profile who has patterns, and check they appear                                            | User patterns appear on page                                                                                                              | Pass |
|                                 | Profile shows the amount of patterns uploaded by the user                          | Go to a user profile and check the amount of patterns they have. Users with no patterns should have a 0 | The amount of user patterns is displayed underneath the bio                                                                               | Pass |
|                                 | Users can edit their profile                                                       | Go to a profile while logged in and edit user bio and profile picture                                   | Users can edit their bio and profile picture                                                                                              | Pass |
|                                 | Users can delete their profile                                                     | Go to a profile when logged in and delete the profile                                                   | User profile was deleted                                                                                                                  | Pass |
| User Story: Registration        | Potential users can access a registration form                                     | Go to sign up page                                                                                      | Can access the signup page via login page                                                                                                 | Pass |
|                                 | Users create account with username, email and password                             | Sign up for an account with Gknit                                                                       | Can sign up for an account using username, email and password                                                                             | Pass |
|                                 | Users receive a welcome message upon registration                                  | Check for message upon login                                                                            | User is displayed a "Successful sign in" and "confirmation email" message                                                                 | Pass |
|                                 | Username and email must be unique to the site                                      | Try to sign up with a duplicate email and username                                                      | Cannot sign up with a duplicate username or email                                                                                         | Pass |
|                                 | Passwords are scrambled when stored                                                | Check admin panel to see if passwords are accessible                                                    | Passwords are scrambled in admin panel, they are inaccessbile                                                                             | Pass |
|                                 | User is assigned a temporary user icon on registration                             | Check that new profile has temp icon assigned                                                           | New user has temp icon assigned                                                                                                           | Pass |
|                                 | User is assigned a Profile object on registration                                  | Go to profile page on creation of new user                                                              | There is a new profile page for my new user                                                                                               | Pass |
|                                 | Profile edit and delete buttons only appear on a user's own page                   | Log out and check user profile page                                                                     | Buttons only appear on profile page when user is logged in and it's their own profile                                                     | Pass |
| User Story: Deploy to Heroku    | Configure variables in Heroku to the necessary values for my project               | Add in the appropriate variable in Heroku                                                               | Added in necessary variables                                                                                                              | Pass |
|                                 | Create Procfile and configure settings.py to work with Heroku                      | Create the procfile in the project                                                                      | Created the procfile and configured for launch                                                                                            | Pass |
|                                 | Successfully deploy to Heroku                                                      | Deploy the project to Heroku from branch                                                                | Deployed the project from branch main                                                                                                     | Pass |
|                                 | Test final build before submission                                                 | Check all pages on Heroku build before submission                                                       | Checked all pages on Heroku branch                                                                                                        | Pass |
</details>

### Performance Testing

Network testing was done using Chrome devtools. My image loading is very slow, in the future I will look into why this is and how to correct it. 

![Waterfall showing slow image loading](templates/assets/images/readme/readme-network-testing.png)

I also did some troubleshooting on slow database queries. While not always slow, they sometimes are causing delays in the site. I had to choose an American server to get an up-to-date verison of PostgreSQL, which may also be contributing to load times. In my research, most sources said that this would likely be solved by upgrading to a paid plan with ElephantSQL. 

![Showing slow queries and recommended time of 1ms or less](templates/assets/images/readme/readme-network-postgres.png)

I also tried to use Lighthouse to test what exactly was the issue on the page, but it wouldn't test and only returned this error. 

![Lighthouse error](templates/assets/images/readme/readme-network-lighthouse.png)

Along with a similar error from PageSpeed Insights. 

![PageSpeed Insights error](templates/assets/images/readme/readme-network-pagespeedinsights.png)

I am using sorl thumbnail for image resizing, but results are still slow. Here's an example of a typical server response:

![Server response of 10 seconds](templates/assets/images/readme/readme-network-server-timing.png)

In the future, I would run more tests to see why my site is so slow. 

  <summary> Lighthouse test for search page </summary>
    <IMG src="templates/assets/images/readme/readme-lighthouse-search.png"  alt="Lighthouse test for search page"/>
    </details>


  <summary> Lighthouse test for pattern page </summary>
    <IMG src="templates/assets/images/readme/readme-lighthouse-pattern-page.png"  alt="Lighthouse test for pattern page"/>
    </details>


### Linting 

#### HTML

I used the W3C schools linter to check my html. It does not like Django tags, so my goal was to solve every error it gave apart from the Django related errors. 

The HTML linter really didn't like Django, and showed a lot of errors in all HTML with Django tags 
![Django errors in W3 HTML checker ](templates/assets/images/readme/readme-lint-django.png)

I used "Validate by Direct Input"

I worked through errors in my code until only the Django related errors were left. 

Some common errors:


  <summary> Button cannot be a child of an "a" tag</summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-01.png"  alt="Button cannot be a child of an a tag error "/>
    </details>

  <summary> Image tags require an alt attribute (I had been using "name" as an alt )</summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-02.png"  alt="Image tags require an alt attribute error"/>
    </details>

  <summary> Stray tags </summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-03.png"  alt="Stray tag error"/>
    </details>


#### Python

I used an ![online Python formatter](https://www.tutorialspoint.com/online_python_formatter.htm) to paste each python file into to observe the differences. I then manually made changes to each file. I did not want to use an automatica linter to avoid breaking any of my Django

#### CSS

I used ![a CSS linter](csslint.net) to check my CSS file. It gave me 6 warnings for the !important tag in my CSS. However, I decided to keep these in because the custom CSS would not appear without them. I believe this is because my Bootstrap is served from a CDN. Installing Bootstrap to the static folder in Cloudinary appendsa random string to each file. Even when this is removed, the Bootstrap files are still broken. This prevented me from using SASS customisation.

  <summary> CSS Lint warnings and no issues</summary>
    <IMG src="templates/assets/images/readme/readme-lint-css.png"  alt="CSS Lint warnings and no issues"/>
    </details>


### Responsive Design 

Responsiveness testing was carried out using Chrome Devtools. Special care was given to the pages that undergo large layout changes between large and small screens. These are 

- Search Page 
- Profile page

In the future I would like to add further layout changes to 

- Add pattern form
- Edit pattern form
- Edit profile form
- Login/Sign Up page
- Pattern detail page

This is discussed more in the known issues section





## Deployment


## Error Hall of Fame

  <summary> This duplicate id error appeared on pages when there were 2 different HTML sections for small and large screen. I've decided to ignore them as due to the way they styling is done, only one element appears on the screen at a time</summary>
    <IMG src="templates/assets/images/readme/readme-error-01.png"  alt="duplicate id error"/>
    </details>



### HTML

I used the W3C schools linter to check my html. It does not like Django tags, so my goal was to solve every error it gave apart from the Django related errors. 

The HTML linter really didn't like Django, and showed a lot of errors in all HTML with Django tags 

![Django errors in W3 HTML checker ](templates/assets/images/readme/readme-lint-django.png)

I used "Validate by Direct Input"

I worked through errors in my code until only the Django related errors were left. 

Some common errors:


  <summary> Button cannot be a child of an "a" tag</summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-01.png"  alt="Button cannot be a child of an a tag error "/>
    </details>

  <summary> Image tags require an alt attribute (I had been using "name" as an alt )</summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-02.png"  alt="Image tags require an alt attribute error"/>
    </details>

  <summary> Stray tags </summary>
    <IMG src="templates/assets/images/readme/readme-lint-common-03.png"  alt="Stray tag error"/>
    </details>


### Python

I used an [online Python formatter](https://www.tutorialspoint.com/online_python_formatter.htm) to paste each python file into to observe the differences. I then manually made changes to each file. I did not want to use an automatica linter to avoid breaking any of my Django

### CSS

I used [a CSS linter](csslint.net) to check my CSS file. It gave me 6 warnings for the !important tag in my CSS. However, I decided to keep these in because the custom CSS would not appear without them. I believe this is because my Bootstrap is served from a CDN. Installing Bootstrap to the static folder in Cloudinary appendsa random string to each file. Even when this is removed, the Bootstrap files are still broken. This prevented me from using SASS customisation.

  <summary> CSS Lint warnings and no issues</summary>
    <IMG src="templates/assets/images/readme/readme-lint-css.png"  alt="CSS Lint warnings and no issues"/>
    </details>

## Known Errors 

- The summernote widget does not respond to screen size in the edit pattern and profile pages
- User cannot upload more than one image for a pattern 
- The sign up page is not styled nicely 


## Citations 

I used a variety of resources to help me understand the new elements that PP4 offers. Of note was the skillshare course by Kalob Taulien. After finishing the LMS, it was extremely beneficial to watch someone put an app together in Django. He explains very clearly what was happening on screen and why. I also spent a lot of time in the boostrap and django docs.


- [Skillshare course](https://skl.sh/3OMfffl)
- [Cloudinary Django resources](https://cloudinary.com/blog/managing-media-files-in-django)
- [Allauth docs](https://docs.allauth.org/en/latest/)
- [Using re_path since URLS is deprecated](https://docs.djangoproject.com/en/4.0/ref/urls/)
- [Adding summernote to forms](https://ctrlzblog.com/how-to-add-a-text-editor-to-a-django-blog-with-summernote/)
- [Bootstrapping a django form](https://ngangasn.com/how-to-use-bootstrap-5-with-django-the-right-way/)
- [Creating the models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
- [Multiple file handling for pattern uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
- [More multiple file handling](https://qasimalbaqali.medium.com/upload-multiple-images-to-a-post-in-django-ff10f66e8f7as)
- [Cloudinary upload widget](https://cloudinary.com/documentation/upload_widget)
- [Classy class based views resource ](https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/FormView/)
- [Sorl thumbnail docs ](https://sorl-thumbnail.readthedocs.io/en/latest/)
- [Deleting a post](https://tutorial-extensions.djangogirls.org/en/homework/)
- [Adding messages to edit/delete post ](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
- [Create search function](https://learndjango.com/tutorials/django-search-tutorial)
- [Classy Class Based Views](https://ccbv.co.uk/)
- [Getting posts by user](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
- [Filtering a user's posts for their profile](https://medium.com/@abdelrahman.hassan.hamdy/leveraging-custom-filters-in-django-for-effective-data-rendering-b3efdb04ae64)
- [Pagination help ](https://docs.djangoproject.com/en/5.0/topics/pagination/)
- [File validation for pattern PDFs ](https://pypi.org/project/django-upload-validator/#:~:text=Django%20Upload%20Validator%20is%20a,extensions%20using%20python%2Dmagic%20library.)
- [Cloudinary delivery PDF fail ](https://support.cloudinary.com/hc/en-us/articles/360016480179-PDF-or-ZIP-files-appearing-in-Media-Library-but-download-URLs-return-an-error)
- [Making a field optional in the upload form](https://subscription.packtpub.com/book/web-development/9781787281141/5/ch05lvl1sec34/making-fields-optional)
- [MIME types for documents](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
- [Accessbile colour schemes](https://venngage.com/blog/accessible-colors/)
- [Accessible colour palette generator ](https://venngage.com/tools/accessible-color-palette-generator)
- [Bootstrap Overrides](https://blog.hubspot.com/website/how-to-override-bootstrap-css)
- [Django widget tweaks ](https://github.com/jazzband/django-widget-tweaks)
- [Fix search filtering when category etc. is null](https://www.w3schools.com/python/ref_string_isdigit.asp)
- [Python Linter](https://www.tutorialspoint.com/online_python_formatter.htm)
 



