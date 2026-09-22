from flask import Flask, jsonify
import os
import psycopg2


app = Flask(__name__)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "task3db"),
        user=os.getenv("POSTGRES_USER", "task3user"),
        password=os.getenv("POSTGRES_PASSWORD", "task3pass"),
        port=5432,
        connect_timeout=3,
    )


@app.get("/")
def home():
    return jsonify({
        "project": "Task 3 - Docker Containerization",
        "status": "running"
    })


@app.get("/health")
def health():
    try:
        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT 1")
        cur.fetchone()

        cur.close()
        conn.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "unavailable",
            "error": str(e)
        }), 503


@app.post("/visit")
def visit():
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits "
        "(id SERIAL PRIMARY KEY, message TEXT NOT NULL)"
    )

    cur.execute(
        "INSERT INTO visits (message) VALUES (%s) RETURNING id",
        ("Docker persistence test",)
    )

    n = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"saved_id": n})


@app.get("/visits")
def visits():
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS visits "
        "(id SERIAL PRIMARY KEY, message TEXT NOT NULL)"
    )

    cur.execute("SELECT id, message FROM visits ORDER BY id")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": r[0], "message": r[1]}
        for r in rows
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
