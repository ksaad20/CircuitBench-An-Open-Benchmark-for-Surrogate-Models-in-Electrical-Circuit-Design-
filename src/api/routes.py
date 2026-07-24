"""Circuit-Bench API routes."""

from __future__ import annotations

from .server import APIServer, create_server


class APIRoutes:
    """Simple route registry for the Circuit-Bench API."""

    def __init__(self, server: APIServer | None = None) -> None:
        """Initialize the route registry."""
        self.server = server if server is not None else create_server()

    def index(self) -> dict[str, str]:
        """Return the API root."""
        return {
            "name": "Circuit-Bench API",
            "version": "0.0.2",
            "status": "active",
        }

    def health(self) -> dict[str, str]:
        """Return API health information."""
        return {
            "status": "ok",
        }

    def apis(self) -> list[dict[str, str]]:
        """Return all registered APIs."""
        return [
            {
                "name": api.name,
                "version": api.version,
                "description": api.description,
            }
            for api in self.server.list()
        ]

    def api(self, name: str) -> dict[str, str]:
        """Return information about a single API."""
        api = self.server.get(name)

        return {
            "name": api.name,
            "version": api.version,
            "description": api.description,
        }


def create_routes(server: APIServer | None = None) -> APIRoutes:
    """Create the default route registry."""
    return APIRoutes(server=server)


def main() -> None:
    """Run a simple demonstration."""
    routes = create_routes()

    print(routes.index())
    print(routes.health())

    for api in routes.apis():
        print(api)


if __name__ == "__main__":
    main()
