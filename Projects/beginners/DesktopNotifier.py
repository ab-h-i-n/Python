#pip install win10toast
from win10toast import ToastNotifier

# Initialize the ToastNotifier
toast = ToastNotifier()

name = input("Enter your name : ").capitalize()

#toast.show_toast(heading,content)
toast.show_toast(f"Hello Mr. {name}", "Notification Succefully send!")


