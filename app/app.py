from typing import Dict

from flask import Flask, Response, jsonify, make_response

from exceptions import APIExceptions
from figures import figures
from utils import is_valid_field

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>REST Chess Solver</h1>"


@app.route("/api/v1/<string:chess_figure>/<string:current_field>", methods=["GET"])
def list_moves(chess_figure: str, current_field: str) -> Response:
    response: Dict = {
        "availableMoves": [],
        "error": None,
        "figure": chess_figure,
        "currentField": current_field.upper(),
    }

    figure_class = figures.get(chess_figure.lower())

    if not figure_class:
        response["error"] = APIExceptions.FigureNotFound
        return make_response(jsonify(response), 404)

    if not is_valid_field(current_field):
        response["error"] = APIExceptions.FieldNotFound
        return make_response(jsonify(response), 409)

    figure_instance = figure_class(current_field)
    available_moves = figure_instance.list_available_moves()

    response["availableMoves"] = available_moves
    return make_response(jsonify(response), 200)


@app.route(
    "/api/v1/<string:chess_figure>/<string:current_field>/<string:dest_field>",
    methods=["GET"],
)
def validate_move(chess_figure: str, current_field: str, dest_field: str) -> Response:
    response: Dict = {
        "move": "",
        "figure": chess_figure,
        "error": None,
        "currentField": current_field.upper(),
        "destField": dest_field.upper(),
    }

    figure_class = figures.get(chess_figure.lower())

    if not figure_class:
        response["error"] = APIExceptions.FigureNotFound
        return make_response(jsonify(response), 404)

    if not is_valid_field(current_field):
        response["error"] = APIExceptions.FieldNotFound
        return make_response(jsonify(response), 409)

    if not is_valid_field(dest_field):
        response["error"] = APIExceptions.DestinationFieldNotFound
        return make_response(jsonify(response), 409)

    figure_instance = figure_class(current_field)
    valid_move = figure_instance.validate_move(dest_field)

    if valid_move:
        response["move"] = "valid"
        status_code = 200
    else:
        response["move"] = "invalid"
        response["error"] = APIExceptions.InvalidMove
        status_code = 409
    return make_response(jsonify(response), status_code)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
