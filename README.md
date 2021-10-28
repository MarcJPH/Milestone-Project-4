# Casa Fitness Website

#### A link to the site can be found [here]()

#### Full Stack Development - Code Institute

## Table of Contents
1. [Introduction](#introduction)
2. [User Experience](#user-experience)
3. [Wireframes](#wireframes)
4. [Database Design](#design)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


### Introduction
#### The Casa Fitness website and community is a place for anyone at any level who wants to get involved in fitness and nutrition for a healthier lifestyle. It provides workout plans that all can be done from home while meal plans are available also, all for a modest montly subscription.

![Site Mock Up](wireframes/.png)

### User Experience

The website will have some workout and meal plans for non subscribers however users who have subscribed will have the full access to all the workouts and nutritional information. The site will have menu's for users to access workouts, meals, a store for Casa Fitness workout gear and the community to allow users to connect and support each other.

User Stories to help achieve this user experience:

### Wireframes

 - [Index Page](wireframes/index_page.png)
 - [ Page](wireframes/activity_page.png)
 - [ Page](wireframes/add_activity_page.png)
 - [ Page](wireframes/edit_activity_page.png)

 


### Database Design

#### ?? was used as the non-relational database for this project. 3 collections were added to contain the data required:
 - age_ranges. This contained the number of different age ranges that could be in included in each activity and used when users were selecting the age range when adding their own activity.


 Collections and fields documented [here.](wireframes/database_design.png)


### Features

Existing features:

 - The site opens up on the index page which contains a **carousel of 3 images** showing 3 of the activities or places listed on the website.
 


Features left to implement:





#### Technologies Used

* HTML5
* CSS
* Javascript
* Python
* Flask
* Flask-PyMongo
* PyMongo
* [Fontawesome](https://fontawesome.com/)
    * Fontawesome is used to provide the icons that are displayed throughout.
* [Jquery](https://jquery.com/)
    * Jquery is used for the Javascript elements used within the project.



### Testing

The following testing was performed to test functionality, browser compatibility, responsiveness and that the user stories documented above are fulfilled by the completed site.

#### Functionality

Test | Action | Expected Outcome | Test Outcome |
---- | ------ | ---------------- | ------------ |
 Indicators on the index.html page. | Clicking on each carousal indicator changed the image. | The image was changed to the next image in the list. | PASS
 


#### Browser Capability

The website and functionality has been tested on the following devices:
 - Iphone 6s
 - Ipad 5th Generation
 - Iphone 12
 - Samsung Galaxy A20

The website and functionality has been tested on the following browsers:
 - Chrome (version 88.0.4324.190)
 - Edge (version 88.0.705.81)
 - Safari (version 14.4.1)


#### Performance

Performance of the website was tested using the Lighthouse function as part of Google developer tools. It was tested for desktop and mobile performance. Test output below.

 - [Lighthouse Test Desktop](testing/.png)
 - [Lighthouse Test Mobile](testing/.png)

The results for the desktop were 

#### Code Validation

The HTML, CSS and Javascript were validated by using the different tools below.

[HTML Validator](https://validator.w3.org/) - The results [before](testing/html_validator_results_before.png) and [after](testing/html_validator_results_after.png) were reviewed and response below:

Before:
1. As designed, no header required.


After:
1. As designed, no header required.



[CSS Validator](https://jigsaw.w3.org/css-validator/) - The [results](testing/css_validator_results.png) were reviewed and response below:

One amendment was required to change font-weight to bold rather than a number which was being used incorrectly.

The Javascript code was checked and no issues found.

The Python code was checked to ensure it was PEP8 compliant by using the [Python Validator.](http://pep8online.com/) The [before](testing/pep8_validator_before.png) results showed 9 errors which were:
 - 3 related to comments not including a space after the #.
 - 4 were the line was too long. This was corrected by moving to two lines.
 - 2 were the Flash message was too long. The message was amended to ensure it was within the line limit.

 After the above changes, no errors were found. Results [here.](testing/pep8_validator_after.png)


#### Responsiveness

The website and the user experiance is functioning well across the different screen sizes for the different devices. As well as using the options within Google Lighthouse, [Responsinator](http://www.responsinator.com/) was also used to test how the site would look and feel on the different sceen sizes. The title text on the cards would not always all be visible on mobile devices when used as landscape. All other visuals and usability are working well.

 - [Responsinator Android Device](testing/responsinator_android.png)
 - [Responsinator Ipad Device](testing/responsinator_ios.png)


#### User Stories Test

To ensure the website met the expectations set by the users and stakeholders listed previously, testing was performed against their criteria.

##### User



##### Admin Owner



#### Defects Found during testing:

1. 





### Deployment

This project is stored [GitPod]() and is hosted using [Heroku](https://kids-activities-project.herokuapp.com/).

#### Running the Project Locally

To run the project locally you will have to clone it first. Follow the below steps to perform the clone:

1. Within **GitHub**, locate and select the repository named **MarcJPH/Milestone-Project-3**.
2. When within the main page of the repository, select the **Code** button which can be found above the list of files section.
3. Select the option of **"Clone with HTTPS"** and then select the copy button which is the clipboard icon.
4. Go to **Workspaces** within GitPod and select the location where you want to place the cloned directory.
5. In the terminal window, type **"git clone"** and then paste the url that was copied from the directory within GitHub. Then press **enter**.
6. Upon pressing enter, the local clone of the directory will be made.


#### Deploying to Heroku using Gitpod

To deploy to Heroku using Gitpod, follow the below steps:

1. On the Heroku dashboard, create a new application.
2. Still within Heroku, got to the Settings tab and click on the Reveal Config Vars button. Click on the Add button and add in settings for IP (0.0.0.0), PORT (5000), MONGODB_NAME, MONGO_URI.
3. To install Heroku via the Terminal, type 'npm install -g heroku'.
4. Log in to Heroku with the command heroku login-i' and type in your username and password.
5. Create a requirements.txt file that contains the list of dependencies the project requires. Type 'pip3 freeze --local > requirements.txt' in the terminal.
6. Create a Proc file by typing echo web: python run.py > Procfile in the terminal.
7. Type 'git remote rm heroku' in the terminal so that only Github is connected to the project.


### Credits

#### Media

The static images of the activity places were sourced from their own websites.

 - [Active Kids](https://activekidsadventurepark.co.uk/)



#### Code







 ##### Disclaimer
The content of this Website is for educational purposes only.