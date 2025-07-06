# Django Project with Artists, Directions, and League Apps

This Django project comprises four interconnected apps: `artists`, `albums`, `directions`, and `league`. The project uses a PostgreSQL database (`allapps_db`) to store and retrieve data.

---

## Table of Contents

- [Project Overview](#project-overview)
- [App Descriptions](#app-descriptions)
  - [Artists](#artists)
  - [Albums](#albums)
  - [Directions](#directions)
  - [League (EPL)](#league-epl)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [License](#license)

---

## Project Overview

This Django-based project serves as a mini-ecosystem for managing:
- Music artists and their albums
- Travel distance directions between locations
- English Premier League historical season data

The application supports RESTful operations using Django REST Framework and persists data in a PostgreSQL database.

---

## App Descriptions

### Artists

Manages a list of music artists.

**Model Fields:**
- `id`: Auto-incremented primary key
- `created_at`: Timestamp of record creation
- `first_name`: Artist's first name
- `last_name`: Artist's last name
- `address`: Artist's address

**Features:**
- Add new artists
- Retrieve a list of all artists
- Retrieve a single artist by ID

---

### Albums

Each artist can have multiple albums.

**Model Fields:**
- `id`: Auto-incremented primary key
- `artist`: ForeignKey to the `Artist` model
- `name`: Name of the song/album

**Features:**
- Add albums associated with artists

---

### Directions

Calculates distance between two destinations.

**Model Fields:**
- `id`: Auto-incremented primary key
- `from_location`: Starting destination
- `to_location`: Ending destination
- `distance`: Distance between the two locations (calculated)

**Features:**
- Submit two destinations via POST
- Retrieve individual or all direction objects
- Update with PUT to trigger distance calculation

---

### League (EPL)

Manages English Premier League season statistics. Access restricted to superusers.

**Model Fields:**
- `id`: Auto-incremented primary key
- `season`: e.g., `2000/2001`
- `winner`, `second`, `third`, `fourth`
- `first_relegated`, `second_relegated`, `third_relegated`

**Features:**
- Create multiple league seasons (POST)
- Retrieve season data by ID
- PUT to calculate or fill in season details (simulated logic)

---

## Installation and Setup

1. **Clone the repository**
   ```
   git clone https://github.com/karianjahi/myapps.git
   cd myapps
   ```
2. Create virtual environment
    ```
    python -m venv env
    source env/bin/activate   # Windows: env\Scripts\activate
    ```

3. Install dependencies
    ```
    pip install -r requirements.txt
    ```

4. Configure PostgreSQL
- Ensure your PostgreSQL instance is running and update settings.py:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'allapps_db',
            'USER': 'your_db_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Apply migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create superuser
    ```
    python manage.py createsuperuser
    ```
7. Run the development server
```
python manage.py runserver
```

## API Endpoints
### Artists
- GET `/artists/` — List all artists

- GET `/artists/<id>/` — Get single artist

- POST `/artists/` — Create a new artist

### Albums
POST `/artists/albums/` -- Add an album to an artist

### Directions
- GET `/directions/` — List all entries

- GET `/directions/<id>/` — Get single entry

- POST `/directions/` — Submit two destinations

- PUT `/directions/<id>/` — Calculate and store distance

### League (Superuser only)
- POST `/league/` — Create a season

- GET `/league/` — List all seasons

- GET `/league/<id>/` — Retrieve season data

- PUT `/league/<id>/` — Simulate/update season details

## Authentication
The League app requires superuser authentication.

Use Django's admin interface or API tools (e.g., Postman) with credentials.

Token or Session Authentication (if enabled in settings).

## Usage Examples
### Create an Artist
```
POST /artists/
Content-Type: application/json

{
  "first_name": "Bob",
  "last_name": "Marley",
  "address": "Kingston, Jamaica"
}
```

### Submit Directions
```
- POST /directions/
Content-Type: application/json

{
  "from_location": "Berlin",
  "to_location": "Munich"
}
```
- Then trigger distance calculation:
`PUT /directions/1/`

### Create EPL Season
- Login as superuser, then:
```
POST /epl-table/
Content-Type: application/json

{
  "season": "2000/2001"
}
```

- Retrieve and simulate season stats:
GET /epl-table/1/
PUT /epl-table/1/

## License
This project is for educational and demonstration purposes only.

## Author
### Dr.rer.nat Joseph Karianjahi Njeri