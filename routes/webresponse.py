from fastapi import APIRouter,Request

WebResponse=APIRouter()

@WebResponse.get("/wompi/")
def handle_transaction_tatus():
    return("working...")