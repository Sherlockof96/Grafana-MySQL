# Grafana-MySQL
The aim is to link the data into MySQL and then display them as graphs by making a dashboard in Grafana.

<h4>Approach</h4>
<li>Creating a database and writing a python script to extract the data into MySQL</li>
<li>Linking MySQL with Grafana</li>
<li>Displaying real-time graphs in Grafana</li>

<h4>How to run:</h4>
<li>Set up your MySQL and then replace your connection in the Script_Database_fromtextfile.py with your own connection</li>
<li>Replace the text file with any text file you want and make changes in the script file accordingly</li>
<li>Using the documentation of Grafana http://docs.grafana.org/ install it.</li>
<li>Make the connection of the data source connection in Grafana as documented. (Use MySQL 5.7 as the version 8.8 is not compatible with Grafana or if you are using the version 8.8 use legacy password encryption while initializing the database)</li>
<li>Copy the json format of the dashboard from the "DashboardJSON.txt" and paste it into the JSON part of Grafana to get the dashboard I created and then make appropriate changes to get your own dashboard.</li>
<li> To see how my dashboard looks like you can view it in "Dashboard1.png" , "Dashboard2.png"</li>
<h4>Note:</h4> 
<li>For my dashboard to work do install the Plotly plugin in your dashboard.</li>

