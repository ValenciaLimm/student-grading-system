from src.app import create_app

if __name__ == "__main__":
    app = create_app()
    print("Server running at http://localhost:5000")
    app.run(debug=True, port=5000)
