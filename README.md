\# Enterprise Agentic AI Service Desk



\## Project Overview



Enterprise Agentic AI Service Desk is an AI-powered IT support platform that automates incident management using multiple intelligent agents. The system analyzes user issues, retrieves solutions from a knowledge base, performs troubleshooting, executes automation tasks, creates tickets when required, routes tickets to the appropriate support team, and stores all information in PostgreSQL.



\---



\## Problem Statement



Traditional IT service desks rely heavily on manual support processes, resulting in slow response times and increased operational costs. Common issues such as WiFi connectivity, VPN access, printer failures, password resets, and software installation requests consume significant support resources.



This project aims to automate these repetitive tasks using AI agents.



\---



\## Objectives



\* Automate IT incident analysis

\* Provide knowledge-based solutions

\* Perform troubleshooting automatically

\* Execute automation actions where possible

\* Create tickets for unresolved incidents

\* Route tickets to the correct support team

\* Store incidents and tickets in PostgreSQL

\* Provide a dashboard for monitoring and management



\---



\## Technologies Used



\* Python

\* FastAPI

\* Streamlit

\* PostgreSQL

\* SQLAlchemy

\* Uvicorn

\* Groq AI (Optional)

\* REST APIs



\---


## System Architecture

The architecture of the Enterprise Agentic AI Service Desk is shown below.

User
  |
  ↓
Streamlit Dashboard
  |
  ↓
FastAPI Backend
  |
  ↓
Workflow Engine
  |
  ↓
AI Agents
  |
  ↓
PostgreSQL Database



\## Agents Used



\### 1. Incident Agent



Classifies incidents and extracts category, device, urgency, and summary.



\### 2. Knowledge Agent



Retrieves relevant solutions from the knowledge base.



\### 3. Troubleshooting Agent



Generates troubleshooting steps for the identified issue.



\### 4. Automation Agent



Attempts automated remediation actions.



\### 5. Decision Agent



Determines whether the issue is resolved or requires ticket creation.



\### 6. Ticket Agent



Creates incident tickets for unresolved issues.



\### 7. Routing Agent



Assigns tickets to the appropriate support team.



\### 8. Notification Agent



Generates notifications for users and support teams.



\---



\## Features



\* Incident Analysis

\* Knowledge Base Search

\* Automated Troubleshooting

\* Automation Execution

\* Ticket Creation

\* Ticket Status Management

\* Ticket Routing

\* Notifications

\* PostgreSQL Integration

\* Dashboard Analytics

\* Search and Filtering



\---



\## API Endpoints



\### Incidents



POST /incidents



Creates and processes a new incident.



\### Tickets



GET /tickets



Returns all tickets.



GET /tickets/{ticket\_id}



Returns a specific ticket.



PUT /tickets/{ticket\_id}/status



Updates ticket status.



\---



\## Dashboard Features



\* Create Incident

\* View Tickets

\* Search Tickets

\* Filter by Category

\* Filter by Status

\* Ticket Analytics

\* Update Ticket Status



\---



\## Database



PostgreSQL stores:



\* Ticket ID

\* Category

\* Priority

\* Status

\* Summary



\---



\## Sample Workflow



User reports:



"Printer is offline"



Workflow:



Incident Analysis

→ Knowledge Search

→ Troubleshooting

→ Automation Attempt

→ Decision



If resolved:

Close Incident



If unresolved:

Create Ticket

→ Route Ticket

→ Notify Team



\---



\## Future Enhancements



\* Groq LLM Integration

\* Email Notifications

\* Role-Based Access Control

\* SLA Monitoring

\* Advanced Analytics

\* Predictive Incident Resolution



\---
## Architecture Diagram

Architecture diagram is available in:

docs/architecture.docx


\## Conclusion



The Enterprise Agentic AI Service Desk successfully automates major IT support operations using intelligent agents. The system improves response time, reduces manual effort, and provides a scalable framework for enterprise incident management.


