# MIO

Stream Four Project: Full Stack Frameworks With Django - Code Institute

For my final milestone project, I have chosen to develop an online clothing store that specializes in minimalist men's wear. 
The inspiration for this project comes for my passion for fashion, particularly minimalist and original pieces. Online clothes shopping
is becoming increasingly commonplace for many reason, convenience being one of them. Many entities have taken advantage of this demand
and developed very popular and successful online stores. Some of these include <a href="https://www.prettylittlething.ie/">PrettyLittleThing</a>,
<a href="https://ie.boohoo.com/">Boohoo</a>, <a href="https://www.asos.com/">ASOS</a>, and <a href="https://www.cosstores.com/en_eur/index.html">COS</a>.
ASOS and COS are among my favourite online clothing stores, and I have taken a significant amount of inspiration from them. 

There are indeed many online clothing stores but, with the exception of COS, few of them specialize in men's minimalist pieces, so 
I believe there is room in the market for more. So, I have taken it upon myseelf to use this project as an opportunity to develop a site that tailors
specifically to minimalist men's wear with a modern and cool twist. 

## Demo 
 A live demo can be found [here](https://m-i-o.herokuapp.com/)
 
 Here is the responsiveness preview in gif form. You should see a short clip of me testing responsiveness.
 ![Responsive View](static/responsive_view/responsiveview.gif)

## UX
### User Stories
#### User:
<ul>
<li>As a user, I want to view and interact with a site that is aesthetically pleasing. I want to enjoy what the site looks like and I want to
feel the desire to return to the site.</li>
<li>As a user, I expect that all articles of clothing adhere to the promised style of minimalism and originality to varying degrees.</li>
<li>As a user, I expect to be able to make an profile and add, edit, and remove my profile details. I also expect to be able to view my order history
from my profile.</li>
<li>As a user, I expect to be able to easily, swiftly, and seamlessly locate and browse through the various articles of clothing.</li>
<li>As a user, I expect to be able to view easily, swiftly, and seamlessly view product details such as size, price, etc.</li>
<li>As a user, I expect to be able to buy clothing without much issue.</li>
<li>As a user, I expect the site to be fully functional.</li>
</ul>

#### Site Owner:
<ul>
<li>As the site owner, I expect to have a functioning admin interface, accessible only to the site's admin.</li>
<li>As the site owner, I expect to be able to use the admin interface to add and remove clothing from the collection without much issue.</li>
<li>As the site owner, I expect to be able to use the admin interface to edit each products details should I need to, such as its price, rating, etc.</li>
<li>As the site owner, I expect to notified by email each time a user makes a purchase.</li>
</ul>

### Strategy Plane
<p><i><strong>What am I aiming to achieve with this project, and for whom?</strong></i></p>
<p>The target audience for this project is anyone who is interested in minimalist men's fashion. Ideally, the target audience
would be looking for an online clothing store that primarly stocks men's wear that is both minimalistic and stylish.</p>
<p>My aim with this project is to provide a one-stop-shop for minimalist men's wear. Oftentimes, it is necessary to visit several
stores in order to find numerous minimalistic and fashionable pieces, especially for men. But typically speaking, there really aren't many
places that one can go to find a wide selection of minimalist men's wear. That is the issues I'm hoping to address with this project,
and that is the gap in the market I'm hoping to capitalize upon.</p>
<p>Due to time constraints, I aimed to build the MVP (Minimum Viable Product). This basically means that 
the project will contain the essential features that allow it to function. There are other features
that I would like to include, but I will not have the time, skill set, and resources to do so.</p>

### Scope Plane
<p><i><strong>What features, based upon the information from the strategy plane, do I want to include in this design?</strong></i></p>
<p>In order to achieve the project aims discussed above I plan to ensure the site's visuals align with the overarching theme 
of minimalism. I want to include a navbar from which the user can navigate to specific sections of the store i.e. viewing
the full collection or just certain types of clothing like hats, jackets, etc. I plan to ensure the user's
journey is easier and more intuitive by enabling them to filter pieces by price, category, rating, etc. I plan to enable the user
to create an account so that they can view their order history and edit their profile details, if they need to.
I plan to feature a checkout system that is as straightforward, reliable, and quick as I can manage. In essence, I'm aiming to
ensure that the user is left with a positive emotional response. It is important to me to make sure that they <strong>want</strong> to
come back again.</p>
<p>However, due to time constraints, I aim to go live with the <strong>MVP</strong> (Minimum Viable Product). This basically means that 
the project will contain the essential features that allow it to present and function well. There are other features
that I would like to include, but I will not have the time, skill set, and resources to do so.</p>

### Structure
<p><i><strong>How is everything structured? How is it logically grouped together? The features, the elements, the data, etc.</strong></i></p>
<p>In order of appearance, the homepage will be separated into three parts. The top will house the homepage link, the searchbar, and the profile and bag links.
Below that will be the navbar, which will contain links to various parts of the site i.e. a link to the full clothing collection and links
to specific types of clothing like trousers, shirts, etc. The middle portion of the homepage will contain the homepage image and a direct link to the
site's full collection. At the bottom of the homepage will be the footer, which will contain social media handles.</p>
<p>Next, will be the poducts page, which will be the page that the full clothing colelction will be displayed for the user to browse through.
From there, the user can select an item and view its details, such as its description and available sizes. They can then choose to
return to the collection or buy the item. At which point, they will be directed their bag where they can view their order summary.</p>
<p>They can then move on to the checkout, where they'll fill in their delivery details and payment information. Then the order will be placed, and they
will be given an option to go back to the full collection to browse and potentially purchase more.</p>
<p>From the homepage, they will also have the option to register and make an account, so that purchasing in the future will be easier because their details will 
be saved.</p>

### Skeleton
 <ul>
    <li>Homepage</li>
    <li>Full clothing collection page</li>
    <li>Product details page for each piece of clothing selected</li>
    <li>Checkout page</li>
    <li>Order confirmation page</li>
    <li>Registration page</li>
</ul> 

[Here](static/wireframes) is a list of the wireframes I developed during the inital mock-up. They are quite self-explanatory and rudimentary, but they didn't need to be overly compelx. 
They merely needed to serve as a base for me to extrapolate upon, so you may observe some  minor deviations in the final project.

### Surface
<p><i><strong>What will the project look like? Colours, images, etc.</strong></i></p>
<p>I believe that form must follow function. It is important to me to make sure that the overall look of the project 
syncronizes well with the theme of minimalism. With that said, I don't plan on overloading the project with lots of colours and
images. In fact, the only image in this project will be the image on the homepage.</p>
<p>Regarding colour, I was thinking of adhering to a black and white palette in order to fully convey the
site's focus on minimalism. However, I decided against that because I felt it necessary to include a small pop of colour
just to add a modicum of dynamism to the aesthetic. So, I plan on making the navbar shade of green that is cool and
unobtrusive, and I plan on making the footer pure black with peach social media handles within it. Everything else on the site
will adhere to a black and white theme.</p>
<p>I plan to include a respectable amount of white space in the project
to create a sense of spaciousness and ensure that the pages don't appear too cluttered.</p>
<p>I will also take some stylistic inspiration from online clothing stores like <a href="https://www.asos.com/">ASOS</a>
and<a href="https://www.cosstores.com/en_eur/index.html">COS</a> in order to adhere to an industry standard look while 
adding bits of personal flair. 

## Features
## Features Implemented
#### Website-Wide Features (features on all pages):
<ul>
  <li>A fixed header and navbar that stays at the top of the screen no matter how far down the user
  scrolls. This ensures that they can always access the navbar without having to scroll up.</li>
  <li>The header contains a search bar with which the user can use to search for specific items on the site. contains a homepage link in the form of the project name "MIO" in the top left. Users can use this
  to navigate back to the homepage. But this does not appear on the mobile version of the site. Instead, they will
  find "Home" listed in the options from the burger icon<li>
  <li>The user can use the navbar to navigate to different sections of the site, such as the full collections page or
  to specific groups of items such as trainers, hats, etc. They can also filter items by price, category, etc. 
  The user can also utilize the navbar to create an profile or view
  their bag.</li>
</ul>

#### Homepage Features:
<ul>
  <li>The homepage contains a link to the full collection of clothing.</li>
  <li>The footer contains social media handles which can direct the user to the relevant social media pages.</li>
</ul>

#### Collections Page Features (features on the page that displays all available items):
<ul>
  <li>On the right, above the available items, the user can sort through and organize them price (low to hight or vice versa),
  by category (A-Z or vice versa), by rating (low to high or vice versa) or by name (A-Z or vice versa).</li>
  <li>On the left, the user can see the exact amount of available products.</li>
  <li>The user can select an item and view its details, such as price, description, etc. They can choose the quauntity
  they want to buy, and they can either add the item to their bag or return back to the products page.</li>
  <li>Adding an item to user's bag, will prompt a little order summar to appear in the top right of the screen below
  the bag icon. It will display the item added, a link to the checkout, and notify the user how much more they need to
  spend to get free delivery, if anything.
  <li>In the product details page, admin users can edit or remove items.</li>
  <li>At the bottom right of the screen is an arrow icon that always navigates the user to the top of the page,
  so that they don't need to scroll.</li>
</ul>

#### Shopping Bag Features:
<ul>
  <li>The user can see a full summary of their order.</li>
  <li>They can choose to increase or decrease the number of the item, or remove it entirely.</li>
  <li>From here, the user can navigate to complete their order or return back to view items.</li>
</ul>

#### Checkout Features:
<ul>
  <li>Here, the user can add and augment their delivery and payment details.</li>
  <li>A full summary of their order is displayed here, along with the grand total.</li>
  <li>The will have the option to proceed with the purchase or return to adjust their bag.</li>
  <li>Going through with the order will trigger an order confirmtion email to the user and an order confirmation box, 
  which will display a summary of said order in a box. Below said box, will be an option to bring to user back to view the full collection and continue their shopping.</li>
</ul>

### Features Left To Implement
<ul>
  <li>The option for the user to log in using their social media account.</li>
  <li>The option of next day delivery</li>
  <li>A "New In" section that displays items recently added to the stock.</li>
  <li>An "On Sale" section that displays items that are on sale.</li>
  <li>A "bookmarking" feature that allows the user to mark items they're interested in, but not willing or able 
  to purchase at that particular moment. A list of their bookmarked items would be stored in their profile.<li>
</ul>

## Technologies Used
### Languages
* [HTML5](https://www.w3schools.com/html/default.asp)
* [CSS3](https://www.w3schools.com/css/default.asp)
* [Javascript](https://www.w3schools.com/js/default.asp)
* [Python3](https://www.w3schools.com/python/default.asp)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/)
### Libraries and Framework
* [Django](https://docs.djangoproject.com/en/3.1/)
* [Bootstrap](https://getbootstrap.com/)
* [FontAwesome](https://fontawesome.com/)
* [Favicon](https://favicon.io/)
* [Google Fonts](https://fonts.google.com/)
* [JQuery](https://api.jquery.com/)
* [Gunicorn](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/gunicorn/)
* [Psycopg2](https://pypi.org/project/psycopg2/)
* [Stripe](https://stripe.com/gb)
* [Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)
### Tools
* [Gitpod](https://www.gitpod.io/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Heroku](https://heroku.com/)
* [AWS S3 Bucket](https://aws.amazon.com/)
* [Boto3](https://boto3.amazonaws.com/)
### Databases
* [Sqlite3](https://www.sqlite.org/index.html) with Django
* [PostgreSQL](https://www.postgresql.org/) with Heroku

## Testing
<p>The first step of my testing began by using <a href="http://ami.responsivedesign.is/">Am I Responsive?</a> to deduce whether my project was indeed responsive and compatible across all devices, the results of which can be observed at the beginning of this readme in the responsiveness preview.</p>

<p>The second step was making sure there were no major issues in DevTools.</p>

<p>The third step involved sharing the deployed link with a few colleagues and friends to double check whether it was actually responsive or not, and they reported no problems.</p>

### Testing functionality

#### NavBar and Footer
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Logo  | Click | The user is brought to the homepage | Passed 
| My Account  |  Click     | Opens a dropdown menu with the option to login or register      | Passed
| My Profile | Click | The user is brought to their profile page where they can see their order history and delivery details | Passed
| Logout | Click | The user is brought to the sign-out page | Passed
| Login | Click | Takes user to a page in which they must enter their username and password | Passed
| Register | Click | The user is brought to the registration form where you are asked to enter your details | Passed
| Product Management | Click | Admin users are brought to a page where they can add a new product without having to sign into the admin backend | Passed
| Navbar      | Click  |  All three optins open a dropdown menu and redirect the user to the relevant pages | Passed
| Social Media Handles | Click | The user is brought to the relevant social media pages | Passed
#### Homepage
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| View Our Collection | Click | User is brought to a page that displays all items | Passed
#### Collection Page
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Sort Bar  | Click  |  User is presented with a dropdown menu that allows sort by various categories in ascending or descending order | Passed
| Item Image   | Click | tUser is taken to a page with the details displayed | Passed
| Edit & Delete | Click | Admin users are unabled with the option of editting or deleting a piece of clothing | Passed
| Back To Top Arrow | Click | The user is brought to the top of the page | Passed
#### Product Details Page
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Product Image  | Click | The image is opened in a new tab | Passed
| Quantity Selector | Click/Type | Select using the plus or minus buttons, or by typing in the quantity the user wants. The user is unable enter less than 1 or more than 99 | Passed
| Edit & Delete | Click | Admin users are unabled with the option of editting or deleting a piece of clothing | Passed
| Keep Shopping | Click | User is brought back to collections page | Passed 
| Add To Bag | Click | An order/checkout summary drops down from bag icon | Passed 
| Secure Checkout Link | Click | The user is brought to the shopping bag page | Passed
#### Shopping Bag
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Quantity Selector | Click/Type | User can adjust item quantity or remove them | Passed
| Keep Shopping | Click | User is brought back to Collections page | Passed
| Secure Checkout | click | User is brought to the checkout page | Passed
#### Checkout Form
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Form Fields | text | All fields, except the card fields, will be populated if user is a returning user | Passed
| Save Profile | Checkbox | Saves first time user details to their profile | Passed
| Adjust bag | Click | Brings the user back to their shopping bag to make changes | Passed
| Card Fields |Text |  Enter the test card number 4242 4242 4242 4242 and any future expiring data, and any CSV. Incompatible card details will trigger an error message | Passed
| Complete Order | Click | Loading animation triggered, user is brought to order success page, and a confirmation email is sent to the user and site owner | Passed
#### Checkout Success
| Test        |  Action    |  Expected Result                  |   Test Result
|  --------   |  --------  | --------------------     |  ------------
| Continue Shopping? | click | User is redirected to the collection page to continue shopping | Passed


### Code Validation
<p>For code validation, I used W3C and PEP8. No major issues were encountered during this of testing.</p>

### Defensive Design
<p>Warning messages are triggered if the user enters incorrect or incompatible usernames, passwords, emails, etc.</p>

## Bugs & Issues of Note 
<p>I did encounter any serious bugs during devlopment. However, there were a few "line too long" errors in the code. I attempted
to amend them, but ended up breaking the site in the process. Due to limitied time, I opted to leave them as is due to the fact that
they do not impact the fucntionality of the site.</p>
<p>Also, one of the individuals that helped my test the project reported that it took quite some time for his confirmation email
to come through after he placed his order. He tried it a second time and the email came through almost immediately. But it is worth noting
that it took quite some time for it to reach him the first time. </p>

## Deployment
The project is stored on **Github** and hosted on **Heroku**
#### Local Deployment
 To run this project, the following tools have to be installed:
* An IDE of your choice (I used [Gitpod](https://www.gitpod.io/) for creating this project)
* [Git](https://git-scm.com/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Python3](https://www.w3schools.com/python/default.asp) It comes pre-installed with Mac.

You will also need to create account with:
* [Stripe](https://stripe.com/gb)
* [AWS](https://aws.amazon.com/) for the [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html)
* An email account of your choice. I used [gmail](https://mail.google.com/)
### Directions
1. You can clone this repository directly into you editor by pasting the following command into the terminal: https://github.com/kel151/mio_v1
2. Or you can save a copy of this directory by clicking the green button " Clone or download" then "Download Zip" and after that extract the Zip file to your folder, change the directory to the directory file location you just created.
3. For this project i stored all  Stripe secret key in both Heroku setting and Gitpod setting. That way i could still use them for development and production. 

In `settings.py` you can set your variables like in the example below
```
import os

SECRET_KEY = os.environ.get(your secret key)
DEBUG = 'DEVELOPMENT' in os.environ
STRIPE_PUBLIC_KEY = os.getenv(your secret key
STRIPE_SECRET_KEY = os.getenv(your secret key)
STRIPE_WH_SECRET = os.getenv(your secret key)
```
For more info on how to set up the Stripe keys visit [Stripe key](https://stripe.com/docs/keys).

3. Install all requirements from the `requirements.txt` file putting this command into your terminal:
```
pip3 install -r requirements.txt
```
4. In the terminal in your IDE migrate the models to crete a database using the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Load the data fixture (Categories, Specials, Products) in that order using the following command in the terminal
```
python3 manage.py loaddata <fixture name>
```
6. Create a superuser, it will alow you to have access to the admin panel.
you need a username, an email, a password. Note the password won't display in the terminal but will be registered.
```
python3 manage.py createsuperuser
```
7. You can now run the the application using the following command in the terminal:
```
python3 manage.py runserver
```
8. To access the admin panel add `/admin` in the url and enter the details for the superuser you created.

#### Heroku Deployment
In order for Heroku to work properly, the local deployment steps are required.
You will also need to have installed  `gunicorn`, `dj-database-url` and `psycopg`. All of those are already in the project requirements.txt, but for future project they are essentials for Heroku to function properly. 

1. Create a `requirements.txt ` file, which will contains the list of dependencies, using the following command in the terminal:
```
pip3 freeze > requirements.txt
```
2. Create a `Procfile` and inside it type:
```
web: gunicorn whisky_shop.wsgi:application
```
3. On [Heroku](https://heroku.com/) website you can now create your **new app**, assign a unique name(try to use a name as close as possible to the project name for consistency), choose the region the closest to you and click **Create app**.
4. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heroku Postgres**, select **Hobby Dev — Free** and click **Provision*** button to add it to your project. (This is where  `dj-database-url` and `Psycopg` are required.)
5. In the Heroku **settings** click on `Reveal Config Vars` and set the following variables.

| KEY                       | VALUE              
|-----------------          | ------------------ 
| AWS_ACCESS_KEY_ID         | your AWS access key here      
| AWS_SECRET_ACCESS_KEY     | your AWS secret key here  
| DATABASE_URL              | your Postgres DB url here
| EMAIL_HOST_PASSWORD       | you email password(generated by gmail)
| EMAIL_HOST_USER           | your email address
| SECRET_KEY                | your secret key
| STRIPE_PUBLIC_KEY         | your stripe public key here
| STRIPE_SECRET_KEY         | your stripe secretkey here
| STRIPE_WH_SECRET          | your stripe WH secret here
| USE_AWS                   | True

6. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in `settings.py`.
You can temporary comment out the current database settings code and just paste the following in `settings.py`:
```
DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")  
    }
```
This is just a temporary set up that allows to make all the migrations required for our data in our DB to be transfer to Heroku **POstgres**. You shouldn't commit and push at this stage for security reasons.

7. Here you can now follow the exact steps, 4, 5 and 6 as explained in local deployment.

8. You can remove the postgres URL form you settings and uncomment the default DATABASE code form your settings.

9. Add your heroku app url to **ALLOWED_HOST** in the settings file and also include local host.
```
ALLOWED_HOSTS = ['your heroku app name here', 'localhost']
```
10. You can now connect Heroku to Github to automatically deploy each time you push to Github.
In Heroku **Dashboards** select 
* Deploy -> Deployment method -> Github
* link your Github repo name to Heroku
* Click **Enable automatic Deployment**
* Now you you run `git push` in the terminal, it will push to Github and Heroku.
11. After your app has been successfully deployed you can view you project by clicking on **open app**

## Credits
### Content
<p>I used the Boutique-Ado tutorial provided by Chris of Code Institute as a point of reference throughout development, tailoring it to suit the specific
needs of my project.</p>

### Media
<p>The images used in this project were taken from <a href="https://unsplash.com/">Unsplash</a>, an open license and resource that I greatly recommend</p>
<p>However, regarding the homepage image, it was taken from<a href="https://hypebeast.com/2016/12/noboyushi-araki-g-dragon-dazed-winter-2016-peaceminusone-ambush-photoshoot">Hypebeast.com</a>. All credits and rights belong to the
appropriate and relevant parties.</a></p>

## Acknowledgements
<ul>
 <li>My mentor, Simen, for his help and advice.</li>
 <li>My second mentor, Brian Macharia, who took over while Simen went on his honeymoon. 
 <li>My friend and fellow member of the Code Institute Slack Community, Sebastien, for all of his advice, kindness, and encouragement. I would also
 like to thank him for his help in consctructing my ReadMe.</li>
 <li>The Student Care team, particularly Mark McGann, for their constant support, encouragement, and check-in messages.</li>
 <li>The tutor team, particularly Michael Park, for his patience, tenacity, and perpetual willingness to help, no matter how late.</li>
 <li>Chris, whose Boutique Ado example served as a template and guide for me during this process, particularly at difficult times. This
 project would not have been possible with Chris' guidance.</li>
</ul>

<strong>This is for educational use.</strong>
