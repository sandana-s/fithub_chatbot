class FitMate:
    def __init__(self):
        self.products = {
            "Yoga Mat": {"description": "A high-quality, non-slip yoga mat for your workouts", "price": 29.99, "available": True},
            "Fitness Tracker": {"description": "Track your heart rate, steps, and sleep with this fitness tracker", "price": 49.99, "available": True},
            "Portable Blender": {"description": "Blend your smoothies on-the-go with this compact portable blender", "price": 39.99, "available": True},
            "Water Bottle": {"description": "A stainless steel, reusable water bottle to stay hydrated", "price": 19.99, "available": True},
            "Resistance Bands": {"description": "Set of resistance bands for strength training and stretching", "price": 14.99, "available": True},
            "Dumbbells": {"description": "Pair of adjustable dumbbells for home strength training", "price": 89.99, "available": False},
            "Foam Roller": {"description": "Foam roller for muscle recovery and relaxation", "price": 24.99, "available": True},
            "Jump Rope": {"description": "Speed jump rope for cardio workouts and endurance training", "price": 9.99, "available": True},
            "Kettlebell": {"description": "Durable kettlebell for strength and conditioning workouts", "price": 49.99, "available": True},
            "Massage Gun": {"description": "Portable massage gun for muscle relaxation and recovery", "price": 99.99, "available": False}
        }
        self.cart = []
        print("FitMate initialized. Type 'start' to begin a conversation.")

    def start(self):
        print("Hello! Welcome to FitHub, your go-to fitness store. How can I assist you today?")

    def handle_query(self, user_input):
        user_input = user_input.lower()

        # Greet
        if any(greeting in user_input for greeting in ["hello", "hi", "hey", "greetings"]):
            return "Hello! Welcome to FitHub. How can I help you with our fitness products today?"

        # Product listing 
        elif any(query in user_input for query in ["list of products","show the products","products","show product","list of product","what products do you have", "show me products", "available products", "what's in stock"]):
            return self.list_products()

        # product information
        elif "tell me about" in user_input:
            product_name = user_input.replace("tell me about", "").strip().capitalize()
            return self.get_product_info(product_name)

        elif "do you have" in user_input:
            product_name = user_input.replace("do you have", "").strip().capitalize()
            return self.get_product_info(product_name)

        #recommendation inquiries
        elif any(word in user_input for word in ["recommend", "suggest","suggest me a product","recommend me a product"]):
            return self.recommend_product()

        # Cart
        elif "add to cart" in user_input:
            product_name = user_input.replace("add to cart", "").strip().capitalize()
            return self.add_to_cart(product_name)

        elif any(cart_query in user_input for cart_query in ["show me my cart","view cart","my cart", "what's in my cart", "my cart","show cart","my cart"]):
            return self.show_cart()

        # Checkout 
        elif any(checkout in user_input for checkout in ["purchase", "checkout", "buy now", "complete order"]):
            return self.complete_purchase()

        # Handle unrecognized input
        else:
            return "I'm sorry, I didn't understand that. You can ask about available products, product recommendations, or view your cart. Let me know how I can assist!"


    def list_products(self):
        available_products = [name for name, details in self.products.items() if details["available"]]
        product_list = "\n- ".join(available_products)
        return f"FitMate: Available products at FitHub:\n- {product_list}"
    
    
    def get_product_info(self, product_name):
        product_name = product_name.lower()
        for name, product in self.products.items():
            if name.lower() == product_name:
                if product["available"]:
                    return f"{name}: {product['description']}, Price: ${product['price']:.2f}."
                else:
                    return f"Sorry, {name} is currently out of stock."
        return "Sorry, we don't have that product."




    def recommend_product(self):
        for product_name, details in self.products.items():
            if details["available"]:
                return f"I recommend the {product_name}: {details['description']}, priced at ${details['price']:.2f}."
        return "I'm sorry, it seems we're out of recommendations at the moment."

    def add_to_cart(self, product_name):
        product_name = product_name.lower()
        for name, product in self.products.items():
            if name.lower() == product_name:
                if product["available"]:
                    self.cart.append(name)
                    return f"{name} has been added to your cart."
                else:
                    return f"Sorry, {name} is currently out of stock."
        return "Sorry, that product is not available."


    def show_cart(self):
        if not self.cart:
            return "Your cart is empty."
        cart_contents = "\n".join(self.cart)
        return f"Your cart contains:\n{cart_contents}"

    def complete_purchase(self):
        if not self.cart:
            return "Your cart is empty. Add items to your cart before checking out."
        total = sum(self.products[item]["price"] for item in self.cart)
        self.cart.clear()  
        return f"Thank you for your purchase! Your total is ${total:.2f}. Your order has been confirmed."

if __name__ == "__main__":
    chatbot = FitMate()
    chatbot.start()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for visiting FitHub. Have a great day!")
            break
        response = chatbot.handle_query(user_input)
        print(f"FitMate: {response}")
