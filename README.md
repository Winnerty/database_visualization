# Database Visualization
## How to use:
0) Set up Flask, jaydebeapi  
`pip install Flask`         
`pip install JayDeBeApi==1.2.3`

1. H2 Database  
Open `path_to_h2_jar` file and insert path to your `h2.jar` file.

2. Open and run `main.py`

3. Beginning  
Go to [127.0.0.1:5000/index.html](https://127.0.0.1:5000/index.html) – this is the main page.                
You can easily move over pages, open Populations or Grades.

4. Architecture  
Pythons understands, with one of three pages is required, executes corresponding query or queries and sends the result to the corresponding HTML template. 
The `H2` folder is in `src` folder. All the queries are in `src/queries.py` file. All the templates are in `templates` folder, they use for loop to go over received data and create a table from it. 
As well I use parameters in URLs, so for each page of a particular academic group there is a custom URL. And on each of 3 pages I have date & time of last generation, it Is made inside `<script>` tag in HTML files.

5. Charts
I used Plotly for creating the charts, both are created and filled with data inside `<script>` tag in `index.html` file.

6. Count of passed subjects
On `Populations` page I count subject as passed if the average grade for the subject is ≥10.

7. Additional   
-8th line in `main.py` is commented, this line was necessary for my computer, you can uncomment it or not. I have left it just in case.       
