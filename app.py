from flask import Flask, render_template, request, session, send_file, redirect, url_for
from collections import Counter
import random
import io

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for session

# Fixed frequency maps (simplified example)
freq_letters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
reverse_freq_letters = freq_letters[::-1]
encryption_map = dict(zip(freq_letters, reverse_freq_letters))
decryption_map = dict(zip(reverse_freq_letters, freq_letters))

# Simple RFC
def encrypt_rfc(plaintext):
    return ''.join(encryption_map.get(c.upper(), c) for c in plaintext)

def decrypt_rfc(ciphertext):
    return ''.join(decryption_map.get(c.upper(), c) for c in ciphertext)

# Transposition layer (simple reverse for both)
def apply_transposition(text):
    return text[::-1]

def reverse_transposition(text):
    return text[::-1]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        text = request.form.get("text", "")
        action = request.form.get("action")
        
        if action == "encrypt":
            encrypted = encrypt_rfc(text)
            rounds = int(request.form.get("rounds", 1))
            for _ in range(rounds):
                encrypted = apply_transposition(encrypted)
            result = encrypted
            session["history"].append({
                "action": "Encrypt",
                "input": text,
                "output": result
            })

        elif action == "decrypt":
            reversed_text = reverse_transposition(text)
            result = decrypt_rfc(reversed_text)
            session["history"].append({
                "action": "Decrypt",
                "input": text,
                "output": result
            })

        session.modified = True  # Required to update session

    return render_template("index.html", result=result, history=session.get("history", []))

@app.route("/save-history")
def save_history():
    history = session.get("history", [])
    if not history:
        return "No history to save."

    output = io.StringIO()
    for i, entry in enumerate(history, 1):
        output.write(f"{i}. Action: {entry['action']}\n")
        output.write(f"   Input : {entry['input']}\n")
        output.write(f"   Output: {entry['output']}\n\n")
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name="cipher_history.txt"
    )

@app.route("/clear-history")
def clear_history():
    session["history"] = []
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)