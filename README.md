- [User Experience (UX)](UX_URL)
   - [Project goals](Project_goals_URL)
   - [User Stories](User_Stories_URL)
   - [Agile Methodology](Agile_Methodology_URL)
   - [Design](Design_URL)
        - [Wireframes](Wireframes_URL)
        - [Database Schema](Database_Schema_URL)


[Features](https://www.productplan.com/glossary/product-features/)



 - [Future Features](https://www.example.com/future-features)

+ [Responsive Design](https://www.smashingmagazine.com/2011/01/guidelines-for-responsive-web-design/)

[Technologies](https://en.wikipedia.org/wiki/List_of_programming_languages)

  + [Languages](https://en.wikipedia.org/wiki/List_of_programming_languages)
 
  + [Frameworks and Libraries](https://en.wikipedia.org/wiki/List_of_JavaScript_libraries)

  + [Tools](https://www.codecademy.com/resources/blog/the-best-ide-for-web-development-in-2021/)

[Testing](https://www.guru99.com/software-testing.html)

[Deployment](https://www.heroku.com/)

[Credits](https://github.com/SuzanDewitz)

  + [Code](https://github.com/SuzanDewitz/TableFinder)

  + [Content](https://www.productplan.com/glossary/product-content/)

  + [Media](https://www.canva.com/)

  + [Inspiration](https://dribbble.com/)

  + [Acknowledgments](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)


  <br>
  <br>


  # Portfolio Project 4 - TableFinder restaurant booking system
 <br>
  <br>

  # User Experience (UX)
   ## Project goals


The overall goal of the website is to create a restaurant webpage that is enticing for the visitors that generates an interest and curiosity to visit the restaurant. Visitors should be able to find general information about the restaurant as well as finding the menu offerings. In addition, visitors should be able to make a reservation for a table directly on the webpage. It will also provide a booking management admin panel for the staff members.

+ User stories
   + First Time Visitor Goals
     + As a first time visitor I can read and learn about the location and history and get a feel for the restaurant.
     + As a first time visitor I can find out what kind of food they serve from their menu.
     + As a first time visitor I can find information about how to make a reservation at the restaurant.
   + Returning Visitor Goals
     + As a returning visitor I can create an account so I can make a reservation online.
     + As a returning visitor I can view the menu to see if has changed.
   + Frequent User Goals
     + As a frequent visitor I can login and find my current bookings.
     + As a frequent visitor I can change or cancel my booking in the login page.
   + Agile methodology
     + The principles of agile methodology were utilized during the project. By assigning user stories to issues and taking advantage of the GitHub Kanban board functionality, the necessary goals and priorities throughout the project could be well defined. In addition, labels were used to further define the priority of eacn user story in the Kanban board.
   + Design
     + The theme for the project were chosen in accordance with the intended target market in mind for the restaurant. With its fancy looks and feel, dark colors and luxurious details and effects, the theme fits perfect for the goal of giving the visitor the impression that this is a very high quality restaurant.

     + Colors

       + The main colors are overall black to provide an elegant look and feel. Furthermore, elements such as buttons, icons, symbols, links and headings are made in gold color that follows the pattern of elegance and adds to the premier look and feel of the webpage.
    + Font

       + The fonts in the theme are clear and modern and contribute perfectly to the overall elegant setting.
   + Images

       + The images in the theme provide great content and presentation of the restaurant and serves as an enticement for the visitors.
   + Wireframes


   <br>
  <br>

Make sure to add corresponding section headers in your README file using Markdown syntax, like this:

User Stories
...

Design and Site Structure
...

And so on for each section.

By doing this, when the user clicks on any of the items, they will be directed to the corresponding section in the README file.





This is a Django project settings file. It includes various configurations that affect the behavior of the Django web framework when running the project.

Some notable settings include:

SECRET_KEY: A secret string used for cryptographic signing. It is used for things like generating CSRF tokens and signing session cookies. It is important to keep this value secret.
DEBUG: A boolean that determines whether or not debug mode is enabled. When debug mode is enabled, Django will display detailed error messages and debugging information in case of an error. This should be turned off in production.
ALLOWED_HOSTS: A list of strings representing the host/domain names that this Django site can serve.
INSTALLED_APPS: A list of strings representing the installed apps in this Django project. An app is a component of a Django project that provides a specific functionality, such as authentication or database management.
TEMPLATES: A list of template engines to use and their configurations. Templates are used for rendering HTML pages.
DATABASES: A dictionary containing the configuration settings for the project's database.
STATIC_URL: The base URL to use for serving static files (CSS, JavaScript, Images). This setting is used in combination with the STATICFILES_DIRS and STATIC_ROOT settings.
DEFAULT_AUTO_FIELD: The type of primary key to use for newly created database tables. This setting is introduced in Django 3.2 and helps to reduce migration issues that arise from changes to the primary key field type.



































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Suzan Dewitz,

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
