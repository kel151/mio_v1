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

# Features
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

## Features Left To Implemented
<ul>
  <li>The option for the user to log in using their social media account.</li>
  <li>The option of next day delivery</li>
  <li>A "New In" section that displays items recently added to the stock.</li>
  <li>An "On Sale" section that displays items that are on sale.</li>
  <li>A "bookmarking" feature that allows the user to mark items they're interested in, but not willing or able 
  to purchase at that particular moment. A list of their bookmarked items would be stored in their profile.<li>
</ul>

## Technologies Used
<ul>
    <li><a href="https://code.visualstudio.com/">Visual Code Studio</a> - code editor used for this project.<p></li>
    <li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - to create the structure of the project and define the "skeleton", so to     speak.<p></li>
    <li><a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">CSS</a> - to design and style the project, adding the "flesh to       the skeleton", so to speak<p></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a> - used as a framework to make design faster and easier.<p></li>
    <li><a href="https://git-scm.com/">Git</a> - used for version control.<p></li>
    <li><a href="https://fontawesome.com/">Font Awesome</a> - used for social media icons.<p></li>
    <li><a href="https://htmlformatter.com//">HTML Formatter</a> - used to beautify html.<p></li>
    <li><a href="https://www.cleancss.com/css-beautify/">CSS Formatter</a> - used to beautify css.<p></li>
    <li><a href="http://ami.responsivedesign.is/">Am I Responsive?</a> - used to test responsiveness.<p></li>
    <li><a href="https://www.javascript.com/">JavaScript</a> - used with Bootstrap.<p></li>
    <li><a href="https://jquery.com/">JQuery</a> - used to support Java Script.<p></li>
</ul>
  
### Additional resources and tools
<ul>
  <li><a href="https://www.w3schools.com/">W3 Schools</a><p></li>
  <li><a href="https://stackoverflow.com/">Stack Overflow</a><p></li>
  <li><a href="https://css-tricks.com/">CSS-Tricks</a><p></li></li>
  <li><a href="https://github.com/">GitHub</a><p></li>
  <li><a href="https://www.youtube.com/">Youtube</a> - used for various tutorials. I find that I am a visual learner i.e. I learn better by watching others do, so I used YouTube tutorials for help pertaining to certain things I find tricky, such as the <a href="https://www.youtube.com/watch?v=23bpce-5s8I">nav bar</a> and the <a href="https://www.youtube.com/watch?v=woVuUbDOeMk&t=5s)">social media links</a><p></li> 
</ul>

## Testing
The first step of my testing began by using <a href="http://ami.responsivedesign.is/">Am I Responsive?</a> to deduce whether my project was indeed responsive and compatible across all devices, the results of which can be observed at the beginning of this readme in the responsiveness preview.

The second stage involved sharing the deployed link with a few colleagues and friends to double check whether it was actually responsive or not, and this is where I ran into a curious issue. It would seem that the particular shade of pink that I used may appear differently on different devices, and this will probably negatively impact visbility for effected users. Below you will a screenshot of what how the site appears to me and most users compared to another screenshot of how it appears to a select few.

This is what most users (myself included) see:
![Colour Difference 1](assets/img/colourdiff1.PNG)

This is what a small number of users may see:
![Colour Difference 2](assets/img/colourdiff2.jpg)

This occurs regardless of using DevTools or sites like Am I Responsive. So, essentially, if the colour appears correctly for you, then it will do so no matter what medium you view it through. Unfortunately, the same is true vice versa. While I remain unsure what the exact cause of this is, it would appear that this is may be due to one's individual device settings. This issue does seem to be localised to the minority, meaning that for the average user the project should appear normally. But this finding has given me a note of improvement and points me towards something that I can work to make better in the future.

The third step of my testing involved the utilization of [Code Verifier](https://validator.w3.org/), which yielded the following result:
![Code Verifier Test](assets/img/cvtest.PNG)

## Deployment
This site is hosted on GitHub pages and it's deployed directly using the master branch. The deployed site will update automatically when new commits are made and then pushed from VSCode. To deploy the site correctly, the landing page must be named 'index.html'.

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/kel151/1stmilestoneproject.git into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

## Credit
### Content
All of text in the "About/A Little About Me..." section was written by me.

### Media
The images used in this project were taken from <a href="https://undraw.co/">Undraw</a>, an open license and highly customizable resource that I greatly recommend. 

## Colour-blindness research sources:
Tuchkov, I. 2018. http://www.garethbotha.com/color-blindness-usability-testing/. Accessed: November 5th 2019.<p>

Bigman, A. 2012. <a href="https://99designs.ie/blog/tips/designers-need-to-understand-color-blindness/">Why all designers need to understand color blindness</a>. Accessed: November 5th 2019.

Hiller, L. 2018. <a href="https://econsultancy.com/considering-colour-blindness-in-ux-design-with-five-examples/">Considering colour blindness in UX design (with five examples)</a>. Accessed: November 5th 2019.
  
Cravit, R. 2019. <a href="https://venngage.com/blog/color-blind-friendly-palette/">How to Use Color Blind Friendly Palettes to Make Your Charts Accessible</a>. Accessed: November 5th 2019.

Botha, G. 2017. <a href="http://www.garethbotha.com/color-blindness-usability-testing/">Color Blindness in Usability Testing</a>. Accessed: November 5th 2019.

## Acknowledgements
<ul>
 <li>My mentor, Aaron Sinnot, for all of his patience, advice, and recommendations.</li>
 <li>My friend and fellow member of the Code Institute Slack Community, Mia, for all of her advice, kindness, and encouragement.</li>
 <li>The Student Care team, particularly Claire Lally, for the constant support, encouragement, and check-in messages.</li>
 <li>Anthony O'Brien, a fellow member of the Code Institute Slack Community, for his patience, tenacity, and perpetual willingness to help, no matter how late.</li>
</ul>

The inspiration for this project came from <a href="https://github.com/Code-Institute-Solutions/StudentExampleProjectGradeFive">a portfolio by Haley Schafer</a>, which was used to expemplify what a high quality milestone 1 project could be.

<strong>This is for educational use.</strong>
