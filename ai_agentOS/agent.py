from agno.agent import Agent
from agno.models.anthropic import Claude
from tools import db_tool



TABLES = """
"Client", "ContactPerson", "CostCenter", "DemandAggregate", "Driver",
"DriverExpense", "DriverRentalSettings", "EmergencyContact", "Guest",
"Invoice", "Notification", "NotificationConfig", "Organization",
"OrganizationSmsTemplateConfig", "Otp", "Package", "PaymentRecords",
"Pin", "RazorPayInvoice", "RentalAgreement", "RentalInspection",
"RentalInspectionImage", "Role", "Route", "SelfDriveRental",
"Tour", "TourExpense", "TourExpenseDocs", "TourGuest", "TourRating",
"TourRequest", "TourRoute", "TourSummary", "TourTracking",
"TourTrackingDocs", "User", "UserNotification", "UserOrg",
"UserRole", "Vehicle", "VehicleDocument", "VehicleModel",
"Vendor", "VendorAdvancePayment", "VendorAdvancePaymentRecords",
"VendorPackage", "VendorPayment", "VendorPaymentRecords",
"geography_columns", "geometry_columns", "revision_changes",
"revisions", "spatial_ref_sys"
"""




agent = Agent(
    model=Claude(
        id="claude-3-haiku-20240307",
        max_tokens=1000
    ),
tools=[db_tool],
    instructions=f"""
    You are an assistant whose job is to answer questions by looking into a PostgreSQL database.

    You can work only with the following tables:
    {TABLES}

    A few important things to keep in mind while answering:

    - Table names in PostgreSQL are case-sensitive, so always use them exactly as given
      and wrap them in double quotes (for example: FROM "TourGuest").
    - Use only the tables listed above. If a table is not in this list, do not use it.
    - Do not change table names, do not pluralize them, and do not guess new ones.

    Before giving any answer, always run a query using the db_tool and base your
    response strictly on the result returned from the database.

    If a question cannot be answered using the available tables, simply reply with:
    "This information is not present in my database."

    Your role is to read the data, not to assume anything beyond it.
    """
)
def run_agent_logic(user_input: str) -> str:
    return agent.run(user_input)
