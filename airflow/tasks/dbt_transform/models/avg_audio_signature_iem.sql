with mapped_ranks as (
	select *
	from {{ ref('stg_maprankvalues' )}}
),
final as (
	select
		inearmonitor.audio_signature,
		avg(mapped_ranks.rank_value) as average_rating,
		count(inearmonitor.audio_signature) as number_of_products
	from inearmonitor,
		mapped_ranks
	where
		inearmonitor.rank_grade = mapped_ranks.rank_grade
	group by
		inearmonitor.audio_signature
	having
		count(inearmonitor.audio_signature) > 35
)
select *
from final