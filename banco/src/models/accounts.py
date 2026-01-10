import sqlalchemy as sa
from src.database import metadata


accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("user_id", sa.Integer, nullable=False, index=True),
    sa.Column("account_id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now(), nullable=False
    ),
    sa.Column("agency_number", sa.Integer, nullable=False),
    sa.Column("balance", sa.Float, nullable=False),
)
