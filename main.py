import flet as ft

# 1. Mock Data (Dummy Recipes to make it look real without a database)
RECIPES = [
    {"title": "Spicy Garlic Tomato Pasta", "time": "25 min", "cal": "650 kcal", "image": "https://images.unsplash.com/photo-1555072956-7758afb20e8f?auto=format&fit=crop&w=300&q=80"},
    {"title": "Honey Glazed Salmon", "time": "35 min", "cal": "550 kcal", "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=300&q=80"},
    {"title": "Classic Beef Burger", "time": "30 min", "cal": "850 kcal", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=300&q=80"}
]

def main(page: ft.Page):
    # App Settings
    page.title = "FreshMeals MVP"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # 2. Reusable UI Component: Recipe Card
    # This keeps our code modular and clean for your 8GB Vivobook
    def create_recipe_card(recipe):
        return ft.Card(
            elevation=2,
            margin=ft.margin.all(10),
            content=ft.Container(
                padding=0,
                content=ft.Column(
                    controls=[
                        # Food Image
                        ft.Image(
                            src=recipe["image"],
                            height=150,
                            width=float("inf"),
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(top_left=10, top_right=10)
                        ),
                        # Recipe Info (Title, Time, Calories)
                        ft.Container(
                            padding=10,
                            content=ft.Column([
                                ft.Text(recipe["title"], weight=ft.FontWeight.BOLD, size=16),
                                ft.Row([
                                    ft.Icon(ft.icons.ACCESS_TIME, size=14, color=ft.colors.GREY),
                                    ft.Text(recipe["time"], color=ft.colors.GREY, size=12),
                                    ft.Icon(ft.icons.LOCAL_FIRE_DEPARTMENT, size=14, color=ft.colors.ORANGE),
                                    ft.Text(recipe["cal"], color=ft.colors.GREY, size=12),
                                ], spacing=5)
                            ])
                        )
                    ],
                    spacing=0
                )
            )
        )

    # 3. Main Content Area (Scrollable Feed)
    recipe_feed = ft.ListView(
        expand=True,
        padding=ft.padding.all(10),
        controls=[
            ft.Text("This Week's Menu", size=22, weight=ft.FontWeight.BOLD), 
            *[create_recipe_card(r) for r in RECIPES] # Generates a card for every recipe
        ]
    )

    # 4. Bottom Navigation Bar (HelloFresh style)
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Menu"),
            ft.NavigationDestination(icon=ft.icons.RECEIPT_LONG_OUTLINED, selected_icon=ft.icons.RECEIPT_LONG, label="My Deliveries"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, selected_icon=ft.icons.PERSON, label="Profile"),
        ],
        selected_index=0,
    )

    # 5. Add everything to the screen
    page.add(recipe_feed)

ft.app(target=main)