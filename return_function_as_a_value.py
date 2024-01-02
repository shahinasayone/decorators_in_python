def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Team")
print(greet())  # prints "Hello, Team!"

# Output: Hello, Team!