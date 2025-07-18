# Plot Point Reviews

**Live Site:** [Plot Point Reviews on Heroku](https://plotpoint-reviews-a2e2369bb816.herokuapp.com/)

Plot Point Reviews is a web application designed for book enthusiasts to discover, review, and discuss their favorite reads. Users can browse a curated list of books, read detailed reviews from fellow readers, and contribute their own ratings and opinions. The platform focuses on user-friendly navigation, accessibility, and fostering a community of engaged readers.

This project showcases a full-stack web application built with Python and Django, featuring a responsive front end and a backend with user authentication and data management.



## UX

The user experience prioritizes simplicity, clarity, and engagement. Visitors can easily browse the catalog, search for specific titles or authors, and access detailed reviews. Logged-in users can contribute their own reviews, add missing books, and manage their content, all through intuitive interfaces. The site also includes admin capabilities for content moderation and a responsive layout optimized for mobile, tablet, and desktop.

### Wireframes


![Wireframe start page](static/images/wireframestart.webp "Wireframe start page")
![Wireframe book page](static/images/wireframebook.webp "Wireframe book page")


![Wireframe start page tablet view](static/images/wireframestarttablet.webp "Wireframe start page table view")
![Wireframe book page tablet view](static/images/wireframebooktablet.webp "Wireframe book page tablet view")


![Wireframe start page phone view](static/images/wireframestartphone.webp "Wireframe start page phone view")
![Wireframe book page phone view](static/images/wireframebookphone.webp "Wireframe book page phone view")


### Colour Scheme

A dark-themed interface with contrasting light text, accented with muted colors for highlights and alerts.

### Typography

Uses Google Fonts with accessible font sizes and consistent hierarchy.

### Features

#### Existing Features

- Responsive navigation bar with login/logout and user-specific options

- Search functionality for books by title or author

- Paginated book list with cover, author, rating, and review count

- Book detail page with reviews and review form

- User registration and login/logout

- Add/edit/delete books and reviews

- Admin access for content moderation

#### Future Features

- Like/upvote reviews

- Book genres and filtering

- User profiles with review history

##  User Stories & Acceptance Criteria

### Site User

#### User Story: View Book List
**As a** Site User  
**I want to** see a list of books  
**so that** I can find something interesting to read or review.

**Acceptance Criteria:**
- A list displays the title, cover image, average rating, and number of reviews for each book.
- I can click on a book to view its detail page.

#### User Story: Read Reviews
**As a** Site User  
**I want to** read reviews  
**so that** I can decide whether a book is for me.

**Acceptance Criteria:**
- Reviews are visible on the book’s detail page.
- Each review includes the rating, review text, and the reviewer’s username.

#### User Story: Search for Books
**As a** Site User  
**I want to** search for books by title or author  
**so that** I can find specific books quickly.

**Acceptance Criteria:**
- I can use a search bar to enter a title or author.
- Matching results are displayed instantly.
- I see a message if no results are found.

---

### Logged-in User

#### User Story: Write a Review
**As a** logged-in user  
**I want to** write a review  
**so that** I can share my opinion about a book.

**Acceptance Criteria:**
- I can fill out a form with review text and a rating.
- My review appears on the book’s detail page after submission.
- I cannot submit more than one review for the same book.

#### User Story: Edit/Delete My Reviews
**As a** logged-in user  
**I want to** edit or delete my reviews  
**so that** I have control over my content.

**Acceptance Criteria:**
- I can see edit and delete buttons on my own reviews.
- I cannot edit or delete reviews written by other users.
- Updates are saved and reflected immediately.

#### User Story: Add New Books
**As a** logged-in user  
**I want to** add books that are missing  
**so that** I can review them.

**Acceptance Criteria:**
- I can submit a form with title, author, and a cover image.
- I receive an error message if the book already exists.
- The new book appears in the list after submission.

---

### Site Owner

#### User Story: Moderate Content
**As a** Site Owner  
**I want to** remove inappropriate reviews or books  
**so that** I can moderate the platform.

**Acceptance Criteria:**
- I can view and manage all books and reviews.
- I can delete any content that violates community guidelines.
- Regular users do not have access to these admin tools.

---

### New User

#### User Story: Register and Log In
**As a** New User  
**I want to** register and log in  
**so that** I can write reviews.

**Acceptance Criteria:**
- I can register using my email and password.
- I see relevant error messages if I enter incorrect data.
- After logging in, I can access review and book submission features.


# Database Design

## Entity relationship diagram

This Entity Relationship Diagram (ERD) illustrates the data structure of the book review web application. It shows how users can create reviews for books, and how books and reviews are linked through foreign key relationships.

![ERD](static/images/flowcharts.webp "ERD")

I used [Lucidchart](https://www.lucidchart.com/) to create the ERD.

# Tools & Technologies

VSCode\
Python / Django\
HTML / CSS\
Bootstrap\
Cloudinary (for image hosting)\
GitHub\
Gimp (for image editing)\
[Cloudconvert](https://cloudconvert.com/png-to-webp) (for image conversion)

# Testing

Each user story has been tested manually to ensure it meets the stated acceptance criteria. Screenshots were taken to document successful execution.

### Site User

- View Book List: Verified display of book cards and navigation to detail page. 
![Screenshot of homepage](static/images/testing/view_book_list.webp "Screenshot of homepage") 

- Read Reviews: Checked review content and formatting. 
![Screenshot of book detail with reviews](static/images/testing/view_book_detail.webp "Screenshot of book detail with reviews")

- Search for Books: Tested valid and invalid queries. 
![Screenshot of search results](static/images/testing/book_search.webp "Screenshot of search results") 
![Screenshot of invalid search](static/images/testing/no_books_found.webp "Screenshot of invalid search")

### Logged-in User

- Write a Review: Submitted a new review and saw it appear. 
![Screenshot of review success message](static/images/testing/add_review.webp "Screenshot of review success message")

- Edit/Delete Reviews: Edited and deleted own review. 
![Screenshot of delete confirmation message](static/images/testing/delete.webp "Screenshot of delete confirmation message")
![Screenshot of delete success message](static/images/testing/delete_success.webp "Screenshot of delete success message")
![Screenshot of edit view](static/images/testing/edit.webp "Screenshot of edit view")
![Screenshot of edit success message](static/images/testing/edit_success.webp "Screenshot of edit success message")

- Add New Books: Added a book, saw it appear in the list, and tested duplicate error. 
![Screenshot of add book success message](static/images/testing/add_book.webp "Screenshot of add book success message")
![Screenshot of duplicate error message](static/images/testing/add_fail_double.webp "Screenshot of duplicate error message")

### New User

- Register/Login: Created new account, tested login and logout.
![Screenshot of register page](static/images/testing/register.webp "Screenshot of register page")
![Screenshot of log in page](static/images/testing/login.webp "Screenshot of log in page")
![Screenshot of login success message](static/images/testing/login_success.webp "Screenshot of login success message")

### Site Owner

- Moderate Content: Logged in as admin and removed inappropriate content.
![Screenshot of Django admin interface](static/images/testing/admin_view.webp "Screenshot of Django admin interface")

All features were also tested on different screen sizes to ensure responsive layout.

## HTML Validation
Three key templates were tested using [W3C Markup Validation Service](https://validator.w3.org/) by copying rendered HTML from the browser’s "View Page Source" and validating via direct input:

- base.html (book list view)

- book_detail.html (book detail view)

- login.html (login page)

All tested pages returned:
“Document checking completed. No errors or warnings to show.”

This confirms that the HTML structure follows current web standards.

## CSS Validation

The custom CSS file (style.css) was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via direct input.
The result was:
“Congratulations! No Error Found.”

This confirms that the stylesheet is free from syntax errors and adheres to modern CSS standards.

## JavaScript Validation

No custom JavaScript was written for this project. All interactive functionality is handled by Bootstrap's built-in components and Django's templating system.

## Python Code Style Validation
To ensure that all Python code in the project follows the PEP8 style guide, the flake8 linter was installed and executed in the project root.

**Tool used:**

```
pip install flake8
```

**Command run:**

```
flake8
```

**Result:**
All Python files passed linting without errors. Minor warnings (such as line length or unused imports) were either addressed or deemed non-critical for functionality or readability.

## Lighthouse testing

![Screenshot of Lighthouse results](static/images/testing/lighthouse.webp "Screenshot of Lighthouse results")

The site was tested using Lighthouse, Google's automated tool for auditing web applications. The audit evaluated five key areas:

**Performance:** 94
The site loads efficiently with optimized static files and responsive design.

**Accessibility:** 92
Semantic HTML, proper use of labels, and good color contrast contribute to a high accessibility score.

**Best Practices:** 78
Most best practices are followed. One known issue relates to mixed content warnings from Cloudinary image URLs (see Known Issues below).

**SEO:** 100
Pages include appropriate meta tags, headings, and are fully indexable by search engines.

**Trust & Safety:**
Lighthouse flagged 9 insecure requests from images hosted on Cloudinary. These were automatically upgraded to HTTPS but still triggered a mixed content warning. This issue does not affect site functionality and is documented under Known Issues.

## Known Issues

![Screenshot of Lighthouse message](static/images/testing/lighthouse_bug.webp "Screenshot of Lighthouse message")

**Mixed Content Warning in Lighthouse Audit**
Despite all image uploads being hosted via Cloudinary and automatically upgraded to HTTPS, Lighthouse continues to report mixed content warnings related to image URLs beginning with http://.

**Cause:**
The warning appears to be triggered by image URLs initially stored or referenced with http:// before Cloudinary automatically redirects them to https://. This may stem from how the image URL is stored in the database after upload.

**Attempts to Fix:**
All relevant database entries were reviewed and updated using Django shell to replace http:// with https:// manually. The Cloudinary configuration in settings.py is also set up to serve media securely.

**Impact:**
The issue does not affect functionality, user experience, or actual security since Cloudinary handles automatic HTTPS upgrades. However, Lighthouse continues to flag it, which may impact the audit score.

**Resolution:**
Future iterations may involve handling the image URL more explicitly in the model or during upload to ensure secure URLs are saved directly.

# Deployment

The site is deployed on [Heroku](https://plotpoint-reviews-a2e2369bb816.herokuapp.com/).

To deploy this project to Heroku:

1. Install required packages:

```
pip install gunicorn whitenoise dj-database-url python-decouple cloudinary cloudinary-storage
```

2. Create a Procfile in your project root with:

```
web: gunicorn plotpointreviews.wsgi
```

3. Create runtime.txt with the Python version, e.g.:

```
python-3.12.3
```

4. Set the following in your settings.py:

- STATIC_URL and STATIC_ROOT

- STATICFILES_STORAGE to 'whitenoise.storage.CompressedManifestStaticFilesStorage'

- Use dj_database_url and decouple to handle DATABASES and SECRET_KEY

- Configure Cloudinary credentials with os.getenv()

5. Create a .env file with:

```
SECRET_KEY=your-secret-key
DEBUG=False
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

6. Set Heroku config vars matching your .env values:

```
heroku config:set SECRET_KEY=... DEBUG=False ...
```

7. Initialize a Git repository (if not already), commit your code, and push to Heroku:

```
git init
heroku git:remote -a your-app-name
git add .
git commit -m "Initial commit"
git push heroku main
```

If you're using GitHub deployment (instead of git push heroku main), connect your GitHub repo in the Heroku dashboard and enable automatic deploys.

8. Run migrations and create a superuser (optional):

```
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

9. Collect static files:

```
heroku run python manage.py collectstatic --noinput
```

# Credits

- All book reviews are written by me
- Book descriptions and covers were sourced from Amazon or Goodreads