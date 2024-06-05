from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

event = Table(
    "event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("danger_lvl", Integer),
)
