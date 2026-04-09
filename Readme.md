# Backend Development with NoSQL - Learning Project

A comprehensive project for learning backend development using NoSQL databases (MongoDB). This project provides implementations in both JavaScript (Node.js) and Python to help you understand core backend concepts.

## Project Structure

```
backend_api/
├── javascript_backend/      # Node.js implementation
│   ├── Config/             # Database and app configuration
│   ├── Controllers/        # Request handlers
│   ├── Middlewares/        # Custom middleware functions
│   ├── Models/             # Mongoose schemas
│   ├── Repositories/       # Data access layer
│   ├── Routes/             # API route definitions
│   ├── Services/           # Business logic
│   ├── Utils/              # Utility functions
│   ├── .env                # Environment variables
│   ├── server.js          # Application entry point
│   └── package.json        # Dependencies
│
├── python_backend/         # Python implementation
│   ├── Config/             # Configuration files
│   ├── Controllers/         # Request handlers (FastAPI)
│   ├── Middlewares/        # Custom middleware
│   ├── Models/             # Pydantic models
│   ├── Repositories/       # Data access layer
│   ├── Routes/             # API route definitions
│   ├── Schemas/            # Data schemas
│   ├── Services/           # Business logic
│   ├── Utils/              # Utility functions
│   ├── .env                # Environment variables
│   ├── main.py             # Application entry point
│   └── requirements.txt     # Dependencies
│
└── README.md
```

## Architecture Pattern

This project follows a **Layered Architecture** (also known as N-Tier Architecture):

```
Request → Routes → Controllers → Services → Repositories → Models/Schemas → Database
              ↓
         Middlewares
```

### Layer Responsibilities

| Layer | Responsibility |
|-------|----------------|
| **Routes** | Define API endpoints and map to controllers |
| **Controllers** | Handle HTTP requests/responses, validation |
| **Services** | Business logic and data transformation |
| **Repositories** | Data access abstraction, database queries |
| **Models/Schemas** | Data validation and structure definition |
| **Config** | Database connection and app settings |

## Prerequisites

- **MongoDB**: Install locally or use MongoDB Atlas (cloud)
- **Node.js** (v18+): For JavaScript implementation
- **Python** (3.10+): For Python implementation

## Setup Instructions

### JavaScript Implementation (Node.js)

1. Navigate to the JavaScript directory:
   ```bash
   cd javascript_backend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables in `.env`:
   ```env
   PORT=3000
   MONGO_URI=mongodb://localhost:27017/your_database
   ```

4. Run the server:
   ```bash
   npm start        # Production
   npm run server   # Development (with nodemon)
   ```

### Python Implementation (FastAPI)

1. Navigate to the Python directory:
   ```bash
   cd python_backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in `.env`:
   ```env
   PORT=8000
   MONGO_URI=mongodb://localhost:27017/your_database
   ```

5. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Key Concepts Covered

### NoSQL/MongoDB Concepts
- Document-based data modeling
- Collections and schemas
- CRUD operations (Create, Read, Update, Delete)
- Indexing and performance optimization
- Aggregation pipelines

### Backend Concepts
- RESTful API design
- Authentication and authorization
- Error handling
- Request validation
- Response formatting

### JavaScript (Node.js)
- Express.js framework
- Mongoose ODM
- ES6+ syntax (async/await, modules)
- Middleware pattern

### Python
- FastAPI framework
- Pydantic for validation
- Motor async driver
- Type hints

## API Endpoints (Template)

```
GET    /api/users          # Get all users
GET    /api/users/:id      # Get user by ID
POST   /api/users          # Create new user
PUT    /api/users/:id      # Update user
DELETE /api/users/:id      # Delete user
```

## Learning Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [Express.js Guide](https://expressjs.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Mongoose Documentation](https://mongoosejs.com/docs/)

## Contributing

Feel free to extend this project with additional features, endpoints, or improvements. Ensure you follow the existing architecture pattern.

## License

ISC