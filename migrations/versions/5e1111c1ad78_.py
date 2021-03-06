"""empty message

Revision ID: 5e1111c1ad78
Revises: f638e50c760c
Create Date: 2021-02-22 21:47:39.766860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e1111c1ad78'
down_revision = 'f638e50c760c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_answer_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_answer_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
