{% set rank_grades = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E+", "E", "E-", "F+", "F", "F-"] %}
{% set ns = namespace(value=10) %}

with iem_ranks as (
	select distinct
		rank_grade,
		case
			{% for grade in rank_grades %}
			WHEN rank_grade = '{{ grade }}' then {{ ns.value }}
			{% set ns.value = ns.value + 0.5 %}
			{% endfor %}
		end as rank_value
	from
		inearmonitor
),

{% set ns = namespace(value=10) %}

headphone_ranks as (
	select distinct
		rank_grade,
		case
			{% for grade in rank_grades %}
			WHEN rank_grade = '{{ grade }}' then {{ ns.value }}
			{% set ns.value = ns.value + 0.5 %}
			{% endfor %}
		end as rank_value
	from
        headphone
),

final as (
	select
			rank_grade,
			rank_value
		from iem_ranks
		union
		select
			rank_grade,
			rank_value
	from headphone_ranks
)

select * from final
