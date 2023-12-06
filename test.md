# Tie the Knot Testing Document

## Functionality

### Add Checklist Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Cursor: text                                                    |        |
| Checklist Item Description input field | Cursor: text                                                    |        |
| Checklist Item Due Date input field    | Cursor: text                                                    |        |
| Checklist Item Due Date icon           | Cursor: pointer                                                 |        |
| Payment Checkbox                       | Cursor: pointer                                                 |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Able to type in input field                                     |        |
| Checklist Item Description input field | Able to type in input field                                     |        |
| Checklist Item Due Date input field    | Able to type in input field                                     |        |
| Checklist Item Due Date icon           | Date picker opens                                               |        |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Checklist                               |        |

### Add Payment Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Cursor: text                                                    |        |
| Payment Item Description input field   | Cursor: text                                                    |        |
| Payment Item Due Date input field      | Cursor: text                                                    |        |
| Payment Item Due Date icon             | Cursor: pointer                                                 |        |
| Payment Checkbox                       | Cursor: pointer                                                 |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Able to type in input field                                     |        |
| Payment Item Description input field   | Able to type in input field                                     |        |
| Payment Item Due Date input field      | Able to type in input field                                     |        |
| Payment Item Due Date icon             | Date picker opens                                               |        |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Payments                                |        |

### Add Guest
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Cursor: text                                                    |        |
| Guest Notes input field                | Cursor: text                                                    |        |
| Guest Table Dropdown Trigger           | Cursor: pointer                                                 |        |
| Guest Table Dropdown Option (`None`)   | Cursor: pointer                                                 |        |
| Guest Table Dropdown Option (not `None`) | Cursor: pointer                                               |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Able to type in input field                                     |        |
| Guest Notes input field                | Able to type in input field                                     |        |
| Guest Table Dropdown Trigger           | Opens dropdown options list                                     |        |
| Guest Table Dropdown Option (`None`)   | Selects "None" as dropdown option                               |        |
| Guest Table Dropdown Option (not `None`) | Selects the option, displays the option in a div next to the trigger |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Guests                                  |        |


### Add Table
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Checklist                               |        |


### Base (Nav and Footer)

##### Logged In
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Cursor: pointer                                   |        |
| Nav - Things to do                   | Cursor: pointer, background colour turns pink     |        |
| Nav - Checklist (Things to do)       | Cursor: pointer, background colour turns grey     |        |
| Nav - Payments (Things to do)        | Cursor: pointer, background colour turns grey     |        |
| Nav - Guest List                     | Cursor: pointer, background colour turns pink     |        |
| Nav - Guests (Guest List)            | Cursor: pointer, background colour turns grey     |        |
| Nav - Table Plan (Guest List)        | Cursor: pointer, background colour turns grey     |        |
| Nav - User's Name                    | Cursor: pointer, background colour turns pink     |        |
| Nav - Dashboard (User's Name)        | Cursor: pointer, background colour turns grey     |        |
| Nav - Log Out (User's Name)          | Cursor: pointer, background colour turns grey     |        |
| Footer - Dashboard                   | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Checklist                   | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Guests                      | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Table Plan                  | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Payments                    | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Facebook icon               | Cursor: pointer, background colour turns pink      |        |
| Footer - Instagram icon              | Cursor: pointer, background colour turns pink      |        |
| Footer - Twitter icon                | Cursor: pointer, background colour turns pink      |        |
| Footer - Youtube icon                | Cursor: pointer, background colour turns pink      |        |
| Footer - Enquiries email address     | Cursor: pointer, background colour turns pink, underlined|        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Redirect to Dashboard                             |        |
| Nav - Things to do                   | Opens Things to do dropdown                       |        |
| Nav - Checklist (Things to do)       | Redirect to Checklist                             |        |
| Nav - Payments (Things to do)        | Redirect to Payments                              |        |
| Nav - Guest List                     | Opens Guest List dropdown                         |        |
| Nav - Guests (Guest List)            | Redirect to Guests                                |        |
| Nav - Table Plan (Guest List)        | Redirect to Table Plan                            |        |
| Nav - User's Name                    | Opens User's Name dropdown                        |        |
| Nav - Dashboard (User's Name)        | Redirect to Dashboard                             |        |
| Nav - Log Out (User's Name)          | Removes User from session, redirect to Home       |        |
| Footer - Dashboard                   | Redirect to Dashboard                             |        |
| Footer - Checklist                   | Redirect to Checklist                             |        |
| Footer - Guests                      | Redirect to Guests                                |        |
| Footer - Table Plan                  | Redirect to Table Plan                            |        |
| Footer - Payments                    | Redirect to Payments                              |        |
| Footer - Facebook icon               | Redirect to Facebook                              |        |
| Footer - Instagram icon              | Redirect to Instagram                             |        |
| Footer - Twitter icon                | Redirect to Twitter                               |        |
| Footer - Youtube icon                | Redirect to Youtube                               |        |
| Footer - Enquiries email address     | Redirect to User's mailbox with enquiries email in a new email box |        |

##### Logged Out
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Cursor: pointer                                   |        |
| Nav - Log In                         | Cursor: pointer, background colour turns pink     |        |
| Nav - Register                       | Cursor: pointer, background colour turns pink     |        |
| Footer - Log In                      | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Register                    | Cursor: pointer, background colour turns pink, underlined |        |
| Footer - Facebook icon               | Cursor: pointer, background colour turns pink |        |
| Footer - Instagram icon              | Cursor: pointer, background colour turns pink |        |
| Footer - Twitter icon                | Cursor: pointer, background colour turns pink |        |
| Footer - Youtube icon                | Cursor: pointer, background colour turns pink |        |
| Footer - Enquiries email address     | Cursor: pointer, background colour turns pink, underlined |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Logo                                 | Redirect to Home                                  |        |
| Nav - Log In                         | Redirect to Log In                                |        |
| Nav - Register                       | Redirect to Register                              |        |
| Footer - Log In                      | Redirect to Log In                                |        |
| Footer - Register                    | Redirect to Register                              |        |
| Footer - Facebook icon               | Redirect to Facebook                              |        |
| Footer - Instagram icon              | Redirect to Instagram                             |        |
| Footer - Twitter icon                | Redirect to Twitter                               |        |
| Footer - Youtube icon                | Redirect to Youtube                               |        |
| Footer - Enquiries email address     | Redirect to User's mailbox with enquiries email in a new email box |        |


### Checklist
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Checklist Item pencil          | Cursor: pointer, background colour turns pink          |        |
| First Checklist Item cross           | Cursor: pointer, background colour turns pink          |        |
| First Checklist Item modal cancel    | Cursor: pointer, border turns pink                     |        |
| First Checklist Item modal confirm   | Cursor: pointer, border turns pink                     |        |
| Second Checklist Item pencil         | Cursor: pointer, background colour turns pink          |        |
| Second Checklist Item cross          | Cursor: pointer, background colour turns pink          |        |
| Second Checklist Item modal cancel   | Cursor: pointer, border turns pink                     |        |
| Second Checklist Item modal confirm  | Cursor: pointer, border turns pink                     |        |
| Add New Checklist Item button        | Cursor: pointer, border turns green                    |        |
| Back button                          | Cursor: pointer, border turns dark green               |        |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Checklist Item pencil          | Open Edit Checklist Item page for this Item            |        |
| First Checklist Item cross           | Open Modal to delete this Checklist Item               |        |
| First Checklist Item modal cancel    | Close modal, return to Checklist page                  |        |
| First Checklist Item modal confirm   | Delete this Checklist Item, redirect to Checklist page |        |
| Second Checklist Item pencil         | Open Edit Checklist Item page for this Item            |        |
| Second Checklist Item cross          | Open Modal to delete this Checklist Item               |        |
| Second Checklist Item modal cancel   | Close modal, return to Checklist page                  |        |
| Second Checklist Item modal confirm  | Delete this Checklist Item, redirect to Checklist page |        |
| Add New Checklist Item button        | Redirect to Add Checklist Item                         |        |
| Back button                          | Redirect to Dashboard                                  |        |

### Dashboard
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Confetti Click Me                    | Cursor: pointer                                   |        |
| Checklist                            | Cursor: pointer, border turns green               |        |
| Payments                             | Cursor: pointer, border turns green               |        |
| Guests                               | Cursor: pointer, border turns green               |        |
| Table Plan                           | Cursor: pointer, border turns green               |        |
| Edit Profile                         | Cursor: pointer, border turns pink                |        |
| Log Out                              | Cursor: pointer, border turns pink                |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Confetti Click Me                    | Confetti effect appears                           |        |
| Checklist                            | Redirect to Checklist                             |        |
| Payments                             | Redirect to Payments                              |        |
| Guests                               | Redirect to Guests                                |        |
| Table Plan                           | Redirect to Table Plan                            |        |
| Edit Profile                         | Redirect to Edit Profile                          |        |
| Log Out                              | Removes User from session, redirect to Home       |        |


### Edit Checklist Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Cursor: text                                                    |        |
| Checklist Item Description input field | Cursor: text                                                    |        |
| Checklist Item Due Date input field    | Cursor: text                                                    |        |
| Checklist Item Due Date icon           | Cursor: pointer                                                 |        |
| Payment Checkbox                       | Cursor: pointer                                                 |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Checklist Item name input field        | Able to type in input field                                     |        |
| Checklist Item Description input field | Able to type in input field                                     |        |
| Checklist Item Due Date input field    | Able to type in input field                                     |        |
| Checklist Item Due Date icon           | Date picker opens                                               |        |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Checklist                               |        |

### Edit Payment Item
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Cursor: text                                                    |        |
| Payment Item Description input field   | Cursor: text                                                    |        |
| Payment Item Due Date input field      | Cursor: text                                                    |        |
| Payment Item Due Date icon             | Cursor: pointer                                                 |        |
| Payment Checkbox                       | Cursor: pointer                                                 |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Payment Item name input field          | Able to type in input field                                     |        |
| Payment Item Description input field   | Able to type in input field                                     |        |
| Payment Item Due Date input field      | Able to type in input field                                     |        |
| Payment Item Due Date icon             | Date picker opens                                               |        |
| Payment Checkbox                       | Checkbox changes to Checked / Unchecked                         |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Payments                                |        |

### Edit Guests
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Cursor: text                                                    |        |
| Guest Notes input field                | Cursor: text                                                    |        |
| Guest Table Dropdown Trigger           | Cursor: pointer                                                 |        |
| Guest Table Dropdown Option (`None`)   | Cursor: pointer                                                 |        |
| Guest Table Dropdown Option (not `None`) | Cursor: pointer                                               |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Guest Name input field                 | Able to type in input field                                     |        |
| Guest Notes input field                | Able to type in input field                                     |        |
| Guest Table Dropdown Trigger           | Opens dropdown options list                                     |        |
| Guest Table Dropdown Option (`None`)   | Selects "None" as dropdown option                               |        |
| Guest Table Dropdown Option (not `None`) | Selects the option, displays the option in a div next to the trigger |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Guests                                  |        |


### Edit Profile
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Disabled Username field              | None                                              |        |
| Old Password input field             | Cursor: text                                      |        |
| New Password input field             | Cursor: text                                      |        |
| Confirm Password input field         | Cursor: text                                      |        |
| Your Name input field                | Cursor: text                                      |        |
| Your Partners Name input field       | Cursor: text                                      |        |
| Wedding Date input field             | Cursor: text                                      |        |
| Wedding Date icon                    | Curson: pointer                                   |        |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |        |
| Back button                          | Cursor: pointer, border turns dark green          |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Disabled Username field              | None                                              |        |
| Old Password input field             | Able to type in input field                       |        |
| New Password input field             | Able to type in input field                       |        |
| Confirm Password input field         | Able to type in input field                       |        |
| Your Name input field                | Able to type in input field                       |        |
| Your Partners Name input field       | Able to type in input field                       |        |
| Wedding Date input field             | Able to type in input field                       |        |
| Wedding Date icon                    | Date picker opens                                 |        |
| Submit button                        | Form is submitted                                 |        |
| Back button                          | User redirected back to Dashboard                 |        |

### Edit Table
| Element Hovered                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |        |
| Submit button                          | Cursor: pointer, background colour to change to lighter green   |        |
| Back button                            | Cursor: pointer, border turns dark green                        |        |


| Element Clicked                        | Expected Result                                                 | Result |
| -------------------------------------- | --------------------------------------------------------------- | :----: |
| Table Name input field                 | Cursor: text                                                    |        |
| Submit button                          | Form is submitted                                               |        |
| Back button                            | User redirected back to Checklist                               |        |


### Guests
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Guest pencil                         | Cursor: pointer, background colour turns pink          |        |
| Guest cross                          | Cursor: pointer, background colour turns pink          |        |
| Guest modal cancel                   | Cursor: pointer, border turns pink                     |        |
| Guest modal confirm                  | Cursor: pointer, border turns pink                     |        |
| Add New Guest button                 | Cursor: pointer, border turns green                    |        |
| Back button                          | Cursor: pointer, border turns dark green                        |        |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Guest pencil                         | Open Edit Guest page for this Guest                    |        |
| Guest cross                          | Open Modal to delete this Guest                        |        |
| Guest modal cancel                   | Close modal, return to Guests page                     |        |
| Guest modal confirm                  | Delete this Guest, redirect to Guests page             |        |
| Add New Guest button                 | Redirect to Add Guest                                  |        |
| Back button                          | User redirected back to Dashboard                      |        |

### Home
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| N/A                                  | N/A                                               |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| N/A                                  | N/A                                               |        |


### Log In
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Cursor: text                                      |        |
| Password input field                 | Cursor: text                                      |        |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |        |
| Back button                          | Cursor: pointer, border turns dark green          |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Able to type in input field                       |        |
| Password input field                 | Able to type in input field                       |        |
| Submit button                        | Form is submitted                                 |        |
| Back button                          | User redirected back to Dashboard                 |        |


### Payments
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Payment Item pencil            | Cursor: pointer, background colour turns pink          |        |
| First Payment Item cross             | Cursor: pointer, background colour turns pink          |        |
| First Payment Item modal cancel      | Cursor: pointer, border turns pink                     |        |
| First Payment Item modal confirm     | Cursor: pointer, border turns pink                     |        |
| Second Payment Item pencil           | Cursor: pointer, background colour turns pink          |        |
| Second Payment Item cross            | Cursor: pointer, background colour turns pink          |        |
| Second Payment Item modal cancel     | Cursor: pointer, border turns pink                     |        |
| Second Payment Item modal confirm    | Cursor: pointer, border turns pink                     |        |
| Add New Payment Item button          | Cursor: pointer, border turns green                    |        |
| Back button                          | Cursor: pointer, border turns dark green               |        |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| First Payment Item pencil            | Open Edit Payment Item page for this Item              |        |
| First Payment Item cross             | Open Modal to delete this Payment Item                 |        |
| First Payment Item modal cancel      | Close modal, return to Checklist page                  |        |
| First Payment Item modal confirm     | Delete this Payment Item, redirect to Checklist page   |        |
| Second Payment Item pencil           | Open Edit Payment Item page for this Item              |        |
| Second Payment Item cross            | Open Modal to delete this Payment Item                 |        |
| Second Payment Item modal cancel     | Close modal, return to Checklist page                  |        |
| Second Payment Item modal confirm    | Delete this Payment Item, redirect to Checklist page   |        |
| Add New Payment Item button          | Redirect to Add Payment Item                           |        |
| Back button                          | Redirect to Dashboard                                  |        |


### Sign Up
| Element Hovered                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Cursor: text                                      |        |
| Password input field                 | Cursor: text                                      |        |
| Confirm Password input field         | Cursor: text                                      |        |
| Your Name input field                | Cursor: text                                      |        |
| Your Partners Name input field       | Cursor: text                                      |        |
| Wedding Date input field             | Cursor: pointer                                   |        |
| Wedding Date icon                    | Date picker opens                                 |        |
| Submit button                        | Cursor: pointer, background colour to change to lighter green |        |
| Back button                          | Cursor: pointer, border turns dark green          |        |

| Element Clicked                      | Expected Result                                   | Result |
| ------------------------------------ | ------------------------------------------------- | :----: |
| Username input field                 | Able to type in input field                       |        |
| Password input field                 | Able to type in input field                       |        |
| Confirm Password input field         | Able to type in input field                       |        |
| Your Name input field                | Able to type in input field                       |        |
| Your Partners Name input field       | Able to type in input field                       |        |
| Wedding Date input field             | Able to type in input field                       |        |
| Wedding Date icon                    | Date picker opens                                 |        |
| Submit button                        | Form is submitted                                 |        |
| Back button                          | User redirected back to Dashboard                 |        |


### Table Plan
| Element Hovered                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Table pencil                         | Cursor: pointer, background colour turns pink          |        |
| Table cross                          | Cursor: pointer, background colour turns pink          |        |
| Table modal cancel                   | Cursor: pointer, border turns pink                     |        |
| Table modal confirm                  | Cursor: pointer, border turns pink                     |        |
| Guest Edit button                    | Cursor: pointer, border turns pink                     |        |
| Unassigned Guests Table pencil       | Cursor: pointer, background colour turns pink          |        |
| Unassigned Guests Table cross        | Cursor: pointer, background colour turns pink          |        |
| Unassigned Guests Table modal cancel | Cursor: pointer, border turns pink                     |        |
| Unassigned Guests Table modal confirm| Cursor: pointer, border turns pink                     |        |
| Unassigned Guests Guest Edit button  | Cursor: pointer, border turns pink                     |        |
| Add New Table button                 | Cursor: pointer, border turns green                    |        |
| Back button                          | Cursor: pointer, border turns dark green          |        |

| Element Clicked                      | Expected Result                                        | Result |
| ------------------------------------ | ------------------------------------------------------ | :----: |
| Table pencil                         | Open Edit Table page for this Table                    |        |
| Table cross                          | Open Modal to delete this Table                        |        |
| Table modal cancel                   | Close modal, return to Table Plan page                 |        |
| Table modal confirm                  | Delete this Table, redirect to Table Plan page         |        |
| Guest Edit button                    | Redirect to Edit Guest page for this Guest             |        |
| Unassigned Guests Table pencil       | Open Edit Table page for this Table                    |        |
| Unassigned Guests Table cross        | Open Modal to delete this Table                        |        |
| Unassigned Guests Table modal cancel | Close modal, return to Table Plan page                 |        |
| Unassigned Guests Table modal confirm| Delete this Table, redirect to Table Plan page         |        |
| Unassigned Guests Guest Edit button  | Redirect to Edit Guest page for this Guest             |        |
| Add New Table button                 | Redirect to Add Table                                  |        |
| Back button                          | User redirected back to Dashboard                      |        |


## Usability