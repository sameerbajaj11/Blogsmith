# Blogsmith

A Blogging application where anyone can come and share their articles for free.


# Implementation

1. Routing: Implemented routing using Django's path function for the entire project, directing requests to different apps.

2. Django ORM: Utilised Django's ORM to create database models, including a one-to-one relationship between User and Profile models.

3. User Authentication: Implemented user authentication and authorization, including signup and login forms with form validation using Django's built-in UserCreationForm    and crispy forms.

4. Signals: Implemented signals to automatically create a user profile with profile picture, username, and email whenever a new user registers.

5. Profile Update: Implemented functionality for users to update their profile information, including username, email, and profile picture, with automatic resizing of      images using Pillow.

6. Blog Post Creation, Update, and Delete: Implemented functionality for users to create, update, and delete blog posts, including restricting access to logged-in users    only using LoginRequiredMixin and UserPassesTestMixin.

7. Pagination: Implemented pagination for blog posts using Django's Paginator object, including custom filtering queries for separate pages for different users' posts.

8. Email and Password Reset: Implemented email and password reset functionality in Django, utilising tokens for secure and specific access.

9. Class-Based Views: Utilised Django's class-based views for all the implemented features, including list, detail, create, update, and delete views.

10.Image Resizing: Implemented automatic resizing of profile pictures using Pillow, optimising disk space and improving user experience.


