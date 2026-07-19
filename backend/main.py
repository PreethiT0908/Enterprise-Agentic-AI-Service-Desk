from fastapi import FastAPI
from api.ticket_routes import router as ticket_router
from api.incident_routes import router as incident_router

app = FastAPI(
    title="Enterprise AI Service Desk API"
)


app.include_router(ticket_router)
app.include_router(incident_router)

@app.get("/")
def home():
    return {
        "message": "Service Desk API Running"
    }