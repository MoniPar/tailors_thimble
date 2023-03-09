# Table of Contents

* [Code Validation](#code-validation)
* [Lighthouse](#lighthouse-testing)
* [Responsiveness](#responsiveness-testing)
* [Browser Compatibility](#browser-compatibilty-testing)
* [User Stories](#user-story-testing)
* [Other Features](#other-features-testing)

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

**APPOINTMENTS LIST**

![No Errors or Warnings to show](documentation/html-val-appts.png)

**APPOINTMENT CREATE**

![No Errors or Warnings to show](documentation/html-val-createappt.png)

**APPOINTMENT READ**

![No Errors or Warnings to show](documentation/html-val-viewappt.png)

**APPOINTMENT UPDATE**

![No Errors or Warnings to show](documentation/html-val-updateappt.png)

**APPOINTMENT DELETE**

![No Errors or Warnings to show](documentation/html-val-deleteappt.png)

**403**

![No Errors or Warnings to show](documentation/html-val-403.png)

**404**

![No Errors or Warnings to show](documentation/html-val-404.png)

</details>

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

<br>

</details>

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



<br>

</details>

[Back To Top](#table-of-contents)

_____

## Lighthouse Testing

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO.  This was run in Chrome DevTools in incognito mode. 

<details>
<summary>Screenshots and results for all pages</summary>
<br>

**HOME**

* Mobile

![Passed](documentation/mobile-home.png)

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
| Appointments List        | mobile  |  95 | 100 | 100 |  97 |
|                          | desktop | 100 | 100 | 100 | 100 |
| Appointment Create       | mobile  |  94 | 100 |  92 |  98 |
|                          | desktop | 100 | 100 |  92 | 100 |
| Appointment Read         | mobile  |  98 | 100 | 100 |  97 |
|                          | desktop |  99 | 100 | 100 | 100 |
| Appointment Update       | mobile  |  98 | 100 | 100 |  98 |
|                          | desktop | 100 | 100 | 100 | 100 |
| Appointment Delete       | mobile  |  98 | 100 | 100 |  97 |
|                          | desktop |  99 | 100 | 100 | 100 |
<br>
</details>

[Back To Top](#table-of-contents)

_____

## Responsiveness Testing


[Back To Top](#table-of-contents)

_____

## Browser Compatibilty Testing


[Back To Top](#table-of-contents)

_____

## User Story Testing


[Back To Top](#table-of-contents)

_____

## Other Features Testing


[Back To Top](#table-of-contents)

