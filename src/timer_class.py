class sessionCurrent:
    def __init__(self, json_data = None) -> None:
        if json_data is None:
            json_data = {}
        self.note = json_data.get("note", None)
        self.project_name = json_data.get("projectName", None)
        self.task_name = json_data.get("taskName", None)
        self.log_id = json_data.get("id", None)

    def __str__(self) -> str:
        return f"log_id = {self.log_id},\ntask_name = {self.task_name},\nproject_name = {self.project_name},\nnote = {self.note},\n"

class userProjects:
    def __init__(self, json_data = None) -> None:
        if json_data is None:
            json_data = {}
        self.project_name = json_data.get("name", None)
        self.total_time_logged = json_data.get("totalTimeLogged", None)
        self.id = json_data.get("id", None)
        self.data = json_data

    def __str__(self) -> str:
        return f"name = {self.project_name},\ntime logged = {self.total_time_logged},\nid = {self.id}\n"


if __name__ == '__main__':
    dothething = userProjects()
    print(dothething)