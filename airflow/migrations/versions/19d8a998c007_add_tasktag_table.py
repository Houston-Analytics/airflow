#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Add TaskTag table

Revision ID: 19d8a998c007
Revises: 952da73b5eff
Create Date: 2020-05-29 14:20:37.831692

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.schema import Sequence, CreateSequence, DropSequence


# revision identifiers, used by Alembic.
revision = '19d8a998c007'
down_revision = '952da73b5eff'
branch_labels = None
depends_on = None

tag_id_sequence = Sequence('tag_id_sequence')


def upgrade():
    """Apply Add TaskTag table"""
    op.execute(CreateSequence(tag_id_sequence))

    op.create_table(
        'task_tag',
        sa.Column('tag_id', sa.Integer, tag_id_sequence, server_default=tag_id_sequence.next_value(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('tag_id', 'name')
    )


def downgrade():
    """Unapply Add TaskTag table"""
    op.drop_table('task_tag')
    op.execute(DropSequence(tag_id_sequence))
