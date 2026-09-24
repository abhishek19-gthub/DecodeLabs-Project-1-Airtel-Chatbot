print("==========================================")
print("       TECHNICAL AIRTEL ASSISTANCE")
print("==========================================")
print("Hello! I am your Airtel Assistance Chatbot.")
print("Type 'help' to see available options.")
print("Type 'exit' or 'bye' to end the chat.")
print("==========================================")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit" or user_input == "bye":
        print("AIRTEL BOT: Thank you for contacting Airtel. Have a nice day!")
        break

    elif user_input == "hello" or user_input == "hi":
        print("AIRTEL BOT: Hello! How may I help you?")

    elif user_input == "no internet":
        print("AIRTEL BOT: Please restart your router and wait for 2 minutes.")

    elif user_input == "slow internet":
        print("AIRTEL BOT: Try restarting your router or switching to 5GHz WiFi.")

    elif user_input == "router not working":
        print("AIRTEL BOT: Check the cables and make sure the router power light is on.")

    elif user_input == "how to check balance":
        print("AIRTEL BOT: Dial *121# from your Airtel number to check your balance.")

    elif user_input == "how to recharge":
        print("AIRTEL BOT: You can recharge using the Airtel Thanks app or website.")

    elif user_input == "how to pay bill":
        print("AIRTEL BOT: Open the Airtel Thanks app and select the Pay Bill option.")

    elif user_input == "network issue":
        print("AIRTEL BOT: Turn Airplane Mode on and off and check your network again.")

    elif user_input == "sim not working":
        print("AIRTEL BOT: Remove and reinsert the SIM. If the problem continues, visit an Airtel store.")

    elif user_input == "customer care number":
        print("AIRTEL BOT: You can call 121 from your Airtel number.")

    elif user_input == "help":
        print("AIRTEL BOT: You can ask me about:")
        print("- no internet")
        print("- slow internet")
        print("- router not working")
        print("- how to check balance")
        print("- how to recharge")
        print("- how to pay bill")
        print("- network issue")
        print("- sim not working")
        print("- customer care number")

    elif user_input == "ok":
        print("AIRTEL BOT: Is there anything else I can help you with?")
        answer = input("You: ").lower().strip()

        if answer == "yes" or answer == "ok":
            print("AIRTEL BOT: Sure! Please tell me your issue.")
        elif answer == "no" or answer == "nope":
            print("AIRTEL BOT: Thank you for contacting Airtel. Have a nice day!")
            break
        else:
            print("AIRTEL BOT: Please type yes or no.")

    else:
        print("AIRTEL BOT: Sorry, I do not understand. Type 'help' for available options.")
