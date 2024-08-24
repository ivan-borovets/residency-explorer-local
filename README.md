# Residency Explorer Local

`residency-explorer-local` is a locally hosted web app that simplifies
managing data about medical residency programs in the US, aiding prospective
residents in making informed decisions during the Residency Match process.

![ProgramOverview](media/01ProgramOverview.png)
![DirectorOverview](media/02DirectorOverview.png)

## Features

- **User-Friendly Data Entry**: Easily input information about medical
  residency programs through intuitive forms.
  ![ProgramCreate](media/03ProgramCreate.png)
  ![ProgStatCreate](media/04ProgStatCreate.png)
  ![DirectorCreate](media/05DirectorCreate.png)

- **Table View**: Data is presented in well-organized tables, making it easy
  to review and manage.
  ![Programs](media/06Programs.png)
  ![ProgramStat](media/07ProgramStat.png)
  ![DirectorsAnn](media/08DirectorsAnn.png)
  ![Peers](media/09Peers.png)

- **Instant Filtering and Sorting**: Real-time data filtering and sorting
  within tables, no page reload needed.
  ![](media/10SortedPO.png)
  ![](media/11OrderedPOAnn.png)

## Installation and Setup (for Windows users)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Generate the `.env` file. This step is required only once during the
   installation.

   2.1. Open `PowerShell`

   2.2. Navigate to the root directory of the project

   2.3. Run
      ```bash
      python ./scripts/generate_dotenv/dotenv_from_toml.py
      ```

## Running the Application (for Windows users)

### First-Time Launch

1. Ensure the `.env` file is present in the root directory of the project.
2. From the root of the project, open PowerShell and run the following command:

```bash
docker compose up --build
```

This will build and start the application. Once the application is ready,
you will be prompted to visit [0.0.0.0:8888](http://0.0.0.0:8888) in your browser.

### Subsequent Launches

After the first launch, you can start and manage the application directly
from `Docker Desktop`.

Open `Docker Desktop` and navigate to the `Containers` section.
You will find a shortcut to start the application under the
`residency-explorer-local` container.
After starting the container, you can click on the link labeled `8888:8888`
to open the application in your browser.
**It is recommended to stop** the application in `Docker Desktop` when
you're done using it to free up system resources.

![DockerAnn](media/12DockerAnn.png)

## For Developers

### Stack

#### Backend:

- `Python 3.12`: Core programming language for the app.
- `Uvicorn`: ASGI server for running the app.

#### Database:

- `PostgreSQL`: Relational database for data storage.
- `SQLAlchemy`: ORM for database interactions.
- `Psycopg2`: Synchronous PostgreSQL adapter for Python.

> Because `starlette-admin` seem not to support async engines

- `Alembic`: Database migrations tool for SQLAlchemy.

#### Data Management:

- `Pydantic`: Data validation and type checking.
- `Pydantic-Settings`: Handling of env variables and settings.
- `Rtoml`: TOML configuration file parser.

#### Admin Interface:

- [`Starlette-admin`](https://github.com/jowilf/starlette-admin): Provides a web interface for managing the database.

### Database schema

![Database Schema](media/13ERD_Residency.png)

### Customization

The primary configuration file for the application is `config.toml`.
After making any changes to this file, you must generate a new `.env` file.
This can be done using the scripts available in the
`./scripts/generate_dotenv/` directory for either `Python` or `Bash`.

Alternatively, you can use the following Makefile commands to generate the `.env` file:

For Python:

```bash
make dotenv.py
```

For Bash:

```bash
make dotenv.sh
```

It's important to ensure that the `.env` file is correct, as only with
a properly configured `.env` will the

```bash
docker compose up --build
``` 

function correctly. 
