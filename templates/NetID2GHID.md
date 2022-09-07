|GitHub|netid|name|
|----|------|----|
{% for netid, student in students.items() -%}
|[@{{student.github}}](https://github.com/{{student.github}})|{{netid}}|{{student.firstname}} {{student.lastname}}|
{% endfor -%}
