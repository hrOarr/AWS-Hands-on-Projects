from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import logging
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

# -------- READ --------
@app.route("/api/events", methods=["GET"])
def get_events():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, title, description FROM events ORDER BY id")
        )
        events = [dict(row._mapping) for row in result]
    return jsonify(events)

# -------- CREATE --------
@app.route("/api/events", methods=["POST"])
def create_event():
    data = request.json
    app.logger.info("Creating events")
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO events (title, description)
                VALUES (:title, :description)
            """),
            data
        )
    return jsonify({"message": "Event created"}), 201

# -------- UPDATE --------
@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    with engine.begin() as conn:
        conn.execute(
            text("""
                UPDATE events
                SET title=:title, description=:description
                WHERE id=:id
            """),
            {"id": event_id, **data}
        )
    return jsonify({"message": "Event updated"})

# -------- DELETE --------
@app.route("/api/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    with engine.begin() as conn:
        conn.execute(
            text("DELETE FROM events WHERE id=:id"),
            {"id": event_id}
        )
    return jsonify({"message": "Event deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)