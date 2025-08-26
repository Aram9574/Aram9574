from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'patients',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tenant_id', sa.String, index=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('consent', sa.Boolean, default=True)
    )

def downgrade():
    op.drop_table('patients')
