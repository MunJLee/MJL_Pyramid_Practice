<%inherit file="baseLayout.mako"/>
<div>
  <table style="border: 1px solid;">
    <tr>
      % for hder in column_pattern:
        <th style="border: 1px solid;">${hder}</th>
      % endfor
    </tr>
    % for rw in query_result:
      <tr style="white-space: nowrap">
      % for pttrn in column_pattern:
        % for key, value in rw.items():
          % if key == pttrn:
            <td style="border: 1px solid;">${value}</td>
          % endif %
        % endfor %
      % endfor %
      </tr>
    % endfor %
  </table>
</div>