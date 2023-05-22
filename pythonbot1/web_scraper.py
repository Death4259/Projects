import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import filedialog

# Define a function to handle the "Scrape" button click
def scrape():
    # Get the URL from the URL entry box
    url = url_entry.get()

    # Send an HTTP request to the URL and get the HTML response
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the HTML elements that contain the data you want to scrape
    data_elements = soup.find_all('div', class_='data')

    # Ask the user to choose an output file
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=(('CSV Files', '*.csv'),))

    # Open the output file for writing and write the data to it
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Data'])
        # Loop over the data elements and write each one to a new row in the CSV file
        for element in data_elements:
            writer.writerow([element.text.strip()])

# Create a tkinter window
window = tk.Tk()
window.title("Web Scraper")

# Create a label and entry box for the URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a "Scrape" button
scrape_button = tk.Button(window, text="Scrape", command=scrape)
scrape_button.pack()

# Run the tkinter event loop
window.mainloop()
