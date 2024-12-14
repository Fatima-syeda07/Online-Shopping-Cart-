import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Categories Data
categories = [
    {"name": "Clothes", "image": "images/Clothes.png"},
    {"name": "Makeup Products", "image": "images/makeup.png"},
    {"name": "Haircare Products", "image": "images/Haircare.png"},
    {"name": "Skincare Products", "image": "images/Skincare.png"}
]

# Products Data
products = [
    # Clothes Category
    {"id": 1, "name": "T-Shirt", "price": 1000.00, "category": "Clothes", "image": "images/Tshirt.png"},
    {"id": 2, "name": "Jeans", "price": 1500.00, "category": "Clothes", "image": "images/jeans.png"},
    {"id": 3, "name": "Jacket", "price": 2000.00, "category": "Clothes", "image": "images/jacket.png"},
    {"id": 4, "name": "Shirt", "price": 1500.00, "category": "Clothes", "image": "images/shirt.png"},
    {"id": 5, "name": "Skirt", "price": 2000.00, "category": "Clothes", "image": "images/skirt.png"},
    {"id": 6, "name": "Frock", "price": 3000.00, "category": "Clothes", "image": "images/frock.png"},
    
    # Makeup Products Category
    {"id": 7, "name": "Lipstick", "price": 500.00, "category": "Makeup Products", "image": "images/lipstick.png"},
    {"id": 8, "name": "Foundation", "price": 1000.00, "category": "Makeup Products", "image": "images/foundation.png"},
    {"id": 9, "name": "Mascara", "price": 400.00, "category": "Makeup Products", "image": "images/mascara.png"},
    {"id": 10, "name": "Eyeliner", "price": 400.00, "category": "Makeup Products", "image": "images/eyeliner.png"},
    {"id": 11, "name": "Eyeshadow Palatte", "price": 1500.00, "category": "Makeup Products", "image": "images/eyeshadow.png"},
    {"id": 12, "name": "Blush", "price": 1000.00, "category": "Makeup Products", "image": "images/blush.png"},
    
    # Haircare Products Category
    {"id": 13, "name": "Shampoo", "price": 1000.00, "category": "Haircare Products", "image": "images/shampoo.png"},
    {"id": 14, "name": "Conditioner", "price": 1200.00, "category": "Haircare Products", "image": "images/conditioner.png"},
    {"id": 15, "name": "Hair Oil", "price": 700.00, "category": "Haircare Products", "image": "images/hair_oil.png"},
    {"id": 16, "name": "Hair Serum", "price": 1500.00, "category": "Haircare Products", "image": "images/hair_serum.png"},
    {"id": 17, "name": "Hair Spray", "price": 900.00, "category": "Haircare Products", "image": "images/hair_spray.png"},
    {"id": 18, "name": "Straightener", "price": 2500.00, "category": "Haircare Products", "image": "images/straightener.png"},
    
    # Skincare Products Category
    {"id": 19, "name": "Moisturizer", "price": 750.00, "category": "Skincare Products", "image": "images/moisturizer.png"},
    {"id": 20, "name": "Sunscreen", "price": 1000.00, "category": "Skincare Products", "image": "images/sunscreen.png"},
    {"id": 21, "name": "Cleanser", "price": 1100.00, "category": "Skincare Products", "image": "images/cleanser.png"},
    {"id": 22, "name": "Face Wash", "price": 900.00, "category": "Skincare Products", "image": "images/face_wash.png"},
    {"id": 23, "name": "Toner", "price": 1000.00, "category": "Skincare Products", "image": "images/toner.png"},
    {"id": 24, "name": "Serum", "price": 1400.00, "category": "Skincare Products", "image": "images/serum.png"}
]

# User credentials storage
credentials = {}
cart = {}  # Stores cart items with quantities

# Colors
BG_COLOR = "#f9f9f9"
NAV_COLOR = "#333333"
NAV_TEXT_COLOR = "#ffffff"
CATEGORY_BG = "#ffffff"
BTN_COLOR = "#e74c3c"
BTN_TEXT_COLOR = "#ffffff"
FRAME_BG = "#f4f4f4"
LABEL_COLOR = "#333333"

# Root window
root = tk.Tk()
root.title("Maal Uthao")
root.geometry("900x600")
root.config(bg=BG_COLOR)

# Functions
def register_user(username_entry, password_entry, register_frame):
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty!")
        return

    if username in credentials:
        messagebox.showerror("Error", "Username already exists!")
        return

    credentials[username] = password
    messagebox.showinfo("Success", "Registration successful! Please login.")
    register_frame.destroy()
    create_login_screen()

def login(username_entry, password_entry, login_frame):
    username = username_entry.get()
    password = password_entry.get()

    if username in credentials and credentials[username] == password:
        login_frame.destroy()
        nav_frame.pack(side="top", fill="x")
        display_frame.pack(fill="both", expand=True, padx=20, pady=10)
        load_categories()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

def load_categories():
    for widget in display_frame.winfo_children():
        widget.destroy()

    row, col = 0, 0
    for category in categories:
        category_frame = tk.Frame(display_frame, bg=CATEGORY_BG, relief="ridge", borderwidth=1)
        category_frame.grid(row=row, column=col, padx=10, pady=10)

        try:
            img = Image.open(category["image"])
            img = img.resize((200, 120), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(category_frame, image=img_tk, bg=CATEGORY_BG)
            img_label.image = img_tk
            img_label.pack(pady=5)
        except:
            img_label = tk.Label(category_frame, text="Image Not Found", bg=CATEGORY_BG, fg="red")
            img_label.pack(pady=5)

        name_label = tk.Label(category_frame, text=category["name"], bg=CATEGORY_BG, fg="#333333", font=("Arial", 14))
        name_label.pack(pady=2)

        view_more_button = tk.Button(category_frame, text="View More", bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                                     font=("Arial", 10), command=lambda c=category["name"]: load_products(c))
        view_more_button.pack(pady=5)

        col += 1
        if col > 1:
            col = 0
            row += 1

def load_products(category_name):
    product_window = tk.Toplevel(root)
    product_window.title(f"{category_name} Products")
    product_window.geometry("800x600")
    product_window.config(bg=BG_COLOR)

    product_frame = tk.Frame(product_window, bg=BG_COLOR)
    product_frame.pack(fill="both", expand=True, padx=20, pady=10)

    filtered_products = [product for product in products if product["category"] == category_name]

    row, col = 0, 0
    for product in filtered_products:
        product_frame_inner = tk.Frame(product_frame, bg=CATEGORY_BG, relief="ridge", borderwidth=1)
        product_frame_inner.grid(row=row, column=col, padx=10, pady=10)

        try:
            img = Image.open(product["image"])
            img = img.resize((200, 120), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(product_frame_inner, image=img_tk, bg=CATEGORY_BG)
            img_label.image = img_tk
            img_label.pack(pady=5)
        except:
            img_label = tk.Label(product_frame_inner, text="Image Not Found", bg=CATEGORY_BG, fg="red")
            img_label.pack(pady=5)

        name_label = tk.Label(product_frame_inner, text=product["name"], bg=CATEGORY_BG, fg="#333333", font=("Arial", 14))
        name_label.pack(pady=2)

        price_label = tk.Label(product_frame_inner, text=f"PKR {product['price']:.2f}", bg=CATEGORY_BG, fg="red",
                               font=("Arial", 12))
        price_label.pack(pady=2)

        add_to_cart_button = tk.Button(product_frame_inner, text="Add to Cart", bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                                       font=("Arial", 10), command=lambda p=product: add_to_cart(p))
        add_to_cart_button.pack(pady=5)

        col += 1
        if col > 2:
            col = 0
            row += 1

def add_to_cart(product):
    if product["id"] in cart:
        cart[product["id"]]["quantity"] += 1
    else:
        cart[product["id"]] = {"product": product, "quantity": 1}

    messagebox.showinfo("Cart Updated", f"{product['name']} added to cart!")

def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Shopping Cart")
    cart_window.geometry("400x400")
    cart_window.config(bg=BG_COLOR)

    total_price = 0
    for item in cart.values():
        product = item["product"]
        quantity = item["quantity"]
        total_price += product["price"] * quantity

        cart_item_label = tk.Label(cart_window, text=f"{product['name']} - Quantity: {quantity} - Total: PKR {product['price'] * quantity:.2f}",
                                   bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 12))
        cart_item_label.pack(pady=5)

    total_label = tk.Label(cart_window, text=f"Total Price: PKR {total_price:.2f}", bg=BG_COLOR, fg="red",
                           font=("Arial", 14, "bold"))
    total_label.pack(pady=10)

    def checkout():
        if cart:
            messagebox.showinfo("Checkout", "Checkout Complete!")
            cart.clear()  # Clear the cart
            cart_window.destroy()
        else:
            messagebox.showwarning("Empty Cart", "Your cart is already empty!")

    checkout_button = tk.Button(cart_window, text="Checkout", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12),
                                 command=checkout)
    checkout_button.pack(pady=10)

# Main Frame Setup
nav_frame = tk.Frame(root, bg=NAV_COLOR)
nav_label = tk.Label(nav_frame, text="Maal Uthao - Online Shopping", bg=NAV_COLOR, fg=NAV_TEXT_COLOR, font=("Arial", 18))
nav_label.pack(side="left", padx=20)
cart_button = tk.Button(nav_frame, text="View Cart", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12),
                        command=view_cart)
cart_button.pack(side="right", padx=20)

display_frame = tk.Frame(root, bg=BG_COLOR)

def create_login_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

    login_frame = tk.Frame(root, bg=FRAME_BG)
    login_frame.pack(pady=100, padx=100)

    username_label = tk.Label(login_frame, text="Username:", bg=FRAME_BG, fg=LABEL_COLOR)
    username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    username_entry = tk.Entry(login_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(login_frame, text="Password:", bg=FRAME_BG, fg=LABEL_COLOR)
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    login_button = tk.Button(login_frame, text="Login", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: login(username_entry, password_entry, login_frame))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    register_button = tk.Button(login_frame, text="Register", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: create_register_screen(login_frame))
    register_button.grid(row=3, column=0, columnspan=2, pady=5)

def create_register_screen(login_frame):
    login_frame.destroy()

    register_frame = tk.Frame(root, bg=FRAME_BG)
    register_frame.pack(pady=100, padx=100)

    username_label = tk.Label(register_frame, text="Username:", bg=FRAME_BG, fg=LABEL_COLOR)
    username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    username_entry = tk.Entry(register_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(register_frame, text="Password:", bg=FRAME_BG, fg=LABEL_COLOR)
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    password_entry = tk.Entry(register_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    register_button = tk.Button(register_frame, text="Register", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: register_user(username_entry, password_entry, register_frame))
    register_button.grid(row=2, column=0, columnspan=2, pady=10)

    back_button = tk.Button(register_frame, text="Back", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=create_login_screen)
    back_button.grid(row=3, column=0, columnspan=2, pady=5)

# Start with Login Screen
create_login_screen()
root.mainloop()
