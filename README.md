# WebSocket Server

WebSocket server for real-time communication.

## Features

- Handle WebSocket connections from clients.
- Send a welcome message upon connection.
- Respond with the length of the received message.
- Periodically broadcast the total number of received messages.
- Dockerized setup for easy deployment.

## Requirements

- Python 3.7+
- Flask
- Flask-SocketIO
- Eventlet
- Docker and Docker Compose

## Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/lukasz-cz/websocket_server.git
    cd websocket_server
    ```

2. Build and start the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. The WebSocket server will be accessible on `ws://localhost:5000`.

## Usage

You can interact with the WebSocket server using tools like **Postman**.

### Events

#### 1. **On Connect**
- Upon successful connection, the server sends a welcome message to the client:
    ```json
    { "message": "Welcome to the WebSocket server!" }
    ```

#### 2. **Client Message**
- Send a message to the server:
    ```json
    { "message": "Hello, Server!" }
    ```
- The server will respond with the length of the message:
    ```json
    { "message": "Message length: 18" }
    ```

#### 3. **Periodic Server Report**
- The server will periodically broadcast the total number of messages received. Example:
    ```json
    { "message": "Total messages received: 5" }
    ```

## License

This project is licensed under the MIT License.
