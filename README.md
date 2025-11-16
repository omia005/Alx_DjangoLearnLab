# Django Permissions & Groups Setup

This project uses Django's group and permission system to restrict access to Book model actions.

## Custom Permissions
The Book model defines four permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups & Permissions Mapping
Configured in Django Admin:

Viewers:
    - can_view

Editors:
    - can_view
    - can_create
    - can_edit

Admins:
    - can_view
    - can_create
    - can_edit
    - can_delete

## Views & Permission Enforcement
Views are protected using PermissionRequiredMixin.

Examples:
BookListView requires `bookshelf.can_view`
BookCreateView requires `bookshelf.can_create`
BookUpdateView requires `bookshelf.can_edit`
BookDeleteView requires `bookshelf.can_delete`

Users must belong to groups with the required permissions.
