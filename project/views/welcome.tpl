% rebase('base_welcome.tpl', message=message)
<div class='col-md-7'>
% include('tab_click.tpl')
% include('svg.tpl', svg=svg_data)
<p>
	Nullam quis risus eget urna mollis ornare vel eu leo. 
	Cum sociis natoque penatibus et magnis dis parturient montes, 
	nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.
</p>

<p>
	Cum sociis natoque penatibus et magnis dis parturient montes, 
	nascetur ridiculus mus. Donec ullamcorper nulla non metus auctor fringilla. 
	Duis mollis, est non commodo luctus, nisi erat porttitor ligula, 
	eget lacinia odio sem nec elit. Donec ullamcorper nulla non metus auctor fringilla.
</p>

<p>
	Maecenas sed diam eget risus varius blandit sit amet non magna. 
	Donec id elit non mi porta gravida at eget metus. Duis mollis, 
	est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit.
</p>
% include('employees_table.tpl', employees=employees)
</div>
<div class='col-md-4'>
	% include('content_right.tpl')
</div>
