import win32print
import win32ui

def print_to_printer(text, printer_name):
    try:
        printer_handle = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(printer_handle, 2)

        printer_dc = win32ui.CreateDC()
        printer_dc.CreatePrinterDC(printer_name)
        printer_dc.StartDoc('My Document')
        printer_dc.StartPage()

        # Print each line of text with a line break after the 48th character
        y = 0  # Starting y position
        for line in text:
            # Split the line into chunks of 48 characters or less
            chunks = [line[i:i+48] for i in range(0, len(line), 48)]
            
            for chunk in chunks:
                printer_dc.TextOut(0, y, chunk)
                y += printer_dc.GetTextExtent(chunk)[1]  # Increase y position by the text height
               
            y += 5  # Add extra vertical space between lines (adjust as needed)

        printer_dc.EndPage()
        printer_dc.EndDoc()
        printer_dc.DeleteDC()
  
        print("Printing successful!")
    except Exception as e:
        print(f"Printing failed: {e}")

print("File saved, printing, NEW LOOP")

if __name__ == "__main__":
    with open('brain.txt', 'r') as f:
        mylist = f.readlines()

    # Calculate the index to split the list in half
    half_index = len(mylist) // 2
    # Slice the list to get the first half
    first_half = mylist[:half_index]
    
    printer_name = "Star TSP100 Tear Bar (TSP113)"
    print_to_printer(mylist, printer_name)
