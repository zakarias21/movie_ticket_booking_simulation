list_of_movies = {
    "ironman": {"time": "7:00pm", "price": 5},
    "venom": {"time": "8:40pm", "price": 7.5},
    "avengers": {"time": "10:20pm", "price": 10}
}
print("Welcome to movie booking")
print("Please choose from the gallery")
print("============================")
for title, info in list_of_movies.items():
    print(f"{info['time']} - {title} - {info['price']:.2f}$")
print("Booking guides")
print("============================")
print("1. Type your favorite movie name")
print("2. Enter number of tickets you want")
print("3. Type 'no' when asked if you want to book another movie")
#the logics and calculations to ask the user to choose a movie and number of tickets.
total_cost = 0
total_tickets=0
while True:
    movie = input("Enter movie name: ").lower()
    if movie in list_of_movies:
        tickets = int(input("Enter number of tickets: "))
        cost = tickets * list_of_movies[movie]["price"]
        total_cost = total_cost + cost
        total_tickets = total_tickets + tickets
        print("Added", tickets, "tickets for", movie.capitalize(),
                "at", list_of_movies[movie]["time"], "Subtotal:", 
cost, "$")
#Confirms total price and asks if they want to book another movie.
#Ends when they say “no” and displays total bookings and cost.
        another = input("Do you want to book another movie? (yes/no): ").lower()
        if another == "no":
            print("==========================")
            print("Booking Summary")
            print("Total tickets booked:", total_tickets)
            print("Total amount:", total_cost, "$")
            print("Thank you for booking! Enjoy your movies.")
            break
        else:
            print("Movie not found. Please try again.");