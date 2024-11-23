from bl import BL
from ui import UI

def main():
    bl_instance = BL()
    ui_instance = UI(bl_instance)
    ui_instance.login_menu()

if __name__ == "__main__":
    main()
