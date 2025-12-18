import os
import requests
from rich import print
from github import Github
from prompt_toolkit.shortcuts import radiolist_dialog

github_client = None
current_user = None


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def login_github(token):
    global github_client, current_user

    headers = {
        "Authorization": f"token {token}"
    }

    r = requests.get("https://api.github.com/user", headers=headers)

    if r.status_code == 200:
        data = r.json()
        current_user = data["login"]
        github_client = Github(token)
        print(f"[green]Connecté en tant que : {current_user}[/green]")
    else:
        print("[red]Token invalide [/red]")

    input("\nEntrée pour continuer")


def user_info():
    if not github_client:
        print("[red]Pas connecté [/red]")
        input("Entrée pour continuer")
        return

    user = github_client.get_user()
    print(f"""
        [bold cyan]Username[/bold cyan] : [green]{user.login}[/green]
        [bold cyan]Repos[/bold cyan]    : [yellow]{user.public_repos}[/yellow]
        [bold cyan]Followers[/bold cyan]: [yellow]{user.followers}[/yellow]
        [bold cyan]Following[/bold cyan]: [yellow]{user.following}[/ yellow]
    """)

    input("Entrée pour continuer")

def bool_menu():
    result = radiolist_dialog(
        title="Choix",
        text="Sélectionne une option :",
        values=[
            (True, "True"),
            (False, "False"),
        ],
        style={
            "radiolist": "bg:#000000 #ffffff",
            "radiolist.selected": "bg:#ffff00 #000000",  # jaune
        }
    ).run()

    return result

def create_repo(name, des):
    global github_client, current_user

    user = github_client.get_user()

    repo = user.create_repo(
    name=name,
    description=des,
    private=False
    )

    print("Repo créé :", repo.html_url)

def menu():
    print("""
 ██████╗ ██╗████████╗   ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝ ██║╚══██╔══╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ███╗██║   ██║         ██║   ██║   ██║██║   ██║██║     
██║   ██║██║   ██║         ██║   ██║   ██║██║   ██║██║     
╚██████╔╝██║   ██║         ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝   ╚═╝         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
    """)

    if not github_client:
        print("[1] Connect GitHub")
    else:
        print(f"[green]Connecté : {current_user}[/green]")
        print("[1] Infos compte")
        print("[2] Create repo")


    print("[*] Clear")
    print("[0] Quit")


def main():
    while True:
        clear()
        menu()

        try:
            choice = input("\n> ")
        except KeyboardInterrupt:
            break

        if choice == "1":
            if not github_client:
                token = input("GitHub Token > ").strip()
                login_github(token)
            else:
                user_info()
        elif choice == "2":
            name_repo = input("Name of the repo : ")
            def_repo = input("Description of the repo : ")
            bool_menu()
            create_repo(name_repo, def_repo)
        elif choice == "*":
            clear()
            print('viole moi')

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
