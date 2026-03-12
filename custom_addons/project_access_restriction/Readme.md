# Project Access Restriction – Odoo 15 Custom Module

## Overview

`project_access_restriction` is a custom Odoo 15 addon that enforces fine-grained access control on the **Project** module. It ensures that non-admin users can only see projects and tasks that are directly assigned to them — protecting sensitive project data from unauthorized visibility.

---

## Problem Statement

By default, Odoo 15's Project module allows all internal users to view **all projects and all tasks**, regardless of whether they are involved in them. This is a problem in organizations where:

- Multiple teams or clients have separate projects
- Task details are confidential between departments
- Employees should only focus on their own work
- Project managers want to control information visibility

---

## Solution

This module overrides Odoo's built-in search methods for both `project.project` and `project.task` models to silently filter records based on the logged-in user's assignments.

**Rule:**
- ✅ **Admins** (`base.group_system`) → See everything
- ✅ **Project Managers** (`project.group_project_manager`) → See everything
- 🔒 **Regular Users** → Only see projects where they have at least one assigned task, and only see their own tasks within those projects

---

## Module Structure

```
project_access_restriction/
├── __init__.py                   # Package initializer
├── __manifest__.py               # Module metadata and dependencies
├── models/
│   ├── __init__.py               # Models package initializer
│   └── project_project.py        # Core access restriction logic
└── security/
    └── ir.model.access.csv       # Access control list
```

---

## Installation

### Prerequisites

- Odoo 15.0 installed and running
- PostgreSQL configured
- Access to the `custom_addons` directory
- Administrator access to Odoo backend

### Step 1: Copy the Module

Place the `project_access_restriction` folder inside your custom addons path:

```
C:\Odoo15\custom_addons\project_access_restriction\
```

### Step 2: Verify addons_path

Make sure your `odoo.conf` includes the custom_addons path:

```ini
addons_path = C:\Odoo15\server\odoo\addons, C:\Odoo15\custom_addons
```

### Step 3: Restart Odoo Server

Open **Windows Services** (`Win + R` → type `services.msc`) → find your Odoo 15 service → click **Restart**.

Or via terminal:
```bash
net stop odoo-server-15
net start odoo-server-15
```

### Step 4: Enable Developer Mode

In Odoo, go to:
**Settings → General Settings → scroll to bottom → Activate Developer Mode**

Or navigate directly to:
```
http://localhost:8070/web?debug=1
```

### Step 5: Update Apps List

Go to **Apps** (top menu) → click **Update Apps List** → click **Update** in the popup.

### Step 6: Install the Module

In the Apps menu, search for:
```
Project Access Restriction
```
Click **Install**.

---

## Configuration

### Setting Up Users

1. Go to **Settings → Users & Companies → Users**
2. Click **Create** to add a new user
3. Set their **Project** access level to `User` (not Administrator)
4. Save the user

### Assigning Tasks to Users

1. Go to **Project** module
2. Open a project
3. Open or create a task
4. In the **Assigned to** field, select the user
5. Save the task

The user will now be able to see that project and only that specific task.

---
