import flet as ft

# 1. Mock Data (MVP Stage)
RECIPES = [
    {"title": "Spicy Garlic Tomato Pasta", "time": "25 min", "cal": "650 kcal", "image": "https://images.unsplash.com/photo-1555072956-7758afb20e8f?auto=format&fit=crop&w=300&q=80"},
    {"title": "Honey Glazed Salmon", "time": "35 min", "cal": "550 kcal", "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=300&q=80"},
    {"title": "Classic Beef Burger", "time": "30 min", "cal": "850 kcal", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=300&q=80"}
]

def main(page: ft.Page):
    # App Settings & Mobile Hardware Simulation
    page.title = "FreshMeals MVP"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.width = 400   # Hardcoding mobile dimensions
    page.window.height = 800
    
    # CRITICAL: Native Scrolling (Avoids nested ListView layout crashes on your Vivobook)
    page.scroll = "auto"

    # 2. Reusable UI Component: Recipe Card
    def create_recipe_card(recipe):
        return ft.Card(
            elevation=2,
            margin=10, # Flet 0.80+: Use simple numbers for margin
            content=ft.Container(
                padding=0,
                content=ft.Column(
                    controls=[
                        # Food Image
                        ft.Image(
                            src=recipe["image"],
                            height=150,
                            width=360, # CRITICAL: Hardcoded width instead of float("inf")
                            fit="cover", # FIX: Use string shorthand instead of the deprecated ImageFit
                            border_radius=ft.BorderRadius.only(top_left=10, top_right=10)
                        ),
                        # Recipe Info
                        ft.Container(
                            padding=10,
                            content=ft.Column([
                                ft.Text(recipe["title"], weight=ft.FontWeight.BOLD, size=16),
                                ft.Row([
                                    # Flet 0.80+: Use simple lowercase strings for Material Icons and Colors
                                    ft.Icon("access_time", size=14, color="grey"),
                                    ft.Text(recipe["time"], color="grey", size=12),
                                    ft.Icon("local_fire_department", size=14, color="orange"),
                                    ft.Text(recipe["cal"], color="grey", size=12),
                                ], spacing=5)
                            ])
                        )
                    ],
                    spacing=0
                )
            )
        )

    # 3. Main Content Area (Standard Column instead of ListView)
    recipe_feed = ft.Column(
        controls=[
            ft.Container(
                padding=10,
                content=ft.Text("This Week's Menu", size=22, weight=ft.FontWeight.BOLD)
            ), 
            *[create_recipe_card(r) for r in RECIPES]
        ]
    )

    # 4. Bottom Navigation Bar
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            # Using ft.NavigationBarDestination and string-based icons
            ft.NavigationBarDestination(icon="home_outlined", selected_icon="home", label="Menu"),
            ft.NavigationBarDestination(icon="receipt_long_outlined", selected_icon="receipt_long", label="My Deliveries"),
            ft.NavigationBarDestination(icon="person_outline", selected_icon="person", label="Profile"),
        ],
        selected_index=0,
    )

    # 5. Mount UI
    page.add(recipe_feed)

# FIX: Use ft.run() instead of the deprecated ft.app()
ft.run(main)
