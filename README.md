# Django Blog Application

This is a Django-based blog application designed to manage articles, with role-based features for writers and editors. It includes article approval, article editing, and a dashboard that displays a summary of writer activity.

## APIs

- **Dashboard**: 
  - Displays a summary of total articles written by each writer. `/api/dashboard/`
- **Article Management**:
  - Create Articles endpoint for writers `/api/article/`.
- **Editor Endpoints**:
  - Added Listing API to show pending articles. `/api/articles_approval/`
  - API to Approve/Reject Articles `/api/articles_approval/5/`
  - APIs to view Editor Approved/Rejected Articles `/api/articles_editor`


```
make build     # Build and start the Docker containers
make up        # Start the Docker containers
make ssh       # SSH into the blogapp container
make server    # Run the Django development server in the blogapp container
make down      # Stop the Docker containers
make flake8    # Run flake8 linting
make test      # Run the tests
```
