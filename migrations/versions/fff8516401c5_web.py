"""web

Revision ID: fff8516401c5
Revises: 
Create Date: 2023-05-28 17:23:41.765594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fff8516401c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('dev', sa.String(length=60), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Game', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Game_dev'), ['dev'], unique=True)
        batch_op.create_index(batch_op.f('ix_Game_name'), ['name'], unique=True)
        batch_op.create_index(batch_op.f('ix_Game_price'), ['price'], unique=False)

    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_User_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_User_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_User_username'))
        batch_op.drop_index(batch_op.f('ix_User_email'))

    op.drop_table('User')
    with op.batch_alter_table('Game', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Game_price'))
        batch_op.drop_index(batch_op.f('ix_Game_name'))
        batch_op.drop_index(batch_op.f('ix_Game_dev'))

    op.drop_table('Game')
    # ### end Alembic commands ###