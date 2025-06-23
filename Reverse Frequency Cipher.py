import tkinter as tk
from tkinter import messagebox
import os

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
            result_text.insert(tk.END, f"🔐 Encrypted Text:\n{encrypted}")
        else:
            messagebox.showwarning("Input Required", "Please enter a message to encrypt.")

    def on_decrypt():
        msg = input_text.get("1.0", tk.END).strip()
        if msg:
            decrypted = decrypt_rfc(msg)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"🔓 Decrypted Text:\n{decrypted}")
        else:
            messagebox.showwarning("Input Required", "Please enter a message to decrypt.")

    def on_reset():
        input_text.delete("1.0", tk.END)
        result_text.delete("1.0", tk.END)

    def on_save():
        content = result_text.get("1.0", tk.END).strip()
        if content:
            try:
                file_path = os.path.join(os.path.dirname(__file__), "result.txt")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Success", f"Result saved in:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")
        else:
            messagebox.showwarning("Nothing to Save", "Result area is empty.")

    root = tk.Tk()
    root.title("🔐 Reverse Frequency Cipher")
    root.geometry("650x550")
    root.configure(bg="#E8F0F2")  # Soft light blue background
    root.resizable(False, False)

    # Main Frame (like card)
    main_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=500)

    # Title
    title_label = tk.Label(main_frame, text="🔐 Reverse Frequency Cipher 🔐", font=("Poppins", 20, "bold"), bg="white", fg="#333")
    title_label.pack(pady=15)

    # Input Label
    tk.Label(main_frame, text="Enter Message:", font=("Poppins", 12), bg="white").pack()
    input_text = tk.Text(main_frame, height=4, width=60, font=("Courier New", 12), bd=1, relief="solid")
    input_text.pack(pady=8)

    # Buttons
    button_frame = tk.Frame(main_frame, bg="white")
    button_frame.pack(pady=10)

    btn_style = {"font": ("Poppins", 11), "width": 12, "bd": 0, "relief": "solid", "highlightthickness": 1}

    encrypt_btn = tk.Button(button_frame, text="Encrypt", bg="#4CAF50", fg="white", activebackground="#45A049",
                            command=on_encrypt, **btn_style)
    encrypt_btn.grid(row=0, column=0, padx=5)

    decrypt_btn = tk.Button(button_frame, text="Decrypt", bg="#2196F3", fg="white", activebackground="#1E88E5",
                            command=on_decrypt, **btn_style)
    decrypt_btn.grid(row=0, column=1, padx=5)

    reset_btn = tk.Button(button_frame, text="Reset", bg="#f44336", fg="white", activebackground="#e53935",
                          command=on_reset, **btn_style)
    reset_btn.grid(row=0, column=2, padx=5)

    save_btn = tk.Button(button_frame, text="Save Result", bg="#9C27B0", fg="white", activebackground="#8E24AA",
                         command=on_save, **btn_style)
    save_btn.grid(row=0, column=3, padx=5)

    # Result Label
    tk.Label(main_frame, text="Result:", font=("Poppins", 12), bg="white").pack()
    result_text = tk.Text(main_frame, height=8, width=60, font=("Courier New", 12), bd=1, relief="solid", wrap="word")
    result_text.pack(pady=8)

    root.mainloop()

# Run App
if __name__ == "__main__":
    create_gui()
