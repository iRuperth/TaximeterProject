def log_journey(name, total_duration, total_price):
    fareContent = f"Name: {name}\n"
    fareContent += f"Total duration: {total_duration:.2f} seconds\n"
    fareContent += f"Total price: {total_price:.2f} €\n" 
    fareContent += "\n" 
    try:
        #Using "with open" to append the fare content to the historical.txt file.
        with open("historical.txt", "a", encoding='utf-8') as file:
                file.write(fareContent)
    except IOError:
            print("Error trying to write to historical.txt")