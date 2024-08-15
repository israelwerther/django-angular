### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV`  

```bash
$ pip install virtualenv
$ python -m venv venv
$ .\venv\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />


## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Resources

- Demo: <https://www.creative-tim.com/live/black-dashboard-django>
- Download Page: <https://www.creative-tim.com/product/black-dashboard-django>
- Documentation: <https://demos.creative-tim.com/black-dashboard-django/docs/1.0/getting-started/getting-started-django.html>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/black-dashboard-django/issues)

<br />

## Reporting Issues

We use GitHub Issues as the official bug tracker for the **Black Dashboard Django**. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the **Black Dashboard Django**. Check the CHANGELOG from your dashboard on our [website](https://www.creative-tim.com/).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser-specific, so specifying in what browser you encountered the issue might help.

<br />

## Technical Support or Questions

If you have questions or need help integrating the product please [contact us](https://www.creative-tim.com/contact-us) instead of opening an issue.

<br />

## Licensing

- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

<br />

## Useful Links

- [More products](https://www.creative-tim.com/bootstrap-themes) from Creative Tim
- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Freebies](https://www.creative-tim.com/bootstrap-themes/free) from Creative Tim
- [Affiliate Program](https://www.creative-tim.com/affiliates/new) (earn money)

<br />

## Social Media

- Twitter: <https://twitter.com/CreativeTim>
- Facebook: <https://www.facebook.com/CreativeTim>
- Dribbble: <https://dribbble.com/creativetim>
- Instagram: <https://www.instagram.com/CreativeTimOfficial>

<br />

## [PRO Version](https://www.creative-tim.com/product/black-dashboard-pro-django)

> For more components, pages and priority on support, feel free to take a look at this amazing starter:

Black Dashboard is a premium [Bootstrap](https://www.admin-dashboards.com/bootstrap-5-templates/) Design now available for download in Django. Made of hundred of elements, designed blocks, and fully coded pages, Black Dashboard PRO is ready to help you create stunning websites and web apps.

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Black](https://github.com/app-generator/django-admin-black-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Django Black Dashboard PRO - Premium Starter crafted by AppSeed and Creative-Tim.](https://user-images.githubusercontent.com/51070104/214872728-230a9955-d391-4900-b352-d68960dbd2c4.png)

<br />

---
[Black Dashboard Django](https://www.creative-tim.com/product/black-dashboard-django) - Provided by [Creative Tim](https://www.creative-tim.com/) and [AppSeed](https://appseed.us).

# Commit Types
Here are the different types of commits that can be used to maintain a clear and organized history in your project:

##

### `feat`
### `fix`
### `docs`
### `test`
### `build`
### `perf`
### `style`
### `refactor`
### `chore`
### `ci`
### `raw`
### `cleanup`
### `remove`

##

### `feat`
Commits of type `feat` indicate that your code is adding a new feature (related to MINOR in semantic versioning).

### `fix`
Commits of type `fix` indicate that your code is solving a problem (bug fix), (related to PATCH in semantic versioning).

### `docs`
Commits of type `docs` indicate changes in the documentation, such as in the README of your repository. (Does not include code changes).

### `test`
Commits of type `test` are used when changes are made to tests, whether creating, modifying, or deleting unit tests. (Does not include code changes).

### `build`
Commits of type `build` are used when modifications are made to build files and dependencies.

### `perf`
Commits of type `perf` are used to identify any code changes related to performance.

### `style`
Commits of type `style` indicate changes related to code formatting, semicolons, trailing spaces, lint... (Does not include code changes).

### `refactor`
Commits of type `refactor` refer to changes due to refactoring that do not alter its functionality, such as changing how a part of the screen is processed while maintaining the same functionality, or performance improvements due to a code review.

### `chore`
Commits of type `chore` indicate updates to build tasks, administrative configurations, packages... such as adding a package to gitignore. (Does not include code changes).

### `ci`
Commits of type `ci` indicate changes related to continuous integration.

### `raw`
Commits of type `raw` indicate changes related to configuration files, data, features, parameters.

### `cleanup`
Commits of type `cleanup` are used to remove commented-out code, unnecessary parts, or any other form of code cleanup to improve readability and maintainability.

### `remove`
Commits of type `remove` indicate the deletion of files, directories, or obsolete or unused features, reducing the project's size and complexity and keeping it more organized.

