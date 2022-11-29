from pydantic import BaseModel, Field, validator


def grade_almost_2_chars(rank: str) -> bool:
	'''
 	Reusable method to valid fields based on the letter grade convention
	'''
	return len(rank) > 2


class InEarMonitor(BaseModel):
	'''
 	Pydantic model containing validators for the schema of InEarMonitor
	'''

	rank: str
	model: str
	signature: str
	tone_grade: str
	driver_type: str
	technical_grade: str
	price: int = Field(-1, ge=-1)
	value_rating: int = Field(-1, ge=-1, le=3)

	_ensure_rank_max_2_chars = validator('rank',
	                                     allow_reuse=True)(grade_atmost_2_chars)
	_ensure_tonegrade_max_2_chars = validator(
	 'tone_grade', allow_reuse=True)(grade_atmost_2_chars)
	_ensure_technicalgrade_max_2_chars = validator(
	 'technical_grade', allow_reuse=True)(grade_atmost_2_chars)

	@validator('signature')
	def ensure_signature_has_no_quotes(cls, signature: str):
		'''
		Ensure that any signature after sanitzation do not have quote
		'''
		if '"' in signature:
			raise ValueError('Signature must not contain quotes')
		return signature.title()


class Headphone(InEarMonitor):
	'''
 	Pydantic model containing validators for Headphones
	
 	Args:
		InEarMonitor (InEarMonitor): subclasses the InEarMonitor class, including all validators
 	'''

	fit_cup: str
