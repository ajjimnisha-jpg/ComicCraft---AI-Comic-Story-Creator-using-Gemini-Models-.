import tkinter as tk
from tkinter import messagebox, filedialog
from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)

def generate_comic():
    idea = idea_box.get("1.0", tk.END).strip()
    if not idea:
        messagebox.showwarning("Input Required", "Please enter a comic idea.")
        return

    try:
        panels = int(panel_var.get())
        if not 2 <= panels <= 10:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Panels", "Choose between 2 and 10 panels.")
        return

    prompt = f"""You are ComicCraft, an AI comic story creator.
Create a creative comic story based on:
{idea}

Create exactly {panels} panels.
Give:
TITLE
CHARACTERS with short descriptions
For each panel:
PANEL number
Scene
Characters
Dialogue
Narration
Use simple English and make it suitable for students."""

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Generating comic...\nPlease wait...\n")
    root.update_idletasks()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        output.delete("1.0", tk.END)
        output.insert(tk.END, response.text)
    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Error: {e}")

def save_comic():
    content = output.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Nothing to Save", "Generate a comic first.")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Comic saved successfully.")

root = tk.Tk()
root.title("ComicCraft - AI Comic Story Creator")
root.geometry("900x700")

tk.Label(root, text="ComicCraft", font=("Arial", 28, "bold")).pack(pady=10)
tk.Label(root, text="AI Comic Story Creator using Gemini Models",
         font=("Arial", 14)).pack()

tk.Label(root, text="Enter your comic idea:", font=("Arial", 12, "bold")).pack(
    anchor="w", padx=20, pady=(20, 5))

idea_box = tk.Text(root, height=6, width=100)
idea_box.pack(padx=20)

panel_frame = tk.Frame(root)
panel_frame.pack(pady=12)

tk.Label(panel_frame, text="Number of panels:").pack(side="left")
panel_var = tk.StringVar(value="6")
tk.Spinbox(panel_frame, from_=2, to=10, textvariable=panel_var,
           width=5).pack(side="left", padx=8)

tk.Button(panel_frame, text="Generate Comic",
          command=generate_comic).pack(side="left", padx=8)
tk.Button(panel_frame, text="Save Comic",
          command=save_comic).pack(side="left")

tk.Label(root, text="Generated Comic:", font=("Arial", 12, "bold")).pack(
    anchor="w", padx=20)

output = tk.Text(root, height=25, width=100, wrap="word")
output.pack(padx=20, pady=5, fill="both", expand=True)

root.mainloop()
