# Tie the Knot Testing Document

## Functionality

### Add Checklist Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Cursor: text                                                    |  Pass  |
| Checklist Item Description input field | Cursor: text                                                    |    Pass    |
| Checklist Item Due Date input field    | Cursor: text                                                    |   Fail     |
| Payment Checkbox                       | Cursor: pointer                                                 |     Pass   |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |    Pass    |
| Back button                            | Cursor: pointer, border turns green                         |   Pass     |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Able to type in input field                                     |      Pass  |
| Checklist Item Description input field | Able to type in input field                                     |    Pass    |
| Checklist Item Due Date input field    | Able to type in input field                                     |  Pass      |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |   Pass     |
| Submit button                          | Form is submitted                                               |   Pass     |
| Back button                            | User redirected back to Checklist                               |   Pass     |

### Add Payment Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Cursor: text                                                    |   Pass     |
| Payment Item Description input field   | Cursor: text                                                    |   Pass     |
| Payment Item Due Date input field      | Cursor: text                                                    |    Fail    |
| Payment Checkbox                       | Cursor: pointer                                                 |   Pass     |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |    Pass    |
| Back button                            | Cursor: pointer, border turns green                         |     Pass   |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Able to type in input field                                     |    Pass    |
| Payment Item Description input field   | Able to type in input field                                     |    Pass    |
| Payment Item Due Date input field      | Able to type in input field                                     |    Pass    |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |   Pass     |
| Submit button                          | Form is submitted                                               |   Pass     |
| Back button                            | User redirected back to Payments                                |    Pass    |

### Add Guest
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Cursor: text                                                    |     Pass   |
| Guest Notes input field                | Cursor: text                                                    |    Pass    |
| Guest Table Dropdown Trigger           | Cursor: pointer                                                 |   Pass     |
| Guest Table Dropdown Option (`None`)   | Cursor: pointer                                                 |    Pass    |
| Guest Table Dropdown Option (not `None`) | Cursor: pointer                                               |   Pass     |
| Click here to create a table           | Cursor: pointer, text colour to change to green                 |   Pass     |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |   Pass     |
| Back button                            | Cursor: pointer, border turns green                         |   Pass     |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Able to type in input field                                     |   Pass     |
| Guest Notes input field                | Able to type in input field                                     |   Pass     |
| Guest Table Dropdown Trigger           | Opens dropdown options list                                     |   Pass     |
| Guest Table Dropdown Option (`None`)   | Selects "None" as dropdown option                               |   Pass     |
| Guest Table Dropdown Option (not `None`) | Selects the option, displays the option in a div next to the trigger |   Pass     |
| Click here to create a table           | User redirected to Add Table page                               |   Pass     |
| Submit button                          | Form is submitted                                               |     Pass   |
| Back button                            | User redirected back to Guests                                  |   Pass     |


### Add Table
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |   Pass     |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |    Pass    |
| Back button                            | Cursor: pointer, border turns green                         |   Pass     |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |   Pass     |
| Submit button                          | Form is submitted                                               |   Pass     |
| Back button                            | User redirected back to Checklist                               |   Pass     |


### Base (Nav and Footer)

##### Logged In
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Cursor: pointer                                   |  Pass      |
| Nav - Things to do                   | Cursor: pointer, background colour turns pink     |  Pass      |
| Nav - Checklist (Things to do)       | Cursor: pointer, background colour turns grey     |   Pass     |
| Nav - Payments (Things to do)        | Cursor: pointer, background colour turns grey     |   Pass     |
| Nav - Guest List                     | Cursor: pointer, background colour turns pink     |   Pass     |
| Nav - Guests (Guest List)            | Cursor: pointer, background colour turns grey     |    Pass    |
| Nav - Table Plan (Guest List)        | Cursor: pointer, background colour turns grey     |   Pass     |
| Nav - User's Name                    | Cursor: pointer, background colour turns pink     |    Pass    |
| Nav - Dashboard (User's Name)        | Cursor: pointer, background colour turns grey     |    Pass    |
| Nav - Log Out (User's Name)          | Cursor: pointer, background colour turns grey     |   Pass     |
| Footer - Dashboard                   | Cursor: pointer, background colour turns pink, underlined |    Pass    |
| Footer - Checklist                   | Cursor: pointer, background colour turns pink, underlined |    Pass    |
| Footer - Guests                      | Cursor: pointer, background colour turns pink, underlined |    Pass    |
| Footer - Table Plan                  | Cursor: pointer, background colour turns pink, underlined |    Pass    |
| Footer - Payments                    | Cursor: pointer, background colour turns pink, underlined |    Pass    |
| Footer - Facebook icon               | Cursor: pointer, background colour turns pink      |    Pass    |
| Footer - Instagram icon              | Cursor: pointer, background colour turns pink      |   Pass     |
| Footer - Twitter icon                | Cursor: pointer, background colour turns pink      |    Pass    |
| Footer - Youtube icon                | Cursor: pointer, background colour turns pink      |    Pass    |
| Footer - Enquiries email address     | Cursor: pointer, background colour turns pink, underlined|     Pass   |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Redirect to Dashboard                             |   Pass     |
| Nav - Things to do                   | Opens Things to do dropdown                       |  Pass      |
| Nav - Checklist (Things to do)       | Redirect to Checklist                             |   Pass     |
| Nav - Payments (Things to do)        | Redirect to Payments                              |   Pass     |
| Nav - Guest List                     | Opens Guest List dropdown                         |    Pass    |
| Nav - Guests (Guest List)            | Redirect to Guests                                |    Pass    |
| Nav - Table Plan (Guest List)        | Redirect to Table Plan                            |    Pass    |
| Nav - User's Name                    | Opens User's Name dropdown                        |    Pass    |
| Nav - Dashboard (User's Name)        | Redirect to Dashboard                             |    Pass    |
| Nav - Log Out (User's Name)          | Removes User from session, redirect to Home       |     Pass   |
| Footer - Dashboard                   | Redirect to Dashboard                             |    Pass    |
| Footer - Checklist                   | Redirect to Checklist                             |   Pass     |
| Footer - Guests                      | Redirect to Guests                                |    Pass    |
| Footer - Table Plan                  | Redirect to Table Plan                            |   Pass     |
| Footer - Payments                    | Redirect to Payments                              |    Pass    |
| Footer - Facebook icon               | Redirect to Facebook in a new tab                 |    Pass    |
| Footer - Instagram icon              | Redirect to Instagram in a new tab                |   Pass     |
| Footer - Twitter icon                | Redirect to Twitter in a new tab                  |    Pass    |
| Footer - Youtube icon                | Redirect to Youtube  in a new tab                 |   Pass     |
| Footer - Enquiries email address     | Redirect to User's mailbox with enquiries email in a new email box |   Pass    |

##### Logged Out
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Cursor: pointer                                   |   Pass     |
| Nav - Log In                         | Cursor: pointer, background colour turns pink     |   Pass     |
| Nav - Register                       | Cursor: pointer, background colour turns pink     |   Pass    |
| Footer - Log In                      | Cursor: pointer, background colour turns pink, underlined |    Pass   |
| Footer - Register                    | Cursor: pointer, background colour turns pink, underlined |   Pass     |
| Footer - Facebook icon               | Cursor: pointer, background colour turns pink |    Pass    |
| Footer - Instagram icon              | Cursor: pointer, background colour turns pink |    Pass    |
| Footer - Twitter icon                | Cursor: pointer, background colour turns pink |    Pass    |
| Footer - Youtube icon                | Cursor: pointer, background colour turns pink |     Pass   |
| Footer - Enquiries email address     | Cursor: pointer, background colour turns pink, underlined |     Pass   |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Redirect to Home                                  |    Pass    |
| Nav - Log In                         | Redirect to Log In                                |    Pass    |
| Nav - Register                       | Redirect to Register                              |    Pass    |
| Footer - Log In                      | Redirect to Log In                                |    Pass    |
| Footer - Register                    | Redirect to Register                              |     Pass   |
| Footer - Facebook icon               | Redirect to Facebook                              |   Pass     |
| Footer - Instagram icon              | Redirect to Instagram                             |     Pass   |
| Footer - Twitter icon                | Redirect to Twitter                               |    Pass    |
| Footer - Youtube icon                | Redirect to Youtube                               |     Pass   |
| Footer - Enquiries email address     | Redirect to User's mailbox with enquiries email in a new email box |   Pass     |


### Checklist
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Checklist Item pencil          | Cursor: pointer, background colour turns pink          | Pass       |
| First Checklist Item cross           | Cursor: pointer, background colour turns pink          |  Pass      |
| First Checklist Item modal cancel    | Cursor: pointer, border turns pink                     |  Pass      |
| First Checklist Item modal confirm   | Cursor: pointer, border turns pink                     |   Pass     |
| Second Checklist Item pencil         | Cursor: pointer, background colour turns pink          |   Pass     |
| Second Checklist Item cross          | Cursor: pointer, background colour turns pink          |    Pass    |
| Second Checklist Item modal cancel   | Cursor: pointer, border turns pink                     |    Pass    |
| Second Checklist Item modal confirm  | Cursor: pointer, border turns pink                     |   Pass     |
| Add New Checklist Item button        | Cursor: pointer, border turns green                    |   Pass     |
| Back button                          | Cursor: pointer, border turns green                |   Pass     |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Checklist Item pencil          | Open Edit Checklist Item page for this Item            |   Pass     |
| First Checklist Item cross           | Open Modal to delete this Checklist Item               |   Pass     |
| First Checklist Item modal cancel    | Close modal, return to Checklist page                  |  Pass      |
| First Checklist Item modal confirm   | Delete this Checklist Item, redirect to Checklist page |  Pass      |
| Second Checklist Item pencil         | Open Edit Checklist Item page for this Item            |  Pass      |
| Second Checklist Item cross          | Open Modal to delete this Checklist Item               |  Pass      |
| Second Checklist Item modal cancel   | Close modal, return to Checklist page                  |  Pass      |
| Second Checklist Item modal confirm  | Delete this Checklist Item, redirect to Checklist page |  Pass      |
| Add New Checklist Item button        | Redirect to Add Checklist Item                         |  Pass      |
| Back button                          | Redirect to Dashboard                                  |   Pass     |

### Dashboard
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Confetti Click Me                    | Cursor: pointer                                   |    Pass    |
| Checklist                            | Cursor: pointer, border turns green               |     Pass   |
| Payments                             | Cursor: pointer, border turns green               |    Pass    |
| Guests                               | Cursor: pointer, border turns green               |    Pass    |
| Table Plan                           | Cursor: pointer, border turns green               |   Pass     |
| Edit Profile                         | Cursor: pointer, border turns pink                |    Pass    |
| Log Out                              | Cursor: pointer, border turns pink                |    Pass    |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Confetti Click Me                    | Confetti effect appears                           |    Pass    |
| Checklist                            | Redirect to Checklist                             |   Pass     |
| Payments                             | Redirect to Payments                              |    Pass    |
| Guests                               | Redirect to Guests                                |   Pass     |
| Table Plan                           | Redirect to Table Plan                            |    Pass    |
| Edit Profile                         | Redirect to Edit Profile                          |    Pass    |
| Log Out                              | Removes User from session, redirect to Home       |    Pass    |


### Edit Checklist Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Cursor: text                                                    |    Pass    |
| Checklist Item Description input field | Cursor: text                                                    |  Pass      |
| Checklist Item Due Date input field    | Cursor: text                                                    |    Fail    |
| Payment Checkbox                       | Cursor: pointer                                                 |    Pass    |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |  Pass      |
| Back button                            | Cursor: pointer, border turns green                         |     Pass   |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Able to type in input field                                     |   Pass     |
| Checklist Item Description input field | Able to type in input field                                     |   Pass     |
| Checklist Item Due Date input field    | Able to type in input field                                     |   Pass     |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |   Pass     |
| Submit button                          | Form is submitted                                               |    Pass    |
| Back button                            | User redirected back to Checklist                               |   Pass     |

### Edit Payment Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Cursor: text                                                    |   Pass     |
| Payment Item Description input field   | Cursor: text                                                    |   Pass     |
| Payment Item Due Date input field      | Cursor: text                                                    |  Fail      |
| Payment Checkbox                       | Cursor: pointer                                                 |    Pass    |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |   Pass     |
| Back button                            | Cursor: pointer, border turns green                         |   Pass     |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Able to type in input field                                     |   Pass     |
| Payment Item Description input field   | Able to type in input field                                     |   Pass     |
| Payment Item Due Date input field      | Able to type in input field                                     |   Pass     |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |   Pass     |
| Submit button                          | Form is submitted                                               |   Pass     |
| Back button                            | User redirected back to Payments                                |  Pass      |

### Edit Guests
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Cursor: text                                                    |   Pass     |
| Guest Notes input field                | Cursor: text                                                    |   Pass     |
| Guest Table Dropdown Trigger           | Cursor: pointer                                                 |   Pass     |
| Guest Table Dropdown Option (`None`)   | Cursor: pointer                                                 |  Pass      |
| Guest Table Dropdown Option (not `None`) | Cursor: pointer                                               |  Pass      |
| Click here to create a table           | Cursor: pointer, text colour to change to green                 |   Pass     |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |   Pass     |
| Back button                            | Cursor: pointer, border turns green                         |    Pass    |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Able to type in input field                                     |   Pass     |
| Guest Notes input field                | Able to type in input field                                     |   Pass     |
| Guest Table Dropdown Trigger           | Opens dropdown options list                                     |   Pass     |
| Guest Table Dropdown Option (`None`)   | Selects "None" as dropdown option                               |   Pass     |
| Guest Table Dropdown Option (not `None`) | Selects the option, displays the option in a div next to the trigger |  Pass      |
| Click here to create a table           | User redirected to Add Table page                               |   Pass     |
| Submit button                          | Form is submitted                                               |     Pass   |
| Back button                            | User redirected back to Guests                                  |    Pass    |


### Edit Profile
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Disabled Username field              | None                                              |    Pass    |
| Old Password input field             | Cursor: text                                      |  Pass      |
| New Password input field             | Cursor: text                                      |   Pass     |
| Confirm Password input field         | Cursor: text                                      |   Pass     |
| Your Name input field                | Cursor: text                                      |   Pass     |
| Your Partners Name input field       | Cursor: text                                      |    Pass    |
| Wedding Date input field             | Cursor: text                                      |    Fail    |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |   Pass     |
| Back button                          | Cursor: pointer, border turns green           |  Pass      |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Disabled Username field              | None                                              |   Pass     |
| Old Password input field             | Able to type in input field                       |  Pass      |
| New Password input field             | Able to type in input field                       |  Pass      |
| Confirm Password input field         | Able to type in input field                       |     Pass   |
| Your Name input field                | Able to type in input field                       |   Pass     |
| Your Partners Name input field       | Able to type in input field                       |    Pass    |
| Wedding Date input field             | Able to type in input field                       |   Pass     |
| Submit button                        | Form is submitted                                 |   Pass     |
| Back button                          | User redirected back to Dashboard                 |    Pass    |

### Edit Table
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |    Pass    |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |   Pass     |
| Back button                            | Cursor: pointer, border turns green                         |    Pass    |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |   Pass     |
| Submit button                          | Form is submitted                                               |    Pass    |
| Back button                            | User redirected back to Checklist                               |   Pass     |


### Guests
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Guest pencil                         | Cursor: pointer, background colour turns pink          |   Pass     |
| Guest cross                          | Cursor: pointer, background colour turns pink          |   Pass     |
| Guest modal cancel                   | Cursor: pointer, border turns pink                     |   Pass     |
| Guest modal confirm                  | Cursor: pointer, border turns pink                     |   Pass     |
| Add New Guest button                 | Cursor: pointer, border turns green                    |    Pass    |
| Back button                          | Cursor: pointer, border turns green                | Pass       |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Guest pencil                         | Open Edit Guest page for this Guest                    |   Pass     |
| Guest cross                          | Open Modal to delete this Guest                        |  Pass      |
| Guest modal cancel                   | Close modal, return to Guests page                     |    Pass    |
| Guest modal confirm                  | Delete this Guest, redirect to Guests page             |   Pass     |
| Add New Guest button                 | Redirect to Add Guest                                  |   Pass     |
| Back button                          | User redirected back to Dashboard                      |    Pass    |

### Home
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| N/A                                  | N/A                                               |    N/A    |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| N/A                                  | N/A                                               |    N/A    |


### Log In
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Cursor: text                                      |  Pass      |
| Password input field                 | Cursor: text                                      |   Pass     |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |   Pass     |
| Back button                          | Cursor: pointer, border turns green           |   Pass     |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Able to type in input field                       |   Pass     |
| Password input field                 | Able to type in input field                       |    Pass    |
| Submit button                        | Form is submitted                                 |    Pass    |
| Back button                          | User redirected to Register page                  |    Pass    |


### Payments
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Payment Item pencil            | Cursor: pointer, background colour turns pink          |    Pass    |
| First Payment Item cross             | Cursor: pointer, background colour turns pink          |   Pass     |
| First Payment Item modal cancel      | Cursor: pointer, border turns pink                     |   Pass     |
| First Payment Item modal confirm     | Cursor: pointer, border turns pink                     |   Pass     |
| Second Payment Item pencil           | Cursor: pointer, background colour turns pink          |   Pass     |
| Second Payment Item cross            | Cursor: pointer, background colour turns pink          |   Pass     |
| Second Payment Item modal cancel     | Cursor: pointer, border turns pink                     |   Pass     |
| Second Payment Item modal confirm    | Cursor: pointer, border turns pink                     |    Pass    |
| Add New Payment Item button          | Cursor: pointer, border turns green                    |    Pass    |
| Back button                          | Cursor: pointer, border turns green                |   Pass     |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Payment Item pencil            | Open Edit Payment Item page for this Item              |  Pass      |
| First Payment Item cross             | Open Modal to delete this Payment Item                 |    Pass    |
| First Payment Item modal cancel      | Close modal, return to Checklist page                  |   Pass     |
| First Payment Item modal confirm     | Delete this Payment Item, redirect to Checklist page   |   Pass     |
| Second Payment Item pencil           | Open Edit Payment Item page for this Item              |  Pass     |
| Second Payment Item cross            | Open Modal to delete this Payment Item                 |   Pass     |
| Second Payment Item modal cancel     | Close modal, return to Checklist page                  |   Pass     |
| Second Payment Item modal confirm    | Delete this Payment Item, redirect to Checklist page   |   Pass     |
| Add New Payment Item button          | Redirect to Add Payment Item                           |    Pass    |
| Back button                          | Redirect to Dashboard                                  |   Pass     |


### Register
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Cursor: text                                      |   Pass     |
| Password input field                 | Cursor: text                                      |   Pass     |
| Confirm Password input field         | Cursor: text                                      |    Pass    |
| Your Name input field                | Cursor: text                                      |   Pass     |
| Your Partners Name input field       | Cursor: text                                      |   Pass     |
| Wedding Date input field             | Cursor: text                                      |    Fail    |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |   Pass     |
| Back button                          | Cursor: pointer, border turns green           |    Pass    |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Able to type in input field                       |   Pass     |
| Password input field                 | Able to type in input field                       |    Pass    |
| Confirm Password input field         | Able to type in input field                       |   Pass     |
| Your Name input field                | Able to type in input field                       |   Pass     |
| Your Partners Name input field       | Able to type in input field                       |    Pass    |
| Wedding Date input field             | Able to type in input field                       |    Pass    |
| Submit button                        | Form is submitted                                 |    Pass    |
| Back button                          | User redirected to Log In page                    |     Pass   |


### Table Plan
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Table pencil                         | Cursor: pointer, background colour turns pink          |    Pass    |
| Table cross                          | Cursor: pointer, background colour turns pink          |     Pass   |
| Table modal cancel                   | Cursor: pointer, border turns pink                     |   Pass     |
| Table modal confirm                  | Cursor: pointer, border turns pink                     |   Pass     |
| Guest Edit button                    | Cursor: pointer, border turns pink                     |    Pass    |
| Unassigned Guests Guest Edit button  | Cursor: pointer, border turns pink                     |     Pass   |
| Add New Table button                 | Cursor: pointer, border turns green                    |   Pass     |
| Back button                          | Cursor: pointer, border turns green                |   Pass     |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Table pencil                         | Open Edit Table page for this Table                    |    Pass    |
| Table cross                          | Open Modal to delete this Table                        |   Pass     |
| Table modal cancel                   | Close modal, return to Table Plan page                 |  Pass      |
| Table modal confirm                  | Delete this Table, redirect to Table Plan page         |   Pass     |
| Guest Edit button                    | Redirect to Edit Guest page for this Guest             |   Pass     |
| Unassigned Guests Guest Edit button  | Redirect to Edit Guest page for this Guest             |     Pass   |
| Add New Table button                 | Redirect to Add Table                                  |   Pass     |
| Back button                          | User redirected back to Dashboard                      |      Pass  |

### Failed Tests
| Page               | Element Hovered                      | Expected Result     | Changes made                                                 | Result |
| -------------------| ------------------------------------ | --------------------|------------------------------------------------------------- | :----: |
| Add Checklist Item | Checklist Item Due Date input field  | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |    Pass    |
| Add Payment Item   | Payment Item Due Date input field    | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |   Pass     |
| Edit Checklist Item| Checklist Item Due Date input field  | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |    Pass    |
| Edit Payment Item  | Payment Item Due Date input field    | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |   Pass     |
| Edit Profile       | Wedding Date input field             | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |    Pass    |
| Register           | Wedding Date input field             | Cursor: text        | Added `cursor: text;` to `input#checklist_date` in style.css |     Pass   |



## Usability