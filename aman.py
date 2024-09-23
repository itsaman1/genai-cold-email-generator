try:
    with open('app/resource/my_portfolio.csv', 'r') as file:
        # Your code to read the file
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the path and try again.")