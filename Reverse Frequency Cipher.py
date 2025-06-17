import tkinter as tk
from tkinter import messagebox

# Reverse Frequency Cipher Logic
freq_letters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
reverse_freq_letters = freq_letters[::-1]

encryption_map = dict(zip(freq_letters, reverse_freq_letters))
decryption_map = dict(zip(reverse_freq_letters, freq_letters))

def encrypt_rfc(plaintext):
    ciphertext = ''
    for char in plaintext.upper():
        if char in encryption_map:
            ciphertext += encryption_map[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt_rfc(ciphertext):
    plaintext = ''
    for char in ciphertext.upper():
        if char in decryption_map:
            plaintext += decryption_map[char]
        else:
            plaintext += char
    return plaintext

# === GUI Setup ===
def create_gui():
    def on_encrypt():
        msg = input_text.get("1.0", tk.END).strip()
        if msg:
            encrypted = encrypt_rfc(msg)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"🔐 Encrypt: {encrypted}")
        else:
            messagebox.showwarning("Input Required", "Please enter a message to encrypt.")

    def on_decrypt():
        msg = input_text.get("1.0", tk.END).strip()
        if msg:
            decrypted = decrypt_rfc(msg)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"🔓 Decrypt: {decrypted}")
        else:
            messagebox.showwarning("Input Required", "Please enter a message to decrypt.")

    def on_reset():
        input_text.delete("1.0", tk.END)
        result_text.delete("1.0", tk.END)

    def on_save():
        content = result_text.get("1.0", tk.END).strip()
        if content:
            try:
                with open("result.txt", "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Success", "Result saved to result.txt")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")
        else:
            messagebox.showwarning("Nothing to Save", "Result area is empty.")

    root = tk.Tk()
    root.title("🔐 Reverse Frequency Cipher")
    root.geometry("580x500")
    root.configure(bg="#f5f5f5")

    # Title
    title_label = tk.Label(root, text="Reverse Frequency Cipher", font=("Poppins", 18, "bold"), bg="#f5f5f5", fg="#333")
    title_label.pack(pady=10)

    # Input
    tk.Label(root, text="Enter Message:", font=("Poppins", 12), bg="#f5f5f5").pack()
    input_text = tk.Text(root, height=4, width=65, font=("Courier", 12))
    input_text.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(root, bg="#f5f5f5")
    button_frame.pack(pady=10)

    encrypt_btn = tk.Button(button_frame, text="Encrypt", font=("Poppins", 12), command=on_encrypt, bg="#4CAF50", fg="white", width=12)
    encrypt_btn.grid(row=0, column=0, padx=5)

    decrypt_btn = tk.Button(button_frame, text="Decrypt", font=("Poppins", 12), command=on_decrypt, bg="#2196F3", fg="white", width=12)
    decrypt_btn.grid(row=0, column=1, padx=5)

    reset_btn = tk.Button(button_frame, text="Reset", font=("Poppins", 12), command=on_reset, bg="#f44336", fg="white", width=12)
    reset_btn.grid(row=0, column=2, padx=5)

    save_btn = tk.Button(button_frame, text="Save Result", font=("Poppins", 12), command=on_save, bg="#9C27B0", fg="white", width=12)
    save_btn.grid(row=0, column=3, padx=5)

    # Result Label
    tk.Label(root, text="Result:", font=("Poppins", 12), bg="#f5f5f5").pack()
    result_text = tk.Text(root, height=8, width=70, font=("Courier", 12), wrap="word", bg="white", relief="solid", bd=1)
    result_text.pack(pady=10)

    root.mainloop()

# Run App
if __name__ == "__main__":
    create_gui()
