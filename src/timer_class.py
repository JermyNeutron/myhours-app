class MyHour_Session_Current:
    def __init__(self, json_data=None) -> None:
        if json_data is None:
            json_data = {}
        self.note = json_data.get("note", None)
        self.project_name = json_data.get("projectName", None)
        self.task_name = json_data.get("taskName", None)
        self.log_id = json_data.get("id", None)

    def __str__(self) -> str:
        return f"log_id = {self.log_id},\ntask_name = {self.task_name},\nproject_name = {self.project_name},\nnote = {self.note},"

if __name__ == '__main__':
    myinstance = MyHour_Session_Current()
    print(myinstance)