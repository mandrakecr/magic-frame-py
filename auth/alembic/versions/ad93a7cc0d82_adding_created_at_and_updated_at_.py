"""adding created at and updated at columns to users

Revision ID: ad93a7cc0d82
Revises: 4137567e76da
Create Date: 2024-12-03 03:41:16.699757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad93a7cc0d82'
down_revision: Union[str, None] = '4137567e76da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth_users', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('auth_users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auth_users', 'updated_at')
    op.drop_column('auth_users', 'created_at')
    # ### end Alembic commands ###
