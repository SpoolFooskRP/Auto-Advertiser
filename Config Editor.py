import yaml

# Define the path to the config file
config_file = "config.yml"

# Read the existing config
with open(config_file, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def ask_boolean(question):
    """Ask the user for a yes/no answer and return True/False."""
    while True:
        user_input = input(f"{question} (yes/no): ").strip().lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def ask_input(question, is_integer=False):
    """Ask the user for input, returning the input."""
    while True:
        user_input = input(f"{question}: ").strip()
        if user_input == "":
            print("This field cannot be empty. Please provide a valid input.")
        elif is_integer:
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid integer.")
        else:
            return user_input

def ask_for_token():
    """Asks the user for the token and ensures it has no unnecessary quotes."""
    token = input(f"Enter your token: ").strip()
    if not token:
        print("The token is required. Please enter a valid token.")
        return ask_for_token()
    return token

def ask_for_channel_ids():
    """Ask for channel IDs."""
    channel_ids = []
    while True:
        channel_id = input("Enter a channel ID (or press Enter to finish): ").strip()
        if channel_id == "":
            break
        # Append the channel ID directly without wrapping in single quotes
        channel_ids.append(channel_id)
    if not channel_ids:
        print("At least one channel ID is required. Please enter at least one.")
        return ask_for_channel_ids()
    return channel_ids

# Ask for token
config['default']['token'] = ask_for_token()

# Ask for interval in minutes
config['default']['interval'] = ask_input("Enter the interval in minutes", is_integer=True)

# Ask for randomize_interval settings
config['default']['randomize_interval']['enabled'] = ask_boolean("Enable randomize interval")
if config['default']['randomize_interval']['enabled']:
    config['default']['randomize_interval']['minimum_interval'] = ask_input("Enter the minimum interval (in minutes)", is_integer=True)
    config['default']['randomize_interval']['maximum_interval'] = ask_input("Enter the maximum interval (in minutes)", is_integer=True)

# Ask for wait_between_messages settings
config['default']['wait_between_messages']['enabled'] = ask_boolean("Enable wait between messages")
if config['default']['wait_between_messages']['enabled']:
    config['default']['wait_between_messages']['minimum_interval'] = ask_input("Enter the minimum wait time between messages (in seconds)", is_integer=True)
    config['default']['wait_between_messages']['maximum_interval'] = ask_input("Enter the maximum wait time between messages (in seconds)", is_integer=True)

# Ask for avoid_spam settings
config['default']['avoid_spam']['enabled'] = ask_boolean("Enable avoid spam")
if config['default']['avoid_spam']['enabled']:
    config['default']['avoid_spam']['minimum_messages'] = ask_input("Enter the minimum number of messages to avoid spam", is_integer=True)
    config['default']['avoid_spam']['maximum_messages'] = ask_input("Enter the maximum number of messages to avoid spam", is_integer=True)

# Ask for work_hours settings
config['default']['work_hours']['enabled'] = ask_boolean("Enable work hours")
if config['default']['work_hours']['enabled']:
    config['default']['work_hours']['start_time'] = ask_input("Enter the start time (0-23)", is_integer=True)
    config['default']['work_hours']['end_time'] = ask_input("Enter the end time (0-23)", is_integer=True)

# Ask for channels
config['default']['channels'] = ask_for_channel_ids()

# Write updated config back to the file
with open(config_file, "w") as file:
    yaml.dump(config, file)

print("Configuration has been updated.")
