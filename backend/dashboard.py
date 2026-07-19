import streamlit as st
import requests
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Enterprise AI Service Desk",
    layout="wide"
)

st.title("Enterprise AI Service Desk")

# =========================
# CREATE INCIDENT
# =========================

st.header("Create New Incident")

issue = st.text_area(
    "Describe your issue"
)

if st.button("Submit Incident"):

    if issue:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/incidents",
                json={
                    "description": issue
                }
            )

            result = response.json()

            st.success(
                "Incident processed successfully"
            )

            st.json(result)

        except Exception as e:

            st.error(
                f"API Error: {e}"
            )

# =========================
# LOAD TICKETS
# =========================

st.divider()

st.header("Ticket Dashboard")

try:

    response = requests.get(
        "http://127.0.0.1:8000/tickets/"
    )

    tickets = response.json()

    if len(tickets) > 0:

        df = pd.DataFrame(tickets)

        # =========================
        # KPI CARDS
        # =========================

        total_tickets = len(df)

        open_tickets = len(
            df[df["status"] == "OPEN"]
        )

        in_progress_tickets = len(
            df[df["status"] == "IN_PROGRESS"]
        )

        resolved_tickets = len(
            df[df["status"] == "RESOLVED"]
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Tickets",
            total_tickets
        )

        col2.metric(
            "Open",
            open_tickets
        )

        col3.metric(
            "In Progress",
            in_progress_tickets
        )

        col4.metric(
            "Resolved",
            resolved_tickets
        )

        st.divider()

        # =========================
        # SEARCH & FILTERS
        # =========================

        st.subheader("Search & Filters")

        col1, col2, col3 = st.columns(3)

        search_ticket = col1.text_input(
            "Search Ticket ID"
        )

        status_filter = col2.selectbox(
            "Filter by Status",
            [
                "All",
                "OPEN",
                "IN_PROGRESS",
                "RESOLVED"
            ]
        )

        category_options = ["All"] + sorted(
            list(df["category"].unique())
        )

        category_filter = col3.selectbox(
            "Filter by Category",
            category_options
        )

        # =========================
        # APPLY FILTERS
        # =========================

        filtered_df = df.copy()

        if search_ticket:

            filtered_df = filtered_df[
                filtered_df["ticket_id"]
                .str.contains(
                    search_ticket,
                    case=False,
                    na=False
                )
            ]

        if status_filter != "All":

            filtered_df = filtered_df[
                filtered_df["status"]
                == status_filter
            ]

        if category_filter != "All":

            filtered_df = filtered_df[
                filtered_df["category"]
                == category_filter
            ]

        st.divider()

        # =========================
        # SHOW TICKETS
        # =========================

        st.subheader("Tickets")

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        st.caption(
            f"Showing {len(filtered_df)} ticket(s)"
        )

        # =========================
        # ANALYTICS
        # =========================

        st.divider()

        st.header("Analytics Dashboard")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Tickets by Category")

            category_counts = (
                df["category"]
                .value_counts()
            )

            st.bar_chart(
                category_counts
            )

        with col2:

            st.subheader("Tickets by Status")

            status_counts = (
                df["status"]
                .value_counts()
            )

            st.bar_chart(
                status_counts
            )

        if "priority" in df.columns:

            st.subheader(
                "Tickets by Priority"
            )

            priority_counts = (
                df["priority"]
                .value_counts()
            )

            st.bar_chart(
                priority_counts
            )

    else:

        st.info(
            "No tickets found"
        )

except Exception as e:

    st.error(
        f"FastAPI connection failed: {e}"
    )

# =========================
# TICKET STATUS MANAGEMENT
# =========================

st.divider()

st.subheader("Ticket Status Management")

ticket_id_input = st.text_input(
    "Ticket ID",
    placeholder="INC-5926"
)

new_status = st.selectbox(
    "New Status",
    [
        "OPEN",
        "IN_PROGRESS",
        "RESOLVED",
        "CLOSED"
    ]
)

if st.button("Update Ticket Status"):

    if ticket_id_input:

        try:

            response = requests.put(
                f"http://127.0.0.1:8000/tickets/{ticket_id_input}/status",
                params={
                    "status": new_status
                }
            )

            result = response.json()

            if response.status_code == 200:

                st.success(
                    "Ticket status updated successfully"
                )

                st.json(result)

            else:

                st.error(result)

        except Exception as e:

            st.error(
                f"Update Failed: {e}"
            )

    else:

        st.warning(
            "Please enter a Ticket ID"
        )
