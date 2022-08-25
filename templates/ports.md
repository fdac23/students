|port|netid|
|----|------|
{% for netid, student in students.items() -%}
|{{student.port}}|{{netid}}|
{% endfor -%}
