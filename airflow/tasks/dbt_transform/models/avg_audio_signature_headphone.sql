with mapped_ranks as (
	select *
	from {{ ref('stg_maprankvalues' )}}
),
final as (
	select
		headphone.audio_signature,
		avg(mapped_ranks.rank_value) as average_rating,
		count(headphone.audio_signature) as number_of_products
	from headphone,
		mapped_ranks
	where
		headphone.rank_grade = mapped_ranks.rank_grade
	group by
		headphone.audio_signature
	having
		count(headphone.audio_signature) > 15
)
select *
from final