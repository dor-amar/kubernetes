import os

def main():
    # Get the environment variables
    app_name = os.getenv("APP_NAME", "DefaultApp")
    app_port = os.getenv("APP_PORT", "8000")

    # Print the environment variables
    print(f"App Name: {app_name}")
    print(f"App Port: {app_port}")

if __name__ == "__main__":
    main()

