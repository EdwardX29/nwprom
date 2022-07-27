# NWProm [website](https://nwprom.herokuapp.com)

![Project Image](https://raw.githubusercontent.com/EdwardX29/nwprom/main/.github/images/nwprom1.png)



---
### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [Author Info](#author-info)

---

## Description

NWProm is a prototype web app for prom date matchmaking. Facilitated anonymous, embarrassment-free prom partner seeking. This website was inspired by [TerpMatch](https://dbknews.com/2019/12/06/umd-terpmatch-dating-website-anonymous/), a matchmaking website for University of Maryland students, and sought to stay true to the original design. **100+ users assisted**.

#### Technologies:

- Python Django MVT
- Bootstrap 5
- Google Single Sign On w/ [Django Social Auth](https://pypi.org/project/django-social-auth/)
- PostgreSQL
- Heroku

[Back To The Top](#nwprom-website)

---

## How To Use

#### Step-by-Step Guide:
  1. Go to https://nwprom.herokuapp.com/
  2. Sign up with Google
  3. Enter your prospective prom dates (name & year)
  4. If a match is made, it will appear
 ![Project Image](https://raw.githubusercontent.com/EdwardX29/nwprom/main/.github/images/nwpromMatch.png)


#### Local Installation 
Clone the repo and run the following in your terminal:
```shell
pip install -r requirements.txt # collect packages
python manage.py makemigrations # prepare migrations
python manage.py migrate # migrate database
```



[Back To The Top](#nwprom-website)

---

## References
[Back To The Top](#nwprom-website)
- [TerpMatch Article](https://dbknews.com/2019/12/06/umd-terpmatch-dating-website-anonymous/)
- [Django Social Auth Library](https://pypi.org/project/django-social-auth/)
---

## Author Info

- Github - [EdwardX29](https://github.com/edwardx29)

[Back To The Top](#nwprom-website)