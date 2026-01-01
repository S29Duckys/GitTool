import os
import time
import getpass
import readchar
import requests
from rich import print
from github import Github
from prompt_toolkit.styles import Style
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

def serch_user(username):
    global github_client

    if not github_client:
        print("[red]Pas connecté [/red]")
        input("Entrée pour continuer")
        return

    try:
        user = github_client.get_user(username)
        
        # Récupérer les clés (peuvent être vides)
        try:
            gpg_keys_count = len(list(user.get_gpg_keys()))
            ssh_keys_count = len(list(user.get_keys()))
        except:
            gpg_keys_count = "N/A"
            ssh_keys_count = "N/A"
        
        print(f"""
        [bold cyan]Username[/bold cyan]       : [green]{user.login}[/green]
        [bold cyan]Name[/bold cyan]           : [green]{user.name or 'N/A'}[/green]
        [bold cyan]ID[/bold cyan]             : [green]{user.id}[/green]
        [bold cyan]Bio[/bold cyan]            : [green]{user.bio or 'N/A'}[/green]
        [bold cyan]Company[/bold cyan]        : [green]{user.company or 'N/A'}[/green]
        [bold cyan]Location[/bold cyan]       : [green]{user.location or 'N/A'}[/green]
        [bold cyan]Blog[/bold cyan]           : [green]{user.blog or 'N/A'}[/green]
        [bold cyan]Email[/bold cyan]          : [green]{user.email or 'N/A'}[/green]
        
        [bold cyan]Repos publics[/bold cyan]  : [yellow]{user.public_repos}[/yellow]
        [bold cyan]Gists publics[/bold cyan]  : [yellow]{user.public_gists}[/yellow]
        [bold cyan]Followers[/bold cyan]      : [yellow]{user.followers}[/yellow]
        [bold cyan]Following[/bold cyan]      : [yellow]{user.following}[/yellow]
        
        [bold cyan]Compte créé le[/bold cyan] : [green]{user.created_at}[/green]
        [bold cyan]Mis à jour le[/bold cyan]  : [green]{user.updated_at}[/green]
        
        [bold cyan]Clés GPG[/bold cyan]       : [green]{gpg_keys_count}[/green]
        [bold cyan]Clés SSH[/bold cyan]       : [green]{ssh_keys_count}[/green]
        [bold cyan]Profile URL[/bold cyan]    : [blue]{user.html_url}[/blue]
        """)
        
    except Exception as e:
        print(f"[red]Erreur: {str(e)}[/red]")
        print("[red]Utilisateur non trouvé ou erreur de connexion[/red]")
    
    input("\nEntrée pour continuer")

def get_repo():
    global github_client

    if not github_client:
        print("[red]Pas connecté [/red]")
        input("Entrée pour continuer")
        return

    user = github_client.get_user()
    repos = user.get_repos()

    print(f"[bold cyan]Repos de {user.login} :[/bold cyan]\n")
    i = 0
    for repo in repos:
        i += 1
        print(f"{i}  -- [green]{repo.name}[/green] : {repo.html_url}")

    print("\n[E] Delete a repo")
    print('[Q] Retour')
    while True:
        key = readchar.readkey().lower()

        if key == "e":
                
            break
        elif key == "q":
            break
    
def delete_repo(repo_name):
    global github_client

    if not github_client:
        print("[red]Pas connecté [/red]")
        input("Entrée pour continuer")
        return
    user = github_client.get_user()
    try:
        repo = user.get_repo(repo_name)
        repo.delete()
        print(f"[green]Repo {repo_name} supprimé ![/green]")
    except Exception as e:
        print(f"[red]Erreur: {str(e)}[/red]")
        print("[red]Repo non trouvé ou erreur de connexion[/red]")

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
        \n\n\n
    [E] Display the repo
    [Q] Retour
    """)
    
    while True:
        key = readchar.readkey().lower()

        if key == "e":
            get_repo()
            while True:
                key = readchar.readkey().lower()            
                if key == "q":
                    break
                elif key == 'e':
                    repo_name = input("Name of the repo to delete : ")
                    delete_repo(repo_name)
                    input("Entrée pour continuer")
                    break
        elif key == "q":
            break

def bool_menu():
    style = Style.from_dict({
        "radiolist": "bg:#000000 #ffffff",
        "radiolist.selected": "bg:#ffff00 #000000", 
    })

    result = radiolist_dialog(
        title="Choix",
        text="Private repo ?",
        values=[
            (True, "True"),
            (False, "False"),
        ],
        style=style
    ).run()

    return result

def create_repo(name, des, private):
    global github_client, current_user

    user = github_client.get_user()

    repo = user.create_repo(
        name=name,
        description=des,
        private=private
    )

    print("[green]Repo créé ![/green]", repo.html_url)
    input("Entrée pour continuer")

def menu():
    print("""[bold red]
 ██████╗ ██╗████████╗   ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝ ██║╚══██╔══╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ███╗██║   ██║         ██║   ██║   ██║██║   ██║██║     
██║   ██║██║   ██║         ██║   ██║   ██║██║   ██║██║     
╚██████╔╝██║   ██║         ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝   ╚═╝         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
[/bold red]
    """)

    if not github_client:
        print("[1] Connect GitHub")
    else:
        print(f"[green]Connecté : {current_user}[/green]")
        print("[1] Infos compte")
        print("[2] Create repo")
        print("[3] Search user")


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
                token = getpass.getpass("GitHub Token > ").strip()
                login_github(token)
            else:
                user_info()
        elif choice == "2":
            name_repo = input("Name of the repo : ")
            def_repo = input("Description of the repo : ")
            private = bool_menu()  
            create_repo(name_repo, def_repo, private)
        elif choice == "3":
            serch_username = input("Username to search : ")
            serch_user(serch_username)
        elif choice == "*":
            clear()
            print('viole moi')

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
