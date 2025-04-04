# Full_Stack_Project_Retro_Readers

This website was created as the 4th Milestone Project for Code Institute's web application development course.

[**__link to deployed site here__**](https://retro-readers-dba048839ab2.herokuapp.com/)
<br><br>

<img src="static/README/head-pic.png">
<br><br>

# Contents

* [User Experience](#user-experience-ux)
    * [Store Admins](#Store-Admins)
    * [Shopper](#Shopper)
* [Design](#design)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
    * [Materialize](#materialize)
    * [Images](#images)
* [Features](#features)
    * [All Features](#multi-page-features)
    * [CRUD Functionality](#crud-functionality)
    * [Future Implementation](#future-implementation)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
    * [Forking Repository](#forking-the-github-repository)
    * [Make Local Clone](#making-a-local-clone)
    * [Version Control](#version-control)
* [Credits](#credits)

<br><br>

# User Experience

An online book store that is going back to the roots of reading. This book store only sells physical books and CDs so customers can buy softcover/hardcover books and CDs for audiobooks.
<br><br>

## Store Admins
As a Store Owner I can Delete a product so that Remove items that are no longer for sale.
<br><br>

As a Store Owner I can Edit/update a product so that Change product prices, descriptions, images and other product criteria.
<br><br>

As a Store OwnerAdd a product so that new items can be added to my store
<br><br>

## Shopper
As a Shopper I can Easily navigate the site so that Find products/information that I require.
<br><br>

As a Shopper I can View a profile page so that I can set a default delivery address and view previous purchases.
<br><br>

As a Shopper I can Reset my password so that I can recover my account.
<br><br>

As a Shopper I can add products I am interested in to a Wishlist so that I can keep a list of item I may purchase in the future
<br><br>

As a Shopper I can easily enter my payment information so that Check out quickly and with no hassles

- Feel my personal and payment information is safe and secure
<br><br>

As a Shopper I can Log in and out so that I can keep my account information secure
<br><br>

As a Shopper I can Register for an account so that Have an account with the site and view my profile

- Email confirmation for account verify
<br><br>

As a Shopper I can Easily select the quantity of a product when purchasing it so that Ensure I don't accidentally select the wrong product quantity
<br><br>

As a Shopper View items in my bag to be purchased** so that Identify the total cost of my purchase and all items I will receive.
<br><br>

As a Shopper I can Adjust the quantity of individual items in my bag so that Easily make changes to my purchase before checkout
<br><br>

As a Shopper I can View an order confirmation after checkout so that Verify that I haven't made any mistakes

- Receive an email confirmation after checking out
<br><br>

As a Shopper I can View my running total of purchases throughout my visit so that I don't overspend and am able to track whether I meet any thresholds for site offers (e.g. free delivery)
<br><br>

As a Shopper I can View the items I currently have selected for purchase so that it enables me to check I still wish to purchase the items, or amend quantities if required
<br><br>

As a Shopper I can View more detail on products so that they can make an informed decision if the item suits their requirements
<br><br>

As a Shopper I can View a category of products/filter products so that they can find specific items interested in without having to scroll through all products
<br><br>

As a Shopper I can Easily see what I've searched for and the number of results so that Quickly decide whether the product I want is available
<br><br>

As a Shopper I can Search for a product by name or description so that Find a specific product I'd like to purchase
<br><br>

As a Shopper I can Sort the list of available products so that Easily identify the best priced and categorically sort products
<br><br>

As a Shopper I can Sort a specific category of products so that Find the best-priced product in a specific category, or sort the products in that category by name
<br><br>

# Design

* Colour Scheme
    * Primary colours used on the website: 
    * ![Color Scheme](static/README/colour-scheme.png)

* Typography
    * [Google Fonts](https://fonts.google.com/) was used in the design instead of the default to present a more book font.


* WireFrames 

I used figma to create my wireframes which are located below


<summary>Desktop</summary>
<br>
<img src="static/README/wireframe and data relations/Wireframe Desktop 1.png">
<br>
<img src="static/README/wireframe and data relations/Wireframe Desktop 2.png">
<br>
<summary>Tablet</summary>
<br>
<img src="static/README//wireframe and data relations/Wireframe Tablet 1.png">
<br>
<img src="static/README//wireframe and data relations/Wireframe Tablet 2.png">
<br>
<summary>Mobile</summary>
<br>
<img src="static/README/wireframe and data relations/Wireframe Mobile 1.png">
<br>
<img src="static/README/wireframe and data relations/Wireframe Mobile 2.png">
<br>
<br><br>

## Database Schema

Schema for PostgreSQL database was created on [Diagrams.net](https://app.diagrams.net/)

<summary>DB Schema</summary>
<br>
<img src="static/README/wireframe and data relations/Data Relation.png">
<br><br>

## Images 

All images were sourced from [Unsplash](https://unsplash.com/)
<br><br>


# Features

## Navbar

The navbar is present across all pages except for custom pages to catch errors. On mobile devices it collapses to a hamburger icon which opens as a sidenav. The links visible are dependent on if the user is logged in.

<summary>Navbar</summary>
<br>
<img src="static/README/navbar.png">
<br><br>
<summary>Navbar signed in admin</summary>
<br>
<img src="static/README/navbar-signed-in-admin.png">
<br><br>
<summary>Navbar signed in</summary>
<br>
<img src="static/README/navbar-signed-in.png">
<br><br>
<summary>Navbar signed out</summary>
<br>
<img src="static/README/navbar-signed-out.png">
<br><br>
<summary>Navbar Books</summary>
<br>
<img src="static/README/navbar-books.png">
<br><br>
<summary>Navbar Genre</summary>
<br>
<img src="static/README/navbar-genere.png">
<br><br>


## Footer
Footer is present across all pages except for custom pages to catch errors, with links to store potential socials.

<br>
<img src="static/README/footer.png">
<br><br>

## Books

This is where customers can see the books they are looking for, they can filter it down by the genre or format they are looking for as well as price. When they look at their chosen book they can view all the details of that book and choose the format they wish to purchase. If they do not need the book they can add it to a wishlist for the future. 

<summary>Book list</summary>
<br>
<img src="static/README/book-list.png">
<br><br>
<summary>Book filters</summary>
<br>
<img src="static/README/book-filters.png">
<br><br>
<summary>Book detail </summary>
<br>
<img src="static/README/books-details.png">
<br><br>
<summary>Book format selection</summary>
<br>
<img src="static/README/book-format-selction.png">
<br><br>
<summary>Add to wish list</summary>
<br>
<img src="static/README/book-wishlist.png">
<br><br>

## The Bag

This is where the customer can collect all books they wish to purchase in one place before they buy them. This will be a running total of the basket and when a book is added a little summary of what has been added.

<summary>Bag - Navbar</summary>
<br>
<img src="static/README/bag-navbar.png">
<br><br>
<summary>Bag - Navbar with total</summary>
<br>
<img src="static/README/bag-navbar-with-total.png">
<br><br>
<summary>The bag</summary>
<br>
<img src="static/README/bag.png">
<br><br>
<summary>Bag Summary</summary>
<br>
<img src="static/README/bag-summary.png">
<br><br>

## Messages

Alerts will appear on the screen to let the user know a certain action has been fulfilled. This confirms they have signed in or out etc...

<summary>Success</summary>
<br>
<img src="static/README/alert-success.png">
<br><br>
<summary>Error</summary>
<br>
<img src="static/README/alert-error.png">
<br><br>

<summary>Info</summary>
<br>
<img src="static/README/alert-info.png">
<br><br>

## Add/edit book

These pages show how store admins can add or update/delete books on the store.

<summary>Add</summary>
<br>
<img src="static/README/add-book.png">
<br><br>
<summary>Edit</summary>
<br>
<img src="static/README/book-edit.png">
<br><br>
<summary>Delete</summary>
<br>
<img src="static/README/book-delete.png">
<br><br>

## Log In 

Login form is rendered and checks for users in the database and password correct. Prompt on form if not already registered with link to register page.


<img src="static/README/signin.png">
<br><br>

## Log Out

Log out functionality available to all logged in users, simply clears all session cookies.

<img src="static/README/signout.png">
<br><br>

## Register

Form is rendered to register for the site, checks if the user is already in the database, if not adds them to the database. Prompt on the form if already registered with a link to the Login page.

<img src="static/README/registar.png">
<br><br>

## Homepage

Homepage is available to all users where they can see the hero image with a welcome message that has a button that takes them to view all books so they can choose their next story.

<summary>Shop Now</summary>
<br>
<img src="static/README/home-shop-now.png">
<br><br>


## My Profile

This is the page the user can see all the orders that have they have made, with a order number, summary of items ordered and total cost as well the ability to update the their default delivery address

<img src="static/README/my-profile.png">
<br><br>

## Checkout

This is the page the user is directed to once they have made their booking, this can also be done from a link in the navbar and also a view my booking button above the list classes. Here the user can view their upcoming classes and make any updates to their booking or delete the booking if they no longer can attend.

<summary>Checkout</summary>
<br>
<img src="static/README/checkout.png">
<br><br>
<summary>Checkout Success</summary>
<br>
<img src="static/README/checkout-success.png">


## Error Pages

### 404 Page

In the event of a page not found the error handler will render a page with a link back to the homepage.

<img src="static/README/404.png">

<br><br>

### 500 Page

In the event of a bad response from the server the error handler will render a page with a link back to the homepage.

<img src="static/README/500.png">

<br><br>

## CRUD Functionality

| Page         | Create                                                  | Read                                                                                 | Update                                                 | Delete                                                                |
| ------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------- |
| Login        |                                                         | Read username for password check                                                     |                                                        |                                                                       |
| Register     | Create new User | Read username to check if User exists                                                |                                                        |                                                                       |
| Orders  |  Creating new orders with buying books                                                      | View all currently orders                                         | Update quantity and address before purchase            | Remove books from bag before purchase                             |
| Books | Add new books                      |     Update book details             |                                                        |  Remove books no longer being sold                                                                  | 

## Future Implementation

To further improve the store for functional use I would add a stock tracker for the quantity of books the store has to sell, therefore if the stock goes to zero the customer would not be able to purchase that book or format of book.

# Technologies

## Languages

* HTML5 - for content and structure.
* CSS3 - for styling.
* Vanilla JS - for initialization of materialised components and for functions that request and handle data from the backend.
* Python (Django)- for the backend functionality.
    
<br><br>

## Tools

* Figma - used to create wireframes.
* Diagrams.net - used to create DB schema.
* Google Dev Tools - used for troubleshooting during development.
* Git/Github - used for version control and storage.
* Heroku - used for deployment.
<br><br>

# Testing

For testing please use the [Testing](/TESTING.md) documentation.
<br><br>

# Deployment

## Deployment to Heroku

To deploy to Heroku:
1. In GitPod CLI, the root directory of the project, run:
    pip3 freeze --local > requirements.txt
    to create a requirements.txt file containing project dependencies.
2. In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'.
    Open the Procfile. Inside the file, check that web: python3 app.py has been added when creating the file
    Save the file.
3. Push the 2 new files to the GitHub repository
4. Login to Heroku, select Create new app, add the name for your app and choose your closest region.
5. Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
6. Navigate to the settings tab, click reveal config vars and input the following:

| Key | Value |
| :---: | :---: |
| DATABASE_URL | postgresql |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | mysecretkey |

Actual Environment variables not disclosed for security.

## Forking the GitHub Repository
<br>

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.
<br><br>

## Making a Local Clone
<br>

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br><br>

## Version Control

Workflow controlled using Git and GitHub. It helps you track different versions of your code and collaborate with other developers. Version control allows you to keep track of your work and helps you to easily explore the changes you have made.

You can think of a repository as a “main folder”, everything associated with a specific project should be kept in a repo for that project.
You will have a local copy (on your computer) and an online copy (on GitHub) of all the files in the repository.

Once Changes on your local copy have been saved they can be added to the staging area using ```Git -add```. And then commited using ```Git commit``` along with your message, meaning they will be saved as a version of the repository which is then ready to be pushed, using ```Git push```, up to the online copy of your repository.
<br><br>

# Credits

* All photos on the homepage were sourced from [Unsplash](https://unsplash.com/).
* Images for book cover are generate via API from [Open Libary](https://openlibrary.org/)
