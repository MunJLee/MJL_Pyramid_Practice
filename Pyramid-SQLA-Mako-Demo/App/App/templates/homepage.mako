<%inherit file="baseLayout.mako"/>
<div>

  <div>
    <h2>${projectname}</h2><br>
    <p>This pyramid project let you query against Chinook sample database dataset.<br>
Currently the routes for Customer table are implemented.<br>
Please see the following example URLs to form a query.<br>
    </p><br>
  </div>

  <div>
    <h3>Examples:</h3>
    <h4>Homepage: <span style="color:DarkSlateGrey;">/</span></h4>
    <h4>Display all Customer table rows: <span style="color:DarkSlateGrey;"><small>/Customer</small></span></h4>
    <h4>Display a selected Customer table column: <span style="color:DarkSlateGrey;"><small>/Customer/[column name]</small></span></h4>
    <p>(ex. /Customer/company)</p>
    <h4>Display rows satisfying a given condition: <span style="color:DarkSlateGrey;"><small>/Customer/[column name]/[condition]</small></span></h4>
    <p>(ex. /Customer/state/NY)</p><br>
  </div>

  <div>
    <h3>Available Search Columns:</h3>
    <p style="color:DarkSlateGrey;">
      % for cl in column_labels:
        % if cl != '_sa_instance_state':
        [${cl}]
        % endif %
      % endfor%
    </p>
  </div>
</div>