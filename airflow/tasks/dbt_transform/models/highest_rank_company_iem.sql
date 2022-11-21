with mapped_ranks as (
	select *
	from {{ ref("stg_maprankvalues") }}
), company as (
	select *
	from {{ ref("stg_companynames") }}
), final as (
	select
		company.company_name,
		avg(mapped_ranks.rank_value) as average_rating,
		count(company.company_name) as number_of_products
	from
		inearmonitor,
		mapped_ranks,
		company
	where
		inearmonitor.rank_grade = mapped_ranks.rank_grade
		and company.company_name = {{ dbt.split_part(
				string_text = 'InEarMonitor.model',
				delimiter_text = "' '",
				part_number = 1
		)}}
group by
	company.company_name
)
select *
from final
