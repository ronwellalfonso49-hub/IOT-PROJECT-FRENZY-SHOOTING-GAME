(function () {
    "use strict";

    const API_BASE = "/api";

    async function fetchStatus() {
        try {
            const res = await fetch(`${API_BASE}/status`);
            if (!res.ok) throw new Error("Failed to fetch status");
            const data = await res.json();
            updateDashboardStats(data);
            if (data.game_finished) {
                setTimeout(() => window.location.reload(), 600);
            }
        } catch (err) {
            console.error("Status fetch error:", err);
        }
    }

    function updateDashboardStats(data) {
        setText("stat-score", data.current_score);
        setText("stat-round", `${data.current_round} / ${data.total_rounds}`);
        setText("stat-hits", data.hits);
        setText("stat-misses", data.misses);
        setText("stat-accuracy", `${data.accuracy}%`);
        setText("stat-reaction", `${data.reaction_time} ms`);
    }

    function setText(id, value) {
        const el = document.getElementById(id);
        if (el) el.textContent = value;
    }

    async function submitMockRound() {
        const btn = document.getElementById("mock-round-btn");
        if (btn) {
            btn.disabled = true;
            btn.textContent = "Submitting...";
        }
        try {
            const res = await fetch(`${API_BASE}/round/mock`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
            });
            if (!res.ok) {
                const err = await res.json().catch(() => ({}));
                alert(err.error || "Failed to submit mock round");
                return;
            }
            await fetchStatus();
        } catch (err) {
            console.error(err);
            alert("Network error submitting mock round");
        } finally {
            if (btn) {
                btn.disabled = false;
                btn.textContent = "\u{1F3AF} Simulate Next Round (Mock)";
            }
        }
    }

    function initDashboard() {
        const mockBtn = document.getElementById("mock-round-btn");
        if (mockBtn) {
            mockBtn.addEventListener("click", submitMockRound);
        }

        const refreshBtn = document.getElementById("refresh-btn");
        if (refreshBtn) {
            refreshBtn.addEventListener("click", fetchStatus);
        }
    }

    document.addEventListener("DOMContentLoaded", initDashboard);
})();
