class FolderStructure:
    def __init__(self, name_surname, student_id, lab_folder, is_ok):
        self.name_surname = name_surname
        self.student_id = student_id
        self.lab_folder = lab_folder
        self.is_ok = is_ok

    def __str__(self):
        return f"{self.name_surname} {self.lab_folder} pusty:{self.is_ok}"
