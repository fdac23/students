|GitHub|netid|name|
|----|------|
{% for netid, student in students.items() -%}
|@{{student.github}}|{{netid}}|{{student.firstname}} {{student.lastname}}|
{% endfor -%}
