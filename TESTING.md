# Table of Contents

* [Code Validation](#code-validation)
* [Lighthouse](#lighthouse-testing)
* [Responsiveness](#responsiveness-testing)
* [Browser Compatibility](#browser-compatibilty-testing)
* [User Stories](#user-story-testing)
* [Features](#features-testing)

_____

## Code Validation

### HTML

HTML code was tested using the [W3C Validator](https://validator.w3.org/) via text input.  The HTML code was copied and pasted in from each page of the website's source code.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

**HOME**

![No Errors or Warnings to show](documentation/html-val-home.png)

**ABOUT**

![No Errors or Warnings to show](documentation/html-val-about.png)

**SERVICES**

![No Errors or Warnings to show](documentation/html-val-services.png)

**SIGNUP/REGISTER**

![No Errors or Warnings to show](documentation/html-val-signup.png)

**LOGIN**

![No Errors or Warnings to show](documentation/html-val-login.png)

**PROFILE**

![No Errors or Warnings to show](documentation/html-val-profile.png)

**LOGOUT**

![No Errors or Warnings to show](documentation/html-val-logout.png)

**APPOINTMENTS**

![No Errors or Warnings to show](documentation/html-val-appts.png)

**CREATE APPOINTMENT**

![No Errors or Warnings to show](documentation/html-val-createappt.png)

**VIEW APPOINTMENT**

![No Errors or Warnings to show](documentation/html-val-viewappt.png)

**UPDATE APPOINTMENT**

![No Errors or Warnings to show](documentation/html-val-updateappt.png)

**DELETE APPOINTMENT**

![No Errors or Warnings to show](documentation/html-val-deleteappt.png)

**403**

![No Errors or Warnings to show](documentation/html-val-403.png)

**404**

![No Errors or Warnings to show](documentation/html-val-404.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

### CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via text input. 

<details>

<summary>Screenshot with results for the styles.css file</summary>

**styles.css**

![No Error Found](documentation/css-val.png)

![15 Warnings](documentation/css-val-warnings.png)

* 12 warnings due to vendor extension prefixes.  The CSS file was run through [Autoprefixer CSS Online](https://autoprefixer.github.io/) for browser support.
* 3 warnings due to having the same `background-color` and `border-color` on the same element.  This is essential since I am overriding Bootstrap's button classes.  A solution to this would be to use different class names for my custom buttons but because of time constraints this was not implemented at this time. 

</details>

<br>

[Back To Top](#table-of-contents)

_____

### Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

<details>

<summary>Screenshots and results for all python files</summary>

Long lines in `settings.py` and `env.py` were cleared using `# noqa`. These were values by the Django generated AUTH_PASSWORD_VALIDATORS, the values for STATICFILES_STORAGE and DEFAULT_FILE_STORAGE and the values for DATABASE_URL and CLOUDINARY_URL in the `env.py` file which were giving errors when separated into two lines.

**tailors_thimble**

* settings.py

![All clear, no errors found](documentation/python-val-settings.py.png)

* urls.py

![All clear, no errors found](documentation/python-val-urls.py.png)

**users**

* admin.py

![All clear, no errors found](documentation/python-val-users_admin.py.png)

* apps.py

![All clear, no errors found](documentation/python-val-users_apps.py.png)

* forms.py

![All clear, no errors found](documentation/python-val-users_forms.py.png)

* models.py

![All clear, no errors found](documentation/python-val-users_models.py.png)

* signals.py

![All clear, no errors found](documentation/python-val-users_signals.py.png)

* views.py

![All clear, no errors found](documentation/python-val-users_views.py.png)

**tailoring**

* admin.py

![All clear, no errors found](documentation/python-val-tailoring_admin.py.png)

* constants.py

![All clear, no errors found](documentation/python-val-tailoring_constants.py.png)

* forms.py

![All clear, no errors found](documentation/python-val-tailoring_forms.py.png)

* models.py

![All clear, no errors found](documentation/python-val-tailoring_models.py.png)

* urls.py

![All clear, no errors found](documentation/python-val-tailoring_urls.py.png)

* views.py

![All clear, no errors found](documentation/python-val-tailoring_views.py.png)

**root**

* env.py

![All clear, no errors found](documentation/python-val-env.py.png)

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Lighthouse Testing

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO.  This was run in Chrome DevTools in incognito mode. 

<details>
<summary>Screenshots and results for all pages</summary>

**HOME**

* Mobile

![Passed](documentation/mobile-home.png)

*Note*: After changing the service-img to scale up evenly for screens > 1200px, the test was run again and the performance dropped a little for mobile. Because of time constraints, it wasn't possible to investigate further at this time. 

![Retest Lower Performance](documentation/mobile-home-retest.png)

* Desktop

![Passed](documentation/desktop-home.png)

**ABOUT**

* Mobile

![Passed](documentation/mobile-about.png)

* Desktop

![Passed](documentation/desktop-about.png)

**SERVICES**

* Mobile

![Passed](documentation/mobile-services.png)

* Desktop

![Passed](documentation/desktop-services.png)

**SIGNIN/REGISTER**

* Mobile

![Passed](documentation/mobile-signup.png)

* Desktop

![Passed](documentation/desktop-signup.png)

**LOGIN**

* Mobile

![Passed](documentation/mobile-login.png)

* Desktop

![Passed](documentation/desktop-login.png)

**PROFILE**

* Mobile

![Passed](documentation/mobile-profile.png)

* Desktop

![Passed](documentation/desktop-profile.png)

**LOGOUT**

* Mobile

![Passed](documentation/mobile-logout.png)

* Desktop

![Passed](documentation/desktop-logout.png)


The following are the results for the Appointment pages

| Page | Device | Performance | Accessibility | Best Practice | SEO |
| ---- | ------ | ----------- | ------------- | ------------- | --- |
| Appointments w/o appointments | mobile  |  96 | 100 | 100 |  97 |
|                               | desktop | 100 | 100 | 100 | 100 |
| Appointments w/o profile | mobile  |  94 | 100 | 100 |  96 |
|                          | desktop | 100 | 100 | 100 | 100 |
| Appointments             | mobile  |  95 | 100 | 100 |  97 |
|                          | desktop | 100 | 100 | 100 | 100 |
| Create Appointment       | mobile  |  94 | 100 |  92 |  98 |
|                          | desktop | 100 | 100 |  92 | 100 |
| View Appointment         | mobile  |  98 | 100 | 100 |  97 |
|                          | desktop |  99 | 100 | 100 | 100 |
| Update Appointment       | mobile  |  98 | 100 | 100 |  98 |
|                          | desktop | 100 | 100 | 100 | 100 |
| Delete Appointment       | mobile  |  98 | 100 | 100 |  97 |
|                          | desktop |  99 | 100 | 100 | 100 |

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Responsiveness Testing

The website is responsive for screens with a mininum width of 320px and a maximum width of 2560px. Friends and family tested the website on their devices and all reported no issues with responsiveness.  Further manual tests were done using Chrome's DevTools.

<details>

<summary>Screenshots of website at different screen sizes.</summary>

**NAVBAR & HOME HERO**

        Mobile - iPhone 320px
![Navbar & Home Hero on mobile](documentation/nav%2Bhero-iphone5_320.jpg)

        Tablet - iPad Mini 768px
![Navbar & Home Hero on tablet](documentation/nav%2Bhero-ipadmini_768.jpg)

        Desktop - Nest Hub - 1024px
![Navbar & Home Hero on desktop](documentation/nav%2Bhero-nesthub_1024.png)

**FOOTER**

        Mobile - Galaxy S9+ - 320px
![Footer on mobile](documentation/footer-galaxys9_320.png)

        Tablet - Surface Pro 7 - 912px
![Footer on tablet](documentation/footer-surfacepro7_912.png)

**HOME**

        Mobile - Galaxy S9 - 320px
![Home on mobile](documentation/home-galaxys9_320.png)

        Tablet - iPad - 768px
![Home on tablet](documentation/home-ipad_768.png)
 
        Desktop - Nest Hub Max - 1280px
![Home on desktop](documentation/home-nesthubmax_1280.png)

**ABOUT**

        Mobile - iPhone 12 Pro -390px
![About on mobile](documentation/about-iphone12pro_390.png)

        Mobile - Samsung Galaxy S20 Ultra - 412px
![About Process on mobile](documentation/about-samsunggals20_412.png)

        Tablet - iPad Air - 820px
![About Process on tablet](documentation/about-ipadair_820.png)

        Desktop - Nest Hub Pro - 1200px
![About Process on desktop](documentation/about-nesthubpro_1200.png)

**SERVICES**

        Mobile - iPhone XR - 414px
![Services on mobile](documentation/services-iphoneXR_414.png)

        Tablet - Surface Pro 7 - 912px
![Services on tablet](documentation/services-surfacepro7_912.png)

        Desktop - Desktop - 1440px
![Services on desktop](documentation/services-desktop_1440.png)

**PROFILE**

        Mobile - iPhone 12 Pro - 800px
![Profile on mobile](documentation/profile-iphone12pro_380.png)

        Tablet - iPad Pro - 1200px
![Profile on tablet](documentation/profile-ipadpro_1024.png)

**APPOINTMENTS**

        Mobile - iPhone 6/7/8 - 375px
![Appointments List on mobile](documentation/appts-iphone678_375.png)

        Tablet - Surface Pro 7 - 912px
![Appointments List on tablet](documentation/appts-surfacepro_812.png)

        Desktop - Nest Hub Max - 1200px
![Appointments List on desktop](documentation/appts-nesthubmax_1200.png)

**ALL OTHER PAGES**

All other pages have been tested with DevTools and results have been recorded in the table below which checks if the cards are clear and visible on mobile and if they are horizontally aligned on Tablet and Desktop.

| Page                  | Mobile | Tablet | Desktop |
| --------------------- | ------ | ------ | ------- |
| Register              | Yes    | Yes    | Yes     |
| Login                 | Yes    | Yes    | Yes     |
| Logout                | Yes    | Yes    | Yes     | 
| View Appointment      | Yes    | Yes    | Yes     |
| Create Appointment    | Yes    | Yes    | Yes     |
| Update Appointment    | Yes    | Yes    | Yes     |
| Delete Appointment    | Yes    | Yes    | Yes     |

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Browser Compatibilty Testing

Website was tested on current Chrome, Firefox, Edge, Brave for compatibility.  It was also tested on Safari on an iPad running on iOS 12.5.7 and an iPhone on the latest iOS.  

<details>

<summary>Table of the results.</summary>

| Intended      | Chrome | Firefox | Edge | Brave | Safari iOS 12 | Safari iOS 15 |
| ------------- | ------ | ------- | ---- | ----- | ------------- | ------------- |
| Appearance    | Good   | Good    | Good | Good  | Poor          | Good          |
| Responsiveness| Good   | Good    | Good | Good  | Fair          | Good          |

The issue with using Safari on iOS 12 is that it doesn't support webp images, therefore all webP images were not visible.

</details>

<br>

[Back To Top](#table-of-contents)

_____

## User Story Testing

As mentioned in the Agile Methodology Section in the [README](/README.md), User Stories were created in [GitHub Issues](https://github.com/MoniPar/tailors_thimble/issues) which guide the process for this project all the way from Setup to Testing.  Epics 1, 2 and 9 are not included in this section as they define Setup, Installation and Testing. Each User Story has been manually tested and the results have been collected in the tables below.

<details>

<summary>Epic 3 - Home Page</summary>

* User Story [#6](https://github.com/MoniPar/tailors_thimble/issues/6)

As a business owner, I would like users visiting our site to land on the homepage so that they can learn about us and the services we provide.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Website URL directs users to the homepage | Achieved | |
| Homepage has some basic information about the business | Achieved | |

* User Story [#7](https://github.com/MoniPar/tailors_thimble/issues/7)

As a User, I can see the website's logo and links at the top of the page so that I can easily navigate to other parts of the website.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Header with Tailor's Thimble logo is displayed | Achieved | |
| Links to Home, About, Services, Register and Login pages are displayed | Achieved | |
| Hamburger button for mobile toggles navbar links. | Achieved | |

* User Story [#8](https://github.com/MoniPar/tailors_thimble/issues/8)

As a User, I can see contact details, shop address and social links at the bottom of the website so that I can follow/contact the business owner and the website creator.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A footer is displayed at the bottom of the page | Achieved | |
| Contact details, social links and shop address are clearly displayed | Achieved | |
| Copyright date and link to the website creator's Linkedin page | Achieved | |
| All footer links open in a new tab | Achieved | | 

* User Story [#9](https://github.com/MoniPar/tailors_thimble/issues/9)

As a Business Owner, I would like the homepage to have a Call to Action so that users are encouraged to schedule an appointment early on.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A hero image that draws the eye to the Schedule an Appointment button | Achieved | |
| Some text about the Bespoke Tailoring Experience | Achieved | |
| A visible Schedule an Appointment button which will eventually link to the Booking form | Achieved | Schedule Appointments button links to the Appointments Page which has a button to create appointments |

* User Story [#10](https://github.com/MoniPar/tailors_thimble/issues/10) 

As a User, I can read about the people behind the business so that I can make up my mind if I feel comfortable using their service.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A short section about the tailor | Achieved | |
| An image of the tailor | Achieved | Image is visible on screens > 768px |
| A read more button that links to the About page when clicked | Achieved |

* User Story [#11](https://github.com/MoniPar/tailors_thimble/issues/11)

As a Business Owner, I can display some of the services we provide on the Homepage so that it gives the user an idea of the type of services we offer.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A services section which displays 2 or 3 different types of services | Achieved | |
| Icons or images to give a bit of visual feedback | Achieved | |
| A read more link that links to the Services page | Achieved | |

</details>

<br>

<details>

<summary>Epic 4 - Other Frontend</summary>

* User Story [#12](https://github.com/MoniPar/tailors_thimble/issues/12)

As a Developer, I can have a favicon added to the tab and website's title so that it gives users more visual feedback when looking at their tabs on their browser.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A representative image from the Tailor's Thimble logo is visible on the title tab | Achieved | |

* User Story [#13](https://github.com/MoniPar/tailors_thimble/issues/13)

As a User, I can easily navigate to the About page so that I can find more information about the people behind the business and how they operate.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| More information about the Master Tailor and his experience in the craft | Achieved | | 
| A section about the process of Bespoke Tailoring with images | Achieved | |
| Another Call to Action with link to the Appointment form | Achieved | Link directs logged in users to the Appointments Page which has a button to the Appointment Form |  

* User Story [#14](https://github.com/MoniPar/tailors_thimble/issues/14)

As a User, I can easily navigate to the Services page so that I can find more information about the kind of work the business caters for. 

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| More services and images | Achieved | |
| A short note about the duration of the process uring clients to book their appointments early | Achieved | | 
| A call to action with link to Appointment form | Achieved | Link directs logged in users to the Appointments Page which has a button to the Appointment Form |

</details>

<br>

<details>

<summary>Epic 5 - Admin Panel</summary>

* User Story [#15](https://github.com/MoniPar/tailors_thimble/issues/15)

As a Business Owner, I have access to the database so that I can manage customer details and appointments.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Admin has the functionality to login to the Admin Panel | Achieved | Business owner can access the Admin panel via url |
| Admin can view, update and delete customers' details and appointments | Achieved | | 
| Admin can approve or dismiss appointments set by the customer | Achieved | Admin can approve appointments. If customer has set the wrong appointment they are contacted by email or phone |  

</details>

<br>

<details>

<summary>Epic 6 - User Registration & Authentication</summary>

* User Story [#16](https://github.com/MoniPar/tailors_thimble/issues/16)

As a User, I can register an account so that I can make an appointment with the Master Tailor.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A new user is directed to the Registration form when they click the Schedule Appointment button | Changed | Directed to Login page with a link to Registration |
| The form has fields for username, email, password and a submit button | Updated | First and last name fields were also added to Registration form|
| Upon clicking the submit button, the user is redirected to the Homepage | Changed | Upon clicking the submit button, the user is directed to the Profile page | 

* User Story [#17](https://github.com/MoniPar/tailors_thimble/issues/17)

As a Returning User, I can use my username and password so that I can login to my user account.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Users are directed to the Login form when they click on the Login link in the navbar | Achieved | |
| Users can also login through the link in the registration form upon clicking the Schedule Appointment button | Updated | Upon clicking the Schedule Appointment button, users are directed to the Login form | 
| Users are asked for their Username and Password | Achieved | | 
| After login, users are directed back to the Home page | Updated | Users logging in through Schedule Appointment button are directed to their Appointments Page. Users logging in through the navbar login link are directed to their Profile Page which has a button to their Appointments Page |

* User Story [#18](https://github.com/MoniPar/tailors_thimble/issues/18)

As a User, I can log out of my account so that I can keep my details secure.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| When user is logged in, the logout link appears in the navbar | Achieved | |
| When logout link is clicked, user is directed to the logout page | Achieved | |
| The logout confirms with the user that they are signing out | Changed | The logout confirms with the user that they are logging out |
| When the user confirms by clicking the Sign Out button, they are redirected to the Home Page | Changed | When the user confirms by clicking the Log Out button, they are redirected to the Home Page |

* User Story [#19](https://github.com/MoniPar/tailors_thimble/issues/19)

As a developer, I can display success and error messages upon form submission so that the user has a better experience with the site.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Success or error alerts are displayed at the top of the page whenever user submits a form | Achieved | |
| These alerts are colour coded and clear | Achieved | | 

</details>

<br>

<details>

<summary>Epic 7 - User Profile</summary> 

* User Story [#20](https://github.com/MoniPar/tailors_thimble/issues/20)

As a Returning User, I can login to my profile so that I can access my information and view my details.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| When returning user logs into their account, a profile link appears in the navbar | Achieved | | 
| When the profile link is clicked, the user will be directed to the Profile page | Achieved | | 
| Only the logged in user is able to view his/her Profile page | Achieved |

* User Story [#21](https://github.com/MoniPar/tailors_thimble/issues/21)

As a Developer, I can automate user profile creation upon registration so that the admin doesn't have to do it manually every time a new user is registered.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The Profile page is populated with more fields consisting of information the business owner needs | Achieved | |
| This includes a phone number, event date, event and outfit type | Achieved | |
| A newly registered user is directed to their profile page where they can view their information after registration | Achieved | |

* User Story [#23](https://github.com/MoniPar/tailors_thimble/issues/23)

As a User, I can update my profile information so that I can change my details when necessary.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The Profile page is an editable form populated with the user's information | Achieved | |
| It can only be accessed by the logged in user | Achieved | |
| The user is able to update their information and submit the form via the Update button | Achieved | |
| Form is validated before saved and the user is aleerted to required fields/invalid input | Achieved | | 
| User is directed back to the Profile page after successful update, showing the updated information | Changed | After successful update, the user is redirected to the Home page were the Schedul Appointment button is clearly visible |

* User Story [#24](https://github.com/MoniPar/tailors_thimble/issues/24)

As a Developer, I can have placeholder text in the profile form so that users have a better experience filling in their forms.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Empty fields have helpful hints to guide users | Updated | Tooltips were also added to give a little more guidance |

* User Story [#37](https://github.com/MoniPar/tailors_thimble/issues/37)

As a Developer, I can direct the user to enter a country code so that they can be reached even if they live abroad.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Phone field has a hint to let user know they need to enter the country code and phone number | Achieved | |
| Phone field accepts a '+' sign and digits | Achieved | |
| Form does not submit with an entry less then 10 and more than 17 characters, alpha characters and symbols other than a '+' at the start | Achieved | |

</details>

<br>

<details>

<summary>Epic 8 - Appointments</summary>

* User Story [#25](https://github.com/MoniPar/tailors_thimble/issues/25)

As a Business Owner, I can login and view appointments scheduled by my customers so that I can contact them back for approval/dismissal.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Admin has the facility to view the Appointments table in the Admin page | Achieved | Admin/the business owner can access the admin page through the url and login using their superuser credentials |
| Appointment table displays the appointment type, date and time, the date submitted, the state of approval and any comments left by the customer | Achieved | The appointment table also displays the customer's username | 
| Admin can approve or dismiss appointments set by the customer | Achieved | Admin/Business owner can approve appointments or leave them unchecked |

* User Story [#26](https://github.com/MoniPar/tailors_thimble/issues/26)

As a Returning User, I can login and view my appointments so that I can check if my appointments have been approved.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User can see their past and future appointments listed | Achieved | A user who has already created appointments can see them listed on the Appointments page |
| User can check if their future appointments have been approved | Achieved | |

* User Story [#27](https://github.com/MoniPar/tailors_thimble/issues/27)

As a Returning User, I can schedule an appointment with the Master Tailor so that I can avail of their services.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| Logged in user can click on the Add Appointment button to book a new appointment | Achieved | |
| Appointment form has the necessary fields to complete appointment schedule | Achieved | Appointment form has fields for Type, Date, Time, and optional Comments |
| Form has information to guide the user on how to schedule an appointment | Achieved | Form has also link that opens in another tab on the Process guidelines | 
| Submit button directs users to the Appointments page which shows all scheduled appointments | Achieved | | 

* User Story [#28](https://github.com/MoniPar/tailors_thimble/issues/28)

As a Returning User, I can update my appointment so that I can make sure of my availability.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User is directed to the Update form when they click on the Edit appointment button | Updated | In Appointment detail view, user is directed to the Update form when they click on the Update button |
| Appointment Update form has fields for date/time and comments | Updated | Appointment Update form has fields for Type, Date, Time and optional comments |
| User is directed back the their Appointment page after clicking the Submit button | Achieved | |

* User Story [#29](https://github.com/MoniPar/tailors_thimble/issues/29)

As a Returning User, I can delete my upcoming appointment so that I can reschedule at a later date.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User can delete an appointment from the Appointment Detail page | Achieved | |
| When user clicks on delete button, they are directed to a confirmation page with Delete and Cancel buttons | Achieved | Delete Confirmation page asks user if they are sure they want to delete this appointment |
| If user clicks Cancel, they are brought back to the Appointment Detail page of the current appointment | Achieved | |
| If user clicks Delete, the appointment is deleted and user is directed back to the Appointments page | Achieved | |

* User Story [#30](https://github.com/MoniPar/tailors_thimble/issues/30)

As a developer, I can restrict access on users' appointments so that only the logged in user and admin are able to access, update and delete said user's appointments.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| A 403 Forbidden is thrown when users try to access, other users appointments through the URL address bar | Achieved | |
| The 403 page is customised so that navigation and footer are included in order for the user to be able to easily navigate to other parts of the website | Achieved | | 

* User Story [#31](https://github.com/MoniPar/tailors_thimble/issues/31)

As a Developer, I can add an empty default choice in the Create Appointment form so that the user is alerted when trying to submit an appointment without selecting the type and time.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The Appointment form displays '------' as default on the Choices fields | Achieved | |
| When user tries to submit the form without selecting an appropriate choice, they are alerted to fill in the required fields | Achieved | | 
| The form submits successfully when all required fields are filled in | Achieved | | 

* User Story [#32](https://github.com/MoniPar/tailors_thimble/issues/32)

As a Developer, I can add alert messages so that user is notified if their form has been submitted or an error has occurred.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| When a user creates an appointment and submits an alert shows up on the top of the page saying "Your appointment has been created successfully!" | Achieved | |
| When a user updates an appointment and submits an alert shows up on the top of the page saying "Your appointment has been updated successfully!" | Achieved | |
| When a user deletes an appointment and confirms, an alert shows up on the top of the page saying "Your appointment has been deleted!" | Achieved | |
| When an error occurs and form is not submitted, user is notified with an alert message at the top | Partially Achieved | Alert is not displayed when user fails to select a value for Type or Time |

* User Story [#34](https://github.com/MoniPar/tailors_thimble/issues/34)

As a Developer, I can add a modal with the Process information so that user doesn't have to navigate back from the Services page to fill in their appointment form.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| The Process link in the Appointment create form opens up a modal with the information regarding the Bespoke Process | Changed | The Process link in the Appointment Create form opens up in a new tab with the information regarding the Bespoke Process |
| The User reads this process and closes the modal to continue filling their form | Changed | The User reads this process and clicks on Appointment Create tab to continue filling their form |

* User Story [#35](https://github.com/MoniPar/tailors_thimble/issues/35)

As a Developer,  I can place validations on the datefield so that users are not allowed to pick dates in the past and dates /times that have already been booked.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User is not allowed to schedule an appointment for date in the past | Achieved | |
| User is not allowed to schedule an appointment for Sundays or Mondays | Achieved | | 
| User is not allowed to schedule an appointment for a date and time that has already been booked | Achieved | |

* User Story [#36](https://github.com/MoniPar/tailors_thimble/issues/36)

As a Developer, I can restrict users from adding an appointment before they add their profile information so that the business owner is able access the profile information before confirming their appointment.

| Acceptance Criteria  | Test     | Comments |
|:--------------------:|:--------:| -------- |
| User is not able to add an appointment unless the fields in the Profile table are filled in | Achieved | |
| If user tries to add an appointment, they get a message saying to finish updating their profile first | Achieved | | 
| The message has a link to their profile page | Achieved | |

</details>

<br>

[Back To Top](#table-of-contents)

_____

## Features Testing

Each feature listed in the [README.md](README.md) has been manually tested on the browsers listed in [Browser Compatibility Testing](#browser-compatibilty-testing) and the results are listed in the tables below.

<details>

<summary>Header & Navigation</summary>

* Unregistered / Not logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Logo                          | hover over    | address shows as home |
|                               | click / tap   | directs to Home page  |
| Hamburger button on mobile    | hover over    | gets border           |
|                               | click / tap   | toggles menu          |
| Home, About & Services links  | hover over    | change colour & address shows as home, about, services respectively |
|                               | click / tap   | directs to Home, About, Services pages respectively |
| *Register, Login links         | hover over    | change colour & address shows as accounts/signup & accounts/login respectively |
|                               | click / tap   | directs to Register, Login pages respectively |
| Active link                   | click / tap different link | link takes bold colour depending on the current page |
| fixed on top                  | scroll page down | navigation stays visible on top |

* Registered / Logged in user 

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Profile, Logout links         | hover over    | change colour & address shows as profile & accounts/logout respectively |
|                               | click / tap   | directs to Profile, Logout pages respectively |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Footer</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Telephone number              | hover over    | brightens & underlined, address shows phone number |
|                               | click / tap   | opens new tab / asks to open or switch app |
| Email address                 | hover over    | brightens & underlined, address shows mailto:... |
|                               | click / tap   | opens outlook, mail, gmail or asks how to open or switch app  |
| Social links                  | hover over    | brightens, address shows relevant address to icon hovered on |
|                               | click / tap   | relevant website opens in a new tab |
| Copyright link                | hover over    | underlined, address shows LinkedIn page |
|                               | click / tap   | LinkedIn page opens in a new tab |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Landing Page</summary>

* Unregistered User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Large Hero                    | view          | displays large background image, Tailor's Timble For All Your Bespoke Tailoring Needs and Schedule Appointment button |
| *Schedule Appointment button  | hover over    | changes colour and background colour, address shows appointments |
|                               | click / tap   | directs to Login Page |

* Logged In User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Schedule Appointment button  | hover over    | changes colour and background colour, address shows appointments |
|                               | click / tap   | directs to Appointments Page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Home Page Content</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Our Philosophy                | view          | displayed with heading and paragraph with mission statement |
| Intro to Master Tailor        | view          | displayed with 'Established 1977' heading and paragraph, image visible on screens > 768px |
| Find out more link            | hover over    | gets underline, address shows about page |
|                               | click / tap   | directs to About page |
| Sample of services            | view          | displayed with 'Our Services' heading, short paragraph, 3 images with relevant captions |
| More services link            | hover over    | address shows services page |
|                               | click / tap   | directs to Services page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>About Page</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Image of Master Tailor        | view          | displayed image of the Master Tailor in workshop clearly and responsively |
| More About information        | view          | displayed with no grammatical or spelling errors |
| Bespoke Process               | view          | displayed responsively with heading, paragraphs, grammar/spelling errors free | 
| Process menu links            | hover over    | slightly darker background, address shows relevant id e.g. #list-ff |
|                               | click / tap   | black background, image and paragraph change to relevant menu title |
| CTA                           | view          | displays background image with The Perfect Fit For all your occasions and Schedule Appointment button |
| *Schedule Appointment button  | hover over    | changes colour and background-colour, address shows appointments page |

* Unregistered / Not logged in user

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Schedule Appointment button  | click / tap   | directs to Login page |

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Schedule Appointment button  | click / tap   | directs to Appointments page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Services Page</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Our Services                  | view          | displays responsively with 'Our Services' heading, short paragraph, 6 images with relevant captions |
| How our service works         | view          | displays responsively with 'How our service works' heading, paragraph, clear highlighted note and link |
| More info on our Bespoke Process here link | hover on | gets underline, address shows about/#process |
|                               | click / tap   | directs to About page Bespoke Process menu | 
| CTA                           | view          | displays background image with The Perfect Fit For all your occasions and Schedule Appointment button |
| *Schedule Appointment button  | hover over    | changes colour and background-colour, address shows appointments page |

* Unregistered / Not logged in user

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Schedule Appointment button  | click / tap   | directs to Login page |

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| *Schedule Appointment button  | click / tap   | directs to Appointments page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Registration</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Navigation bar Register link  | click / tap   | directs to Register page |
| Schedule Appointment button   | click / tap   | directs to Login page |
| Login page -> Register link   | click / tap   | directs to Register page |
| Invalid registration          | fill fields with invalid/empty values then click/tap Register button | tooltips or error messages are displayed at relevant field |
| Register button               | hover over    | background colour changes, colour changes |
| Login link                    | hover over    | colour changes, gets underline, address shows accounts/login |
| Valid registration            | Fill fields with valid values then click/tap Register button | directs to Profile page |
| Success alert                 | view          | displayed on top of the Profile page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Login</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Navigation bar Login link     | click / tap   | directs to Login page |
| Schedule Appointment button   | click / tap   | directs to Login page |
| Register link                 | hover over    | colour changes, gets underline, address shos accounts/signup |
|                               | click / tap   | directs to Registration page |
| Invalid login                 | fill fields with invalid details then click/tap Login button | tooltips are displayed at relevant field |
| Valid login                   | fill fields with valid details then click/tap Login button | directed to Profile page |      
| Success alert                 | view          | displayed on top of the Profile page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Logout</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Navigation bar Logout link    | click / tap   | directs to Logout page|
| Logout button                 | hover over    | background colour changes, colour changes | 
|                               | click / tap   | redirects to Home page|
| Success alert                 | view          | displayed on top of the Home page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Profile</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Navigation bar Profile link   | click / tap   | directs to Profile page |
| Username, First & Last Name, email address printed | view | The correct username, first & last name and email address are printed underneath the banner image |
| Placeholders in fields        | view          | placeholders with examples of values are displayed in each field |
| Astericks showing required fields | view      | all fields have astericks showing that they are required fields |
| Invalid phone                 | type in anything but digits then click/tap Update button | a tooltip is displayed with help text on how to fill in field |
| Invalid date                  | select a date in the past or < 30 days from today then click/tap Update button | error message with hint is displayed next to field, error alert is displayed on top of the page |
| Invalid form                  | leave a field empty | tooltip is displayed next to relevant field reminding you to fill out this field |
| Update button                 | hover over    | background colour changes, colour changes |
| Valid form                    | fill form with valid values then click/tap the Update button | redirects back to Home page |
| Success alert                 | view          | displayed at the top of the Home page |
| Pre-populated fields          | navigate back to the Profile page | all fields are pre-populated with the information previously entered and updated | 
| Appointments button           | hover on      | background colour changes, colour changes, address shows appointments page |
|                               | click / tap   | directs to the Appointments page |

ALL TESTS PASS

</details>

<br>

<details>

<summary>Appointments</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Appointments button on Profile page | click / tap | directs to Appointments page |
| Schedule Appointment button on Home, About, Services pages | click / tap | directs to Appointments page |
| Username's Appointments heading | view        | displays current logged in username in the heading |
| Add Appointment button        | hover on      | background-colour changes, text colour changes, address shows appointments/new |
|                               | click / tap   | directs to Create Appointment page |

* Logged in User with no appointments yet set

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Welcome card with logged in user's first and last name in heading | view | displays welcome card with current logged in user's first and last name in heading |

* Logged in User with an or some apointments set

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Appointment cards displayed in order of date of appointment | view | one appointment card is displayed or if more than one, appointments are displayed in order of date of appointment oldest first | 

ALL TESTS PASSED

</details>

<br>

<details>

<summary>Create Appointment</summary>

* Logged in User without Profile

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Add Appointment button on Appointments page | click / tap | directs to Create Appointment page with highlighted note instead of Create form |
| Note's heading has current user's username | view | displays current logged in user's username in heading |
| Profile page link             | hover on      | changes colour, address shows profile page |
|                               | click / tap   | redirects to current logged in user's Profile page |

* Logged in User with Profile

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Create Appointment page features Schedule an Appointment form and Back to Appointments button | view | displays Schedule an Appointment card with helpful information on how to fill in the form below, a Back to Appointments button below the card |
| Back to Appointments button   | hover on      | text colour changes, background colour changes, address shows appointments page |
| Process link on card          | hover on      | colour changes, gets underline, address shows about/#process |
|                               | click / tap   | opens in a new tab, directs to About page --> Bespoke Process Menu |
| Submit button                 | hover on      | text colour changes, background colour changes |
| Type field validation         | leave unselected & click/tap Submit button | tooltip displayed to remind you to select item on the list |
| Date field validation         | select date in the past, today or a Sunday or a Monday then click/tap Submit button | if other required fields are valid an error message is displayed next to date field with helpful hint |
| Time field validation         | leave unselected & click/tap Submit button | if other fields are valid, tooltip is displayed to remind you to select item in the list |
| Date and Time field validation | select valid date and time from list then click/tap Submit button | if there is already an appointment scheduled for same date and time, error message displays next to field with helpful hint, error alert is displayed at the top of the page |
| Valid form                    | fill in fields with valid data then click/tap Submit button | redirected to Appointments page where you can view newly created Appointment card |
| Success alert                 | view          | displayed at the top of the Appointments page |

ALL TESTS PASSED

</details>

<br>

<details>

<summary>View Appointment</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| View Appointment button on appointment card in Appointments page | click / tap | directs to View Appointment page with that appointment's card detail |
| Unauthorised viewing          | in the URL bar type in a different integer instead of the one present then hit enter | if id is not one of current logged in user's appointments a 403 or 404 page will be thrown |
| View Appointment page displays appointment card and a Back to Appointments button | view | Displays same appointment with some extra text, an Update and a Delete button and a Back to Appointments button underneath the card |
| Back to Appointments button   | hover on      | text colour changes, background colour changes, address shows appointments page |
| Middle section is different for approved appointments and for appointments waiting for approval | view        | displays text notification saying "we will be in touch ..." when appointment not approved OR displays text with current logged in user's first name and address of appointment if appointment is approved |
| Update button                 | hover on      | text colour change, background colour change, address shows appointments/`id`/update |
|                               | click / tap   | directs to Update Appointment page |
| Delete button                 | hover on      | text colour change, backgound colour change, address shows appointments/`id`/delete |
|                               | click / tap   | directs to Delete Appointment page |

ALL TESTS PASSED

</details>

<br>

<details>

<summary>Update Appointment</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Update button on appointment card in View Appointment page | click / tap | directs to Update Appointment page |
| Unauthorised updating         | in the URL bar type in a different integer instead of the one present then hit enter | if id is not one of current logged in user's appointments a 403 or 404 page will be thrown |
| Update Appointment page displays an Edit Appointment form and a Back to Appointments button | view    | Displays a card with Edit Appointment form with 4 fields and Update button, a Back to Appointments button at the bottom of the card |
| Back to Appointments button   | hover on      | text colour changes, background colour changes, address shows appointments page |
|                               | click / tap   | directs to Appointments page |
| Edit Appointment form fields are pre-populated with user's previously created info | view | displays fields pre-populated with logged in user's current appointment's info |
| All fields can be updated as per validation in Create Appointment table above | change field values then click/tap Update button | if fields are not validated, tool tips, error messages and error alert are displayed else ... |
| Update button                 | hover on      | text colour change, background colour change |
|                               | click / tap   | redirects to Appointments page |
| Success alert                 | view          | displayed at the top of Appointments page |

**Note**:- If the Update button is clicked without changing any of the fields of this form, it will throw an error on the Time field.  This is due to the fact that the set date and time are still set in the database.  The user will need to select a different time, update then head back and change to the previously set time again or cancel out of the update altogether by clicking on the Back to Appointments button.

ALL TESTS PASSED

</details>

<br>

<details>

<summary>Delete Appointment</summary>

* Logged in User

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Delete button on appointment card in View Appointment page | click / tap | directs to Delte Appointment page |
| Unauthorised deleting         | in the URL bar type in a different integer instead of the one present then hit enter | if id is not one of current logged in user's appointments, a 403 or 404 page will be thrown |
| Delete Appointment page displays a Delete Appointment card with two buttons | view | Displays a Delete Appointment card with a Yes, Delete and a Cancel button |
| Cancel button                 | hover on      | text colour changes, background colour changes, address shows appointments/`id`/ |
|                               | click / tap   | redirects to the View Appointment page of the current appointment |
| Yes, Delete button            | hover on      | text colour changes, background changes |
|                               | click / tap   | redirects to the Appointments page where you can see that the appointment has been deleted |
| Success alert                 | view          | displayed on the top of the Appointments page |

ALL TESTS PASSED

</details>

<br>

<details>

<summary>Admin Panel</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Access the Admin Panel        | type `/admin/` at the end of the website's URL in the URL bar | displays the Django Administration log in page |
| Superuser login               | type in the Username and password used when creating SuperUser | displays the Django Administration Interface with full permissions|
| Tailor login                  | type in the Username and password given by the SuperUser/Admin | displays the Django Administration Interface with full permissions |
| Staff login                   | type in the Username and password given by the Admin/Tailor | displays the Django Administration Interface with limited permissions |
| User login                    | type in any user's Username and password | access is denied |
| Admin & Tailor has viewing access to all tables | click and view all tables | data for Emails, Users, Appointments and Profiles is displayed |
| Admin & Tailor can add and update data in database | add user, give user first & last name and email address | success alerts are displayed for creation and change |
| Admin & Tailor can search database | type username of user created in search bar | User created is found and displayed |
| Admin & Tailor can delete database entries | tick the checkbox beside user created and select 'Delete selected user' from the dropdown Action field, click go and confirm deletion | successfully deleted 1 user is displayed | 
| Admin & Tailor can logout from Admin Panel | Click on Log out (top right) | redirects to Website's Home page with Register and Login links in the Navigation bar |

ALL TESTS PASSED

</details>

<br>

<details>

<summary>403, 404, 500 pages</summary>

| Feature                       | Action        | Effect                |
| ----------------------------- | ------------- | --------------------- |
| Styles are consistent with the rest of the website | view | displays website's navigation bar and footer, a card with error heading and informative text and Back to Home Page button |
| Back to Home Page button      | hover on      | styles change, address shows home |
|                               | click / tap   | redirects back to the Home page |

ALL TESTS PASSED

</details>

<br>

[Back To Top](#table-of-contents)

[Back to README.md](README.md)
