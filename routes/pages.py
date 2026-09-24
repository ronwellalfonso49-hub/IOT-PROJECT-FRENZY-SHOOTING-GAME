from flask import Blueprint, render_template, redirect, url_for
from game.store import game_store

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def dashboard():
    data = game_store.get_dashboard_data()
    return render_template("dashboard.html", **data)


@pages_bp.route("/start", methods=["POST"])
def start_game():
    game_store.start_game(total_rounds=3)
    return redirect(url_for("pages.dashboard"))


@pages_bp.route("/rounds")
def round_results():
    rounds = game_store.get_rounds_data()
    return render_template("round_results.html", rounds=rounds)


@pages_bp.route("/final")
def final_results():
    results = game_store.get_final_results()
    return render_template("final_results.html", results=results)


@pages_bp.route("/reset", methods=["POST"])
def reset_game():
    game_store.reset_game()
    return redirect(url_for("pages.dashboard"))
