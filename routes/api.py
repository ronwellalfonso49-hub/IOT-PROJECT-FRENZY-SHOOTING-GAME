from flask import Blueprint, request, jsonify
from game.store import game_store

api_bp = Blueprint("api", __name__)


@api_bp.route("/status", methods=["GET"])
def get_status():
    data = game_store.get_dashboard_data()
    return jsonify(data)


@api_bp.route("/round", methods=["POST"])
def submit_round():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400

    required = ["round_number", "hits", "misses", "accuracy", "reaction_time", "score"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    round_data = game_store.add_round(
        round_number=int(data["round_number"]),
        hits=int(data["hits"]),
        misses=int(data["misses"]),
        accuracy=float(data["accuracy"]),
        reaction_time=float(data["reaction_time"]),
        score=int(data["score"]),
    )
    return jsonify(round_data), 201


@api_bp.route("/round/mock", methods=["POST"])
def submit_mock_round():
    if not game_store.game_started:
        return jsonify({"error": "Game not started"}), 400
    if game_store.game_finished:
        return jsonify({"error": "Game already finished"}), 400
    round_data = game_store.generate_mock_round()
    return jsonify(round_data), 201


@api_bp.route("/start", methods=["POST"])
def api_start_game():
    body = request.get_json(silent=True) or {}
    total_rounds = int(body.get("total_rounds", 3))
    data = game_store.start_game(total_rounds=total_rounds)
    return jsonify(data), 201


@api_bp.route("/rounds", methods=["GET"])
def get_rounds():
    rounds = game_store.get_rounds_data()
    return jsonify(rounds)


@api_bp.route("/final", methods=["GET"])
def get_final():
    results = game_store.get_final_results()
    if results is None:
        return jsonify({"error": "No data yet"}), 404
    return jsonify(results)


@api_bp.route("/reset", methods=["POST"])
def api_reset():
    game_store.reset_game()
    return jsonify({"status": "ok"})
