# Flow Yoga - M4
- The website is live and can be accessed in the following url: https://yoga-app-django-m4.herokuapp.com/

<img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/001_home.JPG" style="width:600px;"/>


## Project Goals:
- This is an app where users can buy and access the content for different yoga courses.

## Dev and Business Goals:
- Flow Yoga App has the intention of selling yoga courses to users.
- Users should be able to complete a checkout, buy a course and access its content from their dashboard page.
- Users should be able to contact a teacher or admin via form
- Admins sould be able to see user inquiries.
- Admins should be able to create, update & delete courses.
- Admins should be able to create, update & delete teachers from the admin area.


## User Experience - UX
---

### User Stories
- As a user I want to:
    - be able to register
    - be able to login
    - be able to see a dashboard with my courses inquiries
    - be able to see a dashboard with my purchased courses
    - be able to logout
    - be able to contact the teacher or admins via form
    - be able to complete a checkout
    - be able to see the content for the courses that I've bought

- As an admin I want to:
    - be able to create, update & delete a course
    - be able to create, update & delete teachers
    - be able to create, update & delete contacts

### Design and Architecture
#### **General design idea**
- Minimal and clean look 
- Use Flow Yoga logo for both, frontend and admin pages
- Mobile friendly
- Simple, straight forward checkout
- Easy navigation

#### **DB Schemas**
[Relational DB Schemas](SchemasReadme.md)

#### **Main project directory:**
- **yoga_app**
    - This contains all core project files and static folders.

#### **Apps:**
- **Accounts:**
        - This deals with registration, login, logout and user dashboard functionality

- **Contacts:**
        - This deals with user contact information and emails functionality

- **Courses:**
        - This deals with general courses and individual courses functionality

- **Pages:**
        - This deals with home and about pages functionality

- **Teachers:**
        - This deals with teachers information functionality

#### **Templates:**
- This directory contains all templates organized in separate directories
- Most page templates extend from base.html

#### **Models**
- Accounts Model:
    - user
    - course
    - txn_id
    - currency
    - amount
    - stripe_customer
    - is_paid
    - created_at
    - updated_at


- Course Model:
    - teacher
    - title
    - lessons
    - description
    - price
    - start_date
    - main_pic
    - pic_1
    - pic_2
    - pic_3
    - is_published
    - students


- Contact Model:
    - course
    - course_id
    - name
    - email
    - phone
    - message
    - contact_date
    - user_id


- Teachers Model:
    - name
    - teacher_pic
    - description
    - email
    - phone

### Wireframes
- HOME
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/home_mobile.JPG" style="width:800px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/home_ipad.JPG" style="width:800px;"/>

    - desktop

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/home_desktop.JPG" style="width:800px;"/>

- ABOUT
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/about_phone.JPG" style="width:300px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/about_ipad.JPG" style="width:600px;"/>

    - desktop

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/about_desktop.JPG" style="width:800px;"/>

- REGISTER
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/register_phone.JPG" style="width:300px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/register_ipad.JPG" style="width:800px;"/>
    - desktop

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/register_desktop.JPG" style="width:800px;"/>

- LOGIN
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/login_mobile.JPG" style="width:300px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/login_ipad.JPG" style="width:600px;"/>

    - desktop
    
    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/login_desktop.JPG" style="width:800px;"/>

- INDIVIDUAL COURSE
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/course_phone.JPG" style="width:300px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/course_ipad.JPG" style="width:600px;"/>

    - desktop

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/course_desktop.JPG" style="width:800px;"/>

- COURSE - CONTACT US MODAL
    - mobile

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/contact_us_modal_mobile.JPG" style="width:300px;"/>

    - tablet

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/contact_us_modal_ipad.JPG" style="width:600px;"/>

    - desktop

    <img src="https://yoga-app-ae-ci-m4.s3.eu-west-1.amazonaws.com/wireframes/contact_us_modal_desktop.JPG" style="width:800px;"/>


## FEATURES
---

## TECHNOLOGIES USED
---
### Languages used:
- HTML5
- CSS3
- Javascript
- Python
- Django
- Bootstrap

### Frameworks, Libraries & Programs Used
- Bootstrap
    - Bootstrap was used to assist with the responsiveness and styling of the website.
- Google Fonts
    - Google fonts were used on all pages throughout the project.
- Font Awesome
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
- JQuery
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
- Git
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- Github
    - GitHub is used to store the projects code after being pushed from Git.
- Balsamiq
    - Balsamiq was used to create the wireframes during the design process.
-  Canva
    - https://canva.com was used to create the logo
- AWS S3
    - AWS S3 was used to store static files for the heroku deployment.
- Lightbox
    - Lightbox is used in the individual course pages for the thumbnail images.
    
## TESTING
---
- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- The PEP8 validator was used to validate every page of the project to ensure the all python files are pep8 compliant

### Testing User Stories from User Experience (UX) Section

| Scenario      | Expectation | Results    |
| :---        |    :----   |          ---: |
| Home page links verification | Verify that for new users home page will display the following links: HOME, ALL COURSES, ABOUT, REGISTER AND LOGIN. | Passed  |
| Logo verification| The logo is displayed in all pages and screen sizes.| Passed|
| Services banner verification| Verify that a services banner is displayed above the footer.| Passed|
| Footer verification   | Verify that the footer is displayed in all pages.| Passed|
| Courses displayed in Home Page| Home page will displayed a max of 3 courses ordered by starting date.| Passed|
| Courses enroll now button in home page  | Verify that clicking Enroll now for a given course brings the user to that course's page.| Passed|
| Price and number of lessons - Home and Course pages   | In the course details page verify that the price and number of lessons are being displayed.| Passed|
| Teacher details are displayed in course details  | In the course details page verify that the teacher name and contact option are being displayed.| Passed|
| Modal contact us form is displayed  | Verify that clicking the contact us button will open a modal window where the user can complete and submit a form.| Passed|
| Contact us form behaviour for unregistered users  | For unregistered users verify that the modal window will auto populate the course name.| Passed|
| Contact us form behaviour for registered users  | For registered users verify that the modal window will auto populate the course name, username and user email.| Passed|
| Submit the same Contact us form twice for a given course as a registered user   | Verify that a registered user can only submit 1 inquiry per course, else a validation will be displayed.| Passed|
| Stripe checkout for a course | When clicking enroll now in the course details page the user will be redirected to stripe to complete the checkout.| Passed|
| Stripe checkout - Course details    | Verify that the title, description and price is displayed correctly for each checkout.| Passed|
| Verify Successful checkout  |  Card 4242 4242 4242 4242. 11/23. 100. Any name. Any post code. Verify that the user is redirected to the dashboard and the new course is displayed under "your courses".| Passed|
| Successful checkout with 3d secure 2 authentication  |  Card 4000 0000 0000 3220 >> 3D Secure 2 authentication must be completed for a successful payment. Verify that the user is redirected to the dashboard and the new course is displayed under "your courses".| Passed|
| Declined checkout  | Card 4000 0000 0000 9995 >> Always fails with a decline code of insufficient_funds.| Passed|
| Click back during checkout  | Verify that the user is redirected to the cancel checkout page| Passed|
| Complete a checkout successfully | Verify that the user is redirected to the success checkout page| Passed|
| New user registration and redirect  |Register a new user and verify that the they are redirected to the home page.| Passed|
| Registration validations   | Verify that validations are displayed during registration for all fields.| Passed|
| Login validations   | Verify that that validations are displayed during login for invalid credentials.| Passed|
| Home page links verification for logged user  |Verify that the home page for a logged user will display their Dashboard page and logout links.| Passed|
| Dashboard page verification   | Verify that the dashboard page will display all inquiries and bought courses for that user.| Passed|
| Dashboard page - Your courses   | Verify that the user can access all bought courses and their content via the dashboard page| Passed|
| Dashboard page verification no inquiries or bought courses   | Verify that the dashboard page will display the correct messages when the user does not have any inquiries or bought courses| Passed|
| About page verification   | The about page will display 3 brief sections: About, our story and teachers. Verify that all teachers are displayed here dynamically.| Passed|
| All Courses page verification   | Verify that the All courses page will display cards with all available courses.| Passed|
| All Courses page verification - Pagination max 6 | Verify that the All courses page will display pagination if there are more than 6 courses listed| Passed|
| Only registered, logged in users can complete a checkout   | Verify that users that are not logged in cannot proceed to a checkout| Passed|
| Logout verification   | Verify that a logged in user can logout| Passed

### Further Testing
- Further unit tests need to be created.


## Future features to implement
- Success and Cancel checkout pages could use a bit more work as they are a fairly simple redirect from stripe at the moment.
- Courses content should be individualized for each course, we currently have the course content (lessons and videos) hardcoded.
- Validations during registration could use a bit more customization.

## DEPLOYMENT
---
### Making a clone for local development
- Steps on Github:
    - Go to https://github.com/zippote/yoga-app 
    - Click Code
    - Select HTTPS and copy the following url https://github.com/zippote/yoga-app.git

- Steps on your local:
    - Create a destination folder in your local >> ie: myFolderExample in the C drive
    - Open the cmd and move to that folder >> cd C:\myFolderExample
    - Type the following command: git clone https://github.com/zippote/yoga-app.git
    - Hit enter and wait until the process is completed
    - Open the project using your favourite IDE
    - Fields that will need editing after local deployment:
        - email inbox in settings
        ```python
        # lines 161 to 166 for email configuration
        EMAIL_HOST_USER = "test@mail.com"
        EMAIL_HOST_PASSWORD = "fakepass1"
        ```
        - postgres database settings in settings.py. Alternatively, the default django sqlite can be used.
        ```python
        # lines 98 to 104 for postgres db configuration
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "<your_app_name>",
            "USER": "postgres",
            "PASSWORD": "<your_password>",
            "HOST": "localhost",
            "PORT": "<your_port>",
        ```
        - contacts view.py line 38 for primary and secondary emails
        ```python
        # send email
        send_mail('Yoga Course Inquiry',
                  'There has been an inquiry for ' + course +
                  '. Sign into the admin panel for more info.',
                  'primaryemail@test.com',
                  [teacher_email, 'secondaryemail@test.com'],
                  fail_silently=False)
        ```


### Deploying the app to Heroku
- Step 1: Clone and run the flow yoga app Locally by following the steps above.
- Step 2: Create or link your remote and local GitHub repositories.

- Step 3: In your app create a ```requirements.txt``` file using the terminal command:
```
pip freeze > requirements.txt
```

- Create a ```Procfile``` with the terminal command :
```
echo web: python app.py > Procfile
```
- The ```Procfile``` should contain:
```
web: gunicorn your_app_name.wsgi:application
```

- Do a ```git add``` and ```git commit``` for the new ```requirements``` and ```Procfile``` and then git push the project to Github.

- Step 4: Connecting to Heroku
- Create a new app on the Heroku website by clicking the "New" button in the dashboard. Give it a name and set the region.

- From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select Github.

- Confirm the linking of the Heroku app to the correct Github repository.

- In the Heroku dashboard for the application, click on "Resources" search and select "Heroku Postgres"

- In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

- Set the following config vars and save all changes:

```Config Vars```
| KEY      | VALUE |
| :---        |  ---: |
| AWS_ACCESS_KEY_ID | <YOUR_AWS_KEY_ID>|
| AWS_S3_REGION_NAME | <YOUR_AWS_REGION>|
| AWS_SECRET_ACCESS_KEY | <YOUR_AWS_SECRET_KEY>|
| AWS_STORAGE_BUCKET_NAME | <YOUR_AWS_BUCKET_NAME>|
| DATABASE_URL | <YOUR_POSTGRES_DB>|
| EMAIL_DEV | True|
| NO_TEST | True|
| USE_AWS | True|
| EMAIL_USER1 | <your_admin@email.com>|
| EMAIL_PASS1 | <YOUR_ADMINEMAIL_PASSWORD>|
| SECRET_KEY | <YOUR_SECRET_KEY>|
| STRIPE_PUBLISHABLE_KEY | <YOUR_STRIPE_PUBLISHABLE_KEY>|
| STRIPE_SECRET_KEY | <YOUR_STRIPE_SECRET_KEY>|
| STRIPE_WEBHOOK_SECRET | <YOUR_STRIPE_WEBHOOK_SECRET>|

- In setting.py search for ALLOWED_HOST for heroku, line 22. This will need to be updated:
    ```python
        ALLOWED_HOSTS = ["your_app_name.herokuapp.com"] 
    ```
- In setting.py search for Heroku DB details in lines 87 to 94. This will need to be updated:
    ```python
        DATABASES = {
        # HEROKU DATABASE_URL
        "default": dj_database_url.parse(
            "your_heroku_postgress_key_here"
        )}
    ```
- Do a ```git add``` and ```git commit``` again

- In the Heroku dashboard for the application, click on "Deploy" >> "Manual Deploy" >> Select the branch you want to deploy and click Deploy Branch.

## CREDITS
---
### Code:
- Bootstrap template: https://github.com/twbs/bootstrap/blob/master/

### Media:
- All images are royalty free and were taken from https://unsplash.com
- Logo, success and cancel checkout images were created using https://canva.com
- There are 2 youtube videos with yoga exercises which were picked at random:
    - https://www.youtube.com/watch?v=7OJY0iQwzoo
    - https://www.youtube.com/watch?v=yetbSrCW1TQ
- Text content was taken from several yoga websites such as: www.gaia.com, yoga.ie and others.
- All teachers and yoga courses are fake.

### Resources:
- udemy.com:
    - Jose Portilla (```Python and Django full stack```)
    - Rathan Kumar (```Django Ecommerce```)
    - Max Schwarzmuller (```Python Django - Practical Guide```)

- youtube.com channels:
    - Pyplane
    - JustDjango
    - Dennis Ivy
    - Code Keen
    - Pretty Printed

- stackoverflow.com for general troubleshooting