# REST Chess solver

This project involves creating a simple REST application to support the game of chess.

## Running from sources

### Docker setup

```bash
git clone https://github.com/kamilkaminski01/chess-solver
cd chess-solver/
make build
make start
```

### Local setup

```bash
pip install virtualenv
virtualenv venv

cd chess-solver/

source venv/bin/activate
pip install -r requirements.txt

cd app/
python app.py
```

The app will be available at `localhost:5000` and `127.0.0.1:5000`

### Troubleshooting

In case of errors with typing or missing dependencies, try to rebuild the
Docker image:

```bash
make clear
make build
```

If `make` is not supported, the associated Docker commands can be
used directly in order to build and run the project:

```bash
cd chess-solver/
docker build -t chess-solver .
docker run -d -p 5000:5000 --name chess-solver chess-solver
```

## Makefile

[`Makefile`](Makefile) contains common commands that can be used to build, run 
and test the project. The commands include:

- `build`: builds the project with Docker.
- `start`: runs the project in a Docker environment.
- `run`: runs the project.
- `stop`: stops the currently running Docker container.
- `clear`: stops the currently running Docker container and removes the project image.
- `lint`: performs static code checks.
- `pytest`: runs unit tests

## Code quality standards

All python code is formatted and verified by `black`, `flake8`,
`mypy` and `isort` tools. Their configurations can be found in the
[setup.cfg](app/setup.cfg) file.

Custom functions and methods use **type hints** to improve IDE code
completions, prevent from type errors and extend code documentation.
