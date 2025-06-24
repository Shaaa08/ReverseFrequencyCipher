from flask import Flask, render_template, request

app = Flask(__name__)

freq_letters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
reverse_freq_letters = freq_letters[::-1]
encryption_map = dict(zip(freq_letters, reverse_freq_letters))
decryption_map = dict(zip(reverse_freq_letters, freq_letters))

def encrypt_rfc(plaintext):
    return ''.join(encryption_map.get(c.upper(), c) for c in plaintext)

def decrypt_rfc(ciphertext):
    return ''.join(decryption_map.get(c.upper(), c) for c in ciphertext)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        action = request.form.get("action")
        if action == "encrypt":
            result = encrypt_rfc(text)
        elif action == "decrypt":
            result = decrypt_rfc(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
