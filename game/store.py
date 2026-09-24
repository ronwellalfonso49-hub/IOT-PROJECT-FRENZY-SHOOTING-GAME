import random
from typing import List, Dict, Optional


class GameStore:
    def __init__(self):
        self.current_round: int = 0
        self.total_rounds: int = 3
        self.game_started: bool = False
        self.game_finished: bool = False
        self.rounds: List[Dict] = []
        self.mock_mode: bool = True

    def reset_game(self):
        self.current_round = 0
        self.game_started = False
        self.game_finished = False
        self.rounds = []

    def start_game(self, total_rounds: int = 3):
        self.reset_game()
        self.total_rounds = total_rounds
        self.game_started = True
        self.current_round = 1
        return self.get_dashboard_data()

    def add_round(self, round_number: int, hits: int, misses: int,
                  accuracy: float, reaction_time: float, score: int) -> Dict:
        round_data = {
            "round_number": round_number,
            "hits": hits,
            "misses": misses,
            "accuracy": accuracy,
            "reaction_time": reaction_time,
            "score": score,
        }
        self.rounds.append(round_data)

        if round_number >= self.total_rounds:
            self.game_finished = True
            self.current_round = self.total_rounds
        else:
            self.current_round = round_number + 1

        return round_data

    def generate_mock_round(self) -> Dict:
        round_number = self.current_round
        hits = random.randint(3, 10)
        misses = random.randint(0, 5)
        total_shots = hits + misses
        accuracy = round((hits / total_shots) * 100, 2) if total_shots > 0 else 0.0
        reaction_time = round(random.uniform(200, 800), 2)
        base_score = hits * 100
        accuracy_bonus = int(accuracy * 2)
        speed_bonus = max(0, int((1000 - reaction_time) * 0.2))
        score = base_score + accuracy_bonus + speed_bonus

        return self.add_round(
            round_number=round_number,
            hits=hits,
            misses=misses,
            accuracy=accuracy,
            reaction_time=reaction_time,
            score=score,
        )

    def get_dashboard_data(self) -> Dict:
        if not self.game_started:
            return {
                "game_title": "Frenzy",
                "game_started": False,
                "game_finished": False,
                "total_rounds": self.total_rounds,
                "current_round": 0,
                "current_score": 0,
                "hits": 0,
                "misses": 0,
                "accuracy": 0.0,
                "reaction_time": 0.0,
            }

        latest_round = self.rounds[-1] if self.rounds else None
        total_hits = sum(r["hits"] for r in self.rounds)
        total_misses = sum(r["misses"] for r in self.rounds)
        total_shots = total_hits + total_misses
        avg_accuracy = (
            round((total_hits / total_shots) * 100, 2) if total_shots > 0 else 0.0
        )
        total_score = sum(r["score"] for r in self.rounds)
        avg_reaction = (
            round(sum(r["reaction_time"] for r in self.rounds) / len(self.rounds), 2)
            if self.rounds
            else 0.0
        )

        return {
            "game_title": "Frenzy",
            "game_started": True,
            "game_finished": self.game_finished,
            "total_rounds": self.total_rounds,
            "current_round": self.current_round,
            "current_score": total_score,
            "hits": latest_round["hits"] if latest_round else 0,
            "misses": latest_round["misses"] if latest_round else 0,
            "accuracy": latest_round["accuracy"] if latest_round else avg_accuracy,
            "reaction_time": latest_round["reaction_time"] if latest_round else avg_reaction,
        }

    def get_rounds_data(self) -> List[Dict]:
        return list(self.rounds)

    def get_final_results(self) -> Optional[Dict]:
        if not self.rounds:
            return None

        total_hits = sum(r["hits"] for r in self.rounds)
        total_misses = sum(r["misses"] for r in self.rounds)
        total_shots = total_hits + total_misses
        avg_accuracy = (
            round((total_hits / total_shots) * 100, 2) if total_shots > 0 else 0.0
        )
        total_score = sum(r["score"] for r in self.rounds)
        avg_reaction = (
            round(sum(r["reaction_time"] for r in self.rounds) / len(self.rounds), 2)
            if self.rounds
            else 0.0
        )

        return {
            "total_hits": total_hits,
            "total_misses": total_misses,
            "average_accuracy": avg_accuracy,
            "average_reaction_time": avg_reaction,
            "total_score": total_score,
            "performance_level": "TBD - ML module pending",
            "intelligent_remarks": "TBD - AI remarks pending",
        }


game_store = GameStore()
