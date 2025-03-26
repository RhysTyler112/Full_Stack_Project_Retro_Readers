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
<img src="static/README/Testing pics/homepage-check.png">

<summary>Add Booking</summary>
<br>
<img src="static/README/Testing pics/add-book-checker.png">

<summary>Edit Book</summary>
<br>
<img src="static/README/Testing pics/edit-book-checker.png">

<summary>Log In</summary>
<br>
<img src="static/README/Testing pics/login-checker.png">

<summary>Log Out</summary>
<br>
<img src="static/README/Testing pics/logout-checker.png">

<summary>Register</summary>
<br>
<img src="static/README/Testing pics/registar-checker.png">

<summary>Books</summary>
<br>
<img src="static/README/Testing pics/books-checker.png">

<summary>Book Details</summary>
<br>
<img src="static/README/Testing pics/book-detail-checker.png">

<summary>Wishlist</summary>
<br>
<img src="static/README/Testing pics/wishlist-checker.png">

<summary>Bag</summary>
<br>
<img src="static/README/Testing pics/bag-checker.png">

<summary>Checkout</summary>
<br>
<img src="static/README/Testing pics/checkout-checker.png">

<summary>Checkout Success</summary>
<br>
<img src="static/README/Testing pics/checkout-success-checker.png">

<summary>My Profile</summary>
<br>
<img src="static/README/Testing pics/profile-checker.png">


## CSS Validation

All pages pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors or warnings.


<summary>CSS Validation</summary>
<br>
<img src="static/README/Testing pics/CSS-checker.png">
<br><br>

## JS Validation

Custom JS script file run through [JShint](https://jshint.com/) for validation. Shows undefined variables due to jQuery "$".


<summary>Country Field</summary>
<br>
<img src="static/README/Testing pics/country-feild-js-checker.png">
<br><br>

<summary>Stripe</summary>
<br>
<img src="static/README/Testing pics/stripe-element-checker.png">
<br><br>


## CI Python Linter
A sample of Python files run through CI PEP8 Linter and pass with no warnings, with the exception of the E501 line being too long (84 > 79 characters). I believe this has no impact on the function of the b page so I have left it as it is.


<summary>models.py</summary>
<br>
<img src="static/README/Testing pics/CI/models-profile.png">
<br>
<summary>views.py</summary>
<br>
<img src="static/README/Testing pics/CI/views-profile.png">
<br>
<summary>urls.py</summary>
<br>
<img src="static/README/Testing pics/CI/urls-profile.png">
<br>
<summary>form.py</summary>
<br>
<img src="static/README/Testing pics/CI/form-profile.png">
<br><br>

## Lighthouse


<summary>Homepage</summary>
<br>
<img src="static/README/lighthouse/homepage.png">

<summary>Add Booking</summary>
<br>
<img src="static/README/lighthouse/add-book.png">

<summary>Edit Book</summary>
<br>
<img src="static/README/lighthouse/edit-book.png">

<summary>Log In</summary>
<br>
<img src="static/README/lighthouse/login.png">

<summary>Log Out</summary>
<br>
<img src="static/README/lighthouse/logout.png">

<summary>Register</summary>
<br>
<img src="static/README/lighthouse/registar.png">

<summary>Books - This has been affected by the books cover loading for an external source</summary>
<br>
<img src="static/README/lighthouse/books.png">

<summary>Book Details</summary>
<br>
<img src="static/README/lighthouse/book-detail.png">

<summary>Wishlist</summary>
<br>
<img src="static/README/lighthouse/wishlist.png">

<summary>Bag</summary>
<br>
<img src="static/README/lighthouse/bag.png">

<summary>Checkout</summary>
<br>
<img src="static/README/lighthouse/checkout.png">

<summary>Checkout Success</summary>
<br>
<img src="static/README/lighthouse/checkout-success.png">

<summary>My Profile</summary>
<br>
<img src="static/README/lighthouse/profile.png">

## WAVE Accessibility Checker

A few contrast errors and missing labels

<summary>Homepage</summary>
<br>
<img src="static/README/wave/homepage.png">

<summary>Add Booking</summary>
<br>
<img src="static/README/wave/add-book.png">

<summary>Edit Book</summary>
<br>
<img src="static/README/wave/edit-book.png">

<summary>Log In</summary>
<br>
<img src="static/README/wave/login.png">

<summary>Log Out</summary>
<br>
<img src="static/README/wave/login.png">

<summary>Register</summary>
<br>
<img src="static/README/wave/registar.png">

<summary>Books</summary>
<br>
<img src="static/README/wave/books.png">

<summary>Book Details</summary>
<br>
<img src="static/README/wave/book-details.png">

<summary>Wishlist</summary>
<br>
<img src="static/README/wave/wishlist.png">

<summary>Bag</summary>
<br>
<img src="static/README/wave/bag.png">

<summary>Checkout</summary>
<br>
<img src="static/README/wave/checkout.png">

<summary>Checkout Success</summary>
<br>
<img src="static/README/wave/checkout-success.png">

<summary>My Profile</summary>
<br>
<img src="static/README/wave/profile.png">
<br>
<br>

# User Story Testing

## Owners Goals

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I can create new classes so that members can book them.                                   | Form on the admin panel to create a new class.                                                                                                   |
| I can view and manage all bookings so that issues or conflicts can be handled.            | On the admin panel a list of all bookings made for all users, with a delete button if customer can not make it.                             |
| I can delete a class so that it can not be booked if it is no longer offered.             | A delete button with confirmation next to every class within the admin panel.                                                             |
| I can edit class information so that I can update if any changes occur.                         | Next to every class a edit button exists so form can be accessed and updated.                                                               |
<br><br>

## Visitor Goals

| User Story                                                                                ## Owners Goals

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I can add new books so that members can add them to their wishlist or purchase them.      | Form on the admin panel to add new books.                                                                                                 |
| I can view and manage all orders so that issues or conflicts can be handled.              | On the admin panel, a list of all orders made by users, with the ability to update or delete orders if necessary.                          |
| I can delete a book so that it can no longer be purchased or added to wishlists.          | A delete button with confirmation next to every book in the admin panel.                                                                  |
| I can edit book information so that I can update details like price, description, or stock. | Next to every book, an edit button exists so the form can be accessed and updated.                                                        |
<br><br>

## Visitor Goals

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I can browse a catalog of books so that I can find books I am interested in.              | On the home page, a paginated list of books is displayed, sorted by categories or popularity.                                              |
| I can create an account so that I can manage my orders and wishlist.                      | At the top of the page, there is a link to a registration form so users can create an account.                                             |
| I can add books to my wishlist so that I can save them for later.                         | On each book's detail page, there is a button to add the book to the wishlist.                                                            |
| I can view my wishlist so that I can manage the books I want to purchase.                 | Once logged in, a "Wishlist" link in the navigation bar redirects users to their wishlist page.                                            |
| I can remove books from my wishlist so that I can keep it updated.                        | On the wishlist page, each book has a delete button with confirmation to remove it from the wishlist.                                      |
| I can purchase books so that I can own them.                                              | On each book's detail page, there is an "Add to Bag" button that redirects users to the checkout process.                                  |
| I can view my order history so that I can keep track of my purchases.                     | Once logged in, a "My Orders" link in the navigation bar redirects users to their order history page.                                      |
| I can cancel an order so that I can manage my purchases.                                  | On the order history page, users can cancel orders that have not yet been processed.                                                      |
<br><br>

# Manual Testing

| Feature/Test                                          | Expected Outcome                                                                                                         | Result |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------ |
| Logo in Navbar.                                       | Redirects to the homepage.                                                                                              | Pass   |
| Nav Links.                                            | Redirects to relevant pages.                                                                                           | Pass   |
| Side Nav                                              | Navbar collapses to a sidenav on mobile devices with correct links.                                                    | Pass   |
| Footer Links                                          | Opens relevant external sites in new tabs.                                                                             | Pass   |
| Login button on Homepage.                             | Redirects to the login page.                                                                                           | Pass   |
| Login Form - empty.                                   | Will not submit if fields are empty.                                                                                   | Pass   |
| Login Form - incorrect username.                      | Form submits but does not log in, displays a flash message explaining the issue.                                        | Pass   |
| Login Form - incorrect password.                      | Form submits but does not log in, displays a flash message explaining the issue.                                        | Pass   |
| Login Form - correct details.                         | Form submits and redirects the user to their profile page.                                                             | Pass   |
| Login Nav bar                                         | When a user logs in, the nav bar replaces "Register" and "Login" with "My Profile" and "Logout."                        | Pass   |
| Register link on Login Form.                          | Redirects to the registration page.                                                                                    | Pass   |
| Register Form - empty.                                | Will not submit if fields are empty.                                                                                   | Pass   |
| Register Form - username exists.                      | Form submits but does not register the user, displays a flash message explaining the issue.                            | Pass   |
| Register Form - new user details.                     | Form submits, adds the new user, and redirects to the homepage with a flash message asking the user to log in.          | Pass   |
| Log In link on Register Form.                         | Redirects to the login page.                                                                                           | Pass   |
| Logout Button.                                        | Logs the user out, clears session cookies, and redirects to the homepage.                                              | Pass   |
| Logout Confirmation.                                  | When the user clicks "Logout," a confirmation modal appears to verify their action.                                     | Pass   |
| Wishlist link                                         | Redirects the user to their wishlist page.                                                                             | Pass   |
| Wishlist page - remove book button.                   | Removes the book from the wishlist with a confirmation message.                                                        | Pass   |
| Wishlist page - empty wishlist.                       | Displays a message indicating the wishlist is empty.                                                                   | Pass   |
| Book detail page - add to wishlist button.            | Adds the book to the user's wishlist and displays a confirmation message.                                              | Pass   |
| Book detail page - Add to Bag button.                 | Adds the selected book to the shopping bag and displays a confirmation message.                                         | Pass   |
| Book detail page - Add to Bag button (logged out).    | Redirects the user to the login page if they are not logged in.                                                         | Pass   |
| Bag page - View items in the bag.                     | Displays all books added to the bag, including title, quantity, and price.                                              | Pass   |
| Bag page - Update quantity.                           | Allows the user to update the quantity of a book in the bag, recalculates the total price, and displays a confirmation message. | Pass   |
| Bag page - Remove item.                               | Allows the user to remove a book from the bag, recalculates the total price, and displays a confirmation message.        | Pass   |
| Bag page - Empty bag.                                 | Displays a message indicating the bag is empty if no items are present.                                                 | Pass   |
| Checkout page - View order summary.                   | Displays a summary of the items in the bag, including total price and shipping costs.                                   | Pass   |
| Checkout page - Fill in payment details.              | Allows the user to enter payment and shipping details.                                                                  | Pass   |
| Checkout page - Submit order (valid details).         | Processes the order, redirects to the checkout success page, and displays a confirmation message.                       | Pass   |
| Checkout page - Submit order (invalid details).       | Displays an error message and does not process the order.                                                               | Pass   |
| Checkout success page - View order confirmation.      | Displays a confirmation message with the order number and summary of the purchased items.                               | Pass   |
| Checkout success page - Logged out user.              | Redirects the user to the login page if they are not logged in.                                                         | Pass   |
| Bag page - Continue shopping button.                  | Redirects the user back to the book catalog to browse more books.                                                       | Pass   |
| Checkout page - Back to Bag button.                   | Redirects the user back to the bag page to make changes to their order.                                                 | Pass   |
| Checkout page - Stripe payment integration.           | Processes payment securely using Stripe and redirects to the checkout success page upon successful payment.             | Pass   |
| Checkout page - Stripe payment failure.               | Displays an error message if the payment fails and allows the user to retry.                                            | Pass   |
| Checkout success page - View order history link.      | Redirects the user to their order history page to view past orders.                                                     | Pass   |
| Checkout success page - Home button.                  | Redirects the user to the homepage.                                                                                     | Pass   |
| Order history link                                    | Redirects the user to their order history page.                                                                        | Pass   |
| Order history page - cancel order button.             | Cancels the order with a confirmation message.                                                                         | Pass   |
| Order history page - view order details.              | Displays the details of the selected order.                                                                            | Pass   |
| Type a non-existent page path.                        | Redirects to a 404 error page.                                                                                         | Pass   |
| 404 page - home button.                               | Redirects to the homepage.                                                                                            | Pass   |
| 505 page - home button.                               | Redirects to the homepage.                                                                                            | Pass   |

<br><br>

# Bugs and fixes

### Submit payment overlay not showing
- Decided to remove it all together.
### Check out input bars were not filling div 100%
- Override CSS to fix this issue 
### Open Library was not pulling all data need or correctly
- Made the book details fully editable so any errors or missed data could be fixed
### AWS was not loading images or Favicon
- Update the url connection point from {% media %} to {% static %}
### When delete book from bag all formats were being delete instead of the one intended
- Update code to make sure this does not happen 
### You could add a book to bag with selecting format that causes 500 error on checkout
- Put a safe guard and alert message to ensure a format has to be selected.
### On checkout success totals are not calculating on deployed site, works find locally
- Have not been able to solve this issue.
