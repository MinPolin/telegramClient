import os
#
# API_ID='19462592'
# API_HASH = '8ffe526b9ff8697f6e925f291fd8abee'
#
# SESSION_STRING='1ApWapzMBu8OAI6Cf2L4xj4gItaZbt3tXAg_-COBpkWhSRI4MmbmIoI8oDOFdLdebp7-g4FMNRiqUZJPuMnIwZdgB4UclqZ_P48bAP2DgDC2-s_n4r8fo5h4et9nSfM1LdnFo-aLXu2i6K6GLbjmlDR5lNkhKLXmgNLHfCadAqBqvHhQXoW5S2kg_xlUe_tVsLmkj-NbECj2vr_0Ei6xFYwD03VJSUOGNEIAxtN51EUW-LzGyZV5UjmOctTGrzYRVN5RMwV0NvpGsBdpVjhVQQ2o_eE6LfmbJAcIX4mooNUi31XjdJsq55YnotlpA1jC5s9jt23QwUmDLmyZ1OCfUlcnl1UobjFI='
#
#
# os.environ.setdefault('API_ID', API_ID)
# os.environ.setdefault('API_HASH', API_HASH)
# os.environ.setdefault('SESSION_STRING', SESSION_STRING)


from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

print(type(os.environ.get('API_ID')))