import pprint
from pathlib import Path

import jwt
from cryptography.x509 import load_pem_x509_certificate


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    x509_certificate = load_pem_x509_certificate(
        Path("public_key.pem").read_text().encode()
    ).public_key()
    return jwt.decode(
        access_token,
        key=x509_certificate,
        algorithms=unverified_headers["alg"],
        audience='http://localhost:5000/orders'
    )


token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAvdG9rZW4iLCJzdWIiOjY2NiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwL29yZGVycyIsImlhdCI6MTY5MjQ4MTcxMCwiZXhwIjoxNjkyNDk2MTEwLjIyNzA4Nywic2NvcGUiOiJvcGVuaWQifQ.t0HqLik0yQH22j0GR4l40Yvl4VnafuOga09ExWkBtNP2YkeL4U7e3AYvpBsmPcC_6eYhzZVVmFdA4v3Dq-PBAf9uOj96DbcqashstEW6p29k7gD6oANM7idSgSxBl4_rYWazlCQWuig1bXYOynYCwRawKDex8V5LAQoSYKlczpgskOB5cvhzqFlwu8VdTue8SUo2wQoiRkxpugBI4YgsyCirtGnLdM0AHKHWSU0o781KezCGSp-epHzGVWSuEKp1BXHBrt6mFtUGbiIJ5FFe1HtPVgGJBemQWsmBs7h_QOhlLEVfqLKXn6RyiOCRjEpiFcR8v58Ai98YYKYOLR-AqQ'

try:
    pprint.pprint(decode_and_validate_token(token))
except Exception as err:
    print(f'Error: {err}')

