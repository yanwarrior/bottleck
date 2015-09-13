<table class="table table-striped">
  <tr>
	<td>ID</td>
	<td>Name</td>
	<td>Jobs</td>
	<td>Email</td>
	<td>Age</td>
  </tr>
% for emp in employees:
  <tr>
	<td>{{emp[0]}}</td>
	<td>{{emp[1]}}</td>
	<td>{{emp[2]}}</td>
	<td>{{emp[3]}}</td>
	<td>{{emp[4]}}</td>
  </tr>
% end
</table>
