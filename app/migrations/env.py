import sys
from logging.config import fileConfig
from os.path import dirname, abspath

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.database import DATABASE_URL, Base

from app.city.model import *
from app.employment_rate.model import *
from app.users.model import *
from app.vacancy_title.model import *
from app.work_experience.model import *
from app.vacancy.model import *


config = context.config

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

config = context.config
config.set_main_option('sqlalchemy.url', f"{DATABASE_URL}?async_fallback=True")

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
