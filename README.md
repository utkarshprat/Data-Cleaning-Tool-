      Data Visualization Tool:-
      The Data Cleaner Tool is a Python-based application designed to clean CSV datasets. It provides two cleaning options:
      •   Dropping rows with missing values.
      •   Filling missing values with a specified value.
      The application features a GUI built with Tkinter, allowing users to easily select a CSV file, clean it using the chosen method, and save the cleaned dataset.
   

      Features:-
      •  Load and Display Data:
         - View essential information and preview the first five rows of the dataset.
      •  Cleaning Options:
         - Option 1: Remove rows with missing values.
         - Option 2: Fill missing values with a user-defined value.
      •  Save Cleaned Data:
         - Save the cleaned dataset in a specified directory.
      •  User-Friendly GUI:
         - Intuitive interface for selecting files, cleaning options, and output directories.


      How to Use:-
      Graphical User Interface (GUI)

      1. Run the GUI:
            python cleab_gui.py
      2. Follow the steps:
         • Select a CSV file to clean.
         • Choose an option:
           - Drop rows with missing values.
           - Fill missing values with a specified value.
         • Specify a directory to save the cleaned file.
      3. View Results: The cleaned file will be saved in the selected directory.



      Code Explanation:-
      1. clean.py
         Core logic for cleaning CSV files:
         •  load(file): Loads a CSV file.
         •  drop_na(data): Drops rows with missing values.
         •  fill_na(data, val): Fills missing values with a specified value.
         •  save(data, out_dir, file_name): Saves the cleaned dataset to the specified directory.
         •  clean(file, opt, out_dir, fill_val=None): Integrates all functionalities.

      2. cleab_gui.py
         Provides a graphical user interface (GUI):
         •  Select CSV File: Open a file dialog to choose a CSV file.
         •  Choose Cleaning Option: Drop rows or fill missing values.
         •  Save Cleaned File: Specify where to save the output.
      
      Example Workflow:-
      
         • Run the GUI with `python cleab_gui.py`.
         • Choose and clean your CSV file.
         • Save the cleaned file and confirm success.
      
      Error Handling:-
      
         •  File Not Found: Ensure the CSV file exists and the path is correct.
         •  Invalid Option: Choose a valid cleaning option in the GUI.
         •  No Output Directory**: Specify a directory to save the cleaned file.
         
This README is designed to help users easily understand how to set up and use the tool.

      Sample Images:-
![clean (1)](https://github.com/user-attachments/assets/c119556c-835b-40e6-a2f1-51902c5ca3d6)

![clean (2)](https://github.com/user-attachments/assets/ff5b1e8b-775c-4bcc-9c39-16441d6fb004)

![clean (3)](https://github.com/user-attachments/assets/9889b049-3fe6-42cc-9794-0456eaa3275f)

Updated Dataset after Droping the rows:-

![clean (4)](https://github.com/user-attachments/assets/7cc42ab4-847d-44f9-971c-d8d0166da94f)

