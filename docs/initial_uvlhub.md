# Installation and Configuration of MariaDB and Application Environment

## Update and Upgrade System Packages
```bash
sudo apt update -y
sudo apt upgrade -y
```

---

## Install MariaDB

### Step 1: Install Official Package
MariaDB is available in the official Ubuntu repositories, so it can be installed easily:

```bash
sudo apt install mariadb-server -y
```

### Step 2: Start MariaDB Service
To start the MariaDB service:

```bash
sudo systemctl start mariadb
```

### Step 3: Configure MariaDB
Run the security script for initial configurations:

```bash
sudo mysql_secure_installation
```

#### Default Values:
- **Enter current password for root**: *(press Enter for none)*
- **Switch to unix_socket authentication [Y/n]**: `y`
- **Change the root password? [Y/n]**: `y`
  - New password: `uvlhubdb_root_password`
  - Re-enter new password: `uvlhubdb_root_password`
- **Remove anonymous users? [Y/n]**: `y`
- **Disallow root login remotely? [Y/n]**: `y`
- **Remove test database and access to it? [Y/n]**: `y`
- **Reload privilege tables now? [Y/n]**: `y`

---

## Configure Databases and Users

### Access the MariaDB Command Console:
```bash
sudo mysql -u root -p
```

Use `uvlhubdb_root_password` as the root password.

### Execute the Following Commands:
```sql
CREATE DATABASE uvlhubdb;
CREATE DATABASE uvlhubdb_test;
CREATE USER 'uvlhubdb_user'@'localhost' IDENTIFIED BY 'uvlhubdb_password';
GRANT ALL PRIVILEGES ON uvlhubdb.* TO 'uvlhubdb_user'@'localhost';
GRANT ALL PRIVILEGES ON uvlhubdb_test.* TO 'uvlhubdb_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

---

## Configure App Environment

### Environment Variables
To configure environment variables for the database and other elements, create a `.env` file:
```bash
cp .env.local.example .env
```

### Ignore Webhook Module
The webhook module is only relevant for Docker-based pre-production environments. To exclude it:

```bash
echo "webhook" > .moduleignore
```

---

## Install Dependencies

### Step 1: Create and Activate a Virtual Environment
```bash
sudo apt install python3.12-venv
python3.12 -m venv venv
source venv/bin/activate
```

### Step 2: Install Python Dependencies
Update pip and install required packages:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Install Rosemary in Editable Mode
Rosemary is a CLI tool for project management. Install it manually in editable mode:

```bash
pip install -e ./
```

#### Verify Installation
Run the following command to list all available CLI commands:
```bash
rosemary
```

---

## Run the Application

### Step 1: Populate Database
Reset the database with test data:
```bash
rosemary db:reset
```
Migrate the database with test data:
```bash
rosemary db:migrate
```
Seed the database with test data:
```bash
rosemary db:seed
```

### Step 2: Run the Flask Development Server
Run the application on port 5000:
```bash
flask run --host=0.0.0.0 --reload --debug
```