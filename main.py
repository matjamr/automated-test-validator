from app.AppEngine import AppEngine
from checkPlagiarism import CheckPlagiarism

if __name__ == '__main__':
    appEngine = AppEngine()
    appEngine.start()

    checkPlagiarism = CheckPlagiarism()
    checkPlagiarism.load_file()
    checkPlagiarism.download_tasks()
    checkPlagiarism.task_comparison()