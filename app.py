from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevAlpha Internship</title>
    </head>
    <body>
        <h1>Welcome to DevAlpha Internship</h1>

        <h2>Task 1: Version Control Workflow</h2>
        <ul>
            <li>Install Git</li>
            <li>Create GitHub Repository</li>
            <li>Clone Repository</li>
            <li>Create Branches</li>
            <li>Commit Changes</li>
            <li>Push Code to GitHub</li>
            <li>Create Pull Requests</li>
            <li>Write Documentation</li>
        </ul>

        <h2>Task 2: CI/CD Pipeline Study</h2>
        <ul>
            <li>Create Sample Application</li>
            <li>Configure Jenkins/GitHub Actions</li>
            <li>Automate Build Process</li>
            <li>Automate Testing</li>
            <li>Automate Deployment</li>
        </ul>

        <h2>Task 3: Containerization Project</h2>
        <ul>
            <li>Create Dockerfile</li>
            <li>Build Docker Image</li>
            <li>Run Container</li>
            <li>Use Docker Compose</li>
            <li>Write Documentation</li>
        </ul>

        <h2>Task 4: Complete DevOps Infrastructure</h2>
        <ul>
            <li>GitHub Repository</li>
            <li>Jenkins Pipeline</li>
            <li>Docker Containerization</li>
            <li>AWS Deployment</li>
            <li>Monitoring</li>
            <li>Documentation</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)