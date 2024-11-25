import sys
from os.path import abspath, dirname
from alembic import context
from sqlalchemy import engine_from_config, pool

# Adding the base path of your application to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))

# Import models and Base from your app
from db import Base  # Make sure this is the correct import for your Base
from models import *  # This ensures all your models are imported and registered with Base

# Alembic Config object, allows access to the config
config = context.config

# Set the target_metadata to Base.metadata so Alembic knows how to generate migrations
target_metadata = Base.metadata

# Other configurations needed for the environment to work
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Choose which mode to run the migrations in
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
