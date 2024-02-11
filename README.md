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
- Error Hall of Fame
- Citations 


## What happened to Generation Knit 1.0? 
## UX Design
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
## Data Modelling Relationships
## Structure
### Features
###  Future Features
## Design 
### Colours 
### Typography 
## Languages 
### Django 
### JavaScript
### Bootstrap
## Deployment
## Error Hall of Fame
## Citations 

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

Skillshare course
https://cloudinary.com/blog/managing-media-files-in-django

Allauth docs
https://docs.allauth.org/en/latest/

Using re_path since URLS is deprecated
https://docs.djangoproject.com/en/4.0/ref/urls/

Adding summernote to forms
https://ctrlzblog.com/how-to-add-a-text-editor-to-a-django-blog-with-summernote/

Bootstrapping a django form
https://ngangasn.com/how-to-use-bootstrap-5-with-django-the-right-way/

Creating the models
https://docs.djangoproject.com/en/5.0/topics/db/models/

Multiple file handling for pattern uploads
https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/

More multiple file handling
https://qasimalbaqali.medium.com/upload-multiple-images-to-a-post-in-django-ff10f66e8f7as

Cloudinary upload widget
https://cloudinary.com/documentation/upload_widget

Classy class based views resource 
https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/FormView/

Sorl thumbnail docs 
https://sorl-thumbnail.readthedocs.io/en/latest/

Deleting a post
https://tutorial-extensions.djangogirls.org/en/homework/

Adding messages to edit/delete post 
https://docs.djangoproject.com/en/5.0/ref/contrib/messages/

Create search function
https://learndjango.com/tutorials/django-search-tutorial

Classy Class Based Views
https://ccbv.co.uk/

Getting posts by user
https://docs.djangoproject.com/en/5.0/topics/db/queries/

Filtering a user's posts for their profile
https://medium.com/@abdelrahman.hassan.hamdy/leveraging-custom-filters-in-django-for-effective-data-rendering-b3efdb04ae64

Pagination help 
https://docs.djangoproject.com/en/5.0/topics/pagination/

File validation for pattern PDFs 
https://pypi.org/project/django-upload-validator/#:~:text=Django%20Upload%20Validator%20is%20a,extensions%20using%20python%2Dmagic%20library.

Cloudinary delivery PDF fail 
https://support.cloudinary.com/hc/en-us/articles/360016480179-PDF-or-ZIP-files-appearing-in-Media-Library-but-download-URLs-return-an-error

Making a field optional in the upload form
https://subscription.packtpub.com/book/web-development/9781787281141/5/ch05lvl1sec34/making-fields-optional

MIME types for documents
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome carlalennon lennon,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
