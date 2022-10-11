# Walletdotlog

An expense tracker app. Just a basic CRUD api that I did all on my own without following the tutorial for practicing my django skills.

## Features

- CRUD
- Authentication
- Email confirmation
- Social Login

## Tech Stack

**Client:** React, ReactQuery, TailwindCSS, DaisyUI

**Server:** Django, DjangoRestFramework

## Lessons Learned

I learned a lot building this project. I wanna point out 2 things. First one is authentication and permission. It was a pain in the ass. I learned about different kinds of authentication such as Session based authentication, Token based authentication([JWT](https://jwt.io/)) and [Oauth 2.0](https://oauth.net/2/) along with OpenIdConnect. I managed to sove the authentication need for this project by using these packages - [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/index.html), [django-allauth](https://django-allauth.readthedocs.io/en/latest/) and [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/). My knowledge on this topic after building this project is still in an embryo stage. I have a long way to go deep.

Second one is basic SQL and a little bit about postgresql. I don't know much about either of these as I just used the django's build-in ORM.

## Feedback

If you have any feedback, please reach out to me at ahnge226@gmail.com

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://nayzaw.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nayzaw-minnaing/)

## Related

Here is the related [frontend project.](https://github.com/ahnge/walletdotlog-fe/)
