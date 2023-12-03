# Tie the Knot Wedding Planner
*Tie the Knot is a website designed to assist users who are planning their wedding and need to keep track of their To Do list, their Payments and their Guest List.*

## Purpose and Value

#### User Goal
To use a website to assist the planning of their wedding.

#### Website Goal
For users to be able to keep track of their wedding information with ease.

#### User Stories
> A couple who both come from big families would like a wedding planner website to keep track of who has been invited, any dietary needs and what tables everyone will be sat at.

> A couple who are planning a classic big white wedding and need a wedding planner website to organise their To Do list, including keeping track of what payments need to be made and when.

## Competitor Review

For this project, I had a look at two wedding planning websites:
* Hitched Wedding Planner
* Bridebook Wedding Planner

**Hitched Wedding Planner**

Pros:
* When you first log on, it has the couple's names, which makes the website feel really personalised.

Cons:
* There's a lot of information on the Dashboard page, making it quite overwhelming, and doesn't give an accurate overview of features.

**Bridebook Wedding Planner**

Pros:
* Guests can be grouped by family. Dashboard has some great colours and easy to read cards to take you to each page

Cons: 
* Articles and adverts for suppliers not clearly titled on the home page. The Dashboard page would have made a much better home page.

| Objective           | Importance | Viability / Feasibility | To be added |
|------------|------------|-------------------------|--------|
| Users able to add, update & delete their guest list       |  5  |   4   |  :heavy_check_mark:  |
| Users able to add, update & delete their to do list     |  5     |  5    | :heavy_check_mark: |
| Users able to set a budget and add, update and delete their wedding costs    |  3  |  3   | :heavy_check_mark:   |
| Users able to see when payments need to be made  |  4  |  4  |  |
| Users able to see what table their guests are sat on   |   4    |  3   | :heavy_check_mark: *    |

Table numbers will be added to the Guest List page. However, I would like to add a page specifically for showing the table numbers and the guests assigned to them on individual cards. In future updates I would also like to add the budget feature, so users can keep track of payments and budgets in one place.

## Structure

I started drafting my ideas for structure on [Figma](https://www.figma.com/). I created my wireframes next on [Balsamiq](https://balsamiq.com/), and then moved back to [Figma](https://www.figma.com/) to create my prototype.

I've chosen to have a home page that promotes the features of the website. The user will be prompted to log in or sign up, and the pages for these will come straight from the home page.

Once logged in, the user will have their own dashboard. From here they can see their Checklist, from which they can add, edit and delete Checklist Items. They can also access their Guest list from the Dashboard, and add, edit or delete their Guests. The last page will filter any Items in the Checklist with the "Payment" field ticked, so users can keep track of their payments.

#### Structure Plan
* [Structure Plan](/tie-the-knot/static/images/readme/structure-plan.PNG)

#### Wireframes
* [Home page](/tie-the-knot/static/images/readme/home-page-wireframe.PNG)
* [Sign Up page](/tie-the-knot/static/images/readme/sign-up-page-wireframe.PNG)
* [Log In page](/tie-the-knot/static/images/readme/log-in-page-wireframe.PNG)
* [Dashboard page](/tie-the-knot/static/images/readme/dashboard-page-wireframe.PNG)
* [Checklist page](/tie-the-knot/static/images/readme/checklist-page-wireframe.PNG)
* [Add Checklist page](/tie-the-knot/static/images/readme/add-checklist-item-page-wireframe.PNG)
* [Edit Checklist page](/tie-the-knot/static/images/readme/edit-checklist-item-page-wireframe.PNG)
* [Guest page](/tie-the-knot/static/images/readme/guest-page-wireframe.PNG)
* [Add Guest page](/tie-the-knot/static/images/readme/add-guest-page-wireframe.PNG)
* [Edit Guest page](/tie-the-knot/static/images/readme/edit-guest-page-wireframe.PNG)
* [Payments page](/tie-the-knot/static/images/readme/payments-page-wireframe.PNG)

#### Prototype
* [Checklist page](/tie-the-knot/static/images/readme/checklist-page-prototype.PNG)


## Features

#### Navigation
The navigation includes a logo, which routes to either the Home page or Dashboard, dependent on whether a user is logged in or not. It also includes Log In and Create Account links if the there is no user logged in. If there is a user logged in, the Navigation includes three dropdowns. Dropdown one is "Things to do", which opens a dropdown showing "Checklist" and "Payments". Dropdown two is "Guest List", and opens a dropdown with "Guests" and "Table Plan". Dropdown three has the User's name, and opens a dropdown with "Dashboard" and "Log out".

#### Footer
The footer has a list of internal links for "Dashboard", "Checklist", "Guests", "Table Plan" and "Payments". It also includes links to Facebook, Instagram, Twitter and Youtube. Below is a "Get in touch" email address, which is clickable and opens in the user's emails, and the copyright section.

#### Home Page
The Home page is for when users aren't logged in. There's the website title in a green div, and below is some information about the website with an image of a wedding couple.

#### Create Account
The create account page features a form with users to enter the Username and Password they want to use on their account. There's a Confirm Password field, and fields for the couples names and their wedding date. Upon submission, the following checks are made:
* Does the username entered match any others on the database
* Do the Password and Confirm Password fields match

The User is then created and saved to the database. If there are any issues with the two checks, an appropriate message is flashed to the user. There is also a button on this page to take users to the Log In page, if they already have an account.

#### Log In
The Log In page has a similar form to the Create Account, but only features the Username and Password field. If the Username and Password does not match the database, an error message will be flashed to the user. There's also a button to take users to the Create an Account page, if they don't have one already.

#### Dashboard
Once the user has created and account or logged in, they can access their Dashboard. At the top of the screen there's a green div with their name and their partners name, as well as a countdown to their wedding date. If the wedding date is today, or in the past, the message will change. Beneath this is a button that gives the effect of throwing confetti on screen. This is a feature that I found on Github, made by [catdad (Kiril Vatev)](https://github.com/catdad) called [canvas-confetti](https://github.com/catdad/canvas-confetti). I was able to add this to my website by adding script tag straight to my Dashboard HTML page, and have just slightly adjusted the confetti size, starting point and spread for different screen sizes.

The next green div contains the next set of tasks for the user in the Checklist. The next chronological task to be completed will be displayed, with it's date above. However, if there are other Checklist Items that also have this date, these will be displayed also. For each time the loop reaches a Checklist item with a different date, these are not displayed on this page. If no Checklist Items have been created, a message will display to let the user know, with a link to the Add Checklist Item page.

The final section of the Dashboard has links to the four key pages: Checklist, Payments, Guests and Table Plan. Underneath is two links, one to edit the Users profile information, and the other to Log out. If the user chooses to Log out, the User is removed from the session, and directed back to Log In page.

#### Edit Profile
The Edit Profile page has similar form input elements to the Sign Up page. The Username is greyed out and disabled using the Materialize class "disable". Upon submission, the following is checked:

* Whether the User trying to edit this User Profile is the User that created it. If not the user is redirected to the Log In page.
* If the user has not entered anything into the Old, New or Confirm password boxes, the two name inputs and wedding date input overwrite the current values.
* If the user has entered anything into the Old, New or Confirm password boxes, the following checks are completed:
    * Does the value entered into the Old Password field match the Users current password?
    * Is the value entered into the Old Password field different to the value entered into the New Password field?
    * Does the New Password field match the Confirm New Password field?
    * If the answer to these three above is True, the values of all the form fields will be commit to the database. If not, an appropriate error message is displayed. 
    
This page also features a back button, that takes the User back to the Dashboard.

#### Checklist
The Checklist page shows the user any Checklist Items they have created. Each Checklist Item is grouped with others with the same due date. The title is displayed in bold on the left, with a line divider and then the notes about that Checklist Item. On the far right there's a pencil, that will take the User to that Checklist Item's edit page, and a cross to delete that Checklist Item. I've added a Modal for defensive programming that asks the User if they're sure they want this Item to to be permanently deleted. At the bottom of the list is a button with a link to the Add Checklist Item page. This page also features a back button, that takes the User back to the Dashboard.

#### Add Checklist / Payment Item
When this page is accessed from the Payments page, the title and input labels change from "Checklist Item" to "Payment Item". This page is a simple form, containing input fields for the Checklist/Payment Item's name, notes, due date, and a checkbox for if this item is a payment. Upon submission, the Checklist/Payment Item's name is checked against the database. If that Checklist/Payment Item's name already exists, an error message will flash and the Item will not be saved. If the name is unique, this Item is added to the database, and the User is routed back to the Checklist/Payment page, dependent on where they came from. If the Payment checkbox is ticked, the Item will display on both the Checklist and Payments page. This page also features a back button, that takes the User back to the Checklist or Payment page. If an error occurs when submitting the form, the User is routed back to the Edit page they were on, and the back button will take them back to either the Payment page or Checklist page, dependent on where they came from. 

#### Edit Checklist / Payment Item
This page works very similarly to the Add Checklist/Payment page, except that the values of the Item are already added into the input fields. Upon submission, a check is made to see whether the User trying to edit this Checklist or Payment Item is the User that created it. If not, the user is redirected to the Log In page. If the User editing is the User who created the Item, the Item name is checked against the database. If that name already exists, an error message will flash and the Item will not be saved. The user is then routed back to the Edit page they were on. If the name is unique, the input fields overwrite the current values, regardless of whether they've been changed. This page also features a back button, that takes the User back to the Checklist or Payment page dependent on where they came from. 

#### Payments
The Payments page layout is identical to the Checklist page, except that when looping through each Checklist Item it checks to see if the Item has the Payment tickbox ticked. If this is true, the Checklist Item is displayed. If not, it is not displayed. This page also features a back button, that takes the User back to the Dashboard.

#### Guests
The Guests page is an alphabetised list of all the guests that have been created. Like the Checklist page, these also have the guest name in bold on the left, any notes about the guest in the centre, and a pencil and cross for editing or deleting each guest. I've added defensive programming here by adding a Materialize Modal to ask the User if they're sure they want to delete this guest. At the bottom, there is a button that takes the User to the Add Guest page, and underneath is a back button to the Dashboard.

#### Add Guest
The Add Guest page is a simple form with input boxes for the Guest name and notes. Underneath is a section for selecting the guests table name. If no tables have been created, a message will display with a link to the "Add Table" page. If there are Tables in the database, the default value will be "None", but a dropdown is available for users to select which table name they want to assign this user to. Once clicked, I used Javascript to display the option the User selects as a string in a p element with a border. The input itself is hidden from the User so they cannot freetype into this field. Upon submission, the Guest is committed to the database. This page also features a back button, that takes the User back to the Guests page.

#### Edit Guest
Edit guest is almost the same as the Add Guest page, except the values have been added to the input fields. If a Table Name has been assigned, this will show in the green bordered paragraph element, as if the user has just clicked on it. If no table is assigned the User will only be able to see the "Choose Table" trigger. Upon submission, a check is made to see whether the User trying to edit this Guest is the User that created it. If so, the Guest is committed to the database, and if not the user is redirected to the Log In page. This page also features a back button, that takes the User back to the Guests page.

#### Table Plan
The Table Plan page loops through each table in the Table Name list, and then checks whether each Guest has a foreign key that matches that Table Name. Each Table Name has it's own light green box, and underneath the Title of the Table Name in bold are two icons for editing and deleting the Table Name. I've added defensive programming here by adding a Materialize Modal to ask the User if they're sure they want to delete this table. Below is each iteration of the Guests that are assigned to that Table Name, with an "Edit" button that takes users to the "Edit Guest" page for that guest.

Once all Table Names are displaying, there is another light green box containing any guests that don't have a Table Name assigned to them. Then, a final light green box with "Add New Table" inside, that users can click to go to the "Add Table" box. This page also features a back button, that takes the User back to the Dashboard.

#### Add Table
The Add Table page is a simple form with one input field for the Table Name. Upon submission, the Table is added to the database. This page also features a back button, that takes the User back to the Table Plan page.

#### Edit Table
This form is the same as the Add Table form except the value of the Table Name is already in the input field. Upon submission, a check is made to see whether the User trying to edit this Table is the User that created it. If so, the Table is committed to the database, and if not the user is redirected to the Log In page. This page also features a back button, that takes the User back to the Table Plan page.






## Design
#### Colours
#### Typography
#### Imagery
#### Styling
#### Backgrounds


## Responsive Design
#### 4k Screen
#### Large Laptop
#### Laptop
#### Tablet
#### Mobile
#### Small Mobile

## Fixed Bugs

## Unfixed Bugs

## Deployment

## Digital Testing
#### Spell Check
#### Validators
#### Lighthouse

## Credits
#### Research
#### Frameworks, Libraries and Programs
#### Images
#### Media

## Acknowledgements
