<%inherit file="baseLayout.mako"/>
<div>
  <table style="border: 1px solid;">
    <tr>
      % for hder in column_labels:
        <th style="border: 1px solid;">${hder}</th>
      % endfor
    </tr>

    % for rw in query_result:
    <tr style="white-space: nowrap">
      % for key, value in rw.items():
        % if key == column_labels[0]:
          <td style="border: 1px solid;">${value}</td>
        % endif %
      % endfor %
    <tr>
    % endfor %

  </table>
</div>