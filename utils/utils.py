import re

def cep_with_mask(cep):
    masked_cep = re.sub(r'^(\d{5})-?(\d{3})$', r'\1-\2', cep)
    return masked_cep