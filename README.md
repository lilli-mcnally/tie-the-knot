# Tie the Knot Wedding Planner
*Tie the Knot is a website designed to assist users who are planning their wedding and need to keep track of their To Do list, their Payments and their Guest List.*
![Mockup](/tietheknot/static/images/readme/mockup.PNG)

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
| Users able to see what table their guests are sat on   |   4    |  3   | :heavy_check_mark:     |

Table numbers will be added to the Guest List page. However, I would like to add a page specifically for showing the table numbers and the guests assigned to them on individual cards. In future updates I would also like to add the budget feature, so users can keep track of payments and budgets in one place.

## Structure

I started drafting my ideas for structure on [Figma](https://www.figma.com/). I created my wireframes next on [Balsamiq](https://balsamiq.com/), and then moved back to [Figma](https://www.figma.com/) to create my prototype.

I've chosen to have a home page that promotes the features of the website. The user will be prompted to log in or sign up, and the pages for these will come straight from the home page.

Once logged in, the user will have their own dashboard. From here they can see their Checklist, from which they can add, edit and delete Checklist Items. They can also access their Guest list from the Dashboard, and add, edit or delete their Guests. The last page will filter any Items in the Checklist with the "Payment" field ticked, so users can keep track of their payments.

#### Structure Plan
* [Structure Plan](/tietheknot/static/images/readme/structure-plan.PNG)

#### Wireframes
* [Home page](/tietheknot/static/images/readme/home-page-wireframe.PNG)
* [Sign Up page](/tietheknot/static/images/readme/sign-up-page-wireframe.PNG)
* [Log In page](/tietheknot/static/images/readme/log-in-page-wireframe.PNG)
* [Dashboard page](/tietheknot/static/images/readme/dashboard-page-wireframe.PNG)
* [Checklist page](/tietheknot/static/images/readme/checklist-page-wireframe.PNG)
* [Add Checklist page](/tietheknot/static/images/readme/add-checklist-item-page-wireframe.PNG)
* [Edit Checklist page](/tietheknot/static/images/readme/edit-checklist-item-page-wireframe.PNG)
* [Guest page](/tietheknot/static/images/readme/guest-page-wireframe.png)
* [Add Guest page](/tietheknot/static/images/readme/add-guest-page-wireframe.PNG)
* [Edit Guest page](/tietheknot/static/images/readme/edit-guest-page-wireframe.PNG)
* [Payments page](/tietheknot/static/images/readme/payments-page-wireframe.PNG)

#### Prototype
* [Checklist page](/tietheknot/static/images/readme/checklist-page-prototype.PNG)


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
For this website, I decided to go for mint and sage green, and a coral-pink, as these are all very popular wedding theme colours. The contrast between the green and pink meant I could use pink for Flash messages and other import information, without being as alerting as a red colour. The pink was also a great hover colour for my footer elements, as the change was noticeable but doesn't clash with the sage. 

#### Typography
The whole website uses the font "Spectral", provided by [Google Fonts](https://fonts.google.com/). I liked this font because it has that slightly fancy feel with it being a Serif font. I've used various sizes of font across the site, with the heading of each page is the largest font. Flash messages and Navigation wording is slightly smaller but still matches it's higher importance. I've also used some subheadings with H5 elements, for which the fonts are a little larger than the remaining list, paragraph and anchor element wording. I used italics for information below some of the input fields. I also made Checklist Item names, Guest names and Table names all bold.

The logo has the font "Nickainley" by [Canva](https://www.canva.com/). I chose this font because I like the caligraphy style for the logo.

#### Imagery
The only two images on the website are the logo and an image on the home page. I designed the Logo myself using [Canva](https://www.canva.com/), using a rope knot image from the Canva website. This was originally by [OpenClipart-Vectors](https://pixabay.com/users/openclipart-vectors-30363/) from [Pixabay](https://pixabay.com/). The Home page image was from [Unsplash](https://unsplash.com/), taken by [Victoria Priessnitz](https://unsplash.com/photos/woman-in-white-wedding-dress-standing-on-green-grass-field-during-daytime-ZLkQPMy4r5o). I chose this image because it's focus is on the couple, which fits with the website focusing on what planning tools a couple would need.

#### Styling
I added border radius across the website, so nearly all coloured divs have the same border radius for their scale. I used different divs to split the Dashboard into sections: The names and countdown at the top, the What's Next section just below, and then internal links at the bottom. I also used this design on the Checklist, Payment, Guest and Table Plan pages. The iterations are inside lighter green divs, with an "Add" button at the bottom / end of each list, clearly spaced from the looped list. I included a pencil and a cross in each loop, to clearly define which object a User will be editing or deleting.

The forms have a clear difference in styling, having a green border but white background. Flash messages are consistently at the top, under the title, and always have a pink background to grab the Users attention. The Modals for deleting Guests, Checklist Items, Payments and Tables also have pink buttons to catch the User's attention in case clicked the cross was accidental.

#### Backgrounds
The website consistently features a white background. Most div's with information have green backgrounds, with important information having pink backgrounds. I chose a the dark sage green for the background of my footer so the definition between the main page and footer was clear. I also think the contrasting colours of dark green and white look really nice next to each other.


## Responsive Design

#### 4k Screen
For the largest screen sizes, I changed all paragraphs and links to be 20px, and for H5 elements to be 26px. All the content on the webpage takes up 8/12 screen with the use of the [Materialize](https://materializecss.com/) grid. The Dashboard is spread evenly, and the Checklist Items, Payments and Guests are all evenly spaced. The Table Plan grid is also well spaced with each row being three Tables wide.

#### Large Laptop
On Large Laptop, the paragraph and anchor elements are at 16px, and the Table Plan is two Tables per row. The Dashboard, Guest, Payment and Checklist pages look mainly the same. The Home page image and it's information div adjust very well with each other with the use of percentages in the width and margins.

#### Laptop
At 1400px, all divs across the website expand slightly to take up 11/12 of the width of the screen, again using the [Materialize](https://materializecss.com/) grid. I've also used the grid feature to adjust the size of the forms, which are a bit smaller than the rest of the website divs.

#### Tablet
I've used the [Materialize](https://materializecss.com/) Navigation element to add a hamburger menu for tablet and smaller screens. When clicked, a side Navigation element with a list of internal links. The list includes all six that are at the top when the screen is larger, including the Log Out button at the bottom of the list. I also chose to make this list background pink to give a clear definition for the User between the Navigation list and the page sitting behind it. The four internal links on the Dashboard are now stacked in twos. In the What's next section the Checklist Item name and notes are on top of each other as well. This format is the same on the Checklist, Payment and Guest pages. The Table Plan grid is also one Table per row. At 849px and below, the forms across the whole site change size to be as wide as the Navigation and Headings, to give Users maximum space for completing these forms.

#### Mobile
I adjusted the H5 font size tp 20px for Mobile and smaller devices. I also changed the box that shows the User which Table they've selected for a guest to be assigned to. This box now sits underneath the Choose Table dropdown, to give plenty of space for longer titled Tables. The Footer internal links have now changed from horizontal to a vertical list.

#### Small Mobile
For Smallest Mobile devices, I've adjusted the Logo to be a bit smaller, and the height of the Navigation to fit around it's new size. I've also amended the width of the side Navigation so it only takes up half the screen. I've amended H1 elements to take up a smaller portion of the screen, and the Dashboard internal links now stack one on top of the other.

## Fixed Bugs

#### Grouping Items by Date
I wanted to group Checklist Items and Payments that have the same date on the Checklist and Payment pages. I created a Jinja Template to check if the current Checklist Item had the same date as the one previous to it. However, I kept getting a Jinja template error because the first Checklist Item has no previous. I fixed this by creating a seperate template for the first iteration, and then running an if statement to display the next date, if it doesn't match the previous. The the second template would loop through until there are no more Checklist Items. I did try to remove the second template, but without having the loop.first, the Jinja Template throws an error due to there being no previous iteration.

After I added this, I noticed some dates were coming up twice, and I realised it was because the list was being iterated by index. I went back to my routes.py file and amended the Checklist Items to be called as a list but ordered by the the Checklist Items dates.

#### Duplicate Username / Checklist Item name
My User and Checklist models both have a field that must be unique. I wanted to check whether the Username / Checklist Item name was taken, and show an error message if it was. I spoke to the Code Institute Tutor Support team who worked with me to create a filter for any Checklist Items names that matched what the user had input into the form. I then added an If statement to check if there was any matches, and implemented Flash into my project as the error message. I applied this to the Username field on the Register form as well.

Once I had the Flash messages working, I was able to use this feature for other errors, such as the Log In credentials being incorrect, and a "Registration Successful" message once a User has created their account.

#### Modals
When opening the Modals, I noticed the screen behind the Modal would jump by one or two pixels. I looked into the issue on the internet and found a really [helpful article]((https://stackoverflow.com/questions/34964542/materialize-modal-shifts-background-and-causes-page-jumping-right)) on [Stack Overflow](https://stackoverflow.com/). I added the below which fixed the issue.

`body {
    overflow: auto !important;
}`

#### Removing the empty Unassigned Guests from Table Plan
I wanted created the ability for Users to assign their Guests to a Table Number, and this would then be reflected in their Table Plan. I also knew that Users would need to have access to a list of Guests that don't have a Table assigned to them. I added an extra div for Unassigned Guests, but decided I didn't want this to be visible if there was nothing in it.

I added a function to my Javascript to change the whole green "Display" styling to "None", if the div inside it is equal to `null` (meaning there are no Unassigned Guests). However, I noticed there was a recurring error in the Console of all my other pages, because there was no `innerHTML` of an element that doesn't exist. So, I researched how only run a function if the User is looking at the right page. I found [this article](https://stackoverflow.com/questions/4597050/how-to-check-if-the-url-contains-a-given-string) on [Stack Overflow](https://stackoverflow.com/). I added the below to my Javascript function to check the page URL, which fixed this issue.

`if (window.location.toString().includes("table_plan"))`

#### Hyphens
On my Table Plan, I tried added a few very long names to make sure the formatting was correct for these Guests. I noticed that as I reduced screen size, although the word would break on to the next line, it wouldn't add a hyphen to show it was still one word. I found a [useful page](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens) on [MDN Web Docs](https://developer.mozilla.org/en-US/). I added `hyphens: auto;` to all elements with the class of `green-container` so this would apply to Checkist Items, Payments and Table Names as well.

## Unfixed Bugs

#### Autofill Colour
I noticed when filling in the Log In form, my Google Chrome was suggesting Log In details, but once I clicked them the input field colour would change to blue. I used Developer Tools to try to find where the blue was coming from, and I tried to override it using:

`input:autofill,`
<br>
`input:-webkit-autofill {`
<br>
&emsp; &emsp; `background-color: #dcece7 !important;`
<br>
`}`

However this made no difference. I finally found an [article](https://developer.mozilla.org/en-US/docs/Web/CSS/:autofill) on [MDN Web Docs](https://developer.mozilla.org/en-US/) which states:

> Note: The user agent style sheets of many browsers use !important in their :-webkit-autofill style declarations, making them non-overridable by webpages without resorting to JavaScript hacks ... This means that you cannot set the background-color, background-image, or color in your own rules.

Unfortunately this means I cannot fix this bug, but on the luckily the blue colour does go well with my website anyway.

#### Nav Dropdowns
I had a similar issue with the Materialize Navigation Dropdown menus. I would like it if the dropdown content would render underneath the dropdown trigger. However, the [Materialize](https://materializecss.com/) dropdown is set up to automatically add the location of this dropdown content to inline styling using Javascript. I tried to override this by changing the `top` but writing this in Javascript didn't affect the inline styling Materialize had added.

## Deployment
I managed to deploy the website without any issues, and all my links worked perfectly. I used the following steps to achieve this:

1. I created an account on Heroku for deploying the site, and ElephantSQL to host my database.
2. I created the database on ElephantSQL using the "Create new instance", giving the project a name and selecting my plan and location.
3. Then I created a requirements.txt file, and a Procfile, both of which are needed to deploy on Heroku.
4. I used the "Create new app" button on Heroku and gave my project a name.
5. I copied the URL from my ElephantSQL project and applied it as a Config Var under the Settings tab on Heroku.
6. I added the rest of the variables from my env.py file to my Config Vars section on Heroku.
7. I changed to the Deploy tab on Heroku, and clicked on Connect to Github.
8. I enabled automatic deploys and deployed from the main branch.
9. I built my database by using the Run Console button to open the terminal, and typing `from tietheknot import db`, and then `db.create_all()`
10. My project successfuly deployed, and I checked this was working using the "Open App" button on Heroku.

## Manual Testing
I've completed all my Manual Testing in an external file:
* [Manual Testing](/test.md)

## Digital Testing
### Validators

* [W3C HTML Markup Validation Service](https://validator.w3.org/)
    * Various errors when running HTML Validation, all caused by Jinja Templating
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    * Passed with no errors
* [JSHint](https://jshint.com/)
    * Validator returned with `Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (chosenTable)`
    * All missing semi-colons added
    * All unnecessary semi-colons removed
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * First I used [Black](https://black.readthedocs.io/en/stable/getting_started.html) to format my Python files
    * Then I ran the CI Python Linter:
        * On the `routes.py` file, however there are some lines that still exceed the maximum 79 characters
        * The `models.py` file has no errors
        * the `__init__.py` file has an error due to the routes being imported at the bottom of the file

### Lighthouse
#### Add Checklist Desktop
![Add Checklist Desktop](/tietheknot/static/images/readme/lighthouse/add-checklist-desktop.png)

#### Add Checklist Mobile
![Add Checklist Mobile](/tietheknot/static/images/readme/lighthouse/add-checklist-mobile.png)

#### Add Guest Desktop
![Add Guest Desktop](/tietheknot/static/images/readme/lighthouse/add-guest-desktop.png)

#### Add Guest Mobile
![Add Guest Mobile](/tietheknot/static/images/readme/lighthouse/add-guest-mobile.png)

#### Add Payments Desktop
![Add Payments Desktop](/tietheknot/static/images/readme/lighthouse/add-payments-desktop.png)

#### Add Payments Mobile
![Add Payments Mobile](/tietheknot/static/images/readme/lighthouse/add-payments-mobile.png)

#### Add Table Desktop
![Add Table Desktop](/tietheknot/static/images/readme/lighthouse/add-table-desktop.png)

#### Add Table Mobile
![Add Table Mobile](/tietheknot/static/images/readme/lighthouse/add-table-mobile.png)

#### Checklist Desktop
![Checklist Desktop](/tietheknot/static/images/readme/lighthouse/checklist-desktop.png)

#### Checklist Mobile
![Checklist Mobile](/tietheknot/static/images/readme/lighthouse/checklist-mobile.png)

#### Dashboard Desktop
![Dashboard Desktop](/tietheknot/static/images/readme/lighthouse/dashboard-desktop.png)

#### Dashboard Mobile
![Dashboard Mobile](/tietheknot/static/images/readme/lighthouse/dashboard-mobile.png)

#### Edit Checklist Desktop
![Edit Checklist Desktop](/tietheknot/static/images/readme/lighthouse/edit-checklist-desktop.png)

#### Edit Checklist Mobile
![Edit Checklist Mobile](/tietheknot/static/images/readme/lighthouse/edit-checklist-mobile.png)

#### Edit Guest Desktop
![Edit Guest Desktop](/tietheknot/static/images/readme/lighthouse/edit-guest-desktop.png)

#### Edit Guest Mobile
![Edit Guest Mobile](/tietheknot/static/images/readme/lighthouse/edit-guest-mobile.png)

#### Edit Payments Desktop
![Edit Payments Desktop](/tietheknot/static/images/readme/lighthouse/edit-payments-desktop.png)

#### Edit Payments Mobile
![Edit Payments Mobile](/tietheknot/static/images/readme/lighthouse/edit-payments-mobile.png)

#### Edit Profile Desktop
![Edit Profile Desktop](/tietheknot/static/images/readme/lighthouse/edit-profile-desktop.png)

#### Edit Profile Mobile
![Edit Profile Mobile](/tietheknot/static/images/readme/lighthouse/edit-profile-mobile.png)

#### Edit Table Desktop
![Edit Table Desktop](/tietheknot/static/images/readme/lighthouse/edit-table-desktop.png)

#### Edit Table Mobile
![Edit Table Mobile](/tietheknot/static/images/readme/lighthouse/edit-table-mobile.png)

#### Guests Desktop
![Guests Desktop](/tietheknot/static/images/readme/lighthouse/guests-desktop.png)

#### Guests Mobile
![Guests Mobile](/tietheknot/static/images/readme/lighthouse/guests-mobile.png)

#### Home Desktop
![Home Desktop](/tietheknot/static/images/readme/lighthouse/home-desktop.png)

#### Home Mobile
![Home Mobile](/tietheknot/static/images/readme/lighthouse/home-mobile.png)

#### Log In Desktop
![Log In Desktop](/tietheknot/static/images/readme/lighthouse/log-in-desktop.png)

#### Log In Mobile
![Log In Mobile](/tietheknot/static/images/readme/lighthouse/log-in-mobile.png)

#### Payments Desktop
![Payments Desktop](/tietheknot/static/images/readme/lighthouse/payments-desktop.png)

#### Payments Mobile
![Payments Mobile](/tietheknot/static/images/readme/lighthouse/payments-mobile.png)

#### Register Desktop
![Register Desktop](/tietheknot/static/images/readme/lighthouse/register-desktop.png)

#### Register Mobile
![Register Mobile](/tietheknot/static/images/readme/lighthouse/register-mobile.png)

#### Table Plan Desktop
![Table Plan Desktop](/tietheknot/static/images/readme/lighthouse/table-plan-desktop.png)

#### Table Plan Mobile
![Table Plan Mobile](/tietheknot/static/images/readme/lighthouse/table-plan-mobile.png)


## Credits
* [Canva](https://www.canva.com/)
    * [Logo rope image](https://pixabay.com/users/openclipart-vectors-30363/)
        * [OpenClipart-Vectors - Pixabay](https://pixabay.com/users/openclipart-vectors-30363/)
    * Logo font – "Nickainley" by [Canva](https://www.canva.com/)
* [Figma](https://www.figma.com/)
    * Structure plan
    * Prototype
* [Balsamic](https://balsamiq.com/)
    * Wireframes
* [Materialize](https://materializecss.com/)
    * Grid styling
    * Modals
    * Navbar for all sized screens
    * Buttons
    * Waves classes on submit buttons
    * Checkbox
* [Font Awesome](https://fontawesome.com/)
    * Pencil and cross icons
    * Social media icons
* [Google Fonts](https://fonts.google.com/)
    * Spectral
* [Favicon Converter](https://favicon.io/favicon-converter/)
    * Knot Favicon
* [MDN Wed Docs](https://developer.mozilla.org/en-US/)
    * [Hyphens Auto](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens )
* [Stack Overflow](https://stackoverflow.com/)
    * [Check a URL for a string](https://stackoverflow.com/questions/4597050/how-to-check-if-the-url-contains-a-given-string)
    * [Check if a User is in session](https://stackoverflow.com/questions/15591620/how-to-retrieve-session-data-with-flask)
    * [How to add Regex spaces](https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces)
    * [Used to add four spaces (tab) to readme](https://stackoverflow.com/questions/66828242/how-to-add-tab-spaces-in-git-readme-between-two-sentences )
* [Python String From Time](https://strftime.org/ )
    * Used to format dates on Checklist and Payments page
* [Youtube - Sandeep Sudhakaran](https://www.youtube.com/watch?v=7EeAZx78P2U)
    * Setting up my User Credentials
* [Confetti](Confetti: https://www.npmjs.com/package/canvas-confetti)
    * Added to my Dashboard
* [Bridebook](https://bridebook.com/uk/home)
    * I got the idea for the confetti from the Bridebook home page
* [W3 Schools](https://www.w3schools.com/html/html_emojis.asp)
    * Used to render Emoji's on the page
* [Unsplash - Victoria Priessnitz](https://unsplash.com/photos/woman-in-white-wedding-dress-standing-on-green-grass-field-during-daytime-ZLkQPMy4r5o)
    * Home Page image
* [ElephantSQL](https://www.elephantsql.com/)
* [Heroku](https://heroku.com/)
* [Am I Responsive](https://ui.dev/amiresponsive)

## Acknowledgements
* The fantastic Student Support Team at Code Institute
* My City of Bristol College Tutors