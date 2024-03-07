class sessionCurrent:
    def __init__(self, json_data = None) -> None:
        if json_data is None:
            json_data = {}
        self.note = json_data.get("note", None)
        self.project_name = json_data.get("projectName", None)
        self.task_name = json_data.get("taskName", None)
        self.log_id = json_data.get("id", None)

    def __str__(self) -> str:
        return f"log_id = {self.log_id},\nproject_name = {self.project_name},\ntask_name = {self.task_name},\nnote = {self.note},\n"

class userProjects:
    def __init__(self, json_data = None) -> None:
        if json_data is None:
            json_data = {}
        self.name = json_data.get("name", None)
        self.archived = json_data.get("archived", None)
        self.dateArchived = json_data.get("dateArchived", None)
        self.dateCreated = json_data.get("dateCreated", None)
        self.clientId = json_data.get("clientId", None)
        self.clientName = json_data.get("clientName", None)
        self.budgetAlertPercent = json_data.get("budgetAlertPercent", None)
        self.budgetType = json_data.get("budgetType", None)
        self.totalTimeLogged = json_data.get("totalTimeLogged", None)
        self.budgetValue = json_data.get("budgetValue", None)
        self.totalAmount = json_data.get("totalAmount", None)
        self.totalExpense = json_data.get("totalExpense", None)
        self.laborCost = json_data.get("laborCost", None)
        self.totalCost = json_data.get("totalCost", None)
        self.billableTimeLogged = json_data.get("billableTimeLogged", None)
        self.totalBillableAmount = json_data.get("totalBillableAmount", None)
        self.billable = json_data.get("billable", None)
        self.roundType = json_data.get("roundType", None)
        self.roundInterval = json_data.get("roundInterval", None)
        self.budgetSpentPercentage = json_data.get("budgetSpentPercentage", None)
        self.budgetTarget = json_data.get("budgetTarget", None)
        self.budgetPeriodType = json_data.get("budgetPeriodType", None)
        self.budgetSpent = json_data.get("budgetSpent", None)
        self.customId = json_data.get("customId", None)
        self.id = json_data.get("id", None)
        self.data = json_data

    def __str__(self) -> str:
        return f"name = {self.name},\ntime logged = {self.totalTimeLogged},\nid = {self.id}\n"


if __name__ == '__main__':
    dothething = userProjects()
    print(dothething)