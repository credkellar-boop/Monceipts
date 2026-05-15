.PHONY: build up down test clean merge

# Build all services in the monorepo
build:
	docker-compose build

# Start the Monceipts engine and background watchers
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Run the full CI/CD test suite locally
test:
	pytest app/backend/tests
	flutter test app/frontend

# Execute the consolidation script to pull in external repos
merge:
	chmod +x merge_repos.sh
	./merge_repos.sh

# Clean up temporary data and generated receipts
clean:
	rm -rf data/receipts/*.png
