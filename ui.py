import tkinter as tk
from tkinter import messagebox, font
import threading
import os
import sys
from main import main, stop

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def run_ui():
    root = tk.Tk()
    root.title("MarshmellowUwU")
    root.geometry("480x360")
    root.resizable(False, False)

    bg, fg = "#1e1e1e", "#e0e0e0"
    entry_bg, btn_bg = "#2e2e2e", "#3a3a3a"
    hover_bg, accent = "#505050", "#4caf50"
    root.configure(bg=bg)

    header_font = font.Font(family="Segoe UI", size=14, weight="bold")
    label_font = font.Font(family="Segoe UI", size=10)
    btn_font = font.Font(family="Segoe UI", size=10, weight="bold")

    try:
        icon_path = resource_path("assets/logo.ico")
        root.iconbitmap(icon_path)
    except:
        pass

    bot_frame = tk.Frame(root, bg=bg)
    bot_frame.pack(fill='both', expand=True, padx=20, pady=20)

    labels = ["👤 Kullanıcı Adı:", "👥 İzleyici Sayısı:"]
    for i, txt in enumerate(labels):
        tk.Label(
            bot_frame, text=txt, bg=bg, fg=fg, font=label_font
        ).grid(row=i, column=0, sticky='e', pady=10)

    ue = tk.Entry(bot_frame, bg=entry_bg, fg=fg, insertbackground=fg,
                  relief="flat", font=label_font)
    ue.grid(row=0, column=1, padx=(5,0), pady=10, ipady=4, ipadx=5)
    
    ve = tk.Entry(bot_frame, bg=entry_bg, fg=fg, insertbackground=fg,
                  relief="flat", font=label_font)
    ve.insert(0, "1000")
    ve.grid(row=1, column=1, padx=(5,0), pady=10, ipady=4, ipadx=5)

    def start_bot():
        try:
            u = ue.get().strip()
            v = int(ve.get().strip())
            if not u or v <= 0:
                raise ValueError
            
            max_v = 1000
            v = min(v, max_v)
            
            threading.Thread(target=main, args=(v, u), daemon=True).start()
            messagebox.showinfo("Başladı", f"Bot @{u} için {v} izleyici ile başladı.")
        except Exception as e:
            messagebox.showerror("Hata", "Geçersiz giriş. Kullanıcı adı ve pozitif bir izleyici sayısı girdiğinizden emin olun.")

    def stop_bot():
        stop()
        messagebox.showinfo("Durduruldu", "Bot durduruldu.")

    sb = tk.Button(bot_frame, text="🚀 Başlat", bg=btn_bg, fg=fg,
                   activebackground=accent, font=btn_font, relief="flat",
                   command=start_bot)
    sb.grid(row=2, column=0, columnspan=2, pady=(20,5), ipadx=10, ipady=6)
    sb.bind('<Enter>', lambda e: sb.config(bg=hover_bg))
    sb.bind('<Leave>', lambda e: sb.config(bg=btn_bg))

    tb = tk.Button(bot_frame, text="🛑 Durdur", bg="#a03535", fg=fg,
                   activebackground="#c0392b", font=btn_font, relief="flat",
                   command=stop_bot)
    tb.grid(row=3, column=0, columnspan=2, pady=(5,0), ipadx=10, ipady=6)

    root.mainloop()

if __name__ == "__main__":
    run_ui()