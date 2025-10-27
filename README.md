The Security API is a Flask-based application that exposes endpoints for analyzing and validating data. It’s designed to act as a backend service for security automation — taking in IP addresses or URLs, running checks against external threat intelligence sources, and returning structured results.

The API includes jobs for IP threat lookups and URL validation, making it easy to integrate security checks into larger detection or monitoring systems. Each route handles its own analysis logic and returns clear JSON responses that can be used by other tools.

I built the project with GitHub Actions to automate integration and deployment. This keeps the pipeline consistent and makes it easy to extend the API with new detection jobs over time.

At its core, the goal is to create a lightweight analysis layer that can sit between network data sources and higher-level monitoring tools — something flexible enough to grow with more detection capabilities later on.
