"""Database creation

Revision ID: 5b6f88f55648
Revises: 
Create Date: 2023-03-27 16:21:55.347823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b6f88f55648'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('user_surname', sa.String(), nullable=False),
                    sa.Column('user_patronymic', sa.String(), nullable=True),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.Column('gender', sa.String(), nullable=False),
                    sa.Column('registration_date', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
