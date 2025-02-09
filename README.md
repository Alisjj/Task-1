# Setting Up a Basic Frappe Application from Scratch on macOS

This guide details the step-by-step process of installing and setting up a basic Frappe application on macOS.

## Prerequisites

Ensure that your system meets the following requirements:

- **OS**: macOS (Monterey or later recommended)
- **Python**: 3.10+
- **Node.js**: 18+
- **Redis**: 6+
- **MariaDB**: 10.6+
- **Yarn**
- **pip** and **virtualenv**

## Step 1: Install Dependencies

```sh
brew update && brew upgrade
brew install python@3.10 node@18 redis mariadb yarn
```

## Step 2: Make sure MariaDB is running

```sh
brew services start mariadb
```

## Step 3: Set Up Frappe Bench

Depending on your OS version and python/pip version, you may get an error here regarding an externally-managed-environment
You can work around this for now by running

```sh
pip3 install frappe-bench --break-system-packages
bench init taskapp
cd taskapp
```

## Step 4: Create a custom Frappe App

```sh
bench new-app eglobal
```

## Step 5: Create a New Frappe Site

```sh
bench new-site etask.localhost --admin-password admin
```

Set MariaDB root password if prompted.

## Step 6: Install App on site

```sh
bench --site etask.local install-app eglobal
```

## Step 6: Start the Development Server

```sh
bench start
```

Access your site at `http://etask.localhost:8000`.

## Conclusion

The Frappe environment is now set up with a basic app. One can begin developing by creating custom DocTypes and modules.
