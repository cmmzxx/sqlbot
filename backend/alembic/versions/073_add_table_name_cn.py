"""Add a table display name synchronized from the source table comment."""

from alembic import op
import sqlalchemy as sa


revision = "073_table_name_cn"
down_revision = "f898322341a5"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "core_table",
        sa.Column("table_name_cn", sa.Text(), nullable=True, comment="表中文名称"),
    )
    op.execute(sa.text("UPDATE core_table SET table_name_cn = table_comment"))


def downgrade():
    op.drop_column("core_table", "table_name_cn")
