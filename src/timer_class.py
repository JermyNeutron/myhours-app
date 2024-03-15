class sessionCurrent:
    def __init__(self, json_data = None) -> None:
        if json_data is None:
            json_data = {}
        self.note = json_data.get("note", None)
        self.project_name = json_data.get("projectName", None)
        self.task_name = json_data.get("taskName", None)
        self.log_id = json_data.get("id", None)


    def __str__(self) -> str:
        return f"log_id = {self.log_id},\nproject_name = {self.project_name},\ntask_name = {self.task_name},\nnote = {str(self.note)}\n"


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


    def __repr__(self) -> str:
        return 


class userLogs:
    def __init__(self, json_data=None) -> None:
        if json_data == None:
            json_data = {}
        self.note = json_data.get("note", None)
        self.date = json_data.get("date", None)
        self.duration = json_data.get("duration", None)
        self.projectName = json_data.get("projectName", None)
        self.taskName = json_data.get("taskName", None)
        self.clientName = json_data.get("clientName", None)
        self.projectInvoiceMethod = json_data.get("projectInvoiceMethod", None)
        self.projectArchived = json_data.get("projectArchived", None)
        self.taskArchived = json_data.get("taskArchived", None)
        self.customField1 = json_data.get("customField1", None)
        self.customField2 = json_data.get("customField2", None)
        self.customField3 = json_data.get("customField3", None)
        self.running = json_data.get("running", None)
        self.startTime = json_data.get("startTime", None)
        self.endTime = json_data.get("endTime", None)
        self.times = json_data.get("times", None)
        self.status = json_data.get("status", None)
        self.invoiceId = json_data.get("invoiceId", None)
        self.projectId = json_data.get("projectId", None)
        self.taskId = json_data.get("taskId", None)
        self.billable = json_data.get("billable", None)
        self.inLockedPeriod = json_data.get("inLockedPeriod", None)
        self.expense = json_data.get("expense", None)
        self.userId = json_data.get("userId", None)
        self.amount = json_data.get("amount", None)
        self.rate = json_data.get("rate", None)
        self.laborCost = json_data.get("laborCost", None)
        self.laborRate = json_data.get("laborRate", None)
        self.billableDuration = json_data.get("billableDuration", None)
        self.billableHours = json_data.get("billableHours", None)
        self.laborHours = json_data.get("laborHours", None)
        self.tags = json_data.get("tags", None)
        self.attachments = json_data.get("attachments", None)
        self.billableAmount = json_data.get("billableAmount", None)
        self.id = json_data.get("id", None)
        self.data = json_data


    def __str__(self) -> str:
        return f"log_id = {self.id},\nactive: {self.running},\nproject_name = {self.projectName},\ntask_name = {self.taskName},\nnote = {(str(self.note))}\n"


    def __repr__(self) -> str:
        return f"{self.data}"


if __name__ == '__main__':
    dothething = userLogs()
    print(repr(dothething))