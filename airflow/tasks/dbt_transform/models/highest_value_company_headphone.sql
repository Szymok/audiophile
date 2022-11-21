with company as (
	select *
	from {{ ref("stg_companynames") }}
), final as (
	select
		company.company_name,
		max(headphone.value_rating) as highest_value
	from
		company,
		headphone
	where
		company.company_name = {{ dbt.split_part(
		string_text = 'headphone.model',
		delimiter_text = "' '",
		part_number = 1
) }}
	group by
		company.company_name
)
select *
from final
