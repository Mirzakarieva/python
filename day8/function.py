def greet():
    print("Hello")
    print("How are you?")
    print("The weather is nice today, isn't it?")


def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How are you, {name}?")
    print(f"{name} ,the weather is nice today, isn't it?")

def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is the weather like today in {location}?")
    
# greet_with("Mohira", "Nowhere")
greet_with(location="Nowhere", name="Mohira")