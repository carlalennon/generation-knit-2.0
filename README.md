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
## UX Design

I wanted a simple home page to let the images speak for themselves. Looking at the images is the most pleasurable part of browsing knitting patterns, it should no be marred by stray information all over the page.
## Accessibilty Focus
## User Avatar
## Site Goals
## Agile Method

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

![USer stories on Kanban board](templates/assets/images/readme/readme-user-stories.png)

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
## Structure
### Features
###  Future Features

- Add multiple image uploads to patterns
- Add Cloudinary upload widget to forms for ease of use for user
- Give user the option to change a pdf to an external link or vice versa after pattern is posted
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

Manual testing was carried out on User Stories: 

| User Story       | Task #                                                                             | Acceptance Criteria | Action | Result |   |
|------------------|------------------------------------------------------------------------------------|---------------------|--------|--------|---|
| Upload a Pattern | Users can upload a pattern when logged in                                          |                     |        |        |   |
|                  | The pattern contains at least one image of the garment                             |                     |        |        |   |
|                  | The pattern contains specifications on the pattern eg. yarn weight and needle type |                     |        |        |   |
## Deployment


## Error Hall of Fame

  <summary> This duplicate id error appeared on pages when there were 2 different HTML sections for small and large screen. I've decided to ignore them as due to the way they styling is done, only one element appears on the screen at a time</summary>
    <IMG src="templates/assets/images/readme/readme-error-01.png"  alt="duplicate id error"/>
    </details>


## Linting 

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

I used an ![online Python formatter](https://www.tutorialspoint.com/online_python_formatter.htm) to paste each python file into to observe the differences. I then manually made changes to each file. I did not want to use an automatica linter to avoid breaking any of my Django

### CSS

I used ![a CSS linter](csslint.net) to check my CSS file. It gave me 6 warnings for the !important tag in my CSS. However, I decided to keep these in because the custom CSS would not appear without them. I believe this is because my Bootstrap is served from a CDN. Installing Bootstrap to the static folder in Cloudinary appendsa random string to each file. Even when this is removed, the Bootstrap files are still broken. This prevented me from using SASS customisation.

  <summary> CSS Lint warnings and no issues</summary>
    <IMG src="templates/assets/images/readme/readme-lint-css.png"  alt="CSS Lint warnings and no issues"/>
    </details>

## Known Errors 

- The summernote widget does not respond to screen size in the edit pattern and profile pages
- User cannot upload more than one image for a pattern 
- Users cannot add a link from the pattern edit screen if they chose a PDF on creation of the pattern entry, and vice versa

## Citations 

I used a variety of resources to help me understand the new elements that PP4 offers. Of note was the skillshare course by Kalob Taulien. After finishing the LMS, it was extremely beneficial to watch someone put an app together in Django. He explains very clearly what was happening on screen and why. I also spent a lot of time in the boostrap and django docs.

![]()
- ![Skillshare course](https://skl.sh/3OMfffl)
- ![Cloudinary Django resources](https://cloudinary.com/blog/managing-media-files-in-django)
- ![Allauth docs](https://docs.allauth.org/en/latest/)
- ![Using re_path since URLS is deprecated](https://docs.djangoproject.com/en/4.0/ref/urls/)
- ![Adding summernote to forms](https://ctrlzblog.com/how-to-add-a-text-editor-to-a-django-blog-with-summernote/)
- ![Bootstrapping a django form](https://ngangasn.com/how-to-use-bootstrap-5-with-django-the-right-way/)
- ![Creating the models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
- ![Multiple file handling for pattern uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
- ![More multiple file handling](https://qasimalbaqali.medium.com/upload-multiple-images-to-a-post-in-django-ff10f66e8f7as)
- ![Cloudinary upload widget](https://cloudinary.com/documentation/upload_widget)
- ![Classy class based views resource ](https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/FormView/)
- ![Sorl thumbnail docs ](https://sorl-thumbnail.readthedocs.io/en/latest/)
- ![Deleting a post](https://tutorial-extensions.djangogirls.org/en/homework/)
- ![Adding messages to edit/delete post ](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
- ![Create search function](https://learndjango.com/tutorials/django-search-tutorial)
- ![Classy Class Based Views](https://ccbv.co.uk/)
- ![Getting posts by user](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
- ![Filtering a user's posts for their profile](https://medium.com/@abdelrahman.hassan.hamdy/leveraging-custom-filters-in-django-for-effective-data-rendering-b3efdb04ae64)
- ![Pagination help ](https://docs.djangoproject.com/en/5.0/topics/pagination/)
- ![File validation for pattern PDFs ](https://pypi.org/project/django-upload-validator/#:~:text=Django%20Upload%20Validator%20is%20a,extensions%20using%20python%2Dmagic%20library.)
- ![Cloudinary delivery PDF fail ](https://support.cloudinary.com/hc/en-us/articles/360016480179-PDF-or-ZIP-files-appearing-in-Media-Library-but-download-URLs-return-an-error)
- ![Making a field optional in the upload form](https://subscription.packtpub.com/book/web-development/9781787281141/5/ch05lvl1sec34/making-fields-optional)
- ![MIME types for documents](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
- ![Accessbile colour schemes](https://venngage.com/blog/accessible-colors/)
- ![Accessible colour palette generator ](https://venngage.com/tools/accessible-color-palette-generator)
- ![Bootstrap Overrides](https://blog.hubspot.com/website/how-to-override-bootstrap-css)
- ![Django widget tweaks ](https://github.com/jazzband/django-widget-tweaks)
- ![Fix search filtering when category etc. is null](https://www.w3schools.com/python/ref_string_isdigit.asp)
- ![Python Linter](https://www.tutorialspoint.com/online_python_formatter.htm)
 



### Porting User Stories over from old project 


Rewriting user stories over from old project

As a <role>
I can <capability>
So that <received benefit>

In order to <receive benefit>
as a <role>
I can <goal/desire>

Example:
"As a warehouse employee
I can choose the size of paper to print on 
To make a label that matches the size of a parcel"

"In order to check out multiple items
As a user
I can add multiple items to cart"

Each user story needs a card, conversation and a confirmation.

Card : The user story that fits on a post-it note, as the example above
Conversation : The discussion around the needs of the user story. In the above example, "What paper sizes should be included? What information should be included in the print-out?"
Confirmation : Confirm the understanding and acceptance criteria


Sources: 



