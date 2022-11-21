with mapped_ranks as (
	select *
	from {{ ref('stg_maprankvalues' )}}
),
final as (
	select
		headphone.driver_type,
		avg(mapped_ranks.rank_value) as average_rating,
		count(headphone.driver_type) as number_of_products
from
		headphone,
		mapped_ranks
where
		headphone.rank_grade = mapped_ranks.rank_grade
group by
		headphone.driver_type
)
select *
from final
