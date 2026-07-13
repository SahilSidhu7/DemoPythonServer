import http.server
import json
import socketserver

# Define the port to listen on
PORT = 8000


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """A custom request handler that serves files and responds to API calls."""

    def do_GET(self):
        # 1. Handle API Route
        if self.path == "/api/hello":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # Create a simple JSON response payload
            response_data = {"status": "success", "message": "Hello from Python!"}

            # Write the JSON payload to the response body
            self.wfile.write(json.dumps(response_data).encode("utf-8"))

        # 2. Handle static files (fallback to default behavior)
        else:
            super().do_GET()


def run_server():
    # Allow the server to reuse the address instantly if restarted
    socketserver.TCPServer.allow_reuse_address = True

    # Bind the server to all network interfaces on the specified port
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Server running locally at http://localhost:{PORT}/")
        print(f"📁 Serving static files from your current directory.")
        print("Press Ctrl+C to stop the server.")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")


if __name__ == "__main__":
    run_server()
