% rebase('bottleck/base_welcome.tpl', message=message)
<div class='col-md-7'>
% include('bottleck/tab_click.tpl')
% include('bottleck/employees_table.tpl', employees=employees)
% include('bottleck/svg.tpl', svg=svg_data)
<p>
	Maecenas sed diam eget risus varius blandit sit amet non magna. 
	Donec id elit non mi porta gravida at eget metus. Duis mollis, 
	est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit.
</p>

</div>
<div class='col-md-4'>
	% include('bottleck/content_right.tpl')
</div>
