#!/bin/bash
export DATABASE_URL=${DATABASE_URL}
alembic -c alembic.ini upgrade head
