from project import Project
from datetime import datetime


def main():
    """ The main function that runs the project management program."""
    projects = load_projects("projects.txt")
    while True:
        display_menu()
        choice = input(">>> ").lower()
        if choice == "q":
            break
        elif choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_string = input("Enter date to filter projects by (d/m/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == "a":
            project = create_new_project()
            projects.append(project)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid option, please try again.")


def display_menu():
    """Display the main menu options."""
    print("\nMenu:")
    print(" (L)oad projects")
    print(" (S)ave projects")
    print(" (D)isplay projects")
    print(" (F)ilter projects by date")
    print(" (A)dd new project")
    print(" (U)pdate project")
    print(" (Q)uit")


def load_projects(filename):
    """ Load projects from a file."""
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            parts = line.strip().split("\t")
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """  Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """  Display the projects, separating them into incomplete and completed projects."""
    print("\nIncomplete projects:")
    for project in sorted([p for p in projects if not p.is_complete()]):
        print(project)

    print("\nCompleted projects:")
    for project in sorted([p for p in projects if p.is_complete()]):
        print(project)


def filter_projects_by_date(projects, date_string):
    """Display projects that start after a specified date."""
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    print("\nProjects starting after", date_string + ":")
    for project in sorted([p for p in projects if p.start_date > date], key=lambda p: p.start_date):
        print(project)


def create_new_project():
    """Create a new project by prompting the user for input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (d/m/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete:  ")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    if not projects:
        print("No projects to update.")
        return

    print("Project list:")
    for i in range(len(projects)):
        print(
            f"{i} {projects[i].name}, start: {projects[i].start_date.strftime('%d/%m/%Y')}, priority {projects[i].priority}, estimate: ${projects[i].cost_estimate:,.2f}, completion: {projects[i].completion_percentage}%")

    project_number = int(input("Project choice: "))
    if 0 <= project_number < len(projects):
        index = project_number
        print(
            f"{projects[index].name}, start: {projects[index].start_date.strftime('%d/%m/%Y')}, priority {projects[index].priority}, estimate: ${projects[index].cost_estimate:,.2f}, completion: {projects[index].completion_percentage}%")
        completion_percentage = input("New Percentage: ")
        if completion_percentage:
            projects[index].completion_percentage = int(completion_percentage)

        priority = input(f"New priority: ")
        if priority:
            projects[index].priority = int(priority)
    else:
        print("Invalid project number.")


if __name__ == '__main__':
    main()