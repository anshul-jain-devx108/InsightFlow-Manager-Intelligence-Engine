from app.models.insight import Insight

# Dummy logic – you can use ML or rule-based logic here
def generate_insights(employee) -> list:
    insights = []

    if employee.department.lower() == "sales":
        insights.append(Insight(content=f"{employee.name} closed 5 deals this month!", confidence="High", category="Performance"))

    if employee.role.lower() == "intern":
        insights.append(Insight(content=f"{employee.name} is showing improvement in attendance.", confidence="Medium", category="Behavior"))

    if not insights:
        insights.append(Insight(content="No significant insights this cycle.", confidence="Low", category="Neutral"))

    return insights
