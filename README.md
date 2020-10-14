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
 
 Here is the responsiveness preview:
 ![Responsive View](assets/responsiveview.gif)

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
<p><i>What am I aiming to achieve with this project, and for whom?</i></p>
<p>The target audience for this project is anyone who is interested in minimalist men's fashion. Ideally, the target audience
would be looking for an online clothing store that primarly stocks men's wear that is both minimalist and stylish.</p>
<p>My aim with this project is to provide a one-stop-shop for minimalist men's wear. Oftentimes, it is necessary to visit several
stores in order to find numerous minimalistic and fashionable pieces, especially for men. But typically speaking, there really aren't many
places that one can go to find a wide selection of minimalist men's wear.</p>

### Scope
The purpose of this undertaking is to display my skills and projects in a way that is quick, simple and intuitive. It is meant to serve as a portfolio, showcasing my professional journey and career trajectory.<p>
  
Having worked in the recuitment space, I understand that recruitrs and employers often don't have the time to sift through detailed resumés and portfolios. Additionally, being a marketing professional, I also understand that the attention span of the average buyer/user is growing shorter by the decade. Advertisements and promotions must be able to arrest attention and or convey a message within 2 seconds, lest they risk losing the onlooker forever.<p>

Therefore, this portfolio will be slightly more narrow in scope than some others out there, and <strong>it will prioritise the more "at-a-glance" and "on-the-go" user.</strong>

### Surface
I decided to go with the blue, white, and pink colour scheme because my research showed that seemed to be a happy medium between a colour-blindness friendly aesthetic and an eye-catching and dynamic design. Many sources agreed that a minimalistic design was best so I opted to keep the general layout clean, clear, uncluttered.<p>

From a purely stylistic point of view, I myself do favour the combination of blue and white anyway, for its minimalism, modern feel, and timeless quality. However, I decided to add a pop of pink to evoke a sense of dynamism and creativity, as I find that one of the few failings of blue and white coupled together is that it can come across a little boring, repetitive, and uninspired at times.

I must add that I was inititially going to go with a predominatly greyscale scheme because it is by far the most colour-blindness friendly aesthetic, however, that felt a little too bland for my personal taste. So, I eventually opted to go for a white, blue, and pink combination while still designing with colour-blindness in mind in the places that I could. This is why I added texure and animations to the skill bars because research shows it is much easier for colour-blind individual to make out things that are textured or moving on a screen.<p>
 
### Skeleton
 <ul>
    <li>Landing Page</li>
    <li>About</li>
    <li>Skills</li>
    <li>Projects</li>
    <li>Contact</li>
</ul>

### Structure
[Here](wireframes) are a list of the wireframes I developed during the inital mock-up. They are quite self-explanatory and rudimentary, but they didn't need to be overly compelx. They merely needed to serve as a base for me to extrapolate upon. Two of the wireframes had to be redone because I was having trouble with creating responsive speechbubbles, so I opted for basic rectangles instead because they are far easier to make responsive. This is in reference to the about page and the projects page, so you will see two wireframes for each of those. 

### Features
<ul>
  <li>I opted to use a single page format to make navigation much simpler and intuitive, meaning the user doesn't need to click back and forth between pages.</li>
  <li>The default setting for the navbar seemed to create a very stark and jarring transition to whatever you clicked on. It wasn't a very smooth effect. So, I opted for a smooth scrolling effect instead of just appearing on whatever navbar item you click on, and this made for a much nicer, more fluid experience.</li>
  <li>I made the skill progress bars textured and animated because my research showed that it is often easier for colour-blind individuals to make out things that are textured and or moving on a screen.</li>
 <li>I created the footer to mirror the navbar in design, being black. This made for a very balanced and symmetrical visual experience when both were present and visible on the screen.</li>
 <li>I included social media links in the footer and added a small rotation and colour changing animation to help enhance their visibility and presence.</li>
</ul>

### Features left to implement
<ul>
  <li>I would like to develop a  better way to display my projects. As it is now, it isn't so bad because there aren't many to show. But, in the future, I will need to come up with a more econonic use of space in that section.</li>
  <li>I would like to add an education sections to display that information more clearly and give it its own section. As it is now, it's mentioned in the About section, but I feel it would stand out more if it were given its own place.</li>
  <li>I would like to improve the site's overall look by finding a more uniservsally suitable colour-scheme, because it became clear in the latter part of my testing phase that the pink I had chosen can appear very harsh for some people. An example of this is provided further below in the testing section of this readme. 

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
