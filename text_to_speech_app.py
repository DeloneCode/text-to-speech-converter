import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import pyttsx3
import os
from datetime import datetime

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")
        self.root.geometry("800x600")
        
        # Set dark theme colors
        self.style = ttk.Style()
        self.style.configure("Dark.TFrame", background="#1e1e1e")
        self.style.configure("Dark.TLabel", background="#1e1e1e", foreground="#b19cd9", font=("Helvetica", 10))
        self.style.configure("Dark.TButton", 
                           background="#2d2d2d", 
                           foreground="#b19cd9",
                           padding=5,
                           font=("Helvetica", 10))
        self.style.configure("Dark.Horizontal.TScale", 
                           background="#1e1e1e",
                           troughcolor="#2d2d2d")
        self.style.configure("Dark.TCombobox", 
                           background="#2d2d2d",
                           foreground="#b19cd9",
                           fieldbackground="#2d2d2d",
                           selectbackground="#3d3d3d",
                           selectforeground="#b19cd9")
        
        # Set root background color
        self.root.configure(bg="#1e1e1e")
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20", style="Dark.TFrame")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                              text="TEXT TO SPEECH CONVERTER", 
                              style="Dark.TLabel",
                              font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Text input area
        ttk.Label(self.main_frame, text="Enter your text:", style="Dark.TLabel").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Custom text widget with dark theme
        self.text_input = scrolledtext.ScrolledText(
            self.main_frame, 
            width=70, 
            height=10,
            bg="#2d2d2d",
            fg="#b19cd9",
            insertbackground="#b19cd9",
            font=("Consolas", 10),
            relief="flat"
        )
        self.text_input.grid(row=2, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Voice selection
        ttk.Label(self.main_frame, text="Select voice:", style="Dark.TLabel").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.voice_var = tk.StringVar()
        self.voice_combo = ttk.Combobox(self.main_frame, 
                                      textvariable=self.voice_var,
                                      style="Dark.TCombobox",
                                      state="readonly")
        self.voice_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Rate control
        ttk.Label(self.main_frame, text="Speech rate:", style="Dark.TLabel").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.rate_var = tk.IntVar(value=150)
        self.rate_scale = ttk.Scale(self.main_frame, 
                                  from_=50, 
                                  to=300, 
                                  orient=tk.HORIZONTAL, 
                                  variable=self.rate_var,
                                  style="Dark.Horizontal.TScale")
        self.rate_scale.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons frame with modern styling
        self.button_frame = ttk.Frame(self.main_frame, style="Dark.TFrame")
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Create modern-looking buttons
        save_button = ttk.Button(self.button_frame, 
                               text="SAVE AS WAV", 
                               command=self.save_as_wav,
                               style="Dark.TButton")
        save_button.pack(side=tk.LEFT, padx=10)
        
        speak_button = ttk.Button(self.button_frame, 
                                text="SPEAK", 
                                command=self.speak_text,
                                style="Dark.TButton")
        speak_button.pack(side=tk.LEFT, padx=10)
        
        # Initialize voices
        self.update_voice_list()
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
    def update_voice_list(self):
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        self.voice_combo['values'] = voice_names
        if voice_names:
            self.voice_combo.set(voice_names[0])
    
    def speak_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text first!")
            return
            
        # Set voice
        voices = self.engine.getProperty('voices')
        selected_voice = self.voice_var.get()
        for voice in voices:
            if voice.name == selected_voice:
                self.engine.setProperty('voice', voice.id)
                break
        
        # Set rate
        self.engine.setProperty('rate', self.rate_var.get())
        
        # Speak the text
        self.engine.say(text)
        self.engine.runAndWait()
    
    def save_as_wav(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text first!")
            return
            
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"speech_{timestamp}.wav"
        
        # Ask user where to save the file
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav",
            initialfile=default_filename,
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
        )
        
        if filename:
            # Set voice
            voices = self.engine.getProperty('voices')
            selected_voice = self.voice_var.get()
            for voice in voices:
                if voice.name == selected_voice:
                    self.engine.setProperty('voice', voice.id)
                    break
            
            # Set rate
            self.engine.setProperty('rate', self.rate_var.get())
            
            # Save to file
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            messagebox.showinfo("Success", f"Audio saved to:\n{filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop() 