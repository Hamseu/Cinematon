# Cinematon
## Description: Web-site for booking cinema tickets, working name `Cinematon`
### Web_dev group project members: Frolov Yevgeniy, Dias Mukashev, Nurbek Tazhenov


---

# Our goal:
We decided to make web-app for booking cinema tickets. Our app should be able to show films, 
film session, details of session including cinema, hall, time and cost. It should be comfortable to use by client.
Our app should use modern auth systems with at least some level of comfort and security.
Our client should be able to book multiple tickets at once and see them in their profile, able to delete if needed.
Our app should say if something is abnormal in its working.


---

# Our roles:
Backend and frontend logic: Frolov Yevgeniy.

FrontEnd component architecture and css styles: Nurbek Tazhenov.

Login, register html components and angular router: Dias Mukashev.


---


# Github architecture:
Main: Frolov Yevgeniy
Master: Frolov Yevgeniy
Nurbek-front: Nurbek Tazhenov
Features/register: Dias Mukashev

---

# Project Tools

` Angular 18+ `

` Django 6+ `

---

# Django Structure

## We have 6 models: 
`Ticket`: our ticket, constisting of session id, id, user, payment and seat, row 

`Hall`: hall of cinema, hall id, total seats, seats per row, rows, cinema id 

`Cinema`: Cinema, id, name, location fields 

`Film`: Film id, genre, length, title, imageUrl, description, release_year

`Session`: id, start_time, end_time, cost, hall, film, 

`User`:  Default user from django auth.

## We have cbv and fbv views(generics also).
FBVs are usually login related or just some simple logic.

CBVs are our main backbone.

Generics have only user

## Serializers

We have absolutely default serializers from modelSerializer and Serializer.

We weren't making custom solutions here

## Hosting rules:
Debug = true

Secure = off

host = localhost:8000

## Outside Connection of Django
1. Our db - postgres via Django standard config
2. Angular provider via CORS on localhost:4200, credentials allowed. CSRF allowed

## Endpoints:

# Authentication

### Register
`/register/ POST`

### Login
`/login/ POST`

### Refresh Token
`/login/refresh/ POST`

### Logout
`/logout/ POST`

### Current User
`/me/ GET`

---

# Films (CRUD)

### Get all films
`/films/ GET`

### Create film
`/films/ POST`

### Get film by ID
`/films/<film_id>/ GET`

### Update film
`/films/<film_id>/ PUT/PATCH`

### Delete film
`/films/<film_id>/ DELETE`

### Filter films by genre
`/films/genre/<genre>/ GET`

### Get film sessions
`/films/<film_id>/sessions/ GET`

---

# Cinemas (CRUD)

### Get all cinemas
`/cinemas/ GET`

### Create cinema
`/cinemas/ POST`

### Get cinema by ID
`/cinemas/<cinema_id>/ GET`

### Update cinema
`/cinemas/<cinema_id>/ PUT/PATCH`

### Delete cinema
`/cinemas/<cinema_id>/ DELETE`

### Get cinema halls
`/cinemas/<cinema_id>/halls/ GET`

---

# Halls (CRUD)

### Get all halls
`/halls/ GET`

### Create hall
`/halls/ POST`

### Get hall by ID
`/halls/<hall_id>/ GET`

### Update hall
`/halls/<hall_id>/ PUT/PATCH`

### Delete hall
`/halls/<hall_id>/ DELETE`

### Get hall sessions
`/halls/<hall_id>/sessions/ GET`

---

# Sessions (CRUD)

### Get all sessions
`/sessions/ GET`

### Create session
`/sessions/ POST`

### Get session by ID
`/sessions/<session_id>/ GET`

### Update session
`/sessions/<session_id>/ PUT/PATCH`

### Delete session
`/sessions/<session_id>/ DELETE`

### Get session tickets
`/sessions/<session_id>/tickets/ GET`

---

# Tickets (CRUD)

### Get all tickets
`/tickets/ GET`

### Create ticket
`/tickets/ POST`

### Get ticket by ID
`/tickets/<ticket_id>/ GET`

### Update ticket
`/tickets/<ticket_id>/ PUT/PATCH`

### Delete ticket
`/tickets/<ticket_id>/ DELETE`

### My tickets
`/tickets/my/ GET`


- All models support full CRUD operations (GET, POST, PUT/PATCH, DELETE)
- Nested structure:
  cinemas → halls → sessions → tickets
- Auth required for user-specific endpoints and tickets overall:
  - /tickets/
  - /tickets/id
  - /me/
  - /tickets/my/

---

# Angular Structure

- Number of components: 7 + 2(interceptor and service)
- Home: Display of all our films.
- Ticket(film details): Display of ticket details and available sessions
- Login: Login page.
- Register: Register page.
- Movie-card: Movie cards for Home.
- Profile: Profile of auth. user.
- Hall-component: Component for making hall abstraction and ticket booking logic

- Httpserf: Rest API HTTP service
- AuthInterceptor: Request interceptor(Sends credentials and implements auto-refresh)

---

# Rules of usage

Anonims can observe films and sesions with, but only user can create, get tickets.

User of webapp doesn't have physicall access to change something in our db but tickets.


# We are tried to implement cold, calm and peaceful interface.

---

We have one subroute - hall component , which is subroute of ticket(film details) route


---

# Project Cinematon is made by Frolov Yevgeniy, Dias Mukashev, Nurbek Tazhenov.

Enjoy your film

