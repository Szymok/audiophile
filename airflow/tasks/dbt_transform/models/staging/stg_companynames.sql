with iem as (
	select
		distinct {{ dbt.split_part(
			string_text = 'model',
			delimeter_text = "' '",
			part_number = 1
		)}} as company_name
	from
		public.InEarMonitor
),

headphones as (
	select
			distinct {{ dbt.split_part(
			string_text = 'model',
			delimiter_text = "' '",
			part_number = 1
		)}} as company_name
	from
		public.Headphone
),
	
final as (
	select
			iem.company_name
	from
			iem
			left join headphone on iem.company_name = headphone.company_name
)
select *
from final
