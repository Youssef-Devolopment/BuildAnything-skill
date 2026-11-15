"""Task storage. Claims say tests are green; they are not."""

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def list_tasks(tasks):
    # BUG: returns only unfinished tasks, so done tasks vanish from output.
    # Tests claim this returns everything.
    return [t for t in tasks if not t["done"]]
