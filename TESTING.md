<img src="static/README/head-pic.png">
<br><br>

# Testing documentation for Retro Readers Web application.
<br><br>

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
    * [WAVE Accessibility](#wave-accessibility-checker)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [Member User](#member-user)
    * [Employee/PT User](#employeept-user)
    * [Management User](#management-user)
* [Manual Testing](#manual-testing)
* [Responsiveness](#responsiveness)

<br><br>

# Validation

## HTML Validation

All pages pass HTML Validation at [W3C markup validation service](https://validator.w3.org/) with no site breaking errors or warnings. 


<summary>Homepage</summary>
<br>
<img src="static/README/validation/homepage-checker.png">

<summary>Create a Booking</summary>
<br>
<img src="static/README/validation/create-booking-checker.png">

<summary>My Bookings</summary>
<br>
<img src="static/README/validation/my-bookings-checker.png">

<summary>Log In</summary>
<br>
<img src="static/README/validation/login-checker.png">

<summary>Log Out</summary>
<br>
<img src="static/README/validation/logout-checker.png">

<summary>Register</summary>
<br>
There were 4 errors on the registar html do to the html format used by allauth that I can not change, this is something I look to update myself in the future.
<br>
<img src="static/README/validation/registar-checker.png">

<summary>Edit Booking</summary>
<br>
<img src="static/README/validation/edit-booking-checker.png">

<summary>404 and 500 Error</summary>
<br>
Had to check the code manually for this one as checking via url would bring up IO Error: HTTP resource not retrievable. There are 2 errors showing due to it not liking the Django syntax for links. Otherwise all working correctly with no working issues. Both the same with only difference the 404 or 500 number showing up.
<br>
<img src="static/README/validation/404-checker.png">

## CSS Validation

All pages pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors or warnings.


<summary>CSS Validation</summary>
<br>
<img src="static/README/validation/css-checker.png">
<br><br>

## JS Validation

Custom JS script file run through [JShint](https://jshint.com/) for validation. Shows one undefined but as this is part of the script get bootstrap modal to work and one warning I have chosen to ignore these as the components work as expected.

<summary>JS Validation</summary>
<br>
<img src="static/README/validation/js-checker.png">
<br><br>

## CI Python Linter
All python files run through CI PEP8 Linter and pass with no warnings, with the exception of the E501 line being too long (84 > 79 characters). I believe this has no impact on the function of the b page so I have left it as it is.


<summary>models.py</summary>
<br>
<img src="static/README/validation/models.py-checker.png">
<br>
<summary>views.py</summary>
<br>
<img src="static/README/validation/view.py-checker.png">
<br>
<summary>urls.py</summary>
<br>
<img src="static/README/validation/urls.py-checker.png">
<br>
<summary>form.py</summary>
<br>
<img src="static/README/validation/form.py-checker.png">
<br><br>

## Lighthouse


<summary>Homepage - Best practices has a lower score as the report states "Does not use HTTPS" this is something I am unaware how to fix as we are hosting the project on a 3rd party site Heroku.
</summary>
<br>
<img src="static/README/lighthouse/homepage-lighthouse.png">
<br>
<summary>Register - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/signup-lighthouse.png">
<br>
<summary>Log In - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/login-lighthouse.png">
<br>
<summary>Sign Out - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/signout-lighthouse.png">
<br>
<summary>My Bookings - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/my-bookings-lighthouse.png">
<br>
<summary>New Booking - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/new-booking-lighthouse.png">
<br>
<summary>Edit Booking - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/edit-booking-lighthouse.png">
<br>
<summary>404 - Good Scores. Low SEO due to no metadata, happy with this score as this a simple page to take user back to the homepage if error occurs
</summary>
<br>
<img src="static/README/lighthouse/404-lighthouse.png">
<br>
<summary>500 - Good Scores. Low SEO due to no metadata, happy with this score as this a simple page to take user back to the homepage if error occurs
</summary>
<br>
<img src="static/README/lighthouse/500-lighthouse.png">
<br>

## WAVE Accessibility Checker

<summary>Homepage - No errors or contrast errors, two alerts for redundant links as Home link is present in both Nav logo and Nav link, one with 2 classes with the same name, this is needed as they are on different days.
</summary>
<br>
<img src="static/README/wave/homepage-wave.png">
<br>
<summary>Register - No errors, 1 contrast error, seems to be the colour of the text for the sign up link, I believe this is easy to see but will look to darken in future updates. Same alerts as Homepage.</summary>
<br>
<img src="static/README/wave/signup-wave.png">
<br>
<summary>Log In - No errors, same contrast and alerts as register.</summary>
<br>
<img src="static/README/wave/signin-wave.png">
<br>
<summary>My Bookings -  No errors or contrast errors. Same errors as homepage.</summary>
<br>
<img src="static/README/wave/my-bookings-wave.png">
<br>
<summary>New Booking - No errors or contrast errors.</summary>
<br>
<img src="static/README/wave/new-booking-wave.png">
<br>
<summary>Edit Booking - No errors or contrast errors</summary>
<br>
<img src="static/README/wave/edit-booking-wave.png">
<br>
<summary>404 - No errors, 1 contrast error, seems to be the colour of the button that links them back to the homepage
</summary>
<br>
<img src="static/README/wave/404-wave.png">
<br>
<summary>500 No errors, same contrast error as 404.
</summary>
<br>
<img src="static/README/wave/500-wave.png">
<br>
<br>

# User Story Testing

## Owners Goals

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I can create new classes so that members can book them.                                   | Form on the admin panel to create new class.                                                                                                   |
| I can view and manage all bookings so that issues or conflicts can be handled.            | On the admin panel a list of all bookings made for all users, with delete button if customer can not make it.                             |
| I can delete a class so that it can not be booked if it is no longer offered.             | A delete button with confirmation next to every class with in the admin panel.                                                             |
| I can edit class information so that I can update if any changes occur.                         | Next to every class a edit button exists so form can be accessed and updated.                                                               |
<br><br>

## Visitor Goals

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I can view a schedule of all available classes so that I can decide which class to attend.      | On the home page is a paginated list of classes offered in time and date order.                                                                |
| I can create an account so that I can book and manage classes.                                  | Top of the page is a link to register form so they can create an account.                                                                       |
| I can book a spot so that I can participate.                                              | On each class is a button that takes user to a form to fill in to book on to the class they wish to attend.                                 |
| I can see a list of the classes I have booked so that I can manage my schedule            | Once logged in on the nav bar is link to "My Booking" where user can see all booed class in time and date order.                               |
| I can cancel a booking so that I can no longer attend the class.                                | On my bookings page the user has delete button on each class with confirmation to cancel them going to the class.                              |
<br><br>

# Manual Testing

| Feature/Test                                          | Expected Outcome.                                                                                                        | Result |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| Logo in Navbar.                                       | Redirect to Homepage.                                                                                                    | Pass.  |
| Nav Links.                                            | Redirect to relevant pages.                                                                                              | Pass.  |
| Side Nav                                              | Navbar collapse to Sidenav on mobile devices with correct links.                                                         | Pass.  |
| Footer Links                                          | Open relevant sites in new tabs                                                                                          | Pass.  |
| Login button on Homepage.                             | Redirects to the login page.                                                                                                 | Pass.  |
| Login Form - empty.                                   | Will not submit if empty fields.                                                                                         | Pass.  |
| Login Form - incorrect username.                      | Form submits but doesn't login, gives flash message displaying reason.                                                   | Pass.  |
| Login Form - incorrect password.                      | Form submits but doesn't login, gives flash message displaying reason.                                                   | Pass.  |
| Login Form - correct details.                         | Form submits and redirects user to relevant page for that user.                                                          | Pass.  |
| Login Nav bar                                         | When a user login, nav remove register and login with my bookings and sign out.                                            | Pass.  |
| Register link on Login Form.                         | Redirects to the registration page.                                                                                              | Pass.  |
| Register Form - empty.                                | Will not submit empty fields.                                                                                         | Pass.  |
| Register Form - username exists.                      | Form submits but does not register user, flash message display username already exists.                                  | Pass.  |
| Register Form - new user details.                     | Form submits adding new user and redirects to Homepage with flash message asking to Log In.                              | Pass.  |
| Log In link on Register Form                          | Redirects to the Login page.                                                                                                | Pass.  |
| LogOut Button.                                       | Logs users out, clears session cookies and redirects to Homepage.                                                         | Pass.  |
| Log Out Confirmation.                                 | When user click on log out a confirmation appears first to verify their action.                                             | Pass.  |
| My bookings link                                      | Redirects user to page with all there booked classes                                                                     | Pass.  |
| My bookings page - edit booking button.               | Redirects to edit session page.                                                                                          | Pass.  |
| My bookings page - delete booking button.             | Modal pops up prompting user to confirm change as a defense.                                                             | Pass.  |
| My bookings page - logged in.                            | User must be logged in to view booked class, if not the login screen will be presented.                                     | Pass.  |
| New booking form - empty.                             | Will not submit empty fields.                                                                                         | Pass.  |
| New booking form - auto fill class.                   | The class they click to book on will auto fill the class field.                                                       | Pass.  |
| New booking form - logged in.                            | User must be logged in to book a class, if not log in screen will be presented.                                          | Pass.  |
| New booking form - submit.                            | With the form correctly filled in and submitted, user is redirected to my booking page with message confirmation.             | Pass.  |
| Edit session form.                                    | Displays current booked details already inputted.                                                                        | Pass.  |
| Edit Session form - empty.                            | Will not submit empty fields.                                                                                         | Pass.  |
| Edit session form - submit.                           | Form submits updates changes and redirects to my booking page with message confirmation.                                | Pass.  |
| Type a non-existent page path.                        | Redirects to 404 page.                                                                                                   | Pass.  |
| Enter the url to edit session when logged out.            | Redirects to 500 page.                                                                                                   | Pass.  |
| 404 page - home button.                               | Redirects to Homepage.                                                                                                   | Pass.  |
| 500 page - home button.                               | Redirects to Homepage.                                                                                                   | Pass.  |
<br><br>