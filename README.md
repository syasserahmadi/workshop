# Hariwa Factory Manager 
 
#### Video Demo: https://youtu.be/oDMb9kpjLtU?si=npKVRWpbex04igFk
 
#### Description: 
 
Hariwa Factory Manager is a web application designed to manage the production process of garments in the clothing industry. Manufacturing in this industry is a complex process with multiple categories and sub-categories, requiring constant management for smooth operations. This application aims to automate and streamline the management of these processes as much as possible. 
 
As a family business in the clothing industry, we understand the challenges faced by producers in managing their businesses. Therefore, i've have developed the first phase of this web app, focusing on managing the Cutting and Sewing process. The app is designed to organize data and assist in the management of sewing machine operators on the factory floor. 
 
#### How this app works: 

 
### 1. New User Creation
 
To add a machine operator to the app, the operator needs to sign up (Admins can also do this). after signing in regular users can only see an overview page of the factory floor to get a sense of what their colleagues working on. Admins can also promote users to admin users for better accessibility to different parts of the app.

#### Note: This app uses django password validation and managment technologies for the robust security features. so you should set password which meet certain requirments, the app will notify you when you're password is not optimal.

 
### 2. Creating New Cuts
 
The next step is the "New Cut" page, where you can enter the details of the fabric cutting process. This information can prove useful in other areas of the app.
Although each cut has a unique id, sometimes it's needed for cuts to have a custom code or id. so you can set a custom id by enabling the custom-code radio button.

#### Note: This app uses "Bootstrap form validation" and some "JavaScript" for front end validation of forms and also back end validations are using django and python.

 
### 3. Assigning New Jobs 
 
Once you have a new cut, you can assign jobs to people. The "New Job" page is designed for this purpose. It will display the cuts you created on the page, and when you select one of them, other fields such as sizes, colors, and lines will be populated from the database using the Fetch API. If you make changes to any field, such as colors, the related fields will be automatically updated according to your choices. 
 
### 4. Home Page / Status Page 
 
The homepage features a dashboard that provides an overview of the progress of each cut and a detailed view of who is working on which job. You can also see the recently completed jobs. 
 
### 5. Admin Area 
 
The admin area offers several additional functionalities. You can create new users (regular and admin users), edit user attributes such as name, email, and passwords, and access a more detailed view of the Cuts, Sizes, Colors, Lines, Amounts, and Jobs tables. You can also edit any row in the database, with related tables being updated accordingly. 
 
### Tech Stack

For the backend and user registration/authentication, I utilized Django, along with Django ORM(which uses SQLite as the default database) for this app. The frontend was developed using HTML, CSS, Bootstrap, and JavaScript (primarily for manipulating HTML and making Fetch API calls to the database and client side validations). The Persian font used in the app is called AzarMehr, while the English fonts are from Google Fonts.
 
### Future Development 
 
To ensure the app is straightforward and user-friendly, I focused on implementing only vital features for the management process, while excluding non-essential features like a color picker in the New Cut page but additional features will be added to the app in the future updates.

planned features for future versions include: "User profile manager", "Color picker for new colors added in the New Cuts page", "Salary calculator" and "Packaging section".