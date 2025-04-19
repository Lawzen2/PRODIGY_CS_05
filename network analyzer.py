import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff

# Function to process packets
def process_packet(packet, output_box):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dest_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        output_box.insert(tk.END, f"Source IP: {src_ip} | Destination IP: {dest_ip} | Protocol: {protocol}\n")
        output_box.see(tk.END)

# Function to start sniffing packets
def start_sniffing(output_box):
    sniff(prn=lambda packet: process_packet(packet, output_box), count=10)

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Network Packet Analyzer - Developed by Khalid")
    root.geometry("800x500")
    
    # Welcome screen
    home_screen = tk.Toplevel(root)
    home_screen.title("Welcome - Developed by Khalid")
    home_screen.geometry("400x200")
    welcome_label = tk.Label(home_screen, text="Welcome to the Network Packet Analyzer!", font=("Arial", 14))
    welcome_label.pack(pady=30)
    proceed_button = tk.Button(home_screen, text="Proceed", command=home_screen.destroy)
    proceed_button.pack(pady=10)
    root.wait_window(home_screen)
    
    # Output box for packet details
    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Courier", 10))
    output_box.pack(padx=10, pady=10)
    
    # Start button
    start_button = tk.Button(root, text="Start Capture", command=lambda: start_sniffing(output_box))
    start_button.pack(pady=5)
    
    # Goodbye screen
    def on_closing():
        goodbye_screen = tk.Toplevel(root)
        goodbye_screen.title("Goodbye - Developed by Khalid")
        goodbye_screen.geometry("400x200")
        goodbye_label = tk.Label(goodbye_screen, text="Thank you for using the Network Packet Analyzer!\nGoodbye!", font=("Arial", 14))
        goodbye_label.pack(pady=30)
        exit_button = tk.Button(goodbye_screen, text="Exit", command=root.destroy)
        exit_button.pack(pady=10)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_gui()
